from psi_ingest.units import Measure, parse_measure, to_atm, to_mm


def test_plus_minus_is_not_a_test_sweep_or_a_confidence_interval():
    m = parse_measure("1200 +/- 300 W").to_json()
    assert m["value"] == m["min"] == m["max"] == 1200
    assert m["uncertainty"]["plus"] == m["uncertainty"]["minus"] == 300
    assert "confidence_level" not in m["uncertainty"] and "interval_kind" not in m
    converted = parse_measure("1 ± 0.1 min").scaled(60, "s").to_json()
    assert converted["value"] == 60 and converted["uncertainty"]["plus"] == 6
    assert converted["uncertainty"]["unit"] == "s"


def test_reported_bounds_cannot_become_exact_measurements():
    m = parse_measure("<0.005 mg/m3")
    assert not m.usable and m.value is None and m.min is None
    assert m.to_json()["detection_limit"]["value"] == .005
    assert m.to_json()["detection_limit"]["operator"] == "<"


def test_sweeps_source_disagreements_and_ranges_keep_separate_meanings():
    assert parse_measure("1-2 cm/s").to_json()["interval_kind"] == "reported_range"
    assert Measure(raw="initial 21 / final 19", min=19, max=21, flags=["drifted_during_test"]).to_json()["interval_kind"] == "test_variation"
    assert Measure(raw="20 | 25", min=20, max=25, flags=["sources_disagree"]).to_json()["interval_kind"] == "source_conflict"


def test_bounds_convert_without_becoming_points():
    bound = to_mm(parse_measure("<0.1 cm"))
    assert bound.detection_limit["value"] == 1 and bound.unit == "mm"
    assert not bound.usable and bound.raw == "<0.1 cm"
    bound = to_atm(parse_measure("<=101.325 kPa"), "kPa")
    assert bound.detection_limit["value"] == 1 and bound.unit == "atm"
    assert bound.min is None and bound.value is None


def test_nonfinite_numbers_and_mixed_units_are_not_guessed():
    assert not parse_measure("1e999 mm").usable
    assert not parse_measure("1 cm to 2 mm").usable
