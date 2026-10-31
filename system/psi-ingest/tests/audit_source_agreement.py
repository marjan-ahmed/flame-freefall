"""Audit processed outcomes against saved workbook cells, not recalculation.

This measures transfer agreement only; it cannot establish calibration,
instrument accuracy, formula correctness or independent experimental validity.
"""
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import openpyxl
from psi_ingest.smoke_results import BOOK, DET_FIELDS, DET_SHEET, SHEET, FIELDS

ROOT = Path(__file__).resolve().parents[3]


def audit():
    source = ROOT / "psi-data/raw/summaries" / BOOK
    workbook = openpyxl.load_workbook(source, read_only=True, data_only=True)
    try:
        rows = {name: list(workbook[name].iter_rows(values_only=True)) for name in (SHEET, DET_SHEET)}
        fields: dict[str, tuple[str, int, str]] = {}
        for sheet_name, mapping in ((SHEET, FIELDS), (DET_SHEET, DET_FIELDS)):
            header = rows[sheet_name][1]
            for h, (q, unit, _policy) in mapping.items():
                assert q not in fields
                fields[q] = (sheet_name, header.index(h), unit)
        checked = 0
        mismatches = []
        dataset = ROOT / "psi-data/derived/runs.json"
        runs = json.loads(dataset.read_text(encoding="utf-8"))["runs"]
        for run in runs:
            for o in run["outcomes"]:
                if o["quantity"] not in fields:
                    continue
                s = run["sources"][o["source"]]
                sheet_name, col, unit = fields[o["quantity"]]
                original = rows[sheet_name][s["row"] - 1][col]
                m = o["measure"]
                checked += 1
                if s["file"] != BOOK or s["sheet"] != sheet_name or m["value"] != original or m["raw"] != str(original) or m["unit"] != unit:
                    mismatches.append({"run": run["id"], "quantity": o["quantity"], "row": s["row"]})
        assert checked > 0 and not mismatches, mismatches
        return {"measured_at": datetime.now(timezone.utc).isoformat(),
                "scope": "Transfer agreement of source-processed cached numeric outcomes and raw cells; no formula recalculation, calibration or scientific validation.",
                "dataset_sha256": hashlib.sha256(dataset.read_bytes()).hexdigest(),
                "source": str(source.relative_to(ROOT)), "source_sha256": hashlib.sha256(source.read_bytes()).hexdigest(),
                "cells_checked": checked, "mismatches": mismatches}
    finally:
        workbook.close()


if __name__ == "__main__":
    result = audit()
    target = ROOT / "research/source-agreement.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(f"{result['cells_checked']} source cells checked; no mismatches; {target}")
