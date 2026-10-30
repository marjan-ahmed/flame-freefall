import pytest

from psi_ingest.cli import run


@pytest.fixture(scope="module")
def result():
    return run(write=False)


def _measures(run_):
    for k, v in run_["conditions"].items():
        if isinstance(v, dict) and "raw" in v and ("min" in v or "flags" in v or "value" in v and isinstance(v.get("value"), (int, float))):
            yield k, v
    for o in run_["outcomes"]:
        if "measure" in o:
            yield o["quantity"], o["measure"]


def test_every_row_is_accounted_for(result):
    for f in result["report"]["files"]:
        assert f["rows_read"] == f["runs_emitted"] + len(f["skipped"]) + f["merged_into_previous"], f["file"]


def test_every_value_keeps_its_raw_cell(result):
    for r in result["runs"]:
        for name, m in _measures(r):
            assert m["raw"].strip(), (r["id"], name)


def test_every_run_is_cited(result):
    for r in result["runs"]:
        assert r["sources"], r["id"]
        assert len(r["raw"]) == len(r["sources"]), r["id"]
        for s in r["sources"]:
            if s["kind"] == "report":
                # governed-record citations carry the NTRS link; reports with no
                # governed document are cited by their own title
                assert (s.get("url") or "").startswith("https://ntrs.nasa.gov/") or s.get("title"), r["id"]


def test_ids_are_unique(result):
    ids = [r["id"] for r in result["runs"]]
    assert len(ids) == len(set(ids))


def _by_id(result, rid):
    return next(r for r in result["runs"] if r["id"] == rid)


def test_disagreements_are_recorded_not_resolved(result):
    s1 = _by_id(result, "PSI-98:S1")
    fields = {c["field"] for c in s1["conflicts"]}
    # PSI lists 0.37 in a "(cm)" column; the report says 0.37 mm
    assert "thickness_mm" in fields
    t = s1["conditions"]["thickness_mm"]
    assert "sources_disagree" in t["flags"] and (t["min"], t["max"]) == (0.37, 3.7)
    assert {c["field"] for c in _by_id(result, "PSI-99:2-6")["conflicts"]} == {"flow_cm_s"}


def test_report_values_join_psi_runs(result):
    m7 = _by_id(result, "PSI-25:M7")
    spreads = [o for o in m7["outcomes"] if o["quantity"] == "spread_rate"]
    assert [(o["at"]["flow_cm_s"], o["measure"]["value"]) for o in spreads] == [
        (10, 0.106), (6, 0.099), (5, 0.083), (3, 0.07)]
    assert {s["kind"] for s in m7["sources"]} == {"psi", "report"}


def test_flex_joined_on_identifier_not_number(result):
    stats = {t["table"]: t for t in result["report"]["report_tables"]}
    flex = next(v for k, v in stats.items() if "flex" in k)
    assert flex["joined_to_psi_runs"] >= 270
    assert not [c for r in result["runs"] if r["investigation"] == "flex" for c in r.get("conflicts", [])]


def test_inverse_flames_have_no_ambient_o2(result):
    for r in result["runs"]:
        if (r["conditions"].get("flame_type") or {}).get("value") == "inverse":
            assert "o2_pct" not in r["conditions"], r["id"]


def test_implausible_o2_readings_do_not_widen_the_interval(result):
    b2 = _by_id(result, "PSI-25:B2")["conditions"]["o2_pct"]
    assert "final_reading_suspect" in b2["flags"] and b2["min"] == 22.2


def test_extracted_report_values_are_verified_and_merged(result):
    stats = {t["table"]: t for t in result["report"]["report_tables"]}
    ex = stats["psi-data/extracted/report-outcomes.csv"]
    assert ex["rows"] > 250 and ex["joined_to_psi_runs"] >= 126
    o11 = _by_id(result, "PSI-25:O11")
    assert o11["conditions"]["flow_direction"]["value"] == "stagnation"
    assert any(o["quantity"] == "observation" for o in o11["outcomes"])
    same62 = _by_id(result, "PSI-101:SAME #62")
    assert same62["conditions"]["sample_temperature_c"]["value"] == 574.3
    assert not same62.get("conflicts")


def test_tampered_extraction_is_refused(tmp_path):
    from pathlib import Path

    from psi_ingest.verify import ExtractionNotVerified, load_verified

    root = Path(__file__).resolve().parents[3]
    src = root / "psi-data" / "extracted" / "report-outcomes.csv"
    lines = src.read_text(encoding="utf-8").splitlines()
    bad = tmp_path / "bad.csv"
    # claim a different direction than the verbatim cell says
    tampered = lines[1].replace(",opposed,", ",concurrent,")
    assert tampered != lines[1]
    bad.write_text(lines[0] + "\n" + tampered + "\n", encoding="utf-8")
    with pytest.raises(ExtractionNotVerified):
        load_verified(root, bad)


def test_shared_flex_identifier_is_not_double_counted(result):
    # 193F001 labels both FLEX-070 and FLEX-073 in the PSI table
    ids = [r["id"] for r in result["runs"] if r["investigation"] == "flex"]
    assert "flex:FLEX-070 (report)" not in ids and "flex:FLEX-073 (report)" not in ids
    f70 = _by_id(result, "PSI-69:FLEX-070")
    assert any(s["kind"] == "report" for s in f70["sources"])
    # genuinely report-only tests stay, once
    assert ids.count("flex:FLEX-216 (report)") == 1 and ids.count("flex:FLEX-230 (report)") == 1


def test_flex_pressure_range_excludes_the_zero_reading(result):
    f114 = _by_id(result, "PSI-69:FLEX-114")["conditions"]["pressure_atm"]
    assert f114.get("value") is None and "zero_absolute_pressure" in f114["flags"]
    flex = next(i for i in result["investigations"] if i["id"] == "flex")
    assert flex["coverage"]["pressure_atm"]["min"] > 0.5


def test_bre_examples_are_individual_emulator_tests_not_day_pressures(result):
    bre = [r for r in result["runs"] if r["investigation"] == "acme-bre"]
    days = [r for r in bre if r["granularity"] == "day"]
    tests = [r for r in bre if r["granularity"] == "test"]
    assert len(days) == 18 and len(tests) == 3
    assert all("pressure_atm" not in r["conditions"] for r in days)
    assert {r["label"] for r in tests} == {"19056F1", "19070K1", "19070D1"}
    for r in tests:
        assert r["conditions"]["evidence_role"]["value"] == "condensed-fuel-emulator"
        assert r["conditions"]["result_status"]["value"] == "preliminary"
        assert r["conditions"]["fuel_family"]["value"] == "ethylene"
        assert r["sources"][0]["kind"] == "report" and "Figure" in r["sources"][0]["table"]
        assert r["label"] in r["raw"][0]["original_caption"]
    lunar = _by_id(result, "acme-bre:19070D1")
    assert lunar["conditions"]["o2_pct"]["value"] == 34
    assert lunar["conditions"]["pressure_atm"]["raw"] == "8.2 psia"
    assert abs(lunar["conditions"]["pressure_atm"]["value"] * 101.325 - 56.537) < 0.001
    assert any("24 kJ/g" in n and "22 kJ/g" in n for n in lunar["notes"])
    assert not any(o["quantity"] == "burn_time" for o in lunar["outcomes"])


def test_lunar_overlap_sensitivity_by_direct_arithmetic(result):
    """Independent oracle: no query engine or its distance helper is imported.

    Counts are individual tests/points only; interval overlap is a search
    criterion, not a conclusion about physical equivalence or material safety.
    """
    geometry = {i["id"]: i["geometry_class"] for i in result["investigations"]}
    profiles = [(1.5, 10.1325), (1.5, 5), (3, 10.1325)]
    counts = []
    for oxygen_tolerance, pressure_tolerance_kpa in profiles:
        found = {"solid-fuel": 0, "gaseous-flames": 0, "emulator": 0}
        for r in result["runs"]:
            if r["granularity"] not in ("test", "test-point"):
                continue
            c = r["conditions"]
            o2, p = c.get("o2_pct", {}), c.get("pressure_atm", {})
            if not all("min" in v and "max" in v for v in (o2, p)):
                continue
            if not (o2["min"] <= 34 + oxygen_tolerance and o2["max"] >= 34 - oxygen_tolerance):
                continue
            if not (p["min"] * 101.325 <= 56.5 + pressure_tolerance_kpa and
                    p["max"] * 101.325 >= 56.5 - pressure_tolerance_kpa):
                continue
            group = "emulator" if r["investigation"] == "acme-bre" else geometry[r["investigation"]]
            if group in found:
                found[group] += 1
        counts.append(found)
    assert counts == [
        {"solid-fuel": 0, "gaseous-flames": 10, "emulator": 1},
        {"solid-fuel": 0, "gaseous-flames": 0, "emulator": 1},
        {"solid-fuel": 1, "gaseous-flames": 14, "emulator": 1},
    ]
