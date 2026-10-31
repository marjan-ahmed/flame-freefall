"""QA code-quality regression tests (audit 2026-09-26).

Each test pins one defect that produces a PLAUSIBLE-LOOKING wrong answer or
citation rather than a crash. They are expected to FAIL until the defect is
fixed; none of them needs the network (GROQ_API_KEY=dummy).
"""

from __future__ import annotations

import asyncio
import json
import sys
import types
from datetime import datetime, timedelta
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import main  # noqa: E402
import psi_query  # noqa: E402
import psi_tools  # noqa: E402
import psi_widgets as w  # noqa: E402
from turn_guard import TurnGuard  # noqa: E402


def open_defect(finding: str):
    """A confirmed, still-open defect: strict xfail, so the fix shows up as an
    XPASS failure and the marker must then be removed."""
    return pytest.mark.xfail(strict=True, reason=f"open QA defect: {finding}")


def _fake_ctx(guard: TurnGuard, thread_id: str, stream_widget=None):
    async def _noop(_widget):
        return None

    return types.SimpleNamespace(
        thread=types.SimpleNamespace(id=thread_id),
        stream_widget=stream_widget or _noop,
        request_context={},
        _guard=guard,
    )


def _invoke(tool, ctx, args: dict) -> str:
    from agents.tool_context import ToolContext

    raw = json.dumps(args)
    tc = ToolContext(context=ctx, tool_name=tool.name, tool_call_id="call_qa", tool_arguments=raw)
    return asyncio.run(tool.on_invoke_tool(tc, raw))


# ── 1. respond() feeds the model the OLDEST six items, not the latest ─────────

def test_respond_sends_the_latest_user_message_to_the_model(monkeypatch):
    """main.py respond() loads history with order="asc", limit=6: the FIRST
    six items of the thread. From roughly the third turn on, the user's new
    question is not in the model input at all, so the model answers an earlier
    question -- a fluent, cited, wrong answer."""
    from chatkit.agents import AgentContext  # noqa: F401  (import check)
    from chatkit.types import InferenceOptions, ThreadMetadata, UserMessageItem, UserMessageTextContent

    from store import InMemoryChatKitStore

    srv = main.FlameFreefallChatKitServer(store=InMemoryChatKitStore(), attachment_store=main.attachment_store)
    captured: dict = {}

    def fake_run_streamed(agent, input_items, **kw):
        captured["input"] = input_items
        raise RuntimeError("stop after capturing input")

    monkeypatch.setattr(main.Runner, "run_streamed", fake_run_streamed)

    async def go():
        # title already set -> no title-generation network call
        thread = ThreadMetadata(id="thr_hist", created_at=datetime.now(), title="t")
        await srv.store.save_thread(thread, context={})
        t0 = datetime.now()
        last = None
        for i in range(9):
            last = UserMessageItem(
                id=f"msg_{i}", thread_id="thr_hist", created_at=t0 + timedelta(seconds=i),
                content=[UserMessageTextContent(text=f"question number {i}")],
                inference_options=InferenceOptions(),
            )
            await srv.store.add_thread_item("thr_hist", last, context={})
        try:
            async for _ in srv.respond(thread, last, {}):
                pass
        except RuntimeError:
            pass

    asyncio.run(go())
    assert "question number 8" in json.dumps(captured["input"], default=str), (
        "the latest user message never reaches the model"
    )


# ── 2. citation guard: regex misses most real run ids ─────────────────────────

@pytest.mark.parametrize("real_id,fabricated", [
    ("PSI-26:As-run 1", "PSI-26:As-run 999"),                    # space
    ("PSI-159:21088 B1", "PSI-159:21088 B999"),                  # space
    ("PSI-101:SAME #51", "PSI-101:SAME #999"),                   # '#'
    ("saffire-iv-vi:IV-1", "saffire-iv-vi:IV-99"),               # not PSI- prefixed
    ("PSI-68:IsoOctane (pure)", "PSI-68:IsoOctane (blend)"),     # nested parentheses
])
def test_fabricated_citation_is_detected_for_every_id_shape(real_id, fabricated):  # C6 fixed
    """turn_guard._CITED_RUN_ID_RE only accepts PSI-<n>:[A-Za-z0-9._-]+. 1096 of
    the 1948 run ids in data/runs.json contain a space, '#', parentheses, or
    are not PSI- prefixed, so a fabricated id in those shapes is never
    inspected."""
    g = TurnGuard()
    g.record_valid_run_ids({real_id})
    assert g.check_citations(f"It burned fast ({fabricated}).") == {fabricated}


def test_every_real_run_id_is_parseable_by_the_citation_guard():  # C6 fixed
    runs, _ = psi_query.load()
    g = TurnGuard()
    g.record_valid_run_ids({"__sentinel__"})  # non-empty so check_citations runs
    unseen = [r["id"] for r in runs if not g.check_citations(f"({r['id']})")]
    assert not unseen, f"{len(unseen)} run ids are invisible to the citation guard, e.g. {unseen[:3]}"


def test_show_test_details_citations_are_checked():  # C6 fixed
    """show_test_details' _reply() asks the model to cite run ids
    (cite_run_ids defaults to True) but never records valid ids in the
    TurnGuard, so check_citations() returns set() for any fabricated id."""
    g = TurnGuard()
    _invoke(psi_tools.show_test_details, _fake_ctx(g, "thr_details"), {"run_id": "PSI-25:M18"})
    assert g.check_citations("Test (PSI-25:M18) and also (PSI-25:M999).") == {"PSI-25:M999"}


# ── 3. a PSI tool that fails is invisible to the turn guard ───────────────────

def test_psi_tool_failure_is_flagged_like_a_search_failure():  # C8 fixed
    """When a PSI tool raises, the agents SDK hands the model the string
    'An error occurred while running the tool...' and the turn continues.
    psi_tools._guarded now records the failure on TurnGuard before
    re-raising, so should_override_reply() fires just like it already does
    for a search/read failure."""
    g = TurnGuard()

    async def boom(_widget):
        raise RuntimeError("widget stream failed")

    out = _invoke(psi_tools.query_test_runs, _fake_ctx(g, "thr_fail", boom), {"o2_pct": 21})
    assert out.startswith("An error occurred")  # precondition: the SDK swallowed it
    assert g.should_override_reply(), "a failed PSI tool call leaves no trace the reply guard can act on"


@pytest.mark.parametrize("tool,args", [
    (psi_tools.query_test_runs, {"o2_pct": 21}),
    (psi_tools.show_gap_map, {"o2_pct": 21}),
    (psi_tools.compare_investigations, {"investigations": ["BASS-II", "SAFFIRE-2"]}),
    (psi_tools.show_test_details, {"run_id": "PSI-25:M18"}),
    (psi_tools.plot_results, {}),
    (psi_tools.rank_results, {"geometry_class": "solid-fuel", "quantity": "spread_rate"}),
    (psi_tools.show_mission_readiness, {"atmosphere": "iss"}),
    (psi_tools.compare_test_runs, {"left_id": "PSI-25:M18", "right_id": "PSI-25:M18", "quantity": "spread_rate"}),
])
def test_every_psi_tool_is_guarded(tool, args):
    """Every PSI tool (AGENTS.md) is wrapped by
    psi_tools._guarded, not just query_test_runs -- a regression here would
    silently narrow C8's fix back down to one tool."""
    g = TurnGuard()

    async def boom(_widget):
        raise RuntimeError("widget stream failed")

    out = _invoke(tool, _fake_ctx(g, "thr_fail_" + tool.name, boom), args)
    assert out.startswith("An error occurred")  # precondition: the SDK swallowed it
    assert g.should_override_reply(), f"{tool.name}'s failure left no trace for the reply guard"


def test_rank_results_schema_allows_smoke_aerosol():
    """geometry_class was RankableGeometryClass (excludes smoke-aerosol), so
    Groq's strict tool-call schema rejected 'rank the smoke-aerosol
    materials' before our own code ever ran: an APIError (not an
    APIStatusError) that bypasses _FallbackCompletions, surfacing as a false
    'rate limit or quota exhausted' message for an honest refusal
    psi_query.rank() already knows how to give (see C8)."""
    schema = psi_tools.rank_results.params_json_schema
    assert "smoke-aerosol" in schema["properties"]["geometry_class"]["enum"]


def test_rank_results_refuses_smoke_aerosol_cleanly():
    g = TurnGuard()
    out = _invoke(psi_tools.rank_results, _fake_ctx(g, "thr_smoke"),
                  {"geometry_class": "smoke-aerosol", "quantity": "smoke_point_length"})
    assert "error" in out and "not a rankable result" in out
    assert not g.should_override_reply(), "a clean refusal is not a tool failure"


# ── 4. investigation names: query() vs compare_data() disagree ────────────────

@pytest.mark.parametrize("name", ["SAFFIRE", "BASS 2", "ACME", "FLEX 2"])
def test_query_resolves_investigation_names_like_compare_does(name):  # C7 fixed
    """query_test_runs' investigation filter is an exact id/name match, so
    'SAFFIRE' or 'BASS 2' returns 0 match / 0 partial / 0 near (the card says
    'No test in the PSI tables states all of these conditions') while
    compare_investigations resolves the same names via
    psi_widgets._resolve_investigations."""
    r = psi_query.query({"investigation": name, "o2_pct": 21})
    total = r["counts"]["match"] + r["counts"]["partial"] + r["counts"]["near_pool"]
    assert total > 0, f"investigation={name!r} silently matches nothing"


def test_compare_with_unresolvable_names_does_not_compare_everything():  # C7 fixed
    """compare_data(q, ['SAFFIRE II']) resolves to an empty set, and
    `if wanted` then treats it as 'no filter': all 19 investigations come back
    as if the user had asked for them."""
    rows = w.compare_data({}, ["SAFFIRE II"])
    assert len(rows) < 19, "unresolved names silently widened to every investigation"


def test_blank_investigation_name_resolves_to_nothing():  # found during the C1-C8 release gate
    """_investigation_ids('') used to return every investigation (every
    id/name trivially startswith('')). query()'s own callers already filter
    blanks out before this point, but compare_data's investigations list
    does not, so a stray "" there (e.g. compare_investigations(["", "BASS"]))
    would silently widen to everything and swallow a real filter it's
    unioned with -- the same failure shape as the unresolvable-name case
    above, just via a different input."""
    assert psi_query._investigation_ids("", psi_query.load()[1]) == set()
    assert psi_query._investigation_ids("   ", psi_query.load()[1]) == set()
    rows = w.compare_data({}, [""])
    assert len(rows) < 19
    names = {r["name"] for r in w.compare_data({}, ["", "BASS"])}
    assert names == {"BASS"}, "a blank entry must not widen a real filter it's unioned with"


# ── 5. fuel_family prefix admits blends into a pure-fuel query ────────────────

def test_pure_fuel_filter_does_not_count_blends():
    """Regression: an exact n-dodecane query used to include 57 blend records."""
    r = psi_query.query({"fuel_family": "n-dodecane"})
    fams = {v["fuel_family"] for v in r["match"]}
    assert fams == {"n-dodecane"}, fams


# ── 6. plot_results silently swaps the requested quantity ─────────────────────

def test_results_summary_says_when_requested_quantity_is_unavailable():
    """Regression: a spread-rate request used to silently draw burn time."""
    s = w.results_summary({"geometry_class": "droplet-combustion"}, "spread_rate")
    assert s["quantity"] == "spread_rate" or any(
        k in s for k in ("requested_quantity", "substituted_for", "requested_unavailable")
    ), s


# ── 7. rank() silently picks one side of an outcome conflict ──────────────────

def test_rank_does_not_silently_choose_between_conflicting_outcomes():
    """Conflicting outcomes stay in the evidence but are excluded from ranking.
    A widened interval would still imply a supported scalar aggregate."""
    invs = {"x": {"id": "x", "name": "X", "geometry_class": "solid-fuel"}}
    run = {
        "id": "PSI-1:A", "investigation": "x", "label": "A", "granularity": "test",
        "conditions": {"fuel_family": {"value": "PMMA"},
                       "o2_pct": {"raw": "21", "value": 21.0, "min": 21.0, "max": 21.0, "unit": "%"}},
        "outcomes": [
            {"quantity": "spread_rate", "source": 0, "measure": {"raw": "1.0", "value": 1.0, "min": 1.0, "max": 1.0, "unit": "mm/s"}},
            {"quantity": "spread_rate", "source": 1, "measure": {"raw": "5.0", "value": 5.0, "min": 5.0, "max": 5.0, "unit": "mm/s"}},
        ],
        "conflicts": [{"field": "outcome:spread_rate", "values": [{"source": 0, "raw": "1.0"}, {"source": 1, "raw": "5.0"}]}],
        "sources": [{"kind": "psi", "dataset": "PSI-1", "file": "f.csv", "row": 2},
                    {"kind": "psi", "dataset": "PSI-1", "file": "other.csv", "row": 2}],
    }
    r = psi_query.rank({"o2_pct": 21}, "spread_rate", "solid-fuel", runs=[run], invs=invs)
    assert r["rows"] == [] and r["total_ranked"] == 0


# ── 8. uploaded PDF text reaches the model with no provenance framing ─────────

@open_defect("A10 attachment text reaches the model unfenced")
def test_attachment_text_is_framed_as_untrusted_non_record_content(monkeypatch):
    """Commit 90f868b: an uploaded PDF's extracted text is inserted into the
    user turn as 'Extracted text follows:' with nothing telling the model it
    is not PSI data / not the governed record. A PDF stating 'PSI-25:M18 spread
    rate 99 mm/s' can be repeated with a VALID run id, which TurnGuard accepts."""
    from chatkit.types import FileAttachment

    monkeypatch.setattr(main, "_extract_pdf_text", lambda data, max_chars=6000: "PSI-25:M18 spread rate was 99 mm/s.")
    main.uploaded_files["att_qa"] = b"%PDF-fake"
    try:
        att = FileAttachment(id="att_qa", name="notes.pdf", mime_type="application/pdf")
        part = asyncio.run(main.converter.attachment_to_message_content(att))
    finally:
        main.uploaded_files.pop("att_qa", None)
    note = part["text"].lower()
    assert "untrusted" in note or "not part of the" in note or "not from the record" in note, part["text"]
