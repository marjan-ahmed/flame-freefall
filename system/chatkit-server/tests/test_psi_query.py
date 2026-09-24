import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import psi_query  # noqa: E402
from gen_query_fixtures import FIXTURES, expect, expect_rank  # noqa: E402

FIXTURE_DATA = json.loads(FIXTURES.read_text(encoding="utf-8"))
CASES = FIXTURE_DATA["cases"]
RANK_CASES = FIXTURE_DATA["rank_cases"]


def test_golden_cases():
    for case in CASES:
        got = expect(psi_query.query(case["query"], tolerances=case["tolerances"]))
        assert got == case["expect"], case["name"]


def test_golden_rank_cases():
    for case in RANK_CASES:
        got = expect_rank(psi_query.rank(case["query"], case["quantity"], case["geometry_class"], case["direction"]))
        assert got == case["expect"], case["name"]


def test_rank_never_crosses_geometry_class():
    r = psi_query.rank({}, "burning_rate_k", "droplet-combustion")
    invs = psi_query.load()[1]
    runs_by_id = {x["id"]: x for x in psi_query.load()[0]}
    for row in r["rows"]:
        for run_id in row["runs"]:
            assert invs[runs_by_id[run_id]["investigation"]]["geometry_class"] == "droplet-combustion"


def test_rank_rejects_unrankable_pairs():
    r = psi_query.rank({}, "burning_rate_k", "solid-fuel")
    assert "error" in r
    assert r["rankable"] == psi_query.RANKABLE["solid-fuel"]


def test_headline_is_honest_about_the_flow_gap():
    r = psi_query.query({"o2_pct": 15, "flow_cm_s": 10, "fuel_family": "PMMA"})
    # No PMMA test states BOTH ~15 % O2 and ~10 cm/s — the answer must say so,
    # not manufacture a match.
    assert r["counts"]["match"] == 0
    assert r["partial"], "BASS-II low-O2 rod tests should surface as partial evidence"
    assert all(v["axes"]["flow_cm_s"]["status"] == "not_reported" for v in r["partial"])
    bass_ii = next(c for c in r["coverage"] if c["investigation_id"] == "bass-ii")
    assert bass_ii["axes"]["flow_cm_s"]["reported_by"] < bass_ii["runs"]


def test_every_result_row_is_cited():
    r = psi_query.query({"o2_pct": 21})
    for tier in ("match", "partial", "near"):
        for v in r[tier]:
            assert v["citations"], v["id"]


def test_inverse_flames_never_match_ambient_o2():
    r = psi_query.query({"o2_pct": 21, "geometry_class": "gaseous-flames"})
    ids = [v["id"] for v in r["match"] + r["partial"]]
    runs, _ = psi_query.load()
    inverse = {x["id"] for x in runs if (x["conditions"].get("flame_type") or {}).get("value") == "inverse"}
    assert not inverse & set(ids)


def test_categorical_filter_is_hard_but_reported():
    r = psi_query.query({"o2_pct": 21, "flow_cm_s": 20, "fuel_family": "PMMA"})
    assert all(v["fuel_family"].lower().startswith("pmma") for v in r["match"] + r["partial"] + r["near"])
    assert r["relaxed"], "matching non-PMMA runs should be listed so an empty answer says where data exists"


def test_compact_fits_budget():
    c = psi_query.compact(psi_query.query({"o2_pct": 15, "flow_cm_s": 10, "fuel_family": "PMMA"}))
    assert len(json.dumps(c)) < 6000  # ≈1.5k tokens: Groq free tier is 8k TPM for the whole turn


def test_compact_rank_fits_budget():
    for gc, quantity in (("droplet-combustion", "burning_rate_k"), ("gaseous-flames", "burn_time")):
        c = psi_query.compact_rank(psi_query.rank({}, quantity, gc))
        assert len(json.dumps(c)) < 4000


def test_readiness_covers_every_geometry_class():
    r = psi_query.readiness("lunar")
    assert {c["geometry_class"] for c in r["classes"]} == {
        "solid-fuel", "droplet-combustion", "gaseous-flames", "smoke-aerosol"}


def test_readiness_gaseous_flames_are_covered_near_lunar_atmosphere():
    # ACME BRE targeted 8.2 psia / 34% O2 (near-identical to the Lunar preset)
    r = psi_query.readiness("lunar")
    gas = next(c for c in r["classes"] if c["geometry_class"] == "gaseous-flames")
    assert gas["covered"] and gas["match"] > 0


def test_readiness_findings_are_scoped_to_their_atmosphere():
    lunar_findings = {f["id"] for f in psi_query.readiness("lunar")["findings"]}
    iss_findings = {f["id"] for f in psi_query.readiness("iss")["findings"]}
    assert "lunar-retest-needed" in lunar_findings
    assert "lunar-retest-needed" not in iss_findings
    assert "worst-case-testing" in lunar_findings and "worst-case-testing" in iss_findings  # atmosphere: null


def test_readiness_rejects_unknown_atmosphere():
    r = psi_query.readiness("mars")
    assert "error" in r and "iss" in r["known"]


def test_compact_readiness_fits_budget():
    c = psi_query.compact_readiness(psi_query.readiness("lunar"))
    assert len(json.dumps(c)) < 4000
