"""QA code-quality regression tests for the ingest (audit 2026-09-26).
Expected to FAIL until the defect each one names is fixed."""

import pytest

from psi_ingest.cli import run
from psi_ingest.units import parse_measure, to_atm, to_mm


@pytest.fixture(scope="module")
def result():
    return run(write=False)


def _by_id(result, rid):
    return next(r for r in result["runs"] if r["id"] == rid)


def test_saffire_table_i_results_are_ingested(result):
    """reports.py: commit 899b48f inserted `def _is_note_marker` in the middle
    of saffire_table_i(), so the `for row in res_rows:` loop (and m.stat) now
    sit after `return False` inside _is_note_marker -- unreachable. SAFFIRE-1
    S1's governed µ-g spread rate (1.8 mm/s, knowledge/.../saffire.md Table I)
    never reaches runs.json, and no SAFFIRE-1/2 result is ever confirmed by or
    checked for conflict against the report."""
    s1 = _by_id(result, "PSI-98:S1")
    tables = {s.get("table") for s in s1["sources"]}
    assert "Table I (ignition and results)" in tables, tables
    rates = [o["measure"]["value"] for o in s1["outcomes"] if o["quantity"] == "spread_rate" and "measure" in o]
    assert 1.8 in rates, s1["outcomes"]


@pytest.mark.parametrize("cell,fn", [
    ("760 blarg", lambda m: to_atm(m, "atm")),
    ("5 mil", lambda m: to_mm(m, "mm")),
])
def test_unknown_unit_is_not_left_usable(cell, fn):
    """units.to_atm/to_mm return the measure unchanged (numbers intact, unit
    'psia'/'torr'/'mil') with only an `unknown_unit` flag. Query code relies on normalized units.
    The module's own rule: unreadable -> null plus a flag, never a guess."""
    m = fn(parse_measure(cell))
    assert m.min is None and m.value is None, m
    assert "unknown_unit" in m.flags, m
    # The unit actually read is kept — never relabelled as the canonical one.
    assert m.unit == cell.split()[1], m
