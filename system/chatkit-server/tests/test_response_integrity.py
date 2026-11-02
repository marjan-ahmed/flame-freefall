"""Exercise the real ChatKit event boundary, without a model or network."""

import asyncio
from datetime import datetime
from types import SimpleNamespace

from chatkit.types import (
    AssistantMessageContent, AssistantMessageContentPartDone,
    AssistantMessageContentPartTextDelta, AssistantMessageItem,
    ThreadItemDoneEvent, ThreadItemUpdatedEvent,
)
import pytest

import main
from turn_guard import TurnGuard


def _events(text):
    return [
        ThreadItemUpdatedEvent(item_id="msg_test", update=AssistantMessageContentPartTextDelta(
            content_index=0, delta=text[:10])),
        ThreadItemUpdatedEvent(item_id="msg_test", update=AssistantMessageContentPartTextDelta(
            content_index=0, delta=text[10:])),
        ThreadItemUpdatedEvent(item_id="msg_test", update=AssistantMessageContentPartDone(
            content_index=0, content=AssistantMessageContent(text=text))),
        ThreadItemDoneEvent(item=AssistantMessageItem(
            id="msg_test", thread_id="thr_test", created_at=datetime.now(),
            content=[AssistantMessageContent(text=text)])),
    ]


def _run(guard, text):
    async def execute():
        async def source():
            for event in _events(text):
                yield event
        return [e async for e in main._guard_response_text(SimpleNamespace(_guard=guard), source())]
    return asyncio.run(execute())


@pytest.mark.parametrize("text", ["Spread 0.026 mm/s (PSI-25:invented)",
                                  "Spread 99999 mm/s (PSI-25:M18)",
                                  "Spread 17.9 mm/s (PSI-25:M18)"])
def test_fabrication_never_reaches_stream_or_final_item(text):
    guard = TurnGuard()
    guard.record_valid_run_ids({"PSI-25:M18"})
    output = _run(guard, text)
    serialized = " ".join(e.model_dump_json() for e in output)
    assert text not in serialized
    assert "99999" not in serialized
    assert "invented" not in serialized
    assert output[0].update.delta == main.CITATION_FAILURE_TEXT
    assert output[-1].item.content[0].text == main.CITATION_FAILURE_TEXT


def test_percent_and_time_units_are_checked():
    guard = TurnGuard()
    guard.record_valid_run_ids({"PSI-25:M18"})
    assert guard.check_citations("Oxygen 99% (PSI-25:M18)")
    assert guard.check_citations("Burn time 99999 s (PSI-25:M18)")


def test_verified_citation_survives_checked_release():
    guard = TurnGuard()
    guard.record_valid_run_ids({"PSI-25:M18"})
    text = "Spread 0.026 mm/s (PSI-25:M18)"
    output = _run(guard, text)
    assert len(output) == 3  # one validated text delta, part done, item done
    assert output[0].update.delta == text
    assert output[-1].item.content[0].text == text


def test_zero_results_does_not_allow_invented_citations():
    guard = TurnGuard()
    guard.record_valid_run_ids(set())
    output = _run(guard, "Found a test (PSI-25:M18)")
    assert output[-1].item.content[0].text == main.CITATION_FAILURE_TEXT


def test_invalid_condition_gets_specific_deterministic_refusal():
    guard = TurnGuard()
    guard.record_tool_result("query_test_runs", {"error": "invalid_arguments"})
    output = _run(guard, "No tests exist for your conditions.")
    assert output[0].update.delta == main.INVALID_QUERY_TEXT
    assert output[-1].item.content[0].text == main.INVALID_QUERY_TEXT


def test_psi_numerical_and_safety_claims_never_depend_on_model_prose():
    guard = TurnGuard()
    guard.record_psi_tool("rank_results")
    text = "PMMA is safe for a lunar habitat and burns at 12345 mm/s."
    output = _run(guard, text)
    assert text not in " ".join(e.model_dump_json() for e in output)
    assert output[0].update.delta == main.PSI_EVIDENCE_HANDOFF_TEXT
    assert output[-1].item.content[0].text == main.PSI_EVIDENCE_HANDOFF_TEXT
