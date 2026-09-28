"""Regression tests from the data-forensics audit (2026-09-27).

Each test encodes what the SOURCE says, so it fails while the defect is
present and passes once the pipeline is fixed.
"""

import ast
import re
from pathlib import Path

import pytest

from psi_ingest.cli import run

PKG = Path(__file__).resolve().parents[1] / "psi_ingest"


@pytest.fixture(scope="module")
def result():
    return run(write=False)


def _by_id(result, rid):
    return next(r for r in result["runs"] if r["id"] == rid)


def _unreachable(tree: ast.AST) -> list[int]:
    """Line numbers of statements that follow a return/raise/continue/break
    in the same block — code that can never run."""
    out = []
    for node in ast.walk(tree):
        for field in ("body", "orelse", "finalbody"):
            block = getattr(node, field, None)
            if not isinstance(block, list):
                continue
            for i, stmt in enumerate(block[:-1]):
                if isinstance(stmt, (ast.Return, ast.Raise, ast.Continue, ast.Break)):
                    out.append(block[i + 1].lineno)
                    break
    return out


def test_ingest_code_has_no_unreachable_statements():
    # reports.py: saffire_table_i's "ignition and results" loop (and its
    # m.stat call) sits indented inside _is_note_marker after `return False`,
    # so it never runs — no error, no failing test, every outcome it merges lost.
    bad = {}
    for path in [*PKG.glob("*.py"), *(PKG / "adapters").glob("*.py")]:
        lines = _unreachable(ast.parse(path.read_text(encoding="utf-8")))
        if lines:
            bad[path.name] = lines
    assert not bad, f"unreachable statements (file: first dead line): {bad}"


def test_saffire_table_i_results_are_merged(result):
    # knowledge/investigations/solid-fuel/saffire.md line 188 (Table I, ignition
    # and results): sample 1-1 → µ-g spread rate "1.8 mm/s", spread extent "~84 cm";
    # line 189: sample 1-2 → "1.3 mm/s". PSI-98 has no spread columns, so this
    # table is the only source of Saffire-1's spread rates.
    for rid, rate in (("PSI-98:S1", 1.8), ("PSI-98:S2", 1.3)):
        r = _by_id(result, rid)
        tables = [s.get("table") for s in r["sources"]]
        assert "Table I (ignition and results)" in tables, (rid, tables)
        rates = [o["measure"]["value"] for o in r["outcomes"]
                 if o["quantity"] == "spread_rate" and "measure" in o]
        assert rates == [rate], (rid, rates)
    extent = [o["measure"] for o in _by_id(result, "PSI-98:S1")["outcomes"]
              if o["quantity"] == "spread_extent" and "measure" in o]
    assert extent and extent[0]["value"] == 84.0 and extent[0]["unit"] == "cm"


def test_saffire_table_i_is_counted_in_report_stats(result):
    tables = [s["table"] for s in result["report"]["report_tables"]]
    assert any(t.endswith("saffire Table I") for t in tables), tables


@pytest.mark.xfail(strict=True, reason="CLD Fuel Bottle vs Test Type disagreement not yet recorded (open)")
def test_cld_bottle_vs_test_type_disagreement_is_recorded_not_resolved(result):
    # psi-data/raw/csvs/PSI-21_Experimental table_CLD Flame.csv lines 16-23 and
    # 24-29: "Fuel Bottle" runs C2H4, C2H5, C2H6 … C2H11 (a spreadsheet
    # fill-series artifact) on rows whose Test Type is "Ethylene based test".
    # Lines 18 ("100% C2H6") and 26 ("50% C2H6"): the two cells of the same row
    # disagree (ethane vs ethylene). AGENTS.md: a disagreement is recorded,
    # never resolved by picking one — so a single bare family, whichever it
    # is, fails; the run must carry both readings.
    for rid in ("PSI-21:18177", "PSI-21:18241"):
        r = _by_id(result, rid)
        assert r["conditions"]["test_type"]["value"] == "Ethylene based test"
        fam = r["conditions"].get("fuel_family") or {}
        record = repr((fam, r.get("conflicts"))).lower()
        assert "ethane" in record and "ethylene" in record, (rid, fam, r.get("conflicts"))


def test_saffire_table_i_placeholders_are_not_outcomes(result):
    # knowledge/investigations/solid-fuel/saffire.md Table I (ignition and
    # results): "n/a" (rows 1-2, 2-1 … 2-4) and "n/a (Nomex)" (row 2-7) mean
    # no measurement was made — no outcome, not a text result "n/a".
    assert not _placeholder_outcomes(result, "report")
    # A qualified real result survives: row 2-7 1-g burn extent "~0 (Nomex)".
    s27 = _by_id(result, "PSI-99:2-7")
    assert any(o["quantity"] == "burn_extent_1g" for o in s27["outcomes"]), s27["outcomes"]


@pytest.mark.xfail(strict=True, reason="PSI-side placeholders still become text outcomes (open)")
def test_psi_table_placeholders_are_not_outcomes(result):
    # psi-data/raw/csvs SAFFIRE-2 table, sample 2-7: spread-rate cells
    # "n/a (Nomex)" are kept as text outcomes by the solid-fuel adapter.
    assert not _placeholder_outcomes(result, "psi")


def _placeholder_outcomes(result, kind):
    out = []
    for r in result["runs"]:
        for o in r["outcomes"]:
            t = re.sub(r"\s*\([^)]*\)$", "", (o.get("text") or "").strip().lower())
            if t in ("n/a", "na", "none", "-", "—", "–") and r["sources"][o["source"]]["kind"] == kind:
                out.append((r["id"], o["quantity"], o["text"]))
    return out
