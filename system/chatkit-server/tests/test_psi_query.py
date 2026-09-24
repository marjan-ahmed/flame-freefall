import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import psi_query  # noqa: E402
from gen_query_fixtures import FIXTURES, expect  # noqa: E402

CASES = json.loads(FIXTURES.read_text(encoding="utf-8"))["cases"]


def test_golden_cases():
    for case in CASES:
        got = expect(psi_query.query(case["query"], tolerances=case["tolerances"]))
        assert got == case["expect"], case["name"]


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
