"""Pairwise comparability audit. Missing metadata never means equivalence."""
from __future__ import annotations

import math
import re

VERSION = "comparability-v2"
BASE = ("fuel_family", "fuel", "gravity", "flow_direction", "apparatus", "confinement", "instrument", "measurement_method")
AXES = {
    "solid-fuel": ("o2_pct", "pressure_atm", "flow_cm_s", "fuel_form"),
    "droplet-combustion": ("o2_pct", "pressure_atm", "droplet_d0_mm"),
    "gaseous-flames": ("o2_pct", "pressure_atm", "fuel_flow_mg_s", "nozzle_diameter_mm", "flame_type"),
    "smoke-aerosol": ("flow_cm_s", "rt_r0", "duration_s", "net_aging_s"),
}
DIMENSIONS = ("thickness_mm", "width_cm", "length_cm", "diameter_mm", "nozzle_diameter_mm", "fuel_fraction_pct", "oxidizer_stream_o2_pct", "duct_width_cm", "duct_height_cm", "duct_length_cm")
COMPOSITION = ("diluent", "n2_pct", "co2_pct", "he_pct", "ambient_fuel_pct", "oxidizer_flow_mg_s", "ambient_temperature_k")


def _value(c):
    if not isinstance(c, dict):
        return None
    v = c.get("value")
    if isinstance(v, str):
        return {"value": v, "unit": None, "raw": c.get("raw", v)}
    if v is None or not isinstance(v, (int, float)) or isinstance(v, bool) or not math.isfinite(v) or c.get("min", v) != c.get("max", v) or c.get("detection_limit") or any(f in c.get("flags", []) for f in ("multi", "source_definition_unresolved")):
        return {"value": None, "raw": c.get("raw", "not reported"), "unit": c.get("unit")}
    return {"value": v, "unit": c.get("unit"), "raw": c.get("raw", str(v)),
            **({"uncertainty": c["uncertainty"]} if c.get("uncertainty") else {})}


def _method_value(run, outcome, field):
    """Selected-outcome provenance wins; an invalid pointer never falls back."""
    metadata = outcome.get("metadata", {}) if outcome else {}
    if field not in metadata:
        return _value(run["conditions"].get(field))
    c = metadata[field]
    if not isinstance(c, dict):
        return None
    index, quote = c.get("source"), c.get("quote")
    if not isinstance(index, int) or isinstance(index, bool) or not 0 <= index < len(run.get("sources", [])) or not isinstance(quote, str) or not quote.strip():
        return None
    source = run["sources"][index]
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    if not isinstance(source, dict) or not isinstance(source.get("quote"), str) or source.get("kind") not in ("report", "psi-workbook") or norm(quote) not in norm(source["quote"]):
        return None
    result = _value(c)
    return {**result, "source": index, "quote": quote} if result is not None else None


def compare_runs(left: dict, right: dict, investigations: dict, quantity: str, varied_axis: str | None = None) -> dict:
    lc, rc = left["conditions"], right["conditions"]
    selected = []
    for run in (left, right):
        outcomes = [o for o in run["outcomes"] if o["quantity"] == quantity]
        selected.append(outcomes[0] if len(outcomes) == 1 else None)
    lg = investigations[left["investigation"]]["geometry_class"]
    rg = investigations[right["investigation"]]["geometry_class"]
    fields = list(dict.fromkeys((*BASE, *AXES.get(lg, ()), *AXES.get(rg, ()),
                                *(k for k in (*DIMENSIONS, *COMPOSITION) if k in lc or k in rc))))
    if lg == "solid-fuel" and not any(k in fields for k in ("thickness_mm", "diameter_mm")):
        fields.append("thickness_mm")
    if lg == "solid-fuel" or rg == "solid-fuel":
        forms = [str(c.get("fuel_form", {}).get("value", "")).lower() for c in (lc, rc)]
        required = ("diameter_mm",) if all(f in ("rod", "sphere") for f in forms) else ("thickness_mm", "width_cm", "length_cm")
        fields = list(dict.fromkeys((*fields, *required)))
    checks = []

    def check(field, a, b, conflict=False):
        status = "source-conflict" if conflict else "unknown"
        if not conflict and a is not None and b is not None and a.get("value") is not None and b.get("value") is not None:
            av, bv = a["value"], b["value"]
            equal = (av.strip().lower() == bv.strip().lower()) if isinstance(av, str) and isinstance(bv, str) else av == bv
            if isinstance(av, str) or field == "rt_r0" or field.startswith("outcome_at:") or (a.get("unit") and b.get("unit")):
                status = "match" if equal and a.get("unit") == b.get("unit") else "different"
            if not isinstance(av, str) and a.get("unit") != b.get("unit"):
                status = "unknown"
        checks.append({"field": field, "left": a, "right": b, "status": status})

    check("geometry_class", _value({"value": lg}), _value({"value": rg}))
    check("record_type", _value({"value": "individual" if left["granularity"] in ("test", "test-point") else left["granularity"]}),
          _value({"value": "individual" if right["granularity"] in ("test", "test-point") else right["granularity"]}))
    conflicts = {c["field"] for r in (left, right) for c in r.get("conflicts", [])}
    for field in fields:
        if field in ("instrument", "measurement_method"):
            check(field, _method_value(left, selected[0], field), _method_value(right, selected[1], field), field in conflicts)
        else:
            check(field, _value(lc.get(field)), _value(rc.get(field)), field in conflicts)
    check("outcome:" + quantity, _value(selected[0].get("measure")) if selected[0] else None,
          _value(selected[1].get("measure")) if selected[1] else None, "outcome:" + quantity in conflicts)
    # A per-outcome condition overrides a run-wide envelope. It cannot be
    # ignored even when the run-level conditions happen to match.
    for axis in sorted({k for o in selected if o for k in o.get("at", {})}):
        check("outcome_at:" + axis,
              _value({"value": selected[0].get("at", {}).get(axis)}) if selected[0] else None,
              _value({"value": selected[1].get("at", {}).get(axis)}) if selected[1] else None)
    blockers = [c["field"] for c in checks if c["status"] in ("unknown", "source-conflict")]
    if lg != rg:
        blockers.append("geometry_class")
    if left["id"] == right["id"]:
        blockers.append("same_record")
    if varied_axis is not None and varied_axis not in (*DIMENSIONS, "o2_pct", "pressure_atm", "flow_cm_s", "droplet_d0_mm", "fuel_flow_mg_s"):
        blockers.append("invalid_varied_axis")
    differences = [c["field"] for c in checks if c["status"] == "different" and not c["field"].startswith("outcome:")]
    if left["granularity"] not in ("test", "test-point") or right["granularity"] not in ("test", "test-point"):
        blockers.append("non_individual_record")
    if all(o and o.get("measure") for o in selected) and selected[0]["measure"].get("unit") != selected[1]["measure"].get("unit"):
        blockers.append("outcome_unit")
    unexplained = [f for f in differences if f.removeprefix("outcome_at:") != varied_axis]
    allowed = not blockers and not unexplained
    return {"method_version": VERSION, "left_id": left["id"], "right_id": right["id"], "quantity": quantity,
            "varied_axis": varied_axis, "checks": checks, "unknown_or_conflicted": blockers, "differences": differences,
            "can_compare": allowed, "status": "insufficient_metadata" if blockers else "different_conditions" if unexplained
            else "controlled_difference" if differences else "condition_matched",
            "outcomes": selected, "limitations": "Descriptive comparison only. Missing metadata blocks a condition-matched claim; "
            "reported ranges are not uncertainty intervals. No statistical-significance, predictive or safety claim."}


def comparison_audit(left: dict, right: dict, investigations: dict, quantity: str, varied_axis: str | None = None) -> dict:
    """Separate useful sourced observations from an unsupported equivalence claim.

    This is additive to comparability-v1; its strict required fields and output
    remain unchanged. Keep the TypeScript comparisonAudit twin in sync.
    """
    assessment = compare_runs(left, right, investigations, quantity, varied_axis)
    setup = [c for c in assessment["checks"] if not c["field"].startswith("outcome:")]
    shared = [c for c in setup if c["status"] == "match"]
    differences = [c for c in setup if c["status"] == "different"]
    missing = [c for c in assessment["checks"] if c["status"] == "unknown"]
    conflicts = [c for c in assessment["checks"] if c["status"] == "source-conflict"]
    sourced_outcomes = []
    for run, outcome in zip((left, right), assessment["outcomes"]):
        index = outcome.get("source") if outcome else None
        sources = run.get("sources", [])
        source = sources[index] if isinstance(index, int) and not isinstance(index, bool) and 0 <= index < len(sources) else None
        sourced_outcomes.append({"run_id": run["id"], "outcome": outcome, "source_index": index, "source": source})
    steps = []
    if missing:
        steps.append({"code": "INSPECT_MISSING_METADATA", "fields": [c["field"] for c in missing], "text": "Inspect the linked original sources for these missing or ambiguous fields. The source may not contain the value; do not fill it by inference."})
    if conflicts:
        steps.append({"code": "REVIEW_RETAINED_CONFLICTS", "fields": [c["field"] for c in conflicts], "text": "Inspect both retained source values before using the disputed field."})
    unexplained = [c for c in differences if c["field"].removeprefix("outcome_at:") != varied_axis]
    if unexplained:
        steps.append({"code": "MULTIPLE_SETUP_DIFFERENCES", "fields": [c["field"] for c in unexplained], "text": "These recorded conditions differ beyond the nominated varied condition. Their effects cannot be isolated by this pair."})
    selection = [f for f in assessment["unknown_or_conflicted"] if f in ("geometry_class", "same_record", "non_individual_record", "invalid_varied_axis")]
    if selection:
        steps.append({"code": "REVIEW_SELECTION", "fields": selection, "text": "Choose distinct individual records in one geometry class and a supported varied condition before considering a matched comparison."})
    both_sourced = all(o["outcome"] is not None and o["source"] is not None for o in sourced_outcomes)
    if not both_sourced:
        steps.append({"code": "INSPECT_OUTCOME_SOURCES", "fields": ["outcome:" + quantity], "text": "One or both records lack a single selected outcome with a valid source index. Inspect the original records; no missing outcome or citation is supplied."})
    steps.append({"code": "DESCRIPTIVE_ONLY", "fields": [], "text": "Use this audit to explain shared evidence, setup differences and the remaining source checks. It does not estimate a treatment effect, statistical significance, material safety or gravity equivalence."})
    return {"method_version": "comparison-audit-v1", "assessment": assessment,
            "research_result": "Two source-linked outcomes are available for inspection. Shared facts and recorded differences are separated below; the strict comparability assessment still applies." if both_sourced else "The audit identifies recorded facts and the source checks needed before comparing the selected outcomes.",
            "shared_facts": shared, "recorded_differences": differences, "missing_or_ambiguous": missing, "conflicted_checks": conflicts,
            "retained_conflicts": [{"run_id": run["id"], **c} for run in (left, right) for c in run.get("conflicts", [])],
            "sourced_outcomes": sourced_outcomes, "next_steps": steps,
            "limitations": "An evidence audit is not a controlled experiment. Shared recorded fields do not establish equivalence; unrecorded details remain unknown. No subtraction, ratio, causal effect or safety ranking is inferred from this pair."}
