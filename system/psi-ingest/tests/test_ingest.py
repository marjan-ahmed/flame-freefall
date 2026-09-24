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
