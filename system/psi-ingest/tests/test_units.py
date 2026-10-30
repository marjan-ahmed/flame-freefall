from psi_ingest.units import fraction_to_pct, parse_measure, pct, to_atm, to_mm


def test_single_with_unit_in_cell():
    m = parse_measure("20 cm/s")
    assert (m.value, m.unit, m.raw) == (20.0, "cm/s", "20 cm/s")


def test_column_unit_used_when_cell_has_none():
    assert parse_measure("8.1", "cm/s").unit == "cm/s"


def test_approx_range_multi():
    assert parse_measure("~ 21.5").flags == ["approx"]
    r = parse_measure("21.5 - 21.7")
    assert (r.min, r.max, "range" in r.flags) == (21.5, 21.7, True)
    r = parse_measure("22.1 to 22.0")
    assert (r.min, r.max) == (22.0, 22.1)
    m = parse_measure("10, 6, 5, and 3")
    assert m.values == [10, 6, 5, 3] and m.value is None and "multi" in m.flags
    assert parse_measure("0.5; 1.0; 1.5; 2.0; or 3.0").values == [0.5, 1.0, 1.5, 2.0, 3.0]


def test_thousands_separator_is_not_a_list():
    assert parse_measure("3,150").value == 3150


def test_placeholders_and_refusals():
    for blank in ("", "n/a", "none", "-", "#VALUE!", "\ufffd"):
        assert parse_measure(blank) is None
    assert parse_measure("RAMP").flags == ["ramped"]
    # "037 mm" is probably 0.37 mm — probably is a guess, so it is refused
    m = parse_measure("037 mm")
    assert m.value is None and "suspect_value" in m.flags
    assert parse_measure("5 down to ext").flags == ["unparsed"]
    assert pct(parse_measure("3400%", "%")).flags[-1] == "suspect_value"
    assert fraction_to_pct(parse_measure("21")).value is None


def test_conversions_keep_raw():
    m = to_mm(parse_measure(".33 cm"))
    assert (m.value, m.unit, m.raw, "converted" in m.flags) == (3.3, "mm", ".33 cm", True)
    a = to_atm(parse_measure("760"), "mmHg")
    assert abs(a.value - 1.0) < 1e-6 and a.raw == "760"
    assert fraction_to_pct(parse_measure("0.21")).value == 21.0


def test_zero_absolute_pressure_is_refused_not_used():
    # FLEX-114: "0" mmHg in both the PSI table and the report, yet it burned
    m = to_atm(parse_measure("0"), "mmHg")
    assert m.value is None and "suspect_value" in m.flags and m.raw == "0"


def test_psia_is_absolute_pressure_and_keeps_original_units():
    m = to_atm(parse_measure("8.2 psia"), "psia")
    assert abs(m.value * 101.325 - 56.5370098039776) < 0.0001
    assert m.raw == "8.2 psia" and "converted_from_psia" in m.flags
    # Gauge pressure has no known ambient reference and must not be converted.
    assert "unknown_unit" in to_atm(parse_measure("8.2 psig"), "psig").flags
