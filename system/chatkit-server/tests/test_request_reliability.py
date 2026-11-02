"""Real chat failure regressions: intent binding and code-owned PSI text.

These tests exercise the actual FunctionTool invocation and ChatKit event
types, not just a prompt or a separately reimplemented filter.
"""
from __future__ import annotations

import asyncio
from datetime import datetime
import json
from pathlib import Path
import sys
from types import SimpleNamespace
import uuid

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main
import psi_atmospheres
import psi_query
import psi_tools
from request_intent import parse_request
from turn_guard import TurnGuard
from chatkit.types import (AssistantMessageContent, AssistantMessageItem,
                           ThreadItemAddedEvent, ThreadItemDoneEvent,
                           ThreadItemUpdatedEvent, AssistantMessageContentPartTextDelta,
                           AssistantMessageContentPartDone)


def invoke(text, args, monkeypatch):
    widgets, queries = [], []
    actual_query = psi_query.query

    def capture(q, *a, **kw):
        queries.append(q)
        return actual_query(q, *a, **kw)

    monkeypatch.setattr(psi_query, "query", capture)

    async def stream(widget):
        widgets.append(widget.model_dump_json())

    from agents.tool_context import ToolContext
    raw = json.dumps(args)
    guard = TurnGuard(request_text=text)
    ctx = SimpleNamespace(_guard=guard, thread=SimpleNamespace(id="thr_" + uuid.uuid4().hex), request_context={}, stream_widget=stream)
    result = asyncio.run(psi_tools.query_test_runs.on_invoke_tool(
        ToolContext(context=ctx, tool_name="query_test_runs", tool_call_id="test", tool_arguments=raw), raw))
    return queries, widgets, result, guard


def test_exact_live_prompt_cannot_add_pressure_geometry_or_flow_direction(monkeypatch):
    queries, widgets, result, guard = invoke(
        "Find PMMA tests at 15% oxygen and 10 cm/s. Show the evidence widget.",
        {"o2_pct": 15, "flow_cm_s": 10, "pressure_atm": 1, "fuel_family": "PMMA", "geometry_class": "solid-fuel", "flow_direction": "opposed"}, monkeypatch)
    assert queries == [{"o2_pct": 15, "flow_cm_s": 10, "fuel_family": "PMMA"}]
    assert guard.psi_tool_used
    correction = widgets[0]
    assert "pressure_atm" in correction and "geometry_class" in correction and "flow_direction" in correction
    assert "Only the displayed filters were applied" in correction
    assert "Widget shown" in result


@pytest.mark.parametrize("text", ["Find FLEX tests aboard ISS", "Find FLEX tests aboard ISS for methanol"])
def test_experiment_platform_is_not_an_atmosphere_preset(text):
    intent = parse_request(text)
    assert not intent.errors
    assert intent.atmosphere is None
    assert "pressure_atm" not in intent.query and "o2_pct" not in intent.query


@pytest.mark.parametrize("text", ["Find tests at 15% oxygen excluding PMMA", "Find PMMA tests not opposed", "Find PMMA tests with spread rate 34 mm/s"])
def test_negation_and_outcome_rates_cannot_be_positive_condition_filters(text, monkeypatch):
    queries, widgets, *_ = invoke(text, {"fuel_family": "PMMA", "flow_cm_s": 34}, monkeypatch)
    assert not queries
    assert "No query was executed" in widgets[0]


def test_gap_map_cannot_add_unrequested_pressure_or_direction(monkeypatch):
    from agents.tool_context import ToolContext
    widgets = []
    captured = []
    def summary(q, axis):
        captured.append(q)
        return {}
    monkeypatch.setattr(psi_tools.psi_widgets, "gap_map_summary", summary)
    monkeypatch.setattr(psi_tools.psi_widgets, "gap_map_widget", lambda *a: psi_tools.Card(children=[]))
    async def stream(widget):
        widgets.append(widget.model_dump_json())
    guard = TurnGuard(request_text="Show PMMA coverage by oxygen and flow")
    ctx = SimpleNamespace(_guard=guard, thread=SimpleNamespace(id="thr_" + uuid.uuid4().hex), request_context={}, stream_widget=stream)
    raw = json.dumps({"fuel_family": "PMMA", "pressure_atm": 1, "flow_direction": "opposed"})
    asyncio.run(psi_tools.show_gap_map.on_invoke_tool(ToolContext(context=ctx, tool_name="show_gap_map", tool_call_id="test", tool_arguments=raw), raw))
    assert captured == [{"fuel_family": "PMMA"}]
    assert "Applied request filters" in widgets[0]


def test_details_cannot_substitute_a_different_real_record(monkeypatch):
    from agents.tool_context import ToolContext
    widgets = []
    async def stream(widget):
        widgets.append(widget.model_dump_json())
    ctx = SimpleNamespace(_guard=TurnGuard(request_text="Inspect PSI-25:M18"), thread=SimpleNamespace(id="thr_details"), request_context={}, stream_widget=stream)
    raw = json.dumps({"run_id": "PSI-25:M19"})
    result = asyncio.run(psi_tools.show_test_details.on_invoke_tool(ToolContext(context=ctx, tool_name="show_test_details", tool_call_id="test", tool_arguments=raw), raw))
    assert "no query was executed" in result
    assert "No unrequested record was selected" in widgets[0]


def test_model_omission_or_numeric_substitution_is_corrected_to_user_text(monkeypatch):
    queries, widgets, *_ = invoke("Find PMMA tests at oxygen 15 percent and flow 10 cm/s.", {"o2_pct": 21}, monkeypatch)
    assert queries == [{"o2_pct": 15, "flow_cm_s": 10, "fuel_family": "PMMA"}]
    assert "corrected from your message" in widgets[0]


@pytest.mark.parametrize("text,expected", [
    ("PMMA at O2=15% and 0.1 m/s, 56.5 kPa", {"o2_pct": 15, "flow_cm_s": 10, "pressure_atm": 56.5 * psi_atmospheres.ATM_PER_KPA, "fuel_family": "PMMA"}),
    ("methanol at 21% oxygen and 1 atm with 100 mm/s flow", {"o2_pct": 21, "flow_cm_s": 10, "pressure_atm": 1, "fuel_family": "methanol"}),
    ("BASS II opposed solid-fuel tests at 14.7 psia", {"pressure_atm": 14.7 * psi_atmospheres.ATM_PER_PSIA, "geometry_class": "solid-fuel", "flow_direction": "opposed", "investigation": "bass-ii"}),
    ("Find PMMA* tests", {"fuel_family": "PMMA*"}),
])
def test_explicit_supported_wording_and_units(text, expected):
    intent = parse_request(text)
    assert not intent.errors, intent.errors
    assert intent.query == expected


@pytest.mark.parametrize("name", ["ISS", "Gateway", "Lunar atmosphere", "Moon"])
def test_named_atmospheres_use_existing_cited_preset_and_no_extra_conditions(name):
    intent = parse_request(f"Find PMMA tests for {name}")
    assert not intent.errors
    expected = psi_atmospheres.query_for(intent.atmosphere)
    assert intent.query == {**expected, "fuel_family": "PMMA"}


@pytest.mark.parametrize("text", ["Find PMMA tests at fifteen oxygen", "PMMA at 15 oxygen", "PMMA at 15-20% oxygen", "PMMA below 15% oxygen", "PMMA at 15% oxygen and 10 furlongs/hour", "PMMA near Mars", "PMMA at NaN atm", "PMMA at 101% oxygen", "PMMA at 15% oxygen and 21% oxygen", "the same conditions as before"])
def test_ambiguous_unparseable_or_out_of_range_requests_do_not_execute(text, monkeypatch):
    queries, widgets, result, _ = invoke(text, {"o2_pct": 15, "fuel_family": "PMMA"}, monkeypatch)
    assert queries == []
    assert "No query was executed" in widgets[0]
    assert "no query was executed" in result


def test_unknown_requested_fuel_cannot_be_silently_dropped(monkeypatch):
    queries, widgets, *_ = invoke("Find unobtainium tests at 15% oxygen", {"o2_pct": 15, "fuel_family": "unobtainium"}, monkeypatch)
    assert not queries
    assert "no broader query was run" in widgets[0]


def _assistant(text, item_id="msg_test"):
    return AssistantMessageItem(id=item_id, thread_id="thr_test", created_at=datetime.now(), content=[AssistantMessageContent(text=text, annotations=[])])


def test_synthetic_quantity_unit_error_and_pre_tool_numeric_prose_never_escape():
    guard = TurnGuard(request_text="Find evidence")
    guard.record_valid_run_ids({"acme-bre:19070D1"})
    fabricated = "The spread rate is 34 mm/s (acme-bre:19070D1)."
    # The quantity/unit regression is caught by the improved diagnostic too;
    # output safety no longer depends on the model supplying a checkable id.
    assert guard.check_citations(fabricated)
    ctx = SimpleNamespace(_guard=guard, thread=SimpleNamespace(id="thr_test"))

    async def events():
        yield ThreadItemAddedEvent(item=_assistant(fabricated))
        yield ThreadItemUpdatedEvent(item_id="msg_test", update=AssistantMessageContentPartTextDelta(content_index=0, delta="Also 999 mm/s (PSI-25)."))
        guard.record_psi_tool("query_test_runs")  # Recognition occurs AFTER early model text.
        yield ThreadItemUpdatedEvent(item_id="msg_test", update=AssistantMessageContentPartDone(content_index=0, content=AssistantMessageContent(text=fabricated, annotations=[])))
        yield ThreadItemDoneEvent(item=_assistant(fabricated))

    async def collect():
        return [e async for e in main._guard_response_text(ctx, events())]

    out = asyncio.run(collect())
    wire = " ".join(e.model_dump_json() for e in out)
    assert "34 mm/s" not in wire and "999 mm/s" not in wire and "acme-bre:19070D1" not in wire and "(PSI-25)" not in wire
    assert main.PSI_EVIDENCE_HANDOFF_TEXT in wire
    assert out[-1].item.content[0].text == main.PSI_EVIDENCE_HANDOFF_TEXT


def test_narrative_only_text_remains_available_with_source_cards():
    guard = TurnGuard(request_text="Why was SAME run?")
    ctx = SimpleNamespace(_guard=guard)
    original = ThreadItemDoneEvent(item=_assistant("SAME characterized aerosols; consult its source record."))

    async def events():
        yield original

    async def collect():
        return [e async for e in main._guard_response_text(ctx, events())]

    out = asyncio.run(collect())
    assert out[0].item.content[0].text == original.item.content[0].text


def test_respond_binds_only_current_user_text_not_prior_turn(monkeypatch):
    from chatkit.types import InferenceOptions, ThreadMetadata, UserMessageItem, UserMessageTextContent
    from store import InMemoryChatKitStore
    captured = []

    def stop(_agent, _items, **kwargs):
        captured.append(kwargs["context"]._guard.request_text)
        raise RuntimeError("stop without model call")

    monkeypatch.setattr(main.Runner, "run_streamed", stop)

    async def run():
        store = InMemoryChatKitStore()
        server = main.FlameFreefallChatKitServer(store=store, attachment_store=main.attachment_store)
        thread = ThreadMetadata(id="thr_test", created_at=datetime.now(), title="existing")
        await store.save_thread(thread, {})
        for text in ["Use opposed flow at 1 atm", "Find PMMA tests at 15% oxygen and 10 cm/s"]:
            msg = UserMessageItem(id="user_" + uuid.uuid4().hex, thread_id=thread.id, created_at=datetime.now(), content=[UserMessageTextContent(text=text)], inference_options=InferenceOptions())
            await store.add_thread_item(thread.id, msg, {})
        with pytest.raises(RuntimeError, match="stop"):
            async for _ in server.respond(thread, msg, {}):
                pass

    asyncio.run(run())
    assert captured == ["Find PMMA tests at 15% oxygen and 10 cm/s"]
