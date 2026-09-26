"""Numerical-accuracy QA (2026-09-27): expectations here were computed
INDEPENDENTLY from data/runs.json (exact Decimal arithmetic on the JSON
literals, no psi_query code), not copied from psi_query output — unlike
psi-data/query-fixtures.json, which psi_query generates itself.

Tests marked xfail(strict=True) encode the CORRECT behaviour for a confirmed
defect that is not fixed yet; they flip to XPASS (and so fail) once the code is
fixed, which is the cue to drop the marker.
"""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import psi_atmospheres  # noqa: E402
import psi_query  # noqa: E402


def _ids(result, tier):
    return {v["id"] for v in result[tier]}


# ── verified correct: hand-derived ground truth ─────────────────────────────

def test_preset_pressures_are_the_kpa_division():
    # 101.4/101.325 = 1.00074..., 73.5/101.325 = 0.72539..., 56.5/101.325 = 0.55761...
    got = {k: a["pressure_atm"] for k, a in psi_atmospheres.ATMOSPHERES.items()}
    assert got == {"iss": 1.0007, "gateway": 0.7254, "lunar": 0.5576}


READINESS_TRUTH = {  # (match, partial, near_pool) per class, derived from runs.json by hand-script
    "iss": {"droplet-combustion": (83, 1, 279), "gaseous-flames": (113, 115, 972),
            "smoke-aerosol": (0, 0, 117), "solid-fuel": (1, 60, 207)},
    "gateway": {"droplet-combustion": (6, 0, 357), "gaseous-flames": (0, 15, 1185),
                "smoke-aerosol": (0, 0, 117), "solid-fuel": (1, 0, 267)},
    "lunar": {"droplet-combustion": (0, 0, 363), "gaseous-flames": (10, 75, 1115),
              "smoke-aerosol": (0, 0, 117), "solid-fuel": (0, 0, 268)},
}


@pytest.mark.parametrize("atm", sorted(READINESS_TRUTH))
def test_readiness_counts_match_independent_count(atm):
    r = psi_query.readiness(atm)
    got = {c["geometry_class"]: (c["match"], c["partial"], c["near_pool"]) for c in r["classes"]}
    assert got == READINESS_TRUTH[atm]


def test_rank_even_n_median_and_one_contribution_per_run():
    # o2 21 +/-1.5, flow 20 +/-30 %: PMMA = 6 BASS-II runs, each contributing only its
    # spread rate nearest 20 cm/s; sorted values' two middle ones average to 0.0465.
    r = psi_query.rank({"o2_pct": 21, "flow_cm_s": 20}, "spread_rate", "solid-fuel")
    rows = {x["fuel_family"]: x for x in r["rows"]}
    assert (rows["PMMA"]["n"], rows["PMMA"]["median"]) == (6, 0.0465)
    assert len(set(rows["PMMA"]["runs"])) == len(rows["PMMA"]["runs"])
    s = rows["SIBAL (cotton-fiberglass)"]
    # SIBAL spread rates now from 4 runs: SAFFIRE-1 S1 (1.8), S2 (1.3), SAFFIRE-2 2-5 (2.1), 2-6 (2.6)
    assert (s["n"], s["min"], s["median"], s["max"]) == (4, 1.3, 1.95, 2.6)


def test_rank_never_mixes_geometry_classes():
    r = psi_query.rank({"o2_pct": 20.9}, "spread_rate", "solid-fuel")
    runs, invs = psi_query.load()
    by_id = {x["id"]: x for x in runs}
    for row in r["rows"]:
        assert all(invs[by_id[i]["investigation"]]["geometry_class"] == "solid-fuel" for i in row["runs"])


# ── C5 fixed: tolerance boundary is inclusive on both sides (TOLERANCE_EPS) ──

def test_tolerance_boundary_is_inclusive_both_sides():
    # PSI-23:19254 (ACME s-Flame) is at exactly 1.0 atm; tolerance is +/-0.1 atm.
    # 0.9 atm includes it (d = 0.9999999999999998); 1.1 atm must too.
    assert "PSI-23:19254" in _ids(psi_query.query({"pressure_atm": 0.9}), "match")
    hi = psi_query.query({"pressure_atm": 1.1})
    assert "PSI-23:19254" in _ids(hi, "match")
    assert hi["counts"]["match"] == 499  # exact-decimal count; code gives 430
    # BASS-II PSI-25:P4 O2 interval 17.1-18.5; target 15.6 is exactly 1.5 below
    assert "PSI-25:P4" in _ids(psi_query.query({"o2_pct": 15.6}), "match")


# ── C5 fixed: readiness "nearest tested" shows the value that matched ───────

def test_readiness_nearest_tested_value_is_within_tolerance_for_match_or_partial():
    # Gateway (26.5 % O2) gaseous flames: nearest = ACME BRE PSI-20:2019-02-08, O2 multi "21; 26.5; 40".
    # It is 'partial' because 26.5 matched, but the widget / compact reply says "21% O2".
    for atm_id, atm in psi_atmospheres.ATMOSPHERES.items():
        for c in psi_query.readiness(atm_id)["classes"]:
            n = c["nearest_tested"]
            if n and n["tier"] in ("match", "partial") and n["o2_pct"] is not None:
                assert abs(n["o2_pct"] - atm["o2_pct"]) <= 1.5, (atm_id, c["geometry_class"], n)


# ── C5 fixed: rank()'s "untested" no longer lists materials that WERE tested ─

def test_rank_untested_does_not_list_families_removed_by_the_fuel_filter():
    # SIBAL has spread-rate data at 20.9 % O2 (n=2, PSI-99:2-5/2-6); filtering to PMMA
    # must not relabel it "Not tested at these conditions".
    r = psi_query.rank({"o2_pct": 20.9, "fuel_family": "PMMA"}, "spread_rate", "solid-fuel")
    assert "SIBAL (cotton-fiberglass)" not in r["untested"]


def test_rank_untested_excludes_families_with_runs_at_these_conditions():
    # At 20.9 % O2, Nomex (3), silicone (4) and PMMA/Nomex composite (1) have match/partial
    # solid-fuel runs; they lack a spread-rate value, they were not "untested".
    q = {"o2_pct": 20.9}
    res = psi_query.query({**q, "geometry_class": "solid-fuel"})
    tested = {v["fuel_family"] for t in ("match", "partial") for v in res[t]}
    r = psi_query.rank(q, "spread_rate", "solid-fuel")
    assert not (tested & set(r["untested"])), tested & set(r["untested"])


# ── WARNING (modeling): non-ignition tests ranked as burn time 0 s ───────────

@pytest.mark.xfail(strict=True, reason="CFI-G 'No ignition' rows carry burn_time=0 as a measured value; owner decision")
def test_rank_burn_time_excludes_tests_that_never_ignited():
    # Lunar preset: propane n=8, median 6.0 s — 4 of the 8 are hot_ignition='no', burn time '0'.
    # Among ignited tests only, the median is 43.5 s.
    r = psi_query.rank(psi_atmospheres.query_for("lunar"), "burn_time", "gaseous-flames")
    rows = {x["fuel_family"]: x for x in r["rows"]}
    assert rows["propane"]["min"] > 0
