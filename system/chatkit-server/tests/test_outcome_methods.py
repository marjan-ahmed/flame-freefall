from copy import deepcopy
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from psi_comparison import compare_runs
from test_comparison import cases
import json


def sourced_pair():
    case = cases()[0]
    for record in (case["left"], case["right"]):
        record["sources"] = [{"kind": "report", "quote": "Camera and front tracking were used."}]
        record["conditions"].pop("instrument")
        record["conditions"].pop("measurement_method")
        record["outcomes"][0]["metadata"] = {
            field: {"value": value, "source": 0, "quote": "Camera and front tracking were used."}
            for field, value in (("instrument", "camera"), ("measurement_method", "front tracking"))
        }
    return case


def assess(case):
    return compare_runs(case["left"], case["right"], case["investigations"], case["quantity"])


def test_selected_outcome_method_can_establish_only_its_own_method_checks():
    case = sourced_pair()
    assert assess(case)["can_compare"]
    case["left"]["outcomes"].append({"quantity": "burn_time", "source": 0, "measure": {"value": 1, "min": 1, "max": 1, "unit": "s"}})
    case["right"]["outcomes"].append(deepcopy(case["left"]["outcomes"][-1]))
    other = compare_runs(case["left"], case["right"], case["investigations"], "burn_time")
    assert "instrument" in other["unknown_or_conflicted"]
    assert "measurement_method" in other["unknown_or_conflicted"]


def test_invalid_method_pointer_cannot_fall_back_to_a_campaign_category():
    for bad in (True, -1, 99):
        case = sourced_pair()
        case["left"]["conditions"]["instrument"] = {"value": "camera"}
        case["left"]["outcomes"][0]["metadata"]["instrument"]["source"] = bad
        assert "instrument" in assess(case)["unknown_or_conflicted"]
    case = sourced_pair()
    case["left"]["outcomes"][0]["metadata"]["measurement_method"]["quote"] = "unsupported"
    assert "measurement_method" in assess(case)["unknown_or_conflicted"]


def test_real_flex_rate_method_is_known_without_upgrading_extinction_or_equivalence():
    root = Path(__file__).resolve().parents[3]
    runs = json.loads((root / "psi-data/derived/runs.json").read_text(encoding="utf-8"))["runs"]
    invs = {i["id"]: i for i in json.loads((root / "psi-data/derived/investigations.json").read_text(encoding="utf-8"))["investigations"]}
    records = {r["id"]: r for r in runs}
    left, right = records["PSI-69:FLEX-001"], records["PSI-69:FLEX-002"]
    rates = compare_runs(left, right, invs, "burning_rate_k")
    for field in ("instrument", "measurement_method"):
        check = next(c for c in rates["checks"] if c["field"] == field)
        assert check["status"] == "match"
        for record, c in ((left, check["left"]), (right, check["right"])):
            assert c["quote"] in record["sources"][c["source"]]["quote"]
    assert not rates["can_compare"], "method availability does not fill other missing conditions"
    extinction = compare_runs(left, right, invs, "extinction_diameter")
    assert "measurement_method" in extinction["unknown_or_conflicted"]
