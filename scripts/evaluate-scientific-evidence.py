"""Reproducible internal scientific audit; no model-fitting or safety certification.

Run with the backend venv from the repository root. Source values stay unchanged.
The dimensional checks below are conditional diagnostics, not source corrections.
"""
from collections import Counter
from datetime import datetime, timezone
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "system/chatkit-server"))
from psi_comparison import compare_runs


def evaluate():
    dataset = ROOT / "psi-data/derived/runs.json"
    runs = json.loads(dataset.read_text(encoding="utf-8"))["runs"]
    invs = {i["id"]: i for i in json.loads((ROOT / "psi-data/derived/investigations.json").read_text(encoding="utf-8"))["investigations"]}
    numeric = lambda o: isinstance(o.get("measure", {}).get("value"), (int, float))
    individual = [r for r in runs if r["granularity"] in ("test", "test-point")]
    groups = {}
    for geometry in sorted({i["geometry_class"] for i in invs.values()}):
        selected = [r for r in individual if invs[r["investigation"]]["geometry_class"] == geometry]
        groups[geometry] = {"individual_records": len(selected),
            "numeric_outcome_records": sum(any(numeric(o) for o in r["outcomes"]) for r in selected),
            "missing_conditions": {key: sum(r["conditions"].get(key, {}).get("min") is None for r in selected)
                                   for key in ("o2_pct", "pressure_atm", "flow_cm_s")},
            "reported_uncertainty_outcomes": sum(bool(o.get("measure", {}).get("uncertainty")) for r in selected for o in r["outcomes"])}
    paired = []
    for run in runs:
        if run["investigation"] != "flex-2":
            continue
        by_source = {}
        for o in run["outcomes"]:
            if o["quantity"] in ("burning_rate_k_hot", "burning_rate_k_cool"):
                by_source.setdefault(o["source"], {})[o["quantity"]] = o["measure"]["value"]
        for source, values in by_source.items():
            if len(values) != 2:
                continue
            raw = run["raw"][source]
            paired.append({"test": raw["Test"], "envelope_id": run["id"],
                "hot_mm2_s": values["burning_rate_k_hot"], "cool_mm2_s": values["burning_rate_k_cool"],
                "cool_to_hot_ratio": round(values["burning_rate_k_cool"] / values["burning_rate_k_hot"], 6),
                "printed_atmosphere_inconsistent": raw["Test"] == "R383",
                "source": run["sources"][source],
                "interpretation": "Derived within-burn descriptive ratio, not a fuel ranking or independent replicate estimate."})
    assert len(paired) == 6 and all(p["cool_mm2_s"] < p["hot_mm2_s"] for p in paired)
    saffire = [r for r in runs if r["investigation"] == "saffire-iv-vi"]
    consistency = []
    for r in saffire:
        outcomes = {o["quantity"]: o for o in r["outcomes"]}
        value = lambda key: outcomes.get(key, {}).get("measure", {}).get("value")
        peak, duration, total = value("peak_heat_release"), value("burn_time"), value("total_heat_release_imaging")
        if peak is not None and duration is not None and total is not None:
            ceiling = peak * duration / 1000
            consistency.append({"run_id": r["id"], "peak_W": peak, "duration_s": duration,
                "total_imaging_kJ": total, "conditional_maximum_kJ": round(ceiling, 6),
                "exceeds_conditional_maximum": total > ceiling,
                "quarantined_from_quantitative_analysis": "source_definition_unresolved" in outcomes["total_heat_release_imaging"]["measure"].get("flags", []),
                "source": r["sources"][outcomes["total_heat_release_imaging"]["source"]],
                "qualification": "E <= peak power * duration only if methods, integration interval and peak definition coincide. A mismatch requires source clarification, not replacing values."})
    comparisons = []
    for left, right in itertools.combinations(saffire, 2):
        assessment = compare_runs(left, right, invs, "co2_partial_pressure_increase")
        comparisons.append({"left": left["id"], "right": right["id"],
            "can_compare": assessment["can_compare"], "status": assessment["status"],
            "unknown_or_conflicted": assessment["unknown_or_conflicted"]})
    return {"evaluated_at": datetime.now(timezone.utc).isoformat(),
        "reviewer": "Codex internal source-based scientific evaluation; not NASA review or endorsement",
        "dataset_sha256": hashlib.sha256(dataset.read_bytes()).hexdigest(),
        "records": len(runs), "individual_records": len(individual),
        "outcome_records": sum(bool(r["outcomes"]) for r in runs),
        "granularities": dict(Counter(r["granularity"] for r in runs)),
        "completeness": groups, "paired_flex_literature": paired,
        "saffire_conditional_energy_checks": consistency, "saffire_comparisons": comparisons,
        "verdict": {"source_traceability": "Auditable, with retained raw cells and per-outcome citations; separate transfer audit required.",
                    "descriptive_research": "Useful within source, geometry, endpoint and apparatus limits.",
                    "pooled_material_safety_ranking": "Not established by this heterogeneous index.",
                    "predictive_validation": "Not performed: no held-out predictive model, replicate uncertainty analysis or calibrated risk score.",
                    "partial_gravity": "LUCI is separate rotating-platform literature; microgravity condition overlap is not lunar-gravity validation."}}


def write_report(result):
    target = ROOT / "research/scientific-evaluation.json"
    target.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    lines = ["# Internal scientific evaluation", "", result["reviewer"], "",
        f"Dataset SHA-256: `{result['dataset_sha256']}`. Evaluated {result['evaluated_at']}.", "",
        "## Assessment", "",
        "The index supports source-traceable descriptive research. It does not establish a pooled material safety ranking, a validated predictive model, or lunar fire-safety certification.", "",
        f"The dataset contains {result['records']:,} records, {result['individual_records']:,} individual test/test-point records, and {result['outcome_records']:,} records with outcomes. Literature burns attached to planned fuel envelopes remain envelopes.", "",
        "## Within-burn cool-flame comparison", "",
        "These six paired values were selected by the publication, not sampled as independent replicates. No significance test, confidence interval or general fuel ranking is justified. Ratios below are derived, not source-reported measurements.", "",
        "| Literature burn | Hot K (mm²/s) | Cool K (mm²/s) | Derived cool/hot | Caveat |",
        "| --- | ---: | ---: | ---: | --- |"]
    for p in result["paired_flex_literature"]:
        lines.append(f"| {p['test']} | {p['hot_mm2_s']} | {p['cool_mm2_s']} | {p['cool_to_hot_ratio']} | " + ("Printed atmosphere sums beyond 100%" if p["printed_atmosphere_inconsistent"] else "Selected literature burn") + " |")
    lines += ["", "Source: [Nayagam et al., 2014](https://ntrs.nasa.gov/citations/20140006750). The source's R383 atmosphere is preserved, not repaired.", "", "## Conditional energy consistency", "",
        "If a peak heat-release rate and an integrated energy share a measurement method and integration interval, energy cannot exceed peak power multiplied by duration. This is a diagnostic condition, not proof that those assumptions hold for the table.", "",
        "| Record | Total imaging energy (kJ) | Peak × duration (kJ) | Needs source clarification |",
        "| --- | ---: | ---: | --- |"]
    for c in result["saffire_conditional_energy_checks"]:
        lines.append(f"| {c['run_id']} | {c['total_imaging_kJ']} | {c['conditional_maximum_kJ']} | {c['exceeds_conditional_maximum']} |")
    lines += ["", "Source: [SAFFIRE preliminary results, Table 2](https://ntrs.nasa.gov/citations/20240002981). Do not silently correct a published value. Method labels, integration periods and possible source errors need clarification before model fitting.", "",
        "The governed SAFFIRE prose labels the SIBAL cross-check VI-3, while the original report and Table 1 identify that SIBAL sample as VI-2. Structured records use the table identities. This narrative discrepancy needs governed correction and must not support the VI-3 PMMA result.", "",
        "## Detection and partial-gravity interpretation", "",
        "Camera non-detection applies to the imagers used in the FLEX study; it is not a demonstrated performance criterion for every crew camera.", "",
        "The SAFFIRE VI-3 threshold-crossing observation uses a report-selected concentration threshold and the reported timeline. It is not a demonstrated ignition-to-alarm delay or universal detector response specification. Remote temperature maxima and source-outlet maxima are not necessarily simultaneous; their difference is not an instantaneous thermal gradient.", "",
        "DAFT reports bounds on campaign-average background aerosols, not fire-smoke detection limits. SAME-R cached diagnostics measure transfer agreement, not calibration. LUCI uses a rotating platform, time-varying oxygen and fitted flame tracking; Coriolis effects and changing acceleration prevent treating its results as a stationary lunar habitat certification.", "",
        "## Comparability and missingness", "",
        f"The production comparison audit evaluated {len(result['saffire_comparisons'])} pairs among the five SAFFIRE records. {sum(c['can_compare'] for c in result['saffire_comparisons'])} support a condition-matched comparison under the recorded metadata. A common investigation name is insufficient.", "",
        "Per-geometry missingness, uncertainty counts, full comparison diagnoses and source pointers are in the companion JSON. Missing metadata and uncertainty must remain unknown.", "",
        "## Required scientific work", "",
        "The affected SAFFIRE heat-release/time bundle is quarantined from quantitative analysis while its reported values are retained for source inspection. Source clarification is still needed to admit that bundle to analysis. Obtain independently identified as-run conditions and calibration/uncertainty; establish replicate and study identities; and evaluate any predictive model on held-out studies. This internal review does not substitute for independent subject-matter review or NASA materials qualification.", ""]
    (ROOT / "research/scientific-evaluation.md").write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote scientific evaluation: {len(result['paired_flex_literature'])} paired burns, {len(result['saffire_comparisons'])} comparison audits")


if __name__ == "__main__":
    write_report(evaluate())
