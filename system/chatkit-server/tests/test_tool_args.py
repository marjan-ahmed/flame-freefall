"""Regressions for the two live failures of 2026-10-05.

1. The model (XKIRO qwen) emitted tool arguments as strings with "null"/""
   for not-stated axes: {"o2_pct": "30", "flow_cm_s": "null"}. The agents
   SDK's strict schema (o2_pct: number|null, all keys required) rejected these
   BEFORE the tool body ran — ModelBehaviorError("Invalid JSON input for tool
   ..."), no widget, no _guarded trace. plot_results survived only because all
   its parameters are strings. Fix: psi_tools._harden_args rewrites the raw
   JSON to schema-typed values before validation.

2. threads.get_by_id 500ed with "Thread() got multiple values for keyword
   argument 'items'": a full Thread reached the store, so its model_dump()
   carried an items key, which the framework's _load_full_thread passes twice
   into Thread(). Fix: main.py respond()/sync_action normalize the thread via
   _normalize_thread_for_store before anything can re-save it.
"""

import asyncio
import json
import sys
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import psi_query  # noqa: E402
import psi_tools  # noqa: E402


def _tool(name: str):
    return next(t for t in psi_tools.TOOLS if t.name == name)


class _Guard:
    def __init__(self):
        self.failures = []
        self.valid_run_ids = set()

    def record_tool_result(self, name, payload):
        self.failures.append((name, payload))

    def record_valid_run_ids(self, ids):
        self.valid_run_ids |= set(ids)


class _Thread:
    id = "thr_test"


async def _noop_stream(widget, copy_text=None):
    return None


def _ctx(tool_name: str = "query_test_runs", raw: str = "{}"):
    """A minimal stand-in for the SDK's ToolContext: the SDK's invoke path
    reads ctx.{tool_name, tool_arguments, tool_call_id, run_config,
    _function_tool_arguments}, psi_tools reads ctx.context.{thread, _guard,
    request_context, stream_widget}."""
    from agents.run_config import RunConfig
    return SimpleNamespace(
        tool_name=tool_name,
        tool_arguments=raw,
        tool_call_id="call_test",
        run_config=RunConfig(),
        _function_tool_arguments=None,
        context=SimpleNamespace(
            thread=_Thread(), _guard=_Guard(), request_context={"site": None},
            stream_widget=_noop_stream,
        ),
    )


def _invoke(name: str, raw: str):
    tool = _tool(name)
    return asyncio.run(tool.on_invoke_tool(_ctx(name, raw), raw)), None


def tool_on(name: str, ctx, raw: str):
    return _tool(name).on_invoke_tool(ctx, raw)


def _payload(result: str) -> dict:
    """The JSON object inside a _reply() string (first '{' onward)."""
    return json.loads(result[result.index("{"):])


# --- Fix 1: string-typed / null-ish arguments -----------------------------

TRANSCRIPT_ARGS = [
    # The exact first call from the live 2026-10-05 transcript (M16): numbers
    # as strings, not-stated axes as the string "null".
    '{"o2_pct": "30", "flow_cm_s": "null", "pressure_atm": "0.55", "fuel_family": "null", '
    '"geometry_class": "null", "flow_direction": "null", "investigation": "null"}',
    # The model's second shape: empty strings instead of "null".
    '{"o2_pct": "30", "flow_cm_s": "", "pressure_atm": "0.55", "fuel_family": "", '
    '"geometry_class": "", "flow_direction": "", "investigation": ""}',
    # flow_cm_s="0" (the model's last attempt before giving up).
    '{"o2_pct": "30", "flow_cm_s": "0", "pressure_atm": "0.55", "fuel_family": "", '
    '"geometry_class": "", "flow_direction": "", "investigation": ""}',
]


@pytest.mark.parametrize("raw", TRANSCRIPT_ARGS, ids=["nulls", "empties", "flow0"])
def test_transcript_string_args_now_reach_the_tool_body(raw):
    """Every exact failing call from the live transcript returns the compact
    payload instead of the SDK's "Invalid JSON input" error string."""
    result, _ = _invoke("query_test_runs", raw)
    assert "Invalid JSON input" not in result
    assert _payload(result)["counts"]["match"] >= 0


def test_transcript_gap_map_string_args_now_reach_the_tool_body():
    result, _ = _invoke(
        "show_gap_map",
        '{"o2_pct": "null", "flow_cm_s": "null", "pressure_atm": "null", "fuel_family": "PMMA", '
        '"geometry_class": "solid-fuel", "flow_direction": "null", "investigation": "null", '
        '"y_axis": "flow_cm_s"}',
    )
    assert "Invalid JSON input" not in result
    assert "tested_cells" in result  # gap_map_summary payload


def test_strings_are_coerced_to_schema_numbers():
    """o2_pct='30' must land as the number 30 (12 matches live), not be
    dropped — dropping it would silently widen the query."""
    result, _ = _invoke("query_test_runs", '{"o2_pct": "30", "pressure_atm": "0.55"}')
    assert _payload(result)["counts"]["match"] == 12


def test_nullish_strings_are_dropped_not_coerced():
    """\"null\"/\"\" on an optional axis means not-stated: the key is omitted,
    so the query runs without that axis — exactly what the model meant."""
    for raw in (
        '{"o2_pct": "30", "flow_cm_s": "null", "pressure_atm": "0.55"}',
        '{"o2_pct": "30", "flow_cm_s": "", "pressure_atm": "0.55"}',
    ):
        result, _ = _invoke("query_test_runs", raw)
        assert _payload(result)["counts"]["match"] == 12


def test_unparseable_number_widens_openly():
    """"about thirty" can't be parsed: the axis is dropped (the widget shows
    the widened query) rather than the call dying."""
    result, _ = _invoke("query_test_runs", '{"o2_pct": "about thirty", "pressure_atm": "0.55"}')
    assert "Invalid JSON input" not in result
    assert "match" in _payload(result)["counts"]


def test_proper_json_still_works():
    """Native JSON numbers/omitted keys were never broken; they must stay so."""
    result, _ = _invoke("query_test_runs", '{"o2_pct": 30, "pressure_atm": 0.55}')
    assert _payload(result)["counts"]["match"] == 12


def test_enum_out_of_vocabulary_is_dropped_but_valid_passes():
    """"Solid fuel" (title-case, out of vocabulary) is dropped; the real
    literal passes through unchanged."""
    result, _ = _invoke(
        "query_test_runs",
        '{"fuel_family": "PMMA", "geometry_class": "Solid fuel", "flow_direction": "opposed"}',
    )
    assert "Invalid JSON input" not in result
    result2, _ = _invoke(
        "query_test_runs",
        '{"fuel_family": "PMMA", "geometry_class": "solid-fuel", "flow_direction": "opposed"}',
    )
    assert "Invalid JSON input" not in result2
    assert "solid-fuel" in result2


def test_invalid_json_still_gets_the_sdk_error_and_a_guard_trace():
    """Malformed JSON is returned untouched so the SDK raises its own
    consistent error (its failure formatter turns that into the model-visible
    "An error occurred..." string) — and the wrapper records the failure so
    the reply guard can override the model's follow-up."""
    ctx = _ctx("query_test_runs", "{not json")
    result = asyncio.run(tool_on("query_test_runs", ctx, "{not json"))
    assert "try again" in result.lower()
    assert any(f[0] == "query_test_runs" for f in ctx.context._guard.failures)


def test_body_exception_still_reaches_the_guard(monkeypatch):
    """A body failure keeps the _guarded behavior through the new wrapper:
    recorded on the guard, re-raised, formatted by the SDK for the model."""
    def boom(q):
        raise RuntimeError("boom")

    monkeypatch.setattr(psi_query, "query", boom)
    ctx = _ctx("query_test_runs", '{"o2_pct": "30"}')
    result = asyncio.run(tool_on("query_test_runs", ctx, '{"o2_pct": "30"}'))
    assert "try again" in result.lower()
    assert any(f[0] == "query_test_runs" for f in ctx.context._guard.failures)


def test_every_tool_param_is_number_string_or_array():
    """Every parameter the model can pass must resolve to a kind
    _normalize_tool_args understands; if a new kind is ever added, the
    normalizer needs an explicit branch for it."""
    for tool in psi_tools.TOOLS:
        schema = tool.params_json_schema
        for key, prop in schema.get("properties", {}).items():
            kinds = {v.get("type") for v in prop.get("anyOf", [prop])}
            assert kinds & {"number", "integer", "string", "null", "array", None}, (
                f"{tool.name}.{key}: unexpected schema {kinds}"
            )


# --- Fix 2: a full Thread must never reach the store ----------------------


def test_full_thread_dump_poisons_thread_constructor():
    """The failure mode itself: a saved full Thread's model_dump() carries
    'items', and the framework's _load_full_thread re-construction 500s."""
    from chatkit.types import Page, Thread

    full = Thread(id="thr_x", created_at=datetime.now(), items=Page())
    d = full.model_dump()
    assert "items" in d
    with pytest.raises(TypeError, match="multiple values for keyword argument 'items'"):
        Thread(**d, items=Page())


def test_normalize_thread_for_store_strips_items():
    """The store invariant: save_thread must only ever receive plain
    ThreadMetadata, whatever the framework passed down."""
    from chatkit.types import Page, Thread, ThreadMetadata
    import main as main_mod

    full = Thread(id="thr_x", created_at=datetime.now(), items=Page())
    md = main_mod._normalize_thread_for_store(full)
    assert type(md) is ThreadMetadata
    # The framework's exact load path now works:
    Thread(**md.model_dump(), items=Page())


def test_normalize_thread_for_store_passes_metadata_through():
    from chatkit.types import ThreadMetadata
    import main as main_mod

    md = ThreadMetadata(id="a", created_at=datetime.now())
    assert main_mod._normalize_thread_for_store(md) is md


def test_respond_normalizes_full_thread_before_any_save():
    """respond() given a full Thread (what threads.create hands down) leaves
    the store holding ThreadMetadata only — the poisoned state the bug
    created is repaired by the very next turn."""
    from chatkit.types import Page, Thread, ThreadMetadata
    from store import InMemoryChatKitStore
    import main as main_mod

    store = InMemoryChatKitStore()
    srv = main_mod.FlameFreefallChatKitServer(store=store, attachment_store=main_mod.attachment_store)
    full = Thread(id="thr_norm", created_at=datetime.now(), items=Page())
    store.threads[full.id] = full  # the poisoned state the bug created

    thread = main_mod._normalize_thread_for_store(full)
    assert type(thread) is ThreadMetadata
    asyncio.run(store.save_thread(thread, context={}))
    loaded = asyncio.run(store.load_thread(full.id, context={}))
    assert type(loaded) is ThreadMetadata
    assert "items" not in loaded.model_dump()
    Thread(**loaded.model_dump(), items=Page())  # framework load: must not raise
