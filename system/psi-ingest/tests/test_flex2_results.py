from collections import Counter
from copy import deepcopy

import pytest

from psi_ingest import knowledge
from psi_ingest.adapters import Ctx
from psi_ingest.cli import REPO_ROOT, run
from psi_ingest.flex2_results import DOC, TABLE_HEADING, merge_flex2_literature
from psi_ingest.model import Run, cat


@pytest.fixture(scope="module")
def result():
    return run(write=False, include_review=True)


def test_literature_outcomes_and_provenance(result):
    enriched = [r for r in result["runs"] if any(s.get("doc") == DOC for s in r["sources"])]
    assert len(enriched) == 2
    assert {r["conditions"]["fuel_family"]["value"] for r in enriched} == {"n-decane", "n-octane"}
    outcomes = []
    for r in enriched:
        assert r["granularity"] == "envelope"
        for o in r["outcomes"]:
            source = r["sources"][o["source"]]
            if source.get("doc") != DOC:
                continue
            outcomes.append(o)
            assert "exact fuel identity" in o["note"]
            assert "literature-identified" in o["note"]
            assert source["table"].split("(")[1].rstrip(")") in o["note"]
            assert source["line"] > 0 and source["quote"]
            assert o["measure"]["unit"] == "mm²/s"
    assert len(outcomes) == 13
    assert Counter(o["quantity"] for o in outcomes) == {"burning_rate_k_hot": 7, "burning_rate_k_cool": 6}
    assert all(not r["outcomes"] for r in result["runs"] if r["investigation"] == "flex-2"
               and r["conditions"]["fuel_family"]["value"] not in {"n-decane", "n-octane"})
    assert all(s.get("doc") != DOC for r in result["runs"] if r["investigation"] == "flex" for s in r["sources"])


@pytest.mark.parametrize("column,value", [("Hot-flame K (mm2/s)", "9.99"),
    ("D₀ (mm)", "9.99"), ("Pressure (atm)", "3.0"), ("Test", "R999")])
def test_wrong_table_values_fail_closed(monkeypatch, column, value):
    columns, rows, line = knowledge.table_under(REPO_ROOT, DOC, TABLE_HEADING)
    rows = deepcopy(rows)
    rows[0][column] = value
    monkeypatch.setattr(knowledge, "table_under", lambda *a: (columns, rows, line))
    ctx = Ctx(REPO_ROOT, REPO_ROOT / "psi-data/raw", {})
    with pytest.raises(ValueError, match="numeric cell|pressure|no paper guards"):
        merge_flex2_literature(ctx, [], include_review=True)


@pytest.mark.parametrize("count", [0, 2])
def test_missing_or_ambiguous_envelope_fails_closed(count):
    ctx = Ctx(REPO_ROOT, REPO_ROOT / "psi-data/raw", {})
    runs = [Run("flex-2", "decane", granularity="envelope",
                conditions={"fuel_family": cat("n-decane")}) for _ in range(count)]
    with pytest.raises(ValueError, match="expected one envelope"):
        merge_flex2_literature(ctx, runs, include_review=True)
    assert all(not r.sources and not r.outcomes for r in runs)


def test_join_preserves_envelope_conditions_and_checks_extraction(monkeypatch):
    from psi_ingest.flex2_results import GUARDS

    ctx = Ctx(REPO_ROOT, REPO_ROOT / "psi-data/raw", {})
    runs = [Run("flex-2", fuel, granularity="envelope",
                conditions={"fuel_family": cat(fuel)}) for fuel in ("n-decane", "n-octane")]
    before = deepcopy([r.conditions for r in runs])
    merge_flex2_literature(ctx, runs, include_review=True)
    assert [r.conditions for r in runs] == before
    monkeypatch.setitem(GUARDS, "R377", ["this sentence does not occur in the paper"])
    with pytest.raises(ValueError, match="guard fragment not found"):
        merge_flex2_literature(ctx, runs, include_review=True)


def test_drafts_do_not_reach_serving_data(monkeypatch):
    citation = knowledge.citation(REPO_ROOT, DOC, "flex-2-cool-flame-2014")
    monkeypatch.setattr(knowledge, "citation", lambda *a: {**citation, "doc_status": "draft"})
    ctx = Ctx(REPO_ROOT, REPO_ROOT / "psi-data/raw", {})
    runs = [Run("flex-2", "decane", granularity="envelope",
                conditions={"fuel_family": cat("n-decane")})]
    merge_flex2_literature(ctx, runs)
    assert not runs[0].sources and not runs[0].outcomes
    assert "awaiting owner approval" in ctx.table_notes["flex-2"][0]
    with pytest.raises(ValueError, match="cannot be written"):
        run(include_review=True)


def test_hot_and_cool_rates_cannot_be_swapped(monkeypatch):
    columns, rows, line = knowledge.table_under(REPO_ROOT, DOC, TABLE_HEADING)
    rows = deepcopy(rows)
    hot, cool = "Hot-flame K (mm2/s)", "Cool-flame K (mm2/s)"
    rows[0][hot], rows[0][cool] = rows[0][cool], rows[0][hot]
    monkeypatch.setattr(knowledge, "table_under", lambda *a: (columns, rows, line))
    ctx = Ctx(REPO_ROOT, REPO_ROOT / "psi-data/raw", {})
    with pytest.raises(ValueError, match="differs from paper"):
        merge_flex2_literature(ctx, [], include_review=True)
