from collections import Counter
from pathlib import Path

import openpyxl
import pytest

from psi_ingest.cli import run
from psi_ingest.smoke_results import BOOK, DET_FIELDS, DET_SHEET, FIELDS, SHEET, _merge
from psi_ingest.adapters import Ctx
from psi_ingest.model import Run, cat


@pytest.fixture(scope="module")
def result():
    return run(write=False)


def test_workbook_enriches_existing_runs_without_creating_tests(result):
    rows = [r for r in result["runs"] if r["investigation"] == "same-r"]
    assert len(rows) == 109
    enriched = [r for r in rows if any(s.get("file") == BOOK for s in r["sources"])]
    assert len(enriched) == 108
    assert all(r["granularity"] == "test" for r in enriched)
    assert all(any(o["quantity"] in {q for q, _, _ in FIELDS.values()} for o in r["outcomes"]) for r in enriched)
    assert not any(r["label"] == "SAME #112" for r in rows)


def test_detector_sheet_joins_the_same_runs_with_signed_smoke_signals(result):
    """The ISS/STS detector columns sit on a second sheet of the same workbook:
    the ISS signal deflects positive with smoke; a NEGATIVE STS cell is a
    declared smoke response and is never discarded. Exactly zero STS cells
    (no recorded trace) are skipped, not stated as absence of smoke."""
    quantities = {q for q, _, _ in DET_FIELDS.values()}
    with_detectors = [r for r in result["runs"] if r["investigation"] == "same-r"
                      and any(o["quantity"] in quantities for o in r["outcomes"])]
    assert len(with_detectors) > 50
    for r in with_detectors:
        source_row = {o["source"] for o in r["outcomes"] if o["quantity"] in quantities}
        assert all(r["sources"][s]["sheet"] == DET_SHEET and r["sources"][s]["file"] == BOOK for s in source_row)
        for o in r["outcomes"]:
            if o["quantity"] == "iss_detector_scatter_volts":
                assert o["measure"]["value"] > 0
            if o["quantity"] == "sts_detector_volts" and o["measure"]["value"] < 0:
                assert "smoke response" in o["note"]
    report = next(f for f in result["report"]["files"] if f["file"] == f"summaries/{BOOK} [{DET_SHEET}]")
    assert report["rows_read"] == report["merged_into_previous"] + len(report["skipped"])
    negative = sum(1 for r in with_detectors for o in r["outcomes"]
                   if o["quantity"] == "sts_detector_volts" and o["measure"]["value"] < 0)
    assert any(f"{negative} negative STS readings" in n for n in report["notes"])


def test_join_uses_material_to_disambiguate_the_duplicate_test_number(result):
    rows = {r["id"]: r for r in result["runs"]}
    lampwick = rows["PSI-101:SAME #57"]
    teflon = rows["PSI-101:SAME #57#2"]
    assert lampwick["conditions"]["fuel"]["value"] == "Lampwick"
    assert any(s.get("file") == BOOK for s in lampwick["sources"])
    assert teflon["conditions"]["fuel"]["value"] == "Teflon"
    assert not any(s.get("file") == BOOK for s in teflon["sources"])
    report = next(f for f in result["report"]["files"] if f["file"] == f"summaries/{BOOK} [{SHEET}]")
    assert any("112 / kapton" in s["reason"] for s in report["skipped"])
    assert report["rows_read"] == report["merged_into_previous"] + len(report["skipped"])


def test_completeness_counts_use_records_as_the_denominator(result):
    groups = result["report"]["completeness"]["by_geometry"]
    assert sum(g["records"] for g in groups.values()) == len(result["runs"])
    for row in groups.values():
        assert row["records_with_source_processed_outcomes"] <= row["records_with_numeric_outcomes"] <= row["records"]
        assert all(n <= row["records"] for n in row["conditions_reported_by"].values())
    assert groups["smoke-aerosol"]["records_with_source_processed_outcomes"] == 108
    assert groups["solid-fuel"]["conditions_reported_by"]["pressure_atm"] == 5


def test_every_processed_result_reproduces_its_cached_cell_and_preserves_the_formula(result):
    root = Path(__file__).resolve().parents[3]
    values = openpyxl.load_workbook(root / "psi-data" / "raw" / "summaries" / BOOK, read_only=True, data_only=True)
    formulas = openpyxl.load_workbook(root / "psi-data" / "raw" / "summaries" / BOOK, read_only=True, data_only=False)
    try:
        columns: dict[str, tuple[str, int, str, str]] = {}
        for sheet_name, fields in ((SHEET, FIELDS), (DET_SHEET, DET_FIELDS)):
            header = list(next(values[sheet_name].iter_rows(min_row=2, max_row=2, values_only=True)))
            for h, (q, unit, _policy) in fields.items():
                column = {q: (sheet_name, header.index(h) + 1, unit, h)}
                assert q not in columns
                columns.update(column)
        cached_rows = {
            name: {i: row for i, row in enumerate(values[name].iter_rows(), 1)}
            for name in (SHEET, DET_SHEET)}
        formula_rows = {
            name: {i: row for i, row in enumerate(formulas[name].iter_rows(), 1)}
            for name in (SHEET, DET_SHEET)}
        checked = Counter()
        for run_ in result["runs"]:
            for outcome in run_["outcomes"]:
                if outcome["quantity"] not in columns:
                    continue
                source = run_["sources"][outcome["source"]]
                sheet_name, col, unit, header_name = columns[outcome["quantity"]]
                assert source["kind"] == "psi-workbook" and source["file"] == BOOK and source["sheet"] == sheet_name
                cell = cached_rows[sheet_name][source["row"]][col - 1]
                formula = formula_rows[sheet_name][source["row"]][col - 1]
                measure = outcome["measure"]
                assert measure["value"] == cell.value
                assert measure["raw"] == str(cell.value) and measure["unit"] == unit
                assert {"source_processed", "workbook_cached"} <= set(measure["flags"])
                assert run_["raw"][outcome["source"]][f"Formula {formula.coordinate}"] == formula.value
                if sheet_name == SHEET:
                    assert measure["value"] > 0
                checked[outcome["quantity"]] += 1
        assert set(checked) == set(columns)
    finally:
        values.close()
        formulas.close()


def test_schema_change_or_ambiguous_join_cannot_silently_attach_values(tmp_path):
    wb = openpyxl.Workbook()
    sheet = wb.active
    headers = ["Flight 1=same 2=sameR, g=ground", "Sample Type", "SAME #", *{h: (q, u) for h, (q, u, p) in FIELDS.items()}]
    sheet.append(["Title"])
    sheet.append(headers)
    sheet.append([2, "Kapton", 7, 1, 2, 3, 4])
    ctx = Ctx(tmp_path, tmp_path, {"same-r": {"psi_id": "PSI-101"}})
    a = Run("same-r", "SAME #7", conditions={"fuel": cat("Kapton")})
    b = Run("same-r", "SAME #7", conditions={"fuel": cat("Kapton")})
    _merge(ctx, [a, b], sheet, sheet)
    assert not a.outcomes and not b.outcomes and ctx.reports[-1].skipped
    sheet.cell(2, 4, "Unspecified concentration")
    with pytest.raises(ValueError, match="header"):
        _merge(ctx, [a], sheet, sheet)
