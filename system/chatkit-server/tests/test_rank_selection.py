"""Scientific selection failures must abstain rather than pick source order."""
from copy import deepcopy

import psi_query


def sample():
    runs, invs = psi_query.load()
    row = psi_query.rank({}, "burning_rate_k", "droplet-combustion")["rows"][0]
    run = deepcopy(next(r for r in runs if r["id"] == row["runs"][0]))
    run["outcomes"] = [next(o for o in run["outcomes"] if o["quantity"] == "burning_rate_k")]
    return run, invs


def ranked(run, invs, q=None):
    return psi_query.rank(q or {}, "burning_rate_k", "droplet-combustion", runs=[run], invs=invs)


def test_censored_scalar_is_not_a_rankable_point():
    run, invs = sample()
    run["outcomes"][0]["measure"]["detection_limit"] = {"operator": "<", "value": 1, "raw": "<1"}
    assert ranked(run, invs)["rows"] == []


def test_missing_units_are_not_rankable():
    run, invs = sample()
    run["outcomes"][0]["measure"].pop("unit")
    assert ranked(run, invs)["excluded"]["missing_outcome_unit"] == 1


def test_geometry_filter_cannot_be_silently_overwritten():
    run, invs = sample()
    assert "error" in ranked(run, invs, {"geometry_class": "solid-fuel"})


def test_outcome_pressure_overrides_run_pressure_for_selection():
    run, invs = sample()
    run["conditions"]["pressure_atm"] = {"value": 1, "min": 1, "max": 1, "raw": "1", "unit": "atm"}
    run["outcomes"][0]["at"] = {"pressure_atm": .5}
    result = ranked(run, invs, {"pressure_atm": 1})
    assert result["rows"] == []
    assert result["excluded"]["outcome_outside_query_window"] == 1


def test_duplicate_outcomes_are_ambiguous_even_with_requested_flow():
    run, invs = sample()
    run["conditions"]["flow_cm_s"] = {"value": 5, "min": 5, "max": 5, "raw": "5", "unit": "cm/s"}
    run["outcomes"][0]["at"] = {"flow_cm_s": 5}
    other = deepcopy(run["outcomes"][0])
    other["measure"].update(value=2, min=2, max=2)
    run["outcomes"].append(other)
    for outcomes in (run["outcomes"], list(reversed(run["outcomes"]))):
        run["outcomes"] = outcomes
        assert ranked(run, invs, {"flow_cm_s": 5})["excluded"]["ambiguous_outcome"] == 1


def test_unspecified_outcome_pressure_cannot_choose_a_sweep_member():
    run, invs = sample()
    run["outcomes"][0]["at"] = {"pressure_atm": .5}
    other = deepcopy(run["outcomes"][0])
    other["at"] = {"pressure_atm": 1}
    run["outcomes"].append(other)
    assert ranked(run, invs)["excluded"]["multiple_outcome_conditions"] == 1


def test_condition_uncertainty_is_retained_in_strata():
    run, invs = sample()
    other = deepcopy(run)
    other["id"] += "-uncertain"
    other["conditions"]["pressure_atm"]["uncertainty"] = {"kind": "reported", "plus": .05, "raw": "±0.05"}
    result = psi_query.rank({}, "burning_rate_k", "droplet-combustion", runs=[run, other], invs=invs)
    assert result["total_ranked"] == 2
    assert all(row["n"] == 1 for row in result["rows"])


def test_real_temperature_records_are_not_pooled_despite_identical_recorded_setup():
    # These CFI-G flight runs previously formed a median 26.1 C cohort even
    # though required apparatus/instrument/method metadata was absent.
    runs, invs = psi_query.load()
    ids = {"PSI-159:21265 F3", "PSI-159:21265 F4"}
    selected = [r for r in runs if r["id"] in ids]
    assert len(selected) == 2
    assert all("instrument" not in r["conditions"] for r in selected)
    result = psi_query.rank({}, "peak_burner_temp_c", "gaseous-flames", runs=selected, invs=invs)
    assert result["mode"] == "individual_observations"
    assert len(result["rows"]) == 2
    assert {tuple(row["runs"]) for row in result["rows"]} == {(i,) for i in ids}
    for row in result["rows"]:
        assert row["n"] == 1 and row["row_kind"] == "individual_observation"
        assert row["comparison_status"] == "not_audited"
        original = next(r for r in selected if r["id"] == row["runs"][0])
        outcome = next(o for o in original["outcomes"] if o["quantity"] == "peak_burner_temp_c")
        assert row["value"] == outcome["measure"]["value"]
        assert row["raw"] == outcome["measure"]["raw"]
        assert row["source_index"] == outcome["source"]


def test_equal_missing_setup_does_not_create_a_material_distribution():
    run, invs = sample()
    other = deepcopy(run)
    other["id"] += "-separate-test"
    for record in (run, other):
        record["conditions"] = {"fuel_family": {"value": "n-heptane"}}
    other["outcomes"][0]["measure"].update(value=2, min=2, max=2)
    result = psi_query.rank({}, "burning_rate_k", "droplet-combustion", runs=[run, other], invs=invs)
    assert len(result["rows"]) == 2
    assert all(row["n"] == 1 for row in result["rows"])
    assert "no pooled material estimates" in result["method"]


def test_observation_unit_unknown_is_excluded_and_incompatible_units_are_grouped():
    run, invs = sample()
    missing = deepcopy(run)
    missing["id"] += "-missing-unit"
    missing["outcomes"][0]["measure"].pop("unit", None)
    other = deepcopy(run)
    other["id"] += "-other-unit"
    other["outcomes"][0]["measure"].update(value=99, min=99, max=99, unit="cm2/s")
    result = psi_query.rank({}, "burning_rate_k", "droplet-combustion", runs=[run, missing, other], invs=invs)
    assert result["excluded"]["missing_outcome_unit"] == 1
    assert len(result["rows"]) == 2
    assert [r["unit"] for r in result["rows"]] == sorted(r["unit"] for r in result["rows"])


def test_compact_observations_do_not_ask_model_to_describe_material_medians():
    compact = psi_query.compact_rank(psi_query.rank({}, "burning_rate_k", "droplet-combustion"))
    assert compact["mode"] == "individual_observations"
    assert all("observation" in row and "run" in row and "source_index" in row for row in compact["top"])
    assert all("median" not in row and "range" not in row for row in compact["top"])
