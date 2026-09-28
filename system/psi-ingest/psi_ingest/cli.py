"""`uv run psi-ingest` — regenerate psi-data/derived/ from psi-data/raw/ + knowledge/.

Outputs (all generated; never hand-edit):
  psi-data/derived/runs.json            every run, full provenance + raw cells
  psi-data/derived/investigations.json  per-investigation identity, citation, coverage
  psi-data/derived/ingest-report.json   rows read / emitted / skipped (+why) per file
and a copy of runs.json + investigations.json for the copilot, which deploys
on its own (system/chatkit-server/data/).
"""

from __future__ import annotations

import argparse
import json
import shutil
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

from . import knowledge
from .adapters import Ctx, droplet, gaseous, smoke, solid
from .model import Run
from .reports import merge_all
from .units import Measure

HERE = Path(__file__).resolve().parent
REPO_ROOT = HERE.parents[2]

NUMERIC_AXES = ("o2_pct", "flow_cm_s", "pressure_atm", "thickness_mm", "droplet_d0_mm", "fuel_fraction_pct",
                "oxidizer_stream_o2_pct")


def load_registry() -> dict:
    return yaml.safe_load((HERE.parent / "registry.yaml").read_text(encoding="utf-8"))["investigations"]


def assign_ids(runs: list[Run], registry: dict, report: dict) -> None:
    seen: Counter = Counter()
    for r in runs:
        psi = registry[r.investigation]["psi_id"] if any(s["kind"].startswith("psi") for s in r.sources) else None
        base = f"{psi}:{r.label}" if psi else f"{r.investigation}:{r.label}"
        seen[base] += 1
        if seen[base] > 1:
            report.setdefault("duplicate_labels", []).append(base)
            base = f"{base}#{seen[base]}"
        r.id = base


def coverage(runs: list[Run]) -> dict:
    out = {}
    for axis in NUMERIC_AXES:
        ms = [r.conditions[axis] for r in runs if isinstance(r.conditions.get(axis), Measure) and r.conditions[axis].usable]
        if ms:
            out[axis] = {"runs": len(ms), "min": min(m.min for m in ms), "max": max(m.max for m in ms),
                         "unit": ms[0].unit}
    fams = Counter((r.conditions.get("fuel_family") or {}).get("value") for r in runs)
    out["fuel_family"] = {k or "unassigned": v for k, v in fams.most_common()}
    return out


def investigations(runs: list[Run], ctx: Ctx) -> list[dict]:
    out = []
    for key, reg in ctx.registry.items():
        rs = [r for r in runs if r.investigation == key]
        cit = knowledge.citation(ctx.repo_root, reg["ksor_doc"], reg["source_id"]) if reg["ksor_doc"] else None
        out.append({
            "id": key,
            "name": reg["name"],
            "full_name": reg["full_name"],
            "psi_id": reg["psi_id"],
            "geometry_class": reg["geometry_class"],
            "citation": cit,
            "runs": len(rs),
            "granularity": dict(Counter(r.granularity for r in rs)),
            "runs_with_report_data": sum(any(s["kind"] == "report" for s in r.sources) for r in rs),
            "runs_with_outcomes": sum(bool(r.outcomes) for r in rs),
            "conflicts": sum(len(r.conflicts) for r in rs),
            "outcome_quantities": dict(Counter(o.quantity for r in rs for o in r.outcomes).most_common()),
            "coverage": coverage(rs),
            "table_notes": ctx.table_notes.get(key, []),
            "psi_files": sorted({s["file"] for r in rs for s in r.sources if s["kind"].startswith("psi")}),
        })
    return out


def run(repo_root: Path = REPO_ROOT, write: bool = True) -> dict:
    ctx = Ctx(repo_root=repo_root, raw_dir=repo_root / "psi-data" / "raw", registry=load_registry())
    runs: list[Run] = []
    for module in (solid, droplet, gaseous, smoke):
        for adapter in module.ADAPTERS:
            runs.extend(adapter(ctx))
    merge_stats = merge_all(ctx, runs)
    report: dict = {}
    assign_ids(runs, ctx.registry, report)

    generated = {"generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 "generator": "system/psi-ingest"}
    runs_json = [r.to_json() for r in runs]
    invs = investigations(runs, ctx)
    report.update({
        **generated,
        "totals": {
            "runs": len(runs),
            "by_granularity": dict(Counter(r.granularity for r in runs)),
            "investigations": sum(1 for i in invs if i["runs"]),
            "runs_with_outcomes": sum(bool(r.outcomes) for r in runs),
            "runs_with_report_data": sum(any(s["kind"] == "report" for s in r.sources) for r in runs),
            "conflicts": sum(len(r.conflicts) for r in runs),
            "rows_read": sum(f.rows_read for f in ctx.reports),
            "rows_skipped": sum(len(f.skipped) for f in ctx.reports),
        },
        "files": [f.to_json() for f in ctx.reports],
        "report_tables": merge_stats,
        "not_ingested": NOT_INGESTED,
    })
    if write:
        out = repo_root / "psi-data" / "derived"
        out.mkdir(parents=True, exist_ok=True)
        _dump(out / "runs.json", {**generated, "runs": runs_json})
        _dump(out / "investigations.json", {**generated, "investigations": invs})
        _dump(out / "ingest-report.json", report)
        copilot = repo_root / "system" / "chatkit-server" / "data"
        copilot.mkdir(exist_ok=True)
        for name in ("runs.json", "investigations.json"):
            shutil.copyfile(out / name, copilot / name)
    return {"runs": runs_json, "investigations": invs, "report": report}


NOT_INGESTED = [
    {"file": "matrices/BASS Test Matrix 050213.xlsx",
     "why": "planning matrix whose first row contains account credentials; never read. The as-run matrix and PSI-26 cover the same tests."},
    {"file": "matrices/BASS test matrix.xlsx", "why": "as-run operations matrix (camera/radiometer settings); PSI-25/26 carry the test rows"},
    {"file": "matrices/ACME Daily Test Point Log 2.xlsx", "why": "downlink/data-volume log, not test conditions"},
    {"file": "matrices/SAME VPRED Matrix PLN-005 Baseline.xls", "why": "pre-flight planning matrix (not as-run)"},
    {"file": "matrices/thermal precipitator map corrected 10-12-2011 (1).xlsx", "why": "SAME-R hardware usage map, not test conditions"},
    {"file": "summaries/SAFFIRE-*_MergeResult*.xlsx", "why": "camera image downlink logs (file names, byte counts) — no combustion data"},
    {"file": "summaries/Combined SAMER Results 06 02 14.xlsx", "why": "SAME/SAME-R smoke diagnostics workbook; not yet mapped (PSI-101/102 carry the runs)"},
    {"file": "reports/*.pdf (other than BASS-II, SPICE, SAME-R)",
     "why": "converted to psi-data/derived/report-extractions/ but no per-test table with intact headers found yet; "
            "report values enter via governed knowledge/ tables or verified extractions (see report_tables)"},
]


def _dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="run without writing outputs")
    args = ap.parse_args()
    result = run(write=not args.check)
    t = result["report"]["totals"]
    print(f"psi-ingest: {t['runs']} runs from {t['investigations']} investigations "
          f"({t['by_granularity']}); {t['runs_with_outcomes']} with outcomes, "
          f"{t['runs_with_report_data']} with report data, {t['conflicts']} source conflicts; "
          f"{t['rows_read']} rows read, {t['rows_skipped']} skipped")


if __name__ == "__main__":
    main()
