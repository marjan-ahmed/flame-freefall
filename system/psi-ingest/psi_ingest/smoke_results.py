"""Join source-processed SAME-R diagnostics without inventing new tests.

The reduced workbook sheets combine SAME, SAME-R, and analysis rows. Only
flight 2 rows with an unambiguous SAME-R number AND material are admitted.
Formula caches are retained as published processed values, never recomputed.

Two sheets of the same workbook are joined, keyed identically:

- ``Reduced data sheet`` — mass concentrations and particle diameters, mapped
  since the workbook was first connected for the smoke/aerosol records.
- ``Reduced Data with ISS Det`` — the SAME rows with two extra instrument
  columns, the ISS and STS smoke-detector analog signals. Sign semantics come
  from the SAME final science report: smoke deflects the ISS detector's
  scattered-light signal POSITIVE and the STS detector's signal NEGATIVE, so a
  negative STS cell is a smoke response, never discarded; exactly zero is the
  only cell that cannot be told apart from a trace that was never recorded.
"""

from __future__ import annotations

from collections import defaultdict
import openpyxl

from .adapters import Ctx
from .model import Run
from .units import parse_measure

BOOK = "Combined SAMER Results 06 02 14.xlsx"
SHEET = "Reduced data sheet"
DET_SHEET = "Reduced Data with ISS Det"
KEY_HEADERS = ("Flight 1=same 2=sameR, g=ground", "Sample Type", "SAME #")

# header → (quantity, unit, admitted-value policy)
FIELDS = {
    "DustTrak A (mg/m3) Mpass_2nd  offset, dilution and Gain corrected":
        ("dusttrak_a_mass_concentration", "mg/m³", "positive_only"),
    "DustTrak B calibratred and corrected for dilution (mg/m3)":
        ("dusttrak_b_mass_concentration", "mg/m³", "positive_only"),
    "M1/M0 (micro-m)--AMD": ("aerosol_arithmetic_mean_diameter", "µm", "positive_only"),
    "Diameter of Average mass (micro-m)": ("aerosol_diameter_of_average_mass", "µm", "positive_only"),
}
DET_FIELDS = {
    "ISS Detector Scatter (volts)": ("iss_detector_scatter_volts", "V", "positive_only"),
    "STS Detector (volts)": ("sts_detector_volts", "V", "nonzero"),
}
# Columns present beside the detector signals but never mapped to outcomes:
# an offset is instrument processing, and no unit label is attached anywhere.
UNMAPPED_DETAIL_COLUMNS = ("STS Detector offset (volts)", "STS detector delta",
                           "Yeild: Dust Trak mass/mass lostt")

# How a cached cell may enter the record, per quantity policy above.
_ADMITS = {
    "positive_only": lambda m: m.value is not None and m.value > 0,
    "nonzero": lambda m: m.value is not None and m.value != 0,
}

_SIGNAL_NOTE = {
    "iss_detector_scatter_volts": "smoke deflects this ISS forward-scattering signal upward; "
                                  "the sheet states no zero-point, so the reading is an instrument-scale "
                                  "voltage, not calibrated smoke density",
    "sts_detector_volts": "smoke deflects this STS signal downward against the sheet's own "
                          "'STS Detector offset (volts)' baseline column; a negative reading is a smoke response",
}


def _key(value: object) -> str:
    if isinstance(value, float) and value.is_integer():
        return str(int(value))
    return str(value).strip().lower()


def merge_same_r_diagnostics(ctx: Ctx, runs: list[Run]) -> None:
    """Join source-processed diagnostics from the SAME-R workbook's sheets."""
    path = ctx.raw_dir / "summaries" / BOOK
    # Both representations are needed: the source's saved numeric result and
    # the formula that produced it. Loading a workbook does not execute formulas.
    cached = openpyxl.load_workbook(path, read_only=True, data_only=True)
    formulas = openpyxl.load_workbook(path, read_only=True, data_only=False)
    try:
        _join(ctx, runs, cached[SHEET], formulas[SHEET], FIELDS)
        _join(ctx, runs, cached[DET_SHEET], formulas[DET_SHEET], DET_FIELDS)
        ctx.note("same-r", "Additional mass concentrations, particle diameters and smoke-detector "
                 "signals come from source-processed sheets of the Combined SAMER workbook: cached "
                 "published calculations and one-per-test instrument readings, not new measurements "
                 "or independent tests; not recalculated; no uncertainty supplied.")
    finally:
        cached.close()
        formulas.close()


def _same_r_candidates(runs: list[Run]) -> dict[tuple[str, str], list[Run]]:
    by_key = defaultdict(list)
    for run in runs:
        if run.investigation == "same-r":
            material = (run.conditions.get("fuel") or {}).get("value", "")
            by_key[(_key(run.label.removeprefix("SAME #")), _key(material))].append(run)
    return by_key


def _join(ctx: Ctx, runs: list[Run], sheet, formula_sheet, fields: dict[str, tuple[str, str, str]]) -> None:
    """One workbook sheet → existing SAME-R flight 2 runs, by test number AND material.

    The reduced sheet does not disambiguate disabled diagnostics from real
    zeros: cells admitted as ``positive_only`` with a nonpositive value are
    retained in raw data but never become a quantitative absence-of-smoke claim.
    For the detector quantities a NEGATIVE cell is a declared smoke response,
    so only exactly zero is excluded.
    """
    report = ctx.report(f"summaries/{BOOK} [{sheet.title}]", "same-r")
    header = [str(v).strip() if v is not None else "" for v in next(sheet.iter_rows(min_row=2, max_row=2, values_only=True))]
    for name in (*KEY_HEADERS, *fields):
        if header.count(name) != 1:
            raise ValueError(f"{BOOK} [{sheet.title}]: missing or ambiguous header {name!r}")
    index = {name: header.index(name) for name in (*KEY_HEADERS, *fields)}
    by_key = _same_r_candidates(runs)

    rows = list(sheet.iter_rows(min_row=3))
    formula_rows = list(formula_sheet.iter_rows(min_row=3))
    identities = defaultdict(int)
    for cells in rows:
        if cells[index[KEY_HEADERS[0]]].value == 2:
            identities[(_key(cells[index[KEY_HEADERS[2]]].value), _key(cells[index[KEY_HEADERS[1]]].value))] += 1

    omitted_nonpositive = 0
    negative_sts_kept = 0
    for line, (cells, source_cells) in enumerate(zip(rows, formula_rows, strict=True), start=3):
        report.rows_read += 1
        if cells[index[KEY_HEADERS[0]]].value != 2:
            report.skip(line, "not a SAME-R flight 2 data row")
            continue
        key = (_key(cells[index[KEY_HEADERS[2]]].value), _key(cells[index[KEY_HEADERS[1]]].value))
        candidates = by_key.get(key, [])
        if len(candidates) != 1 or identities[key] != 1:
            report.skip(line, f"no unique PSI SAME-R number/material join: {key[0]} / {key[1]}")
            continue

        values = []
        for column, (quantity, unit, policy) in fields.items():
            cell = cells[index[column]]
            measure = parse_measure(cell.value, unit)
            if measure is None or not measure.usable:
                continue
            if not _ADMITS[policy](measure):
                omitted_nonpositive += 1
                continue
            values.append((quantity, measure.flag("source_processed", "workbook_cached"), cell.coordinate))
        if not values:
            report.skip(line, f"no admissible numeric diagnostics under the sheet's policy ({key[0]} / {key[1]})")
            continue

        detector_pass = sheet.title == DET_SHEET
        run = candidates[0]
        source = len(run.sources)
        run.sources.append({"kind": "psi-workbook", "dataset": ctx.psi_id("same-r"),
                            "file": BOOK, "sheet": sheet.title, "row": line})
        raw = {name: str(cell.value) for name, cell in zip(header, cells) if name and cell.value is not None}
        raw.update({f"Formula {cell.coordinate}": str(cell.value) for cell in source_cells if cell.data_type == "f"})
        run.raw.append(raw)
        for quantity, measure, coordinate in values:
            negative_sts_kept += quantity == "sts_detector_volts" and measure.value < 0
            run.outcome(quantity, measure, source=source,
                        note=f"{sheet.title}!{coordinate}: source-processed cached workbook result; "
                             "formula retained with source cells, not recalculated; measurement "
                             f"uncertainty not supplied. {_SIGNAL_NOTE.get(quantity, '')}".strip())
        run.notes.append("SAME-R workbook diagnostics joined by exact test number and material. "
                         "Source-processed results are not independent additional tests. "
                         f"{sheet.title} does not mark disabled diagnostics, so exactly-zero (or, "
                         "for concentrations and diameters, nonpositive) cells are kept in raw data "
                         "but never stated as absence of smoke." + (
                             " A negative STS detector cell IS a smoke response and is kept."
                             if detector_pass else ""))
        report.merged_into_previous += 1

    report.notes.extend([
        f"Only existing SAME-R flight 2 records are enriched; no test identifiers or material assignments are repaired.",
        f"Only the explicitly unit-labeled columns are mapped ({', '.join(q for q, _, _ in fields.values())}); "
        "formulas and cached cells are retained; the sheet's unlabeled computed columns "
        f"({', '.join(UNMAPPED_DETAIL_COLUMNS) if sheet.title == DET_SHEET else 'with no explicit unit'}) are not.",
        f"{omitted_nonpositive} cached cells excluded under the sheet-admission policy"
        + (f"; {negative_sts_kept} negative STS readings kept as declared smoke responses." if sheet.title == DET_SHEET else ""),
    ])


def _merge(ctx: Ctx, runs: list[Run], sheet, formula_sheet) -> None:
    """Test seam: one join pass against a supplied sheet pair."""
    _join(ctx, runs, sheet, formula_sheet, FIELDS)
