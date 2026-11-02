"""Adversarial comparisons, also emitted as fixtures for the TS twin."""
from copy import deepcopy

from psi_comparison import compare_runs


def cases():
    conditions = {k: {"value": v} for k, v in {
        "fuel_family": "PMMA", "fuel": "PMMA", "gravity": "microgravity",
        "flow_direction": "opposed", "apparatus": "test chamber", "confinement": "duct",
        "instrument": "camera", "measurement_method": "front tracking", "fuel_form": "sheet",
    }.items()}
    for k, v, unit in [("o2_pct", 21, "%"), ("pressure_atm", 1, "atm"),
                        ("flow_cm_s", 5, "cm/s"), ("thickness_mm", 1, "mm"), ("width_cm", 2, "cm"), ("length_cm", 10, "cm")]:
        conditions[k] = {"value": v, "min": v, "max": v, "unit": unit, "raw": str(v)}
    run = {"id": "synthetic:a", "investigation": "synthetic", "granularity": "test",
           "conditions": conditions, "outcomes": [{"quantity": "spread_rate", "source": 0,
           "measure": {"raw": "0.1", "value": .1, "min": .1, "max": .1, "unit": "mm/s"}}]}
    inv = {"synthetic": {"geometry_class": "solid-fuel"}}
    def case(name, change, status, varied=None):
        right = deepcopy(run)
        right["id"] = "synthetic:b"
        change(right)
        return {"name": name, "left": deepcopy(run), "right": right, "investigations": inv,
                "quantity": "spread_rate", "varied_axis": varied, "status": status}
    return [
        case("complete metadata", lambda r: None, "condition_matched"),
        case("same record is not a second test", lambda r: r.update(id="synthetic:a"), "insufficient_metadata"),
        case("missing pressure", lambda r: r["conditions"].pop("pressure_atm"), "insufficient_metadata"),
        case("missing specimen width", lambda r: r["conditions"].pop("width_cm"), "insufficient_metadata"),
        case("unit change is not controlled variation", lambda r: r["conditions"]["flow_cm_s"].update(unit="mm/s"), "insufficient_metadata", "flow_cm_s"),
        case("different flow", lambda r: r["conditions"]["flow_cm_s"].update(value=10, min=10, max=10), "different_conditions"),
        case("declared flow variation", lambda r: r["conditions"]["flow_cm_s"].update(value=10, min=10, max=10), "controlled_difference", "flow_cm_s"),
        case("conflict", lambda r: r.update(conflicts=[{"field": "pressure_atm"}]), "insufficient_metadata"),
        case("unresolved source definition", lambda r: r["outcomes"][0]["measure"].update(flags=["source_definition_unresolved"]), "insufficient_metadata"),
        case("summary", lambda r: r.update(granularity="summary"), "insufficient_metadata"),
        case("censored outcome", lambda r: r["outcomes"][0].update(measure={"raw": "<.1", "detection_limit": {"value": .1, "operator": "<"}}), "insufficient_metadata"),
        case("outcome unit differs", lambda r: r["outcomes"][0]["measure"].update(unit="cm/s"), "insufficient_metadata"),
        case("outcome unit missing", lambda r: r["outcomes"][0]["measure"].pop("unit"), "insufficient_metadata"),
        case("unpaired outcome condition", lambda r: r["outcomes"][0].update(at={"flow_cm_s": 9}), "insufficient_metadata"),
        case("missing diluent", lambda r: r["conditions"].update(diluent={"value": "helium"}), "insufficient_metadata"),
        case("range is not exact", lambda r: r["conditions"]["o2_pct"].update(min=20, max=22), "insufficient_metadata"),
        case("duplicate outcomes", lambda r: r["outcomes"].append(deepcopy(r["outcomes"][0])), "insufficient_metadata"),
        case("invalid varied axis", lambda r: None, "insufficient_metadata", "gravity"),
    ]


def test_comparison_policy():
    for c in cases():
        got = compare_runs(c["left"], c["right"], c["investigations"], c["quantity"], c["varied_axis"])
        assert got["status"] == c["status"], c["name"]
        assert got["can_compare"] == (c["status"] in ("condition_matched", "controlled_difference"))


def test_nonfinite_measurements_cannot_establish_comparability():
    for invalid in (float("inf"), float("nan"), True):
        c = cases()[0]
        for side in ("left", "right"):
            c[side]["conditions"]["pressure_atm"].update(value=invalid, min=invalid, max=invalid)
        got = compare_runs(c["left"], c["right"], c["investigations"], c["quantity"])
        assert not got["can_compare"]
        assert "pressure_atm" in got["unknown_or_conflicted"]
