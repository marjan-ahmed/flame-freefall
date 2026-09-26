"""Deterministic provenance gaps found by the grounding-provenance live pass
(2026-09-27), pinned without the network.

The model can only cite what its tool payload tells it. Live, asked "What
flame spread rates were measured in SAFFIRE-1, and which source table are
they from?", gpt-oss-120b answered "1.8 mm/s in run PSI-98:S1 (PSI-98 line
2)" -- faithfully copying compact()'s one-per-run `cite`, which always
prefers the PSI line even when the listed value came from a report table.
The PSI-98 CSV has no spread-rate column at all; 1.8 mm/s is from Table I
of "Results of Large-Scale Spacecraft Flammability Tests". The fault is in
the payload, not the model, so it can be pinned here.

Gaps are xfail(strict): the suite stays green today and turns red (XPASS)
once the payload carries per-value provenance, prompting removal of the
marker. The PASSING tests pin the facts the gap statements rest on.
"""

import asyncio
import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import psi_query  # noqa: E402

GAP = pytest.mark.xfail(strict=True, reason="tool payload attributes values to a source that does not hold them "
                                            "(grounding-provenance 2026-09-27)")


def _run(run_id: str) -> dict:
    runs, _ = psi_query.load()
    return next(r for r in runs if r["id"] == run_id)


def _slim(q: dict, run_id: str) -> dict:
    c = psi_query.compact(psi_query.query(q))
    return next(v for t in ("match", "partial", "near") for v in c[t] if v["id"] == run_id)


def _source_of(run: dict, quantity: str) -> dict:
    o = next(o for o in run["outcomes"] if o["quantity"] == quantity and "measure" in o)
    return run["sources"][o["source"]]


# ── facts the gaps rest on (these pass) ─────────────────────────────────────

def test_saffire1_spread_rate_comes_from_a_report_table_not_the_psi_line():
    src = _source_of(_run("PSI-98:S1"), "spread_rate")
    assert src["kind"] == "report" and src["table"].startswith("Table I")


def test_compact_no_longer_hands_a_run_level_cite():
    # C3 (fixed): the one-per-run `cite` (always the PSI line) was what the model
    # copied as the source of report-only values. There is no run-level source
    # any more; every value carries its own.
    v = _slim({"investigation": "SAFFIRE-1"}, "PSI-98:S1")
    assert not {"cite", "test_row", "citations"} & set(v), v


# ── C3: every value names the source that actually holds it ────────────────

def _expected_tag(run: dict, src_index: int, reports: dict) -> str:
    s = run["sources"][src_index]
    if s["kind"] == "report":
        key = next(k for k, v in reports.items() if v == f"{s['table']}, {s['title']}")
        return f"report {key}"
    if s["kind"] == "psi-workbook":
        return f"{s['dataset']} workbook sheet {s.get('sheet')} row {s['row']}"
    return f"{s['dataset']} line {s['row']}"


@pytest.mark.parametrize("q", [
    {"investigation": "SAFFIRE-1"},
    {"investigation": "SAFFIRE-2"},
    {"investigation": "BASS-II", "o2_pct": 22, "flow_cm_s": 9},
    {"investigation": "FLEX", "fuel_family": "n-heptane"},
    {"o2_pct": 21, "pressure_atm": 1.0},
])
def test_every_compact_outcome_is_tagged_with_its_true_source(q):
    """Source of truth: runs.json outcome["source"] (+ confirmed_by) indexes the
    run's own sources[]. Each outcome string the model sees must end with that
    source's tag — never another source of the same run."""
    c = psi_query.compact(psi_query.query(q))
    runs = {r["id"]: r for r in psi_query.load()[0]}
    checked = 0
    for t in ("match", "partial", "near"):
        for v in c[t]:
            run = runs[v["id"]]
            for s in v["outcomes"]:
                body, _, tag = s.rpartition(" [")
                assert body and tag.endswith("]"), s
                qty = body.split("=", 1)[0]
                cands = [o for o in run["outcomes"] if o["quantity"] == qty]
                tags = {"; also ".join(_expected_tag(run, i, c["reports"])
                                       for i in [o["source"], *o.get("confirmed_by", [])]) for o in cands}
                assert tag[:-1] in tags, (v["id"], s, tags)
                checked += 1
    assert checked, "no outcomes listed — the query no longer exercises this"


def test_report_only_values_are_never_tagged_with_a_psi_line():
    # PSI-98:S1 1.8 mm/s: saffire.md Table I (ignition and results); the
    # PSI-98 CSV has no spread-rate column.  PSI-25:M1 0.071 mm/s: BASS-II
    # report Table 5.1; the PSI-25 CSV has no spread-rate column.
    for q, rid, value, table in (
        ({"investigation": "SAFFIRE-1"}, "PSI-98:S1", "spread_rate=1.8 mm/s", "Table I (ignition and results)"),
        ({"investigation": "BASS-II", "o2_pct": 22, "flow_cm_s": 9}, "PSI-25:M1", "spread_rate=0.071 mm/s", "Table 5.1"),
    ):
        c = psi_query.compact(psi_query.query(q))
        v = next(v for t in ("match", "partial", "near") for v in c[t] if v["id"] == rid)
        s = next(s for s in v["outcomes"] if s.startswith(value))
        tag = s.rpartition(" [")[2].rstrip("]")
        assert tag.startswith("report "), s  # never a PSI line
        assert c["reports"][tag.split(" ", 1)[1]].startswith(table), c["reports"]


def test_show_test_details_results_are_tagged_with_their_source():
    p = _details_payload("PSI-25:M1")
    rate = next(r for r in p["results"] if r.startswith("spread_rate=0.071 mm/s"))
    assert "Table 5.1" in rate and "Burning and Suppression of Solids-II (BASS-II) Summary Report" in rate, rate
    assert "PSI-25 line" not in rate, rate


# ── gaps ─────────────────────────────────────────────────────────────────────

def test_compact_cite_names_the_source_of_a_report_only_value_saffire1():  # C3 fixed
    """SAFFIRE-1 spread rate (PSI-98:S1 1.8 mm/s) is in report Table I only.
    The table name lives in the payload's top-level "reports" map (looked up
    by the outcome's "[report N]" tag), not repeated inline per outcome --
    see the compact()-payload budget note in AGENTS.md -- so the check is
    against the WHOLE compact payload, not just this one run's slim view."""
    c = psi_query.compact(psi_query.query({"investigation": "SAFFIRE-1"}))
    assert "Table I" in json.dumps(c, ensure_ascii=False)


def test_compact_cite_names_the_source_of_a_report_only_value_bass_ii():  # C3 fixed
    """BASS-II PSI-25:M1 spread rate 0.071 mm/s and burn time 384 s (6.4 min)
    come from report Table 5.1, yet the payload cites only 'PSI-25 line 28'."""
    run = _run("PSI-25:M1")
    assert _source_of(run, "spread_rate")["table"] == "Table 5.1"
    c = psi_query.compact(psi_query.query({"investigation": "BASS-II", "o2_pct": 22, "flow_cm_s": 9}))
    assert "Table 5.1" in json.dumps(c, ensure_ascii=False)


def _invoke_show_test_details(run_id: str) -> str:
    from agents.tool_context import ToolContext

    import psi_tools
    from turn_guard import TurnGuard

    async def _noop(*a, **k):
        return None
    inner = SimpleNamespace(thread=SimpleNamespace(id=f"thr_grounding_{run_id}"), stream_widget=_noop,
                            request_context={}, _guard=TurnGuard())
    args = json.dumps({"run_id": run_id})
    ctx = ToolContext(context=inner, tool_name="show_test_details", tool_call_id="c1", tool_arguments=args)
    return asyncio.run(psi_tools.show_test_details.on_invoke_tool(ctx, args))


def _details_payload(run_id: str) -> dict:
    out = _invoke_show_test_details(run_id)
    return json.loads(out[out.index("\n{") + 1:])


def test_show_test_details_payload_carries_both_conflicting_values():
    # passes: both sides of PSI-99:2-6's flow disagreement reach the model
    p = _details_payload("PSI-99:2-6")
    vals = {v["raw"] for c in p["conflicts"] if c["field"] == "flow_cm_s" for v in c["values"]}
    assert vals == {"20 cm/s", "25 cm/s"}


def test_show_test_details_conflicts_name_which_source_said_what():  # C4 fixed
    """Conflict values used to arrive as {"source": 0} / {"source": 1} with
    "sources": 3 a bare count -- the model could not say 'the PSI table says
    20 cm/s, the report says 25 cm/s' without guessing which index is which.
    Now each value's "source" is a label naming where it actually came from."""
    p = _details_payload("PSI-99:2-6")
    flow = next(c for c in p["conflicts"] if c["field"] == "flow_cm_s")
    labels = {v["raw"]: v["source"] for v in flow["values"]}
    assert labels["20 cm/s"] == "PSI-99 line 7"
    assert labels["25 cm/s"].startswith("Table I (conditions)") and \
        "Results of Large-Scale Spacecraft Flammability Tests" in labels["25 cm/s"]
    # No bare numeric index survives anywhere in the payload.
    for c in p["conflicts"]:
        for v in c["values"]:
            assert isinstance(v["source"], str) and not v["source"].isdigit(), v


def test_show_test_details_results_name_their_source():  # C3 fixed
    """'Where does the 0.071 mm/s for PSI-25:M1 come from?' routes here, and the
    payload has no per-result source at all -- any answer is a guess."""
    p = _details_payload("PSI-25:M1")
    assert "Table 5.1" in json.dumps(p, ensure_ascii=False)
