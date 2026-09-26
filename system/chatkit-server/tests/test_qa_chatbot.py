"""Deterministic gaps found by the chatbot-qa live pass (2026-09-27), pinned
without the network.

turn_guard.check_citations() is the server-side check that a run id the
model cites in prose was really in that turn's query_test_runs payload. Its
regex only recognises "(PSI-<digits>:<[A-Za-z0-9._-]+>)" with an ASCII
hyphen and one id per parenthesis, so it is blind to:
  - ids containing a space (1084 of 1948 real ids, e.g. "PSI-159:21088 B1",
    "PSI-26:As-run 1") and ids without a PSI- prefix (12: "flex:", "spice:",
    "saffire-iv-vi:");
  - the live model's typography: gpt-oss-120b writes run ids with U+2011
    NON-BREAKING HYPHEN ("PSI‑25:M18"), seen live in this pass;
  - several ids in one parenthesis, "(PSI-25:M18, PSI-25:M99)".
A fabricated id in any of those shapes is never flagged. Marked xfail(strict)
so the suite stays green today and turns red (XPASS) the moment the guard is
fixed, prompting removal of the marker.
"""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from turn_guard import TurnGuard  # noqa: E402

DATA = Path(__file__).resolve().parents[1] / "data" / "runs.json"


def _guard(valid: set[str]) -> TurnGuard:
    g = TurnGuard()
    g.record_valid_run_ids(valid)
    return g


def test_ascii_single_id_fabrication_is_caught():
    # the case the guard already handles -- keep it that way
    assert _guard({"PSI-25:M18"}).check_citations("spread 0.026 mm/s (PSI-25:M99)") == {"PSI-25:M99"}


def test_correctly_cited_real_value_is_not_flagged():
    # C6's new value-sanity check must not fire on a genuinely correct
    # citation -- PSI-25:M18's real spread rate is 0.026 mm/s.
    assert not _guard({"PSI-25:M18"}).check_citations("spread rate 0.026 mm/s (PSI-25:M18)")


# C6 fixed (turn_guard's citation shape/matching rebuilt on the known-id set):

def test_nonbreaking_hyphen_fabrication_is_caught():
    # exactly how gpt-oss-120b typesets ids in live replies
    fabricated = "PSI‑25:M99"
    assert _guard({"PSI-25:M18"}).check_citations(f"({fabricated})")


def test_space_containing_fabrication_is_caught():
    assert _guard({"PSI-159:21088 B1"}).check_citations("burn time 13 s (PSI-159:21088 Z9)")


def test_multi_id_parenthesis_fabrication_is_caught():
    assert _guard({"PSI-25:M18"}).check_citations("(PSI-25:M18, PSI-25:M99)")


# Regression for the live multi-turn failure 2026-09-27 (respond() loaded the
# OLDEST 6 items, order='asc'; turn 4 re-answered turn 2's question). Passes
# against the working-tree fix (order='desc' + reversed) in main.py.
def test_respond_sends_the_newest_user_message_to_the_model(monkeypatch):
    """Five user turns (each followed by a widget + assistant reply, as in a
    real thread). The model input for the 5th turn must contain the 5th
    question. Runner is stubbed to capture its input and stop -- no network."""
    import asyncio
    from datetime import datetime, timedelta

    import main
    from chatkit.types import (AssistantMessageContent, AssistantMessageItem, InferenceOptions, ThreadMetadata,
                               UserMessageItem, UserMessageTextContent)
    from store import InMemoryChatKitStore

    store = InMemoryChatKitStore()
    server = main.FlameFreefallChatKitServer(store=store, attachment_store=main.attachment_store)

    async def _no_title(*a, **k):
        return None
    monkeypatch.setattr(server, "_maybe_update_thread_title", _no_title)
    captured: list = []

    def _capture(agent, input_items, **kw):
        captured.append(input_items)
        raise RuntimeError("stop after capturing input")
    monkeypatch.setattr(main.Runner, "run_streamed", staticmethod(_capture))

    async def run() -> None:
        t0 = datetime(2026, 9, 27, 12, 0, 0)
        thread = ThreadMetadata(id="thr_qa", created_at=t0)
        await store.save_thread(thread, context={})
        questions = [f"question number {i}" for i in range(1, 6)]
        for i, q in enumerate(questions):
            base = t0 + timedelta(minutes=i)
            await store.add_thread_item(thread.id, UserMessageItem(
                id=f"u{i}", thread_id=thread.id, created_at=base,
                content=[UserMessageTextContent(text=q)], inference_options=InferenceOptions()), context={})
            if i < len(questions) - 1:  # earlier turns already answered
                for j, kind in enumerate(("widget-ish reply", "reply")):
                    await store.add_thread_item(thread.id, AssistantMessageItem(
                        id=f"a{i}{j}", thread_id=thread.id, created_at=base + timedelta(seconds=j + 1),
                        content=[AssistantMessageContent(text=f"{kind} {i}", annotations=[])]), context={})
        try:
            async for _ in server.respond(thread, None, context={}):
                pass
        except RuntimeError:
            pass  # the stub's stop signal, raised after input was captured

    asyncio.run(run())
    assert captured, "Runner was never called"
    assert "question number 5" in json.dumps(captured[0], default=str)


# C5 fixed: readiness()'s nearest_tested now reports the value that actually
# matched (_nearest_reported_value), not a multi-value cell's bare minimum.
def test_readiness_nearest_does_not_misstate_multi_value_o2():
    import psi_query
    gas = next(c for c in psi_query.compact_readiness(psi_query.readiness("gateway"))["classes"]
               if c["geometry_class"] == "gaseous-flames")
    # nearest partial run PSI-20:2019-02-08 has O2 cell "21; 26.5; 40" -- it WAS run at 26.5
    assert not gas["nearest_tested"].startswith("21% O2")


def test_every_real_id_shape_is_recognisable():  # C6 fixed
    """A correct citation of any real run id must be *seen* by the guard
    (so that a fabricated one of the same shape would be too): cite each
    real id with a wrong suffix and expect it flagged."""
    ids = [r["id"] for r in json.loads(DATA.read_text(encoding="utf-8"))["runs"]]
    missed = [i for i in ids if not _guard({i}).check_citations(f"({i}X)")]
    assert not missed, f"{len(missed)} of {len(ids)} id shapes invisible to check_citations, e.g. {missed[:3]}"
