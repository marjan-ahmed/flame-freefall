"""ChatKit backend for the Flame in Freefall chat widget — dev only.

Runs the actual ChatKit server protocol (openai-chatkit has no documented
wire format to hand-roll; ChatKitServer.process() is the real implementation)
and answers through Groq's OpenAI-compatible API rather than OpenAI's own,
via the openai-agents SDK's custom-provider path.

Run: uv run uvicorn main:app --reload --port 8000
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
import uuid
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

# stdout is fully buffered (not line-buffered) once redirected to a file —
# our own print()s (llm-fallback, etc.) were sitting unflushed in that
# buffer, invisible in the log while the process kept running (confirmed
# live 2026-09-22: real tool calls happened but never showed up here).
sys.stdout.reconfigure(line_buffering=True)

import openai
from agents import Agent, AsyncOpenAI, ModelSettings, OpenAIChatCompletionsModel, Runner, RunHooks, set_tracing_disabled
from agents.mcp import MCPServerStreamableHttp
from chatkit.agents import AgentContext, ThreadItemConverter, stream_agent_response
from chatkit.server import ChatKitServer, StreamingResult
from chatkit.store import AttachmentStore
from chatkit.types import (
    AssistantMessageItem,
    Attachment,
    AttachmentCreateParams,
    AttachmentUploadDescriptor,
    CustomTask,
    FileAttachment,
    ThreadItemAddedEvent,
    ThreadItemUpdatedEvent,
    ThreadMetadata,
    ThreadStreamEvent,
    UserMessageItem,
    Workflow,
    WorkflowItem,
    WorkflowTaskAdded,
    WorkflowTaskUpdated,
)
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from openai.types.responses import EasyInputMessageParam

from comparison_widget import show_comparison
from postgres_store import PostgresChatKitStore

# ONE .env at the repo root — same convention system/site/next.config.mjs
# uses, so the Groq key set up earlier is already in the right place.
load_dotenv(Path(__file__).resolve().parents[2] / ".env")

# Tracing would otherwise try to authenticate against OpenAI's own platform
# with a key this backend never has — it only ever talks to Groq.
set_tracing_disabled(True)

# Automatic cross-provider fallback: OpenAIChatCompletionsModel just needs
# an object shaped like AsyncOpenAI (duck-typed — it only ever calls
# .chat.completions.create). Each provider needs its OWN model id (Groq
# wants "openai/gpt-oss-120b", HF's router wants a full repo id like
# "meta-llama/Llama-3.1-8B-Instruct") — since OpenAIChatCompletionsModel
# binds one model id for its whole lifetime, this rewrites `model` in the
# call kwargs per provider, tried in order, falling through on a 429.
#
# Caveat 1: Groq's rate-limit error names an ORGANIZATION, not a key — two
# keys on the same Groq account share the same daily quota (confirmed live
# 2026-09-22, same pattern the Gemini keys hit earlier this session).
# Caveat 2: meta-llama/Llama-3.1-8B-Instruct is a much smaller model than
# gpt-oss-120b — tool-call triggering works (verified live) but argument
# filling was weaker in a quick test (empty args where content was
# expected), so search/read/show_comparison calls may be less reliable
# once this tier is actually reached.
class _FallbackCompletions:
    def __init__(self, providers: list[tuple[AsyncOpenAI, str]]) -> None:
        self._providers = providers

    async def create(self, **kwargs):
        last_exc: Exception | None = None
        for index, (client, model_id) in enumerate(self._providers):
            try:
                return await client.chat.completions.create(**{**kwargs, "model": model_id})
            except openai.RateLimitError as exc:
                last_exc = exc
                print(f"[llm-fallback] provider {index} ({model_id}) rate-limited, trying next")
        raise last_exc  # type: ignore[misc]


class FallbackAsyncOpenAI:
    """Duck-typed AsyncOpenAI substitute. `.chat` is the only thing actually
    overridden (the fallback logic); everything else the SDK reads off the
    client (e.g. `.base_url`, used for tracing metadata) proxies to the
    FIRST real client via __getattr__ — fine for metadata, since it's only
    used for trace labeling, never for the actual request routing."""

    def __init__(self, providers: list[tuple[AsyncOpenAI, str]]) -> None:
        self._providers = providers
        self.chat = SimpleNamespace(completions=_FallbackCompletions(providers))

    def __getattr__(self, name: str):
        return getattr(self._providers[0][0], name)


GROQ_MODEL_ID = "openai/gpt-oss-120b"
HF_MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct"

_groq_keys = [os.environ["GROQ_API_KEY"]]
if fallback_key := os.environ.get("GROQ_API_KEY_FALLBACK"):
    _groq_keys.append(fallback_key)

_providers: list[tuple[AsyncOpenAI, str]] = [
    (AsyncOpenAI(api_key=k, base_url="https://api.groq.com/openai/v1"), GROQ_MODEL_ID) for k in _groq_keys
]
if hf_token := os.environ.get("HF_TOKEN"):
    _providers.append(
        (AsyncOpenAI(api_key=hf_token, base_url="https://router.huggingface.co/v1"), HF_MODEL_ID)
    )

chat_client = FallbackAsyncOpenAI(_providers) if len(_providers) > 1 else _providers[0][0]
model = OpenAIChatCompletionsModel(model=_providers[0][1], openai_client=chat_client)

# The Flame in Freefall record's own MCP door (`ksor serve`, run separately —
# see AGENTS.md "Serving to agents"). search/outline/read over the actual
# corpus, cited retrieval rather than the model's own (ungrounded) knowledge.
# Connected once at FastAPI startup (see lifespan below), not per-request.
handbook_mcp_url = os.environ.get("HANDBOOK_MCP_URL", "http://127.0.0.1:8080/mcp")
handbook_mcp = MCPServerStreamableHttp(
    name="handbook",
    params={"url": handbook_mcp_url},
    cache_tools_list=True,
)

# reasoning_format="hidden" (Groq-specific): without it, gpt-oss-120b's chain
# of thought comes back as a `reasoning` field, which chatkit-python's
# stream_agent_response maps into a "workflow" item it never finishes
# populating (it only reads response.reasoning_summary_text.* events; Groq
# sends response.reasoning_text.* instead) — the widget gets stuck showing an
# empty "Thought for a moment" and the real answer never displays, confirmed
# live 2026-09-22 (Runner.run_streamed itself produced the correct final
# output in isolation; the gap is specifically in that chatkit-python event
# mapping). Hiding reasoning server-side sidesteps it entirely; content is
# unaffected either way.
# Groq's free tier caps openai/gpt-oss-120b at 8000 tokens/minute — a single
# default-sized search/read result plus history can blow past that (confirmed
# live 2026-09-22: a 8067-token request got a 413). Keep every knob small:
# short instructions, k=2 on search, a low token_budget on read, capped
# output, and a short history window (below).
assistant = Agent(
    name="Flame in Freefall assistant",
    instructions=(
        "Assistant for Flame in Freefall (NASA microgravity combustion: "
        "BASS-II, SAFFIRE, FLEX, ACME; fire-safety standards).\n\n"
        "Greetings, thanks, and chit-chat ('hi', 'who are you', 'thanks') get "
        "a direct reply — NEVER call a tool for these, there is nothing to "
        "look up.\n\n"
        "For anything that actually asks about the corpus, ground the answer "
        "in the handbook MCP tools, not general knowledge — but call a tool "
        "only when the question needs it, and only once per distinct fact "
        "you're missing, not speculatively. Keep tool calls small: search "
        "with k=2, read with token_budget<=600 and a specific heading rather "
        "than a whole document. Say so if the record doesn't cover "
        "something. Be concise.\n\n"
        "HARD BUDGET: at most 2 tool calls per investigation you mention "
        "(one outline or search, one read), and never repeat a call you "
        "already made. If you hit that budget and still don't have a fact, "
        "use '—' for it rather than searching again — going over this budget "
        "causes a real failure (rate limit), not just a slower answer.\n\n"
        "When the question compares 2+ investigations (flame spread rate, "
        "O2%, pressure, gravity, geometry), you MUST call show_comparison — "
        "do this even if you only found some of the facts, passing '—' for "
        "whatever you didn't find. NEVER write a markdown table, bullet "
        "list, or any other manual side-by-side layout comparing "
        "investigations — that is what show_comparison is for, and writing "
        "one yourself is a mistake, not just a style choice."
    ),
    model=model,
    model_settings=ModelSettings(
        extra_body={"reasoning_format": "hidden"},
        max_tokens=400,
    ),
    mcp_servers=[handbook_mcp],
    tools=[show_comparison],
)


# The default ThreadItemConverter.assistant_message_to_input wraps prior
# assistant turns in a Responses-API content part (type "output_text") — the
# Chat Completions converter this backend's model uses (required for Groq,
# which has no Responses API) doesn't recognize that type and throws
# `UserError: Unknown content` on any second turn. Plain string content is
# valid on both APIs, so history round-trips through either one.
class ChatCompletionsThreadItemConverter(ThreadItemConverter):
    async def assistant_message_to_input(self, item: AssistantMessageItem):
        return EasyInputMessageParam(
            type="message",
            role="assistant",
            content="\n".join(c.text for c in item.content),
        )


converter = ChatCompletionsThreadItemConverter()


# Live tool-call visibility, as a real persisted step list rather than a
# transient toast. AgentContext.workflow_item is the SAME field
# stream_agent_response already manages for reasoning ("Thought for a
# moment") — reusing it means the step list collapses automatically the
# moment the real answer starts streaming, for free, via that existing
# mechanism (stream_agent_response closes ctx.workflow_item on
# response.output_item.added for a "message" item).
#
# RunHooks fires for every LOCAL tool dispatch, MCP tools included — the
# dispatch loop is local even though search/outline/read execute on the
# remote handbook MCP server, so on_tool_start/on_tool_end do fire for them
# (confirmed live 2026-09-22).
class ToolCallVisibilityHooks(RunHooks):
    def __init__(self) -> None:
        self._task_index: dict[str, int] = {}

    def _describe_args(self, context) -> str:
        raw = getattr(context, "tool_arguments", None)
        if not raw:
            return ""
        try:
            parsed = json.loads(raw)
        except (TypeError, ValueError):
            return str(raw)[:200]
        return ", ".join(f"{k}={v!r}" for k, v in parsed.items())

    async def on_tool_start(self, context, agent, tool) -> None:
        ctx: AgentContext = context.context
        print(f"[tool-call] START {tool.name}({self._describe_args(context)})")
        if ctx.workflow_item is None:
            ctx.workflow_item = WorkflowItem(
                id=ctx.generate_id("workflow"),
                thread_id=ctx.thread.id,
                created_at=datetime.now(),
                workflow=Workflow(type="custom", tasks=[]),
            )
            await ctx.stream(ThreadItemAddedEvent(item=ctx.workflow_item))

        args_desc = self._describe_args(context)
        task = CustomTask(
            title=tool.name,
            content=args_desc or "…",
            status_indicator="loading",
        )
        task_index = len(ctx.workflow_item.workflow.tasks)
        ctx.workflow_item.workflow.tasks.append(task)
        call_id = getattr(context, "tool_call_id", f"{tool.name}:{task_index}")
        self._task_index[call_id] = task_index
        await ctx.stream(
            ThreadItemUpdatedEvent(
                item_id=ctx.workflow_item.id,
                update=WorkflowTaskAdded(task_index=task_index, task=task),
            )
        )

    async def on_tool_end(self, context, agent, tool, result) -> None:
        ctx: AgentContext = context.context
        result_preview = str(result)[:500]
        print(f"[tool-call] END   {tool.name} -> {result_preview}")
        if ctx.workflow_item is None:
            return
        call_id = getattr(context, "tool_call_id", None)
        task_index = self._task_index.pop(call_id, None)
        if task_index is None or task_index >= len(ctx.workflow_item.workflow.tasks):
            return
        task = ctx.workflow_item.workflow.tasks[task_index]
        task.status_indicator = "complete"
        await ctx.stream(
            ThreadItemUpdatedEvent(
                item_id=ctx.workflow_item.id,
                update=WorkflowTaskUpdated(task_index=task_index, task=task),
            )
        )


tool_call_hooks = ToolCallVisibilityHooks()

# openai-agents' Chat Completions adapter has no native per-item id (only the
# Responses API carries one), so it stamps every output item with the same
# literal constant, "__fake_id__" — and chatkit-python's stream_agent_response
# reuses that raw id directly as the ChatKit assistant-message item id
# (unlike the reasoning/workflow item, which it gives a freshly generated
# id). Every turn in a thread therefore collides on the SAME ChatKit item id,
# so ChatKit's client-side state drops or misroutes every turn after the
# first. Confirmed live 2026-09-22 via a captured SSE stream: user and
# workflow items get real unique ids; every assistant_message item across
# every turn was "__fake_id__". Rewritten here to a real unique id, once per
# turn, consistently across its added/updated/done events.
_FAKE_ITEM_ID = "__fake_id__"


async def _uniquify_fake_item_ids(
    events: AsyncIterator[ThreadStreamEvent],
) -> AsyncIterator[ThreadStreamEvent]:
    real_id: str | None = None
    async for event in events:
        if getattr(event, "item_id", None) == _FAKE_ITEM_ID:
            if real_id is None:
                real_id = f"msg_{uuid.uuid4().hex[:24]}"
            event.item_id = real_id
        elif getattr(getattr(event, "item", None), "id", None) == _FAKE_ITEM_ID:
            if real_id is None:
                real_id = f"msg_{uuid.uuid4().hex[:24]}"
            event.item.id = real_id
        yield event


# Raw uploaded bytes, keyed by attachment id — separate from
# InMemoryChatKitStore.attachments (metadata only). Dev-only: in memory, lost
# on restart, no size/type re-validation server-side beyond what the widget
# already enforces client-side.
uploaded_files: dict[str, bytes] = {}


# Base URL for attachment uploads - configurable via env for production
attachment_base_url = os.environ.get("ATTACHMENT_BASE_URL", "http://127.0.0.1:8000")


class InMemoryAttachmentStore(AttachmentStore[dict]):
    """Two-phase upload: create_attachment hands back a URL this same
    process serves (POST /chatkit/upload/{id}); the browser PUTs/POSTs the
    file there next, independent of the ChatKit protocol request/response.
    """

    async def create_attachment(self, input: AttachmentCreateParams, context: dict) -> Attachment:
        attachment_id = self.generate_attachment_id(input.mime_type, context)
        return FileAttachment(
            id=attachment_id,
            name=input.name,
            mime_type=input.mime_type,
            upload_descriptor=AttachmentUploadDescriptor(
                url=f"{attachment_base_url}/chatkit/upload/{attachment_id}",
                method="POST",
            ),
        )

    async def delete_attachment(self, attachment_id: str, context: dict) -> None:
        uploaded_files.pop(attachment_id, None)


attachment_store = InMemoryAttachmentStore()


def _item_text(item) -> str:
    content = getattr(item, "content", None) or []
    return " ".join(getattr(c, "text", "") for c in content).strip()


async def generate_short_title(items) -> str:
    """One small, cheap LLM call — not the main assistant — so titling
    doesn't compete with the real answer for the tight Groq/HF token
    budgets. Goes through the same provider fallback chain as everything
    else (chat_client.chat.completions.create ignores the `model` kwarg
    here; each tier substitutes its own, same as the main model)."""
    transcript = "\n".join(t for t in (_item_text(i) for i in reversed(items)) if t)[:800]
    resp = await chat_client.chat.completions.create(
        model=_providers[0][1],
        messages=[
            {
                "role": "system",
                "content": "Reply with ONLY a 3-6 word title summarizing this chat. No quotes, no trailing punctuation.",
            },
            {"role": "user", "content": transcript},
        ],
        max_tokens=20,
    )
    return (resp.choices[0].message.content or "").strip().strip('"')


class FlameFreefallChatKitServer(ChatKitServer[dict]):
    async def respond(
        self,
        thread: ThreadMetadata,
        input_user_message: UserMessageItem | None,
        context: dict,
    ) -> AsyncIterator[ThreadStreamEvent]:
        # Short window: full history plus a tool result adds up fast against
        # Groq's 8000 TPM cap (see note above the Agent definition).
        items_page = await self.store.load_thread_items(
            thread.id,
            after=None,
            limit=6,
            order="asc",
            context=context,
        )
        input_items = await converter.to_agent_input(items_page.data)

        agent_context = AgentContext(thread=thread, store=self.store, request_context=context)
        result = Runner.run_streamed(assistant, input_items, context=agent_context, hooks=tool_call_hooks)

        # Started before the main stream, awaited after: title generation
        # runs concurrently with the real answer rather than adding latency
        # to it. thread.title update()s the SAME object the "thread not
        # found" check above already validated — save_thread persists it,
        # and chatkit's own protocol layer emits the ThreadUpdatedEvent the
        # client's history list picks up.
        title_task = asyncio.create_task(self._maybe_update_thread_title(thread, context))
        async for event in _uniquify_fake_item_ids(stream_agent_response(agent_context, result)):
            yield event
        await title_task

    async def _maybe_update_thread_title(self, thread: ThreadMetadata, context: dict) -> None:
        if thread.title is not None:
            return
        items_page = await self.store.load_thread_items(
            thread.id, after=None, limit=6, order="desc", context=context
        )
        if not items_page.data:
            return
        try:
            title = await generate_short_title(items_page.data)
        except Exception as exc:
            print(f"[thread-title] generation failed: {exc}")
            return
        if not title:
            return
        thread.title = title
        await self.store.save_thread(thread, context=context)


# Initialize Postgres store (falls back to in-memory if DB not configured)
def _make_store():
    if os.environ.get("KSOR_DB_URL") or os.environ.get("DATABASE_URL"):
        return PostgresChatKitStore()
    return InMemoryChatKitStore()


server = FlameFreefallChatKitServer(store=_make_store(), attachment_store=attachment_store)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    async with handbook_mcp:
        yield


# CORS origins - configurable via env for production
cors_origins = os.environ.get("CORS_ORIGINS", "http://localhost:3000").split(",")

app = FastAPI(lifespan=lifespan)

# The Next.js dev server runs on a different port — a different origin.
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/chatkit")
async def chatkit_endpoint(request: Request):
    result = await server.process(await request.body(), context={})
    if isinstance(result, StreamingResult):
        return StreamingResponse(result, media_type="text/event-stream")
    return Response(content=result.json, media_type="application/json")


@app.post("/chatkit/upload/{attachment_id}")
async def upload_attachment(attachment_id: str, request: Request):
    if attachment_id not in server.store.attachments:  # type: ignore[attr-defined]
        raise HTTPException(status_code=404, detail="unknown attachment id")
    uploaded_files[attachment_id] = await request.body()
    return {"status": "ok"}


@app.get("/health")
async def health():
    return {"status": "ok", "providers": [model_id for _, model_id in _providers]}
