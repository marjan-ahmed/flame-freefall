"""Real report-backed audit outcome, independent of synthetic comparability fixtures."""
import json
from copy import deepcopy
from pathlib import Path
import re

from psi_comparison import compare_runs, comparison_audit

ROOT = Path(__file__).resolve().parents[3]
EXAMPLE = json.loads((Path(__file__).parent / "comparison-audit-real-case.json").read_text(encoding="utf-8"))
RUNS = json.loads((ROOT / "psi-data/derived/runs.json").read_text(encoding="utf-8"))["runs"]
INVS = {i["id"]: i for i in json.loads((ROOT / "psi-data/derived/investigations.json").read_text(encoding="utf-8"))["investigations"]}
LEFT = next(r for r in RUNS if r["id"] == EXAMPLE["left_id"])
RIGHT = next(r for r in RUNS if r["id"] == EXAMPLE["right_id"])


def test_real_saffire_audit_identifies_supported_facts_without_relaxing_comparability():
    before = deepcopy((LEFT, RIGHT))
    audit = comparison_audit(LEFT, RIGHT, INVS, EXAMPLE["quantity"])
    assert audit["assessment"] == compare_runs(LEFT, RIGHT, INVS, EXAMPLE["quantity"])
    assert audit["assessment"]["status"] == "insufficient_metadata"
    assert not audit["assessment"]["can_compare"]
    for key, expected in (("shared_facts", "shared_fields"), ("recorded_differences", "different_fields"), ("missing_or_ambiguous", "missing_fields")):
        assert [c["field"] for c in audit[key]] == EXAMPLE[expected]
    assert [s["code"] for s in audit["next_steps"]] == EXAMPLE["next_step_codes"]
    assert [e["outcome"]["measure"]["value"] for e in audit["sourced_outcomes"]] == EXAMPLE["outcome_values"]
    assert audit["research_result"].startswith("Two source-linked outcomes")
    assert (LEFT, RIGHT) == before
    extraction = (ROOT / EXAMPLE["source_extraction"]).read_text(encoding="utf-8")
    rows = [[re.sub(r"<[^>]*>", " ", c).strip() for c in re.findall(r"<td[^>]*>([\s\S]*?)</td>", row)] for row in re.findall(r"<tr>([\s\S]*?)</tr>", extraction)]
    for index, entry in enumerate(audit["sourced_outcomes"]):
        assert entry["source"]["url"] == EXAMPLE["source_url"]
        assert entry["source"]["table"] == EXAMPLE["source_table"]
        assert entry["source_index"] == 1
        row = next(row for row in rows if row and row[0] == (LEFT, RIGHT)[index]["label"])
        assert float(row[7]) == EXAMPLE["outcome_values"][index]


def test_one_declared_variable_does_not_hide_confounding_or_missingness():
    audit = comparison_audit(LEFT, RIGHT, INVS, EXAMPLE["quantity"], "pressure_atm")
    assert not audit["assessment"]["can_compare"]
    step = next(s for s in audit["next_steps"] if s["code"] == "MULTIPLE_SETUP_DIFFERENCES")
    assert step["fields"] == ["fuel", "o2_pct"]
    assert any(s["code"] == "INSPECT_MISSING_METADATA" for s in audit["next_steps"])


def test_conflicting_values_and_invalid_citation_are_preserved_not_inferred():
    changed = deepcopy(RIGHT)
    changed["conflicts"] = [{"field": "o2_pct", "values": [{"source": 0, "raw": "28.8"}, {"source": 1, "raw": "30"}]}]
    next(o for o in changed["outcomes"] if o["quantity"] == EXAMPLE["quantity"])["source"] = 999
    audit = comparison_audit(LEFT, changed, INVS, EXAMPLE["quantity"])
    assert audit["retained_conflicts"][0]["values"] == changed["conflicts"][0]["values"]
    assert audit["sourced_outcomes"][1]["source"] is None
    assert not audit["research_result"].startswith("Two source-linked outcomes")
    assert {"REVIEW_RETAINED_CONFLICTS", "INSPECT_OUTCOME_SOURCES"}.issubset({s["code"] for s in audit["next_steps"]})


def test_absent_outcome_is_not_subtracted_or_imputed():
    audit = comparison_audit(LEFT, RIGHT, INVS, "smoke_threshold_crossing_time")
    assert audit["sourced_outcomes"][0]["outcome"]["measure"]["value"] == 981
    assert audit["sourced_outcomes"][1]["outcome"] is None
    assert "difference" not in audit and "ratio" not in audit
    assert any(s["code"] == "INSPECT_OUTCOME_SOURCES" for s in audit["next_steps"])
