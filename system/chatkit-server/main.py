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
from chatkit.agents import AgentContext, ThreadItemConverter, stream_agent_response, stream_widget
from chatkit.server import ChatKitServer, StreamingResult
from chatkit.store import AttachmentStore
from chatkit.types import (
    SyncCustomActionResponse,
    AssistantMessageContent,
    AssistantMessageItem,
    Attachment,
    AttachmentCreateParams,
    AttachmentUploadDescriptor,
    CustomTask,
    FileAttachment,
    ThreadItemAddedEvent,
    ThreadItemDoneEvent,
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

import psi_widgets
from chatkit.widgets import Caption, Card, Markdown, Text
from psi_tools import TOOLS as PSI_TOOLS
from postgres_store import PostgresChatKitStore
from store import InMemoryChatKitStore
from turn_guard import TurnGuard

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
# "Qwen/Qwen2.5-72B-Instruct") — since OpenAIChatCompletionsModel
# binds one model id for its whole lifetime, this rewrites `model` in the
# call kwargs per provider, tried in order, falling through on a rate limit
# OR a bad/unreachable model (see Caveat 3).
#
# Caveat 1: Groq's rate-limit error names an ORGANIZATION, not a key — two
# keys on the same Groq account share the same daily quota FOR THE SAME
# MODEL (confirmed live 2026-09-22, same pattern the Gemini keys hit earlier
# this session), so GROQ_API_KEY_FALLBACK is not real headroom against a
# quota 429 on one model, only against a transient/per-key outage. Quota IS
# scoped per model id, though (confirmed live 2026-09-24: gpt-oss-120b's
# daily quota was fully exhausted while qwen/qwen3.8-27b, same account, same
# keys, was still reachable) -- see Caveat 5. Once every Groq (key, model)
# pair is exhausted, HF_MODEL_ID is the only tier with independent quota.
# Caveat 2: HF's router only serves a model through the providers THIS
# account has enabled (confirmed live 2026-09-24: this account only has
# `together` enabled, not `featherless-ai` — meta-llama/Llama-3.1-8B-Instruct
# routes through together and works, Qwen/Qwen2.5-7B-Instruct's only live
# provider is featherless-ai and 400s outright as "not supported by any
# provider you have enabled"). Verify a candidate HF_MODEL_ID with a plain
# curl against router.huggingface.co before changing this, not just a Hub
# model-card lookup.
# Caveat 3: a BadRequestError (wrong/unreachable model id, as above) used to
# NOT be caught below — only RateLimitError was — so a broken HF_MODEL_ID
# would crash the whole chat turn instead of degrading, and Groq being
# exhausted (Caveat 1) makes that the exact moment this tier is needed most.
# Caveat 4: narrowing to RateLimitError/BadRequestError still missed every
# OTHER HTTP-status failure a provider can return -- confirmed live
# 2026-09-24 in production: Groq's daily quota was exhausted (RateLimitError,
# caught, fell through correctly) and the HF tier then returned a 402
# ("depleted your monthly included credits"), which is an APIStatusError but
# neither of the two caught subtypes, so it crashed the whole turn with a raw
# traceback instead of the graceful fallback this class exists for. Widened
# to APIStatusError, the actual base class RateLimitError/BadRequestError
# both already derive from -- ANY HTTP-status failure from one provider now
# tries the next, not just those two.
# Caveat 5: since quota is per model id (Caveat 1), the primary/fallback
# split below isn't just "strong model, weak model" -- it's real independent
# headroom. GROQ_PRIMARY_MODEL_ID (qwen/qwen3.8-27b) is tried on every Groq
# key first, THEN GROQ_FALLBACK_MODEL_ID (openai/gpt-oss-120b) on every Groq
# key, before HF. Swapping which model leads buys nothing on its own if both
# are already exhausted -- it only helps when one model's daily quota still
# has headroom while the other's doesn't, which is exactly what was
# happening live 2026-09-24.
class _FallbackCompletions:
    def __init__(self, providers: list[tuple[AsyncOpenAI, str]]) -> None:
        self._providers = providers

    async def create(self, **kwargs):
        last_exc: Exception | None = None
        for index, (client, model_id) in enumerate(self._providers):
            try:
                return await client.chat.completions.create(**{**kwargs, "model": model_id})
            except openai.APIStatusError as exc:
                last_exc = exc
                print(f"[llm-fallback] provider {index} ({model_id}) failed ({type(exc).__name__}: {exc}), trying next")
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


# Primary/fallback are both Groq-hosted (separate quota buckets per Caveat
# 5, confirmed real Groq model ids via GET /openai/v1/models, not guessed).
#
# Caveat 6: qwen/qwen3.8-27b briefly WAS primary (2026-09-24) to dodge
# gpt-oss-120b's exhausted daily quota, but its rate limit is on INPUT
# tokens per MINUTE (ITPM), not tokens per day, and its limit (7000) is
# smaller than gpt-oss-120b's TPM (8000) that this app's whole token budget
# (BASE_INSTRUCTIONS length, search k=2, read token_budget, history window
# -- see notes above the Agent definition) was actually sized around.
# Confirmed live in production logs: real requests with a tool result in
# them run 7000-13000+ input tokens, so qwen 413'd on nearly every non-trivial
# turn ("Request too large... on input tokens per minute (ITPM): Limit
# 7000"), fell through gpt-oss-120b (still exhausted from the day before)
# to HF (still out of monthly credits), and EVERY turn hit the
# every-provider-exhausted fallback -- confirmed via Vercel runtime logs,
# not guessed. gpt-oss-120b is primary again; qwen tried second (cheap, and
# its tight ITPM means it still helps on genuinely small turns), HF last.
GROQ_PRIMARY_MODEL_ID = "openai/gpt-oss-120b"
GROQ_FALLBACK_MODEL_ID = "qwen/qwen3.8-27b"
HF_MODEL_ID = "Qwen/Qwen2.5-72B-Instruct"

_groq_keys = [os.environ["GROQ_API_KEY"]]
if fallback_key := os.environ.get("GROQ_API_KEY_FALLBACK"):
    _groq_keys.append(fallback_key)

# max_retries=0 on every client: the openai SDK's OWN retry-with-backoff on
# 429s runs INSIDE client.chat.completions.create(), before
# _FallbackCompletions ever gets a chance to move to the next provider --
# confirmed live 2026-09-24 in production ("Retrying request in 17.000000
# seconds (retry 1 of 2)" in the Vercel logs), and with gpt-oss-120b back as
# primary while still rate-limited, that SDK-level sleep-and-retry across
# multiple provider attempts blew Vercel's 60s function budget outright
# ("Vercel Runtime Timeout Error: Task timed out after 60 seconds") -- the
# whole function got killed by the platform before our own fallback logic,
# or even the except-Exception guard in respond(), ever ran. We want a rate
# limit to fail INSTANTLY so _FallbackCompletions can try the next provider
# in milliseconds, not have the SDK silently retry the SAME exhausted one.
_groq_clients = [
    AsyncOpenAI(api_key=k, base_url="https://api.groq.com/openai/v1", max_retries=0) for k in _groq_keys
]

# Every Groq key tried on the primary model before any key is tried on the
# fallback model -- see Caveat 5 above for why this ordering (not "strong
# model then weak model") is the one that actually buys independent quota.
_providers: list[tuple[AsyncOpenAI, str]] = (
    [(client, GROQ_PRIMARY_MODEL_ID) for client in _groq_clients]
    + [(client, GROQ_FALLBACK_MODEL_ID) for client in _groq_clients]
)
if hf_token := os.environ.get("HF_TOKEN"):
    _providers.append(
        (AsyncOpenAI(api_key=hf_token, base_url="https://router.huggingface.co/v1", max_retries=0), HF_MODEL_ID)
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

# Deterministic source links for narrative answers: the model was told (in
# prose, via WITH_TOOLS_INSTRUCTIONS) to name and link its source, and that
# worked right up until it didn't -- an accurate, fully grounded answer with
# zero source named anywhere (confirmed live 2026-09-24). An LLM instruction
# is a request, not a guarantee. This is the guarantee: every search/read
# result search/read actually returns gets its citation link streamed as a
# widget by CODE, from the tool's own JSON, independent of what the model
# writes afterward -- the same principle the PSI widgets already use (the
# evidence card renders before the model's prose, from the query result
# directly, not from the model repeating it).
DOCS_BASE_URL = "https://marjan-ahmed.github.io/flame-freefall/docs"
_DOC_TITLES: dict[str, tuple[str, str]] = {}  # slug -> (title, heading_path)


async def _load_doc_titles() -> None:
    """One-time prefetch via outline (not the agent) so a citation card can
    show a real title, not a raw slug. Best-effort: an empty cache just means
    citation links fall back to a prettified slug, never a missing link."""
    try:
        result = await handbook_mcp.call_tool("outline", {"depth": 5})
        data = json.loads(result.content[0].text)
        for node in data.get("nodes", []):
            if node.get("kind") == "document" and node.get("slug") and node.get("heading_path"):
                _DOC_TITLES[node["slug"]] = (node.get("title") or node["slug"], node["heading_path"])
        print(f"[doc-titles] cached {len(_DOC_TITLES)} document titles")
    except Exception as exc:
        print(f"[doc-titles] prefetch failed, citation links will use slugs: {exc!r}")


def _doc_url(stable_id: str) -> str:
    return f"{DOCS_BASE_URL}/{stable_id.removeprefix('knowledge/')}"


def _doc_title(slug: str | None, fallback: str) -> str:
    if slug and slug in _DOC_TITLES:
        return _DOC_TITLES[slug][0]
    return fallback.replace("-", " ").title() if fallback else "source document"

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
BASE_INSTRUCTIONS = (
    "Assistant for Flame in Freefall: NASA microgravity-combustion test data "
    "(BASS, BASS-II, SAFFIRE I-VI, FLEX, FLEX-2, CFI, CFI-G, ACME, SPICE, "
    "SLICE, SAME) and the fire-safety standards that frame it.\n\n"
    "Greetings, thanks, and chit-chat ('hi', 'who are you', 'thanks') get "
    "a direct reply — NEVER call a tool for these, there is nothing to "
    "look up.\n\n"
    "NUMBERS COME ONLY FROM TOOLS, and every view is a widget. Pick ONE tool "
    "per question, called once with only the conditions the user gave:\n"
    "- query_test_runs: which tests exist / what was measured at some O2, "
    "flow, pressure, fuel (the default).\n"
    "- show_gap_map: what has or hasn't been tested, where the gaps are.\n"
    "- compare_investigations: comparing investigations side by side.\n"
    "- show_test_details: one named test (id like PSI-25:M18).\n"
    "- plot_results: a chart of a measured result against a condition.\n"
    "Then write the short summary the tool asks for, citing run ids. Say "
    "plainly when there is no test at the requested conditions. Never state "
    "a number that is not in a tool result, never average across tests, and "
    "never write your own table or chart. The widgets carry buttons for the "
    "next step, so you don't need to offer every option.\n\n"
)

# Told to the model ONLY while handbook_mcp is actually connected (mirrors
# assistant.mcp_servers below) — telling the model these tools exist when
# they aren't actually registered makes it try to call them anyway, which
# the Chat Completions API rejects outright ("attempted to call tool
# 'search' which was not in request.tools") and crashes the whole turn,
# not just the tool call (confirmed live 2026-09-22, MCP door unreachable).
# The PSI tools are local (read data/runs.json), so they are available in
# both modes; only the narrative corpus depends on the MCP door.
WITH_TOOLS_INSTRUCTIONS = BASE_INSTRUCTIONS + (
    "For narrative questions (why an experiment was run, how the hardware "
    "worked, what a standard requires, what the decadal surveys prioritize) "
    "use the handbook MCP tools, not general knowledge: search with k=2, "
    "read with token_budget<=600 and a specific heading. Say so if the "
    "record doesn't cover something. Be concise.\n\n"
    # A genuinely FAILED search/read call is handled unconditionally in code
    # now (ctx._guard / _guard_response_text in this file overrides the
    # reply text regardless of what's written here), so this only needs to
    # cover the one case code can't see: a search that succeeds but finds
    # nothing relevant -- still the model's own call to make honestly.
    "If search finds nothing relevant, say plainly the record doesn't cover "
    "it — never answer from general knowledge instead.\n\n"
    "Name the source document by title at least once in every narrative reply "
    "(e.g. 'per the Spacecraft Materials Fire Safety decadal-survey paper...'). "
    "A clickable link to it is added automatically below your reply — you do "
    "not need to build or write a URL yourself, just name the document in prose.\n\n"
    "HARD BUDGET: at most 3 tool calls per turn, never repeat a call — "
    "going over causes a real failure (rate limit), not just a slower answer."
)

WITHOUT_TOOLS_INSTRUCTIONS = BASE_INSTRUCTIONS + (
    "The narrative corpus connection is temporarily unavailable. "
    "The PSI test-data tools still work for test conditions and results. For "
    "narrative questions, say plainly the record can't be searched right "
    "now (do not answer from general knowledge as if it were the record) "
    "and suggest trying again shortly."
)

assistant = Agent(
    name="Flame in Freefall assistant",
    instructions=WITHOUT_TOOLS_INSTRUCTIONS,
    model=model,
    model_settings=ModelSettings(
        extra_body={"reasoning_format": "hidden"},
        # Hidden reasoning still spends this budget: at 400 a cited summary
        # was cut off mid-sentence (seen live 2026-09-24). 900 leaves room for
        # both and stays well inside Groq's 8000 TPM with the compact tool result.
        max_tokens=900,
    ),
    mcp_servers=[],
    tools=PSI_TOOLS,
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
        if tool.name in ("search", "read"):
            data = self._parse_tool_json(result)
            await self._cite_sources(ctx, tool.name, data)
            if failure := ctx._guard.record_tool_result(tool.name, data):
                print(f"[tool-health] {tool.name} failed: {failure}")
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

    def _parse_tool_json(self, result) -> dict | None:
        """search/read return their JSON payload as {"text": "<json>"} (an MCP
        tool-call result); parse it once so both citation streaming and the
        failure check below read the same object."""
        text = result.get("text") if isinstance(result, dict) else None
        if not text:
            return None
        try:
            data = json.loads(text)
        except (TypeError, ValueError):
            return None
        return data if isinstance(data, dict) else None

    async def _cite_sources(self, ctx: AgentContext, tool_name: str, data: dict | None) -> None:
        """Stream a clickable source link straight from search/read's own
        JSON -- see the comment above DOCS_BASE_URL for why this is code,
        not another prompt instruction."""
        if not data:
            return
        links: list[tuple[str, str]] = []
        if tool_name == "search" and data.get("ok"):
            for hit in data.get("hits", []):
                prov = hit.get("provenance") or {}
                stable_id = prov.get("stable_id")
                if not ctx._guard.should_cite(stable_id):
                    continue
                links.append((_doc_title(hit.get("slug") or prov.get("slug"), hit.get("slug") or ""), _doc_url(stable_id)))
        elif tool_name == "read":
            prov = data.get("provenance") or {}
            stable_id = prov.get("stable_id")
            if ctx._guard.should_cite(stable_id):
                links.append((data.get("title") or _doc_title(prov.get("slug"), prov.get("slug") or ""), _doc_url(stable_id)))
        if not links:
            return
        body = "\n".join(f"Source: [{title}]({url})" for title, url in links)
        try:
            await ctx.stream_widget(Card(children=[Markdown(value=body)]))
        except Exception as exc:
            print(f"[doc-citation] stream failed: {exc!r}")


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


# Fixed, code-authored line the user sees when a search/read call genuinely
# failed this turn (ctx._guard.should_override_reply()) -- WITH_TOOLS_INSTRUCTIONS
# already asks the model to write something like this itself, but an
# instruction is a request, not a guarantee (confirmed live 2026-09-24: the
# model answered from training knowledge instead, labeled as a "general
# explanation", after a failed search). Keep in sync with the tone of that
# prompt instruction but never rely on the model reproducing it.
TOOL_FAILURE_ABSTENTION_TEXT = (
    "The record couldn't be checked just now — the search or read call to it "
    "failed. I can't give a grounded answer to this question at the moment; "
    "please try again shortly."
)

# Streamed as a Card, not chat text, when EVERY model provider fails for a
# turn (all of Groq's keys rate-limited/quota-exhausted AND the HF fallback
# out of credits, etc.) -- confirmed live 2026-09-24 in production: this used
# to be an uncaught exception all the way up through Runner.run_streamed,
# which ChatKit's client surfaces as a bare "There was an error while
# generating the assistant's response," indistinguishable from a real bug.
# respond() below catches that case and streams this instead -- the same
# "degrade honestly instead of crashing" guarantee TOOL_FAILURE_ABSTENTION_TEXT
# already gives search/read failures, extended to a full model-call failure.
MODEL_UNAVAILABLE_TEXT = (
    "The assistant can't reach any model provider right now (rate limit or "
    "quota exhausted on every configured provider). This isn't a bug in your "
    "question — please try again in a few minutes."
)


async def _guard_response_text(
    ctx: AgentContext, events: AsyncIterator[ThreadStreamEvent],
) -> AsyncIterator[ThreadStreamEvent]:
    """Two guarantees a prompt instruction alone cannot make, both enforced
    from signals ctx._guard (turn_guard.TurnGuard) already computed during
    the run -- the same "render from code, not from what the model says"
    principle the citation cards above already use. This function's own job
    is ONLY the chatkit wire-event matching; all classification logic lives
    in TurnGuard.

    1. If ctx._guard.should_override_reply() is set (a search/read call
       genuinely failed this turn), every piece of the model's own final
       text is swapped for TOOL_FAILURE_ABSTENTION_TEXT. on_tool_end always
       runs before the model's follow-up text is generated in the same
       turn, so by the time any assistant-message text event reaches this
       wrapper the flag, if it's going to be set at all, already is --
       there is no race.

    2. Otherwise, if query_test_runs ran this turn, the model's finished
       text is checked for a cited run id that isn't in the payload it was
       given. Unlike case 1 this is left as a loud server-log warning
       rather than a text edit: surgically removing one fabricated citation
       from a token stream that already reached the client is a much
       larger change to this streaming path than swapping the whole
       message, so detection stops here for now rather than risking the
       success path."""
    replaced_indices: set[int] = set()
    async for event in events:
        update = getattr(event, "update", None)
        utype = getattr(update, "type", None)
        if utype == "assistant_message.content_part.text_delta":
            if ctx._guard.should_override_reply():
                idx = update.content_index
                if idx not in replaced_indices:
                    replaced_indices.add(idx)
                    update.delta = TOOL_FAILURE_ABSTENTION_TEXT
                else:
                    update.delta = ""
        elif utype == "assistant_message.content_part.done":
            if ctx._guard.should_override_reply():
                update.content.text = TOOL_FAILURE_ABSTENTION_TEXT
            else:
                fabricated = ctx._guard.check_citations(update.content.text or "")
                if fabricated:
                    print(f"[citation-check] fabricated run id(s) in reply, not present in "
                          f"query_test_runs payload: {sorted(fabricated)} (valid ids this turn: "
                          f"{sorted(ctx._guard.valid_run_ids)})")
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


# Widget buttons → the widget they open. Answered by the server directly: no
# model call, no tokens, instant — the user steers the data from the chat.
def _action_widget(kind: str, payload: dict, site: str | None = None):
    q = _clean_query(payload.get("q") or {})
    if kind == "evidence":
        return psi_widgets.evidence_widget(q, site=site)
    if kind == "gap_map":
        y = payload.get("y") if payload.get("y") in psi_widgets.Y_BINS else "flow_cm_s"
        return psi_widgets.gap_map_widget(q, y)
    if kind == "compare":
        return psi_widgets.compare_widget(q)
    if kind == "results":
        x = payload.get("x") if payload.get("x") in psi_widgets.X_AXES else "flow_cm_s"
        quantity = payload.get("quantity") if isinstance(payload.get("quantity"), str) else None
        return psi_widgets.results_widget(q, quantity, x)
    if kind == "test" and isinstance(payload.get("id"), str):
        return psi_widgets.test_widget(payload["id"], site=site)
    return None


# Base URLs of the sites that host this chat. A cross-origin fetch sends only
# the ORIGIN (no path) in Origin/Referer, so the GitHub Pages base path
# (/flame-freefall) cannot be read from the request: the request's Origin picks
# the matching entry here instead. Without this, "Open in the Explorer" links
# pointed at localhost for every real user (found 2026-09-24).
SITE_URLS = [
    u.strip().rstrip("/")
    for u in os.environ.get(
        "SITE_URLS", "http://localhost:3000,https://marjan-ahmed.github.io/flame-freefall"
    ).split(",")
    if u.strip()
]


def _site_for(request: Request) -> str | None:
    origin = (request.headers.get("origin") or "").rstrip("/")
    if not origin:
        referer = request.headers.get("referer") or ""
        parts = referer.split("/")
        origin = "/".join(parts[:3]) if len(parts) >= 3 else ""
    for url in SITE_URLS:
        if origin and (url == origin or url.startswith(origin + "/")):
            return url
    return None


def _clean_query(raw: dict) -> dict:
    """Action payloads come back from the browser: keep only known keys with
    well-typed values, never pass anything else into the query."""
    q = {}
    for k, v in raw.items():
        if k in psi_widgets.psi_query.NUMERIC_AXES:
            try:
                q[k] = float(v)
            except (TypeError, ValueError):
                continue
        elif k in psi_widgets.psi_query.CATEGORICAL_AXES and isinstance(v, str) and len(v) < 80:
            q[k] = v
    return q


class FlameFreefallChatKitServer(ChatKitServer[dict]):
    async def sync_action(self, thread, action, sender, context):
        """Sync (streaming=False) actions update the widget that was clicked,
        in place: ChatKit replaces it with `updated_item`. Used by an evidence
        card's Details / Hide details buttons."""
        payload = action.payload or {}
        kind = str(action.type).removeprefix("psi.")
        if kind != "expand" or sender is None:
            print(f"[sync_action] ignored {action.type!r}")
            return SyncCustomActionResponse()
        run_id = payload.get("id") if isinstance(payload.get("id"), str) else None
        try:
            widget = psi_widgets.evidence_widget(
                _clean_query(payload.get("q") or {}),
                site=(context or {}).get("site"),
                expanded=run_id if payload.get("open") else None,
            )
        except Exception as exc:  # keep the card as it was rather than fail the click
            print(f"[sync_action] expand failed: {exc!r}")
            return SyncCustomActionResponse(updated_item=sender)
        updated = sender.model_copy(update={"widget": widget})
        await self.store.save_item(thread.id, updated, context=context)
        print(f"[sync_action] expand {run_id} open={bool(payload.get('open'))}")
        return SyncCustomActionResponse(updated_item=updated)

    async def action(self, thread, action, sender, context):
        kind = str(action.type).removeprefix("psi.")
        try:
            widget = _action_widget(kind, action.payload or {}, (context or {}).get("site"))
        except Exception as exc:  # a button must never spin forever: answer with the failure
            print(f"[action] {kind} failed: {exc!r}")
            widget = Card(children=[Text(value="Sorry, that view could not be opened.", size="sm"),
                                    Caption(value=f"{kind}: {type(exc).__name__}", size="sm")])
        if widget is None:
            print(f"[action] unknown {action.type!r}")
            widget = Card(children=[Text(value="That button is not recognised by this server version.", size="sm")])
        print(f"[action] {kind} {action.payload}")
        async for event in stream_widget(
            thread, widget, None, lambda item_type: self.store.generate_item_id(item_type, thread, context)
        ):
            yield event

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
        agent_context._guard = TurnGuard()  # type: ignore[attr-defined]
        result = Runner.run_streamed(assistant, input_items, context=agent_context, hooks=tool_call_hooks)

        # Started before the main stream, awaited after: title generation
        # runs concurrently with the real answer rather than adding latency
        # to it. thread.title update()s the SAME object the "thread not
        # found" check above already validated — save_thread persists it,
        # and chatkit's own protocol layer emits the ThreadUpdatedEvent the
        # client's history list picks up.
        title_task = asyncio.create_task(self._maybe_update_thread_title(thread, context))
        try:
            async for event in _guard_response_text(
                agent_context, _uniquify_fake_item_ids(stream_agent_response(agent_context, result))
            ):
                yield event
        except Exception as exc:
            # Every configured model provider failed this turn (all Groq
            # (key, model) pairs exhausted, HF fallback also exhausted, etc.)
            # -- confirmed live 2026-09-24 in production: this used to
            # propagate uncaught all the way through Runner.run_streamed,
            # which ChatKit's client shows as a bare "There was an error
            # while generating the assistant's response," indistinguishable
            # from a real bug. Same "degrade honestly, never crash the chat"
            # guarantee TOOL_FAILURE_ABSTENTION_TEXT already gives search/read
            # failures, extended to a full model-call failure. Streamed as a
            # plain assistant message, not a Card -- this is a normal chat
            # reply the user should be able to read like any other answer,
            # not a distinct widget component (the widgets are reserved for
            # actual PSI evidence/data, per the user's own feedback).
            print(f"[respond] every model provider failed: {exc!r}")
            yield ThreadItemDoneEvent(
                item=AssistantMessageItem(
                    id=self.store.generate_item_id("message", thread, context),
                    thread_id=thread.id,
                    content=[AssistantMessageContent(text=MODEL_UNAVAILABLE_TEXT, annotations=[])],
                    created_at=datetime.now(),
                )
            )
        await title_task

    async def _maybe_update_thread_title(self, thread: ThreadMetadata, context: dict) -> None:
        # Whole body guarded, not just the LLM call — a Postgres hiccup here
        # (e.g. Neon waking from idle) must never surface anywhere; this is
        # cosmetic background work, run as a fire-and-forget task and
        # awaited only to prevent an orphaned task, never something a chat
        # response's success should depend on (confirmed live 2026-09-22).
        try:
            if thread.title is not None:
                return
            items_page = await self.store.load_thread_items(
                thread.id, after=None, limit=6, order="desc", context=context
            )
            if not items_page.data:
                return
            title = await generate_short_title(items_page.data)
            if not title:
                return
            thread.title = title
            await self.store.save_thread(thread, context=context)
        except Exception as exc:
            print(f"[thread-title] update failed: {exc}")


# Initialize Postgres store (falls back to in-memory if DB not configured)
def _make_store():
    if os.environ.get("KSOR_DB_URL") or os.environ.get("DATABASE_URL"):
        return PostgresChatKitStore()
    return InMemoryChatKitStore()


server = FlameFreefallChatKitServer(store=_make_store(), attachment_store=attachment_store)


@asynccontextmanager
async def lifespan(_app: FastAPI):
    # A hard failure to connect here used to crash the ENTIRE app at boot
    # (every request, including /health, 500ing with FUNCTION_INVOCATION_FAILED)
    # whenever the MCP door was unreachable — e.g. HANDBOOK_MCP_URL unset/
    # defaulting to localhost in a serverless environment, or ksor serve
    # briefly asleep on a free-tier host. Confirmed live 2026-09-22. A chat
    # that never needs a tool call (a greeting, "who are you") has no reason
    # to depend on the corpus door being up — only an actual tool call
    # should fail, and only for that one request.
    # Catching the connect failure alone wasn't enough — the assistant still
    # listed handbook_mcp in mcp_servers, and Runner.run_streamed calls
    # get_mcp_tools() on every run (to enumerate tools for the model)
    # regardless of whether the turn needs one, which throws "Server not
    # initialized" on an unconnected server — turning EVERY message into a
    # stream.error, not just tool-needing ones (confirmed live 2026-09-22).
    # The assistant only gets the tool once it actually has a live session.
    try:
        async with handbook_mcp:
            assistant.mcp_servers = [handbook_mcp]
            assistant.instructions = WITH_TOOLS_INSTRUCTIONS
            await _load_doc_titles()
            yield
    except Exception as exc:
        print(f"[handbook-mcp] connect failed at startup, continuing without corpus tools: {exc}")
        assistant.mcp_servers = []
        assistant.instructions = WITHOUT_TOOLS_INSTRUCTIONS
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
    result = await server.process(await request.body(), context={"site": _site_for(request)})
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
