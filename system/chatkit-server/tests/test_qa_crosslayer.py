"""Cross-layer parity checks beyond psi-data/query-fixtures.json (QA, 2026-09-27).

Runs the SAME inputs through the Python side (psi_query / psi_atmospheres /
psi_widgets) and the TypeScript side (system/site/lib/psi-query.ts,
psi-atmospheres.ts, dashboard-data.ts) via a Node subprocess, and diffs them.
The fixture file pins 11 hand-picked query cases; these add tolerance-edge,
key-order, tolerance-override, categorical-spelling and empty-result cases, plus
the three seams that have NO fixture at all:

  * psi_atmospheres.py  vs  lib/psi-atmospheres.ts        (twinned "by hand")
  * psi_query.readiness()  vs  dashboard missionReadinessSummary()
  * psi_widgets gap map (O2 x pressure)  vs  dashboard geometryHeatmaps()

Two known divergences xfail while they exist; once fixed, the same tests turn
into plain parity assertions with no edit needed.

Needs node (>=24) and jiti (root node_modules, from `npm install`); skipped
otherwise. Uses the committed data in psi-data/derived/ on the TS side and
system/chatkit-server/data/ on the Python side, which must be byte-identical.
"""

from __future__ import annotations

import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

HERE = Path(__file__).resolve().parents[1]
REPO = HERE.parents[1]
sys.path.insert(0, str(HERE))
import psi_atmospheres  # noqa: E402
import psi_query  # noqa: E402
import psi_widgets  # noqa: E402

pytestmark = pytest.mark.skipif(
    shutil.which("node") is None or not (REPO / "node_modules" / "jiti").is_dir(),
    reason="node + jiti (repo-root npm install) needed for the TypeScript side",
)

# ── inputs ───────────────────────────────────────────────────────────────────
# Each exercises something the golden fixtures don't: exact tolerance edges
# (abs and rel), a query whose keys arrive in a non-canonical order (the model's
# tool args do), tolerance overrides, prefix/case/name/en-dash categorical
# spellings, zero targets on rel axes, and empty results.
QUERY_CASES: list[tuple[dict, dict | None]] = [
    ({"o2_pct": 22.5}, None),                                   # 21 + 1.5: abs edge
    ({"o2_pct": 19.5, "pressure_atm": 1.1}, None),              # 1.0 + 0.1 lands just outside in float
    ({"pressure_atm": 1.0, "o2_pct": 21.0}, None),              # reversed key order
    ({"flow_cm_s": 10 / 1.3}, None),                            # rel edge below 10 cm/s
    ({"flow_cm_s": 10 / 0.7, "fuel_family": "PMMA"}, None),     # rel edge above
    ({"flow_cm_s": 0}, None),                                   # rel axis, zero target
    ({"flow_cm_s": -6}, None),                                  # negative readings exist in the data
    ({"droplet_d0_mm": 3.2}, None),
    ({"droplet_d0_mm": 5.0, "o2_pct": 15, "geometry_class": "droplet-combustion"}, None),
    ({"thickness_mm": 2.0, "pressure_atm": 0.5, "geometry_class": "solid-fuel"}, {"thickness_mm": 2, "flow_cm_s": 0.05}),
    ({"o2_pct": 16.0, "droplet_d0_mm": 2.04, "geometry_class": "droplet-combustion", "flow_cm_s": 1.54},
     {"pressure_atm": 0.05, "droplet_d0_mm": 2}),
    ({"fuel_family": "wax"}, None),                             # prefix → every wax
    ({"fuel_family": "n-dodecane", "o2_pct": 21}, None),        # prefix also hits n-dodecane/iso-dodecane
    ({"fuel_family": "sibal", "o2_pct": 21, "flow_cm_s": 20}, None),
    ({"investigation": "SAFFIRE IV–VI", "o2_pct": 21}, None),   # by name, with the en dash
    ({"investigation": "saffire-iv-vi"}, None),
    ({"flow_direction": "OPPOSED", "flow_cm_s": 5}, None),
    ({"fuel_form": "candle"}, None),
    ({"geometry_class": "smoke-aerosol", "o2_pct": 21}, None),  # class with no O2 at all
    ({"fuel_family": "unobtanium", "o2_pct": 21}, None),        # empty → relaxed
    ({"o2_pct": 99}, None),
    ({}, None),
    ({"o2_pct": 34.0, "pressure_atm": 0.5576}, None),           # lunar preset
    ({"o2_pct": 26.5, "pressure_atm": 0.7254, "geometry_class": "gaseous-flames"}, None),
]
RANK_CASES: list[tuple[dict, str, str, str]] = [
    ({}, "spread_rate", "solid-fuel", "desc"),
    ({"flow_cm_s": 10}, "spread_rate", "solid-fuel", "asc"),
    ({"o2_pct": 21, "flow_cm_s": 20}, "spread_rate", "solid-fuel", "desc"),
    ({"o2_pct": 21}, "burning_rate_k", "droplet-combustion", "desc"),
    ({"o2_pct": 15, "pressure_atm": 1.0}, "extinction_diameter", "droplet-combustion", "asc"),
    ({"o2_pct": 34.0, "pressure_atm": 0.5576}, "burn_time", "gaseous-flames", "desc"),
    ({"o2_pct": 20.9, "pressure_atm": 1.0007}, "peak_burner_temp_c", "gaseous-flames", "asc"),
    ({"fuel_family": "ethylene"}, "burn_time", "gaseous-flames", "desc"),
    ({}, "spread_rate", "smoke-aerosol", "desc"),              # error path
]

# ── the TypeScript side ─────────────────────────────────────────────────────
_TS = r"""
import { readFileSync } from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";
const repo = process.cwd(), site = path.join(repo, "system/site");
const { createJiti } = createRequire(path.join(repo, "package.json"))("jiti");
const jiti = createJiti(path.join(site, "x.ts"), { alias: { "@": site } });
const pq = await jiti.import(path.join(site, "lib/psi-query.ts"));
const dash = await jiti.import(path.join(site, "lib/dashboard-data.ts"));
const atm = await jiti.import(path.join(site, "lib/psi-atmospheres.ts"));
const read = (p) => JSON.parse(readFileSync(path.join(repo, p), "utf8"));
const runs = read("psi-data/derived/runs.json").runs;
const invs = read("psi-data/derived/investigations.json").investigations;
const input = JSON.parse(readFileSync(0, "utf8"));
const q = input.queries.map(([query, tol]) => {
  const r = pq.query(runs, invs, query, tol ?? {});
  const tier = (vs) => vs.map((v) => ({ id: v.run.id, distance: v.distance,
    axes: Object.fromEntries(Object.entries(v.axes).map(([k, a]) => [k, a.status])) }));
  return { counts: r.counts, match: tier(r.match), partial: tier(r.partial), near: tier(r.near),
           coverage: r.coverage, relaxed: r.relaxed, geometry_classes: r.geometry_classes };
});
const rk = input.ranks.map(([query, quantity, gc, dir]) => {
  const r = pq.rank(runs, invs, query, quantity, gc, dir);
  return "error" in r ? { error: true, rankable: r.rankable }
    : { rows: r.rows, total_ranked: r.total_ranked, untested: r.untested };
});
const nan = pq.query(runs, invs, { o2_pct: NaN }).counts;
process.stdout.write(JSON.stringify({
  query: q, rank: rk, nan,
  atmospheres: atm.ATMOSPHERES,
  readiness: dash.missionReadinessSummary().map((s) => ({ id: s.atmosphere.id,
    classes: s.classes.map((c) => [c.geometryClass, c.match, c.partial, c.covered]) })),
  heatmaps: dash.geometryHeatmaps().map((h) => [h.geometryClass, h.grid, h.totalRuns, h.reportedRuns]),
  markers: dash.atmosphereMarkers().map((m) => [m.id, m.xBin, m.yBin]),
  bins: { o2: dash.O2_BINS, pressure: dash.PRESSURE_BINS },
}));
"""


@pytest.fixture(scope="module")
def ts() -> dict:
    payload = json.dumps({"queries": QUERY_CASES, "ranks": RANK_CASES})
    p = subprocess.run(["node", "--input-type=module", "-e", _TS], cwd=REPO, input=payload,
                       capture_output=True, text=True, encoding="utf-8", timeout=300)
    assert p.returncode == 0, p.stderr[-3000:]
    return json.loads(p.stdout)


def _py_query(q: dict, tol: dict | None) -> dict:
    r = psi_query.query(q, tol)
    tier = lambda vs: [{"id": v["id"], "distance": v["distance"],  # noqa: E731
                        "axes": {k: a["status"] for k, a in v["axes"].items()}} for v in vs]
    return {"counts": r["counts"], "match": tier(r["match"]), "partial": tier(r["partial"]), "near": tier(r["near"]),
            "coverage": r["coverage"], "relaxed": r["relaxed"], "geometry_classes": r["geometry_classes"]}


def _strip_distance(r: dict) -> dict:
    return {**r, **{t: [{k: v for k, v in x.items() if k != "distance"} for x in r[t]] for t in ("match", "partial", "near")}}


def test_backend_and_site_read_identical_data():
    for name in ("runs.json", "investigations.json"):
        assert (REPO / "psi-data/derived" / name).read_bytes() == (HERE / "data" / name).read_bytes(), name


@pytest.mark.parametrize("i", range(len(QUERY_CASES)))
def test_query_parity_beyond_fixtures(ts, i):
    """Same counts, same run ids in the same order per tier, same per-axis
    status, same coverage, relaxed and geometry classes. (distance: see xfail.)"""
    q, tol = QUERY_CASES[i]
    assert _strip_distance(_py_query(q, tol)) == _strip_distance(ts["query"][i]), q


def test_query_distance_rounding_parity(ts):
    """KNOWN DIVERGENCE: psi_query.py rounds `distance` with round(d, 3) (exact
    decimal of the double: 0.2875 → 0.287) while psi-query.ts uses
    Math.round(d * 1000) / 1000 (0.2875 * 1000 == 287.5 → 0.288). Seen for
    droplet_d0_mm=3.2, run PSI-69:FLEX-043 (d0 2.97 mm): Python 0.287, TS 0.288.
    Tiers and order are unaffected (they use the unrounded score); the Explorer
    shows the value on near-tier cards. 12 of 5,436 generated cases differ."""
    py = _py_query({"droplet_d0_mm": 3.2}, None)
    t = ts["query"][QUERY_CASES.index(({"droplet_d0_mm": 3.2}, None))]
    if any(a["distance"] != b["distance"] for a, b in zip(py["match"], t["match"])):
        pytest.xfail("Python round(d,3) vs TS Math.round(d*1000)/1000 — see docstring")
    assert py["match"] == t["match"]


def test_query_nan_target_parity(ts):
    """KNOWN DIVERGENCE: a NaN numeric target is kept by Python (float('nan')
    passes `v is not None`, every distance becomes NaN → every run lands in
    `near`) but dropped by TS (`!Number.isNaN`), which then treats the query as
    unconstrained → every run is a `match`. Unreachable from the Explorer (its
    queryFromParams drops NaN first); reachable in principle from a chat tool
    call whose float arg parses as NaN."""
    py = psi_query.query({"o2_pct": float("nan")})["counts"]
    if py != ts["nan"]:
        pytest.xfail(f"Python {py} vs TS {ts['nan']}")
    assert py == ts["nan"]


@pytest.mark.parametrize("i", range(len(RANK_CASES)))
def test_rank_parity_beyond_fixtures(ts, i):
    q, quantity, gc, direction = RANK_CASES[i]
    r = psi_query.rank(q, quantity, gc, direction)
    py = {"error": True, "rankable": r["rankable"]} if "error" in r else \
        {"rows": r["rows"], "total_ranked": r["total_ranked"], "untested": r["untested"]}
    assert py == ts["rank"][i], RANK_CASES[i]


def test_atmosphere_presets_twin(ts):
    keys = ("id", "label", "o2_pct", "pressure_atm", "pressure_source_value", "doc", "doc_title", "quote")
    py = {k: {f: v[f] for f in keys} for k, v in psi_atmospheres.ATMOSPHERES.items()}
    assert py == ts["atmospheres"]


def test_readiness_matches_dashboard_cards(ts):
    """psi_query.readiness() has no TS twin; the dashboard re-derives coverage
    from the twinned query(). Per atmosphere and class: same match, partial,
    covered."""
    py = [{"id": a, "classes": [[c["geometry_class"], c["match"], c["partial"], c["covered"]]
                                 for c in psi_query.readiness(a)["classes"]]}
          for a in psi_atmospheres.ATMOSPHERES]
    assert py == ts["readiness"]


def test_gap_map_matches_dashboard_heatmap(ts):
    """Chat gap map (O2 x pressure, filtered to one class) vs dashboard
    heatmap: same bins, same per-cell counts, same totals — kept in sync by
    comment only, so pinned here."""
    assert [list(b) for b in psi_widgets.O2_BINS] == ts["bins"]["o2"]
    assert [list(b) for b in psi_widgets.Y_BINS["pressure_atm"]] == ts["bins"]["pressure"]
    py = []
    for gc in sorted({i["geometry_class"] for i in psi_query.load()[1].values()}):
        d = psi_widgets.gap_map_data({"geometry_class": gc}, "pressure_atm")
        grid = [[len(d["grid"].get((x, y), ())) for x in range(len(psi_widgets.O2_BINS))]
                for y in range(len(psi_widgets.Y_BINS["pressure_atm"]))]
        reported = sum(1 for r in d["runs"] if psi_widgets._measure(r, "o2_pct") and psi_widgets._measure(r, "pressure_atm"))
        py.append([gc, grid, len(d["runs"]), reported])
    assert py == ts["heatmaps"]
    py_markers = [[k, psi_widgets._bin_of(a["o2_pct"], psi_widgets.O2_BINS),
                   psi_widgets._bin_of(a["pressure_atm"], psi_widgets.Y_BINS["pressure_atm"])]
                  for k, a in psi_atmospheres.ATMOSPHERES.items()]
    assert py_markers == ts["markers"]


def test_shade_thresholds_match_dashboard():
    """psi_widgets.SHADES thresholds vs heatmap.tsx shadeVar() (0 / 1-2 / 3-9 /
    10-29 / 30+) and the --heat-* colors in app/global.css."""
    assert [t for t, _ in psi_widgets.SHADES] == [0, 1, 3, 10, 30]
    css = (REPO / "system/site/app/global.css").read_text(encoding="utf-8")
    for i, (_, c) in enumerate(psi_widgets.SHADES):
        assert f"--heat-{i}: {c['light']};" in css and f"--heat-{i}: {c['dark']};" in css, i
    tsx = (REPO / "system/site/components/dashboard/heatmap.tsx").read_text(encoding="utf-8")
    for needle in ("n === 0", "n < 3", "n < 10", "n < 30"):
        assert needle in tsx, needle
