// Server-only data prep for the home-page dashboard: condition-coverage
// heatmaps and mission-readiness coverage, computed at build time from the
// same derived data the chat and Explorer read — nothing here is authored,
// nothing is a new scientific value, everything traces to psi-data/derived/.
//
// The heatmap bins mirror system/chatkit-server/psi_widgets.py's O2_BINS /
// Y_BINS["pressure_atm"] (same SHADES color scale, see app/global.css
// --heat-*) so the dashboard and the chat's gap map read as one system.
// Mission-readiness coverage reuses the TWINNED query() from ./psi-query
// (already pinned to psi-data/query-fixtures.json), not a third
// reimplementation of the match/partial/near tiers.

import { GEOMETRY_LABEL } from "@/components/explore/format";

import { psiInvestigations, psiIngestReport, slimRuns } from "./psi-data";
import { ATMOSPHERES, type Atmosphere } from "./psi-atmospheres";
import { query } from "./psi-query";
import type { Investigation, Measure, SlimRun } from "./psi-types";

export const O2_BINS: [number, number][] = [
  [0, 14], [14, 16], [16, 18], [18, 20], [20, 22], [22, 25], [25, 30], [30, 35], [35, 45], [45, 101],
];
export const PRESSURE_BINS: [number, number][] = [
  [0, 0.6], [0.6, 0.9], [0.9, 1.1], [1.1, 1.6], [1.6, 2.5], [2.5, 3.5], [3.5, 100],
];

function binOf(x: number, bins: [number, number][]): number | null {
  for (let i = 0; i < bins.length; i += 1) {
    const [lo, hi] = bins[i];
    if (x >= lo && x < hi) return i;
  }
  return null;
}

function measureOf(run: SlimRun, axis: "o2_pct" | "pressure_atm"): Measure | undefined {
  const m = run.conditions[axis] as Measure | undefined;
  return m && typeof m.min === "number" ? m : undefined;
}

function pointsOf(m: Measure): number[] {
  if (m.flags?.includes("multi") && m.values?.length) return m.values;
  return [((m.min as number) + (m.max as number)) / 2];
}

export type ClassHeatmap = {
  geometryClass: string;
  label: string;
  /** grid[yi (pressure band)][xi (O2 band)] = test count */
  grid: number[][];
  totalRuns: number;
  reportedRuns: number; // runs reporting BOTH o2_pct and pressure_atm
};

/** One O2 x pressure grid per geometry class — the dashboard's hero heatmap. */
export function geometryHeatmaps(): ClassHeatmap[] {
  const runs = slimRuns();
  const invs = psiInvestigations();
  const byId = new Map(invs.map((i) => [i.id, i]));
  const classes = [...new Set(invs.map((i) => i.geometry_class))].sort();

  return classes.map((gc) => {
    const grid: number[][] = PRESSURE_BINS.map(() => O2_BINS.map(() => 0));
    let totalRuns = 0;
    let reportedRuns = 0;
    for (const r of runs) {
      if (byId.get(r.investigation)?.geometry_class !== gc) continue;
      totalRuns += 1;
      const o2 = measureOf(r, "o2_pct");
      const p = measureOf(r, "pressure_atm");
      if (!o2 || !p) continue;
      reportedRuns += 1;
      const xs = new Set(pointsOf(o2).map((v) => binOf(v, O2_BINS)).filter((v): v is number => v !== null));
      const ys = new Set(pointsOf(p).map((v) => binOf(v, PRESSURE_BINS)).filter((v): v is number => v !== null));
      for (const x of xs) for (const y of ys) grid[y][x] += 1;
    }
    return { geometryClass: gc, label: GEOMETRY_LABEL[gc] ?? gc, grid, totalRuns, reportedRuns };
  });
}

export type AtmosphereMarker = { id: string; label: string; xBin: number | null; yBin: number | null };

/** Where each named mission atmosphere sits on the O2 x pressure grid — for
 * overlaying on the heatmap. null when the preset falls outside the binned
 * range (it never does today, but a future preset might). */
export function atmosphereMarkers(): AtmosphereMarker[] {
  return Object.values(ATMOSPHERES).map((atm) => ({
    id: atm.id,
    label: atm.label,
    xBin: binOf(atm.o2_pct, O2_BINS),
    yBin: binOf(atm.pressure_atm, PRESSURE_BINS),
  }));
}

export type ReadinessClass = { geometryClass: string; label: string; match: number; partial: number; covered: boolean };
export type ReadinessSummary = { atmosphere: Atmosphere; classes: ReadinessClass[] };

/** How many tests exist near each named mission atmosphere, per geometry
 * class — the SAME match/partial tiers the chat's show_mission_readiness
 * tool computes in Python (psi_query.readiness()), run here through the
 * twinned query() so both surfaces agree by construction, not by hand. */
export function missionReadinessSummary(): ReadinessSummary[] {
  const runs = slimRuns();
  const invs = psiInvestigations();
  const classes = [...new Set(invs.map((i) => i.geometry_class))].sort();
  return Object.values(ATMOSPHERES).map((atm) => ({
    atmosphere: atm,
    classes: classes.map((gc) => {
      const r = query(runs, invs, { o2_pct: atm.o2_pct, pressure_atm: atm.pressure_atm, geometry_class: gc });
      return {
        geometryClass: gc,
        label: GEOMETRY_LABEL[gc] ?? gc,
        match: r.counts.match,
        partial: r.counts.partial,
        covered: r.counts.match > 0 || r.counts.partial > 0,
      };
    }),
  }));
}

export type DashboardTotals = {
  investigations: number;
  runs: number;
  tests: number;
  withOutcomes: number;
  reportConfirmed: number;
  conflicts: number;
};

export function dashboardTotals(): DashboardTotals {
  const totals = (psiIngestReport() as { totals: Record<string, unknown> }).totals as {
    investigations: number;
    runs: number;
    by_granularity: Record<string, number>;
    runs_with_outcomes: number;
    runs_with_report_data: number;
    conflicts: number;
  };
  const tests = (totals.by_granularity.test ?? 0) + (totals.by_granularity["test-point"] ?? 0);
  return {
    investigations: totals.investigations,
    runs: totals.runs,
    tests,
    withOutcomes: totals.runs_with_outcomes,
    reportConfirmed: totals.runs_with_report_data,
    conflicts: totals.conflicts,
  };
}

export function geometryClasses(): string[] {
  return [...new Set(psiInvestigations().map((i: Investigation) => i.geometry_class))].sort();
}

export type CoverageGap = { geometryClass: string; label: string };

/** Geometry classes with NO O2%/pressure data at all (empty heatmap row) and
 * that never register as covered near any named mission atmosphere — the
 * single fact worth surfacing before a reader scans the full grid, not
 * buried as one gap chip among many. Computed, not hand-listed, so it stays
 * correct as investigations are added. */
export function totalCoverageGaps(heatmaps: ClassHeatmap[], readiness: ReadinessSummary[]): CoverageGap[] {
  return heatmaps
    .filter((h) => h.reportedRuns === 0)
    .filter((h) => readiness.every((r) => !r.classes.find((c) => c.geometryClass === h.geometryClass)?.covered))
    .map((h) => ({ geometryClass: h.geometryClass, label: h.label }));
}
