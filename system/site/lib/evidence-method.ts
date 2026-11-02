import { NUMERIC_AXES, query, queryFromParams, queryToParams, type NumericAxis, type Query } from "./psi-query.ts";
import type { Investigation, Outcome, SlimRun } from "./psi-types.ts";

export type Tolerances = Partial<Record<NumericAxis, number>>;
export const METHOD_VERSION = "atmosphere-overlap-v2";

export function tolerancesFromParams(params: URLSearchParams): Tolerances {
  const result: Tolerances = {};
  for (const axis of Object.keys(NUMERIC_AXES) as NumericAxis[]) {
    const raw = params.get(`tol_${axis}`);
    if (raw === null || raw.trim() === "") continue;
    const n = Number(raw);
    if (Number.isFinite(n) && n >= 0) result[axis] = n;
  }
  return result;
}

export function evidenceParams(q: Query, tolerances: Tolerances, individual: boolean): URLSearchParams {
  const params = queryToParams(q);
  // An explicit unconstrained search must survive sharing and reloading.
  params.set("search", "1");
  for (const [axis, value] of Object.entries(tolerances)) params.set(`tol_${axis}`, String(value));
  if (individual) params.set("individual", "1");
  return params;
}

export const individualRuns = (runs: SlimRun[]) => runs.filter(r => r.granularity === "test" || r.granularity === "test-point");

export function initialExplorerQuery(params: URLSearchParams, fallback: Query): Query {
  // Run-detail, comparison, and tolerance-only links are also deliberately unconstrained.
  return params.size ? queryFromParams(params) : fallback;
}

export type OutcomeSeries = { key: string; quantity: string; geometry: string; unit: string; entries: { run: SlimRun; outcome: Outcome; index: number }[] };

/** Units and geometry are separate axes of comparability; never merge them on a plot. */
export function outcomeSeries(runs: SlimRun[], investigations: Investigation[]): OutcomeSeries[] {
  const invs = new Map(investigations.map(i => [i.id, i]));
  const series = new Map<string, OutcomeSeries>();
  for (const run of runs) run.outcomes.forEach((outcome, index) => {
    const m = outcome.measure;
    if (!m || m.detection_limit || m.interval_kind === "source_conflict" || m.flags?.includes("source_conflict")) return;
    if (!Number.isFinite(m.min) || !Number.isFinite(m.max) || m.min! > m.max!) return;
    if (run.conflicts?.some(c => c.field === outcome.quantity || c.field === `outcome:${outcome.quantity}`)) return;
    const geometry = invs.get(run.investigation)?.geometry_class ?? "unknown";
    const unit = m.unit?.trim() || "unit not reported";
    const key = JSON.stringify([outcome.quantity, geometry, unit]);
    const group = series.get(key) ?? { key, quantity: outcome.quantity, geometry, unit, entries: [] };
    group.entries.push({ run, outcome, index });
    series.set(key, group);
  });
  return [...series.values()].sort((a, b) => b.entries.length - a.entries.length || a.key.localeCompare(b.key));
}

/** Strict paired points only: no midpoint, cross-product, summary or disputed condition. */
export function pairedPoint(run: SlimRun, x: NumericAxis, y: NumericAxis): [number, number] | null {
  if (!["test", "test-point"].includes(run.granularity)) return null;
  if (run.conflicts?.some(c => [x, y].includes(c.field as NumericAxis))) return null;
  const a = run.conditions[x], b = run.conditions[y];
  if (!a || !b || !("min" in a) || !("min" in b)) return null;
  if (a.detection_limit || b.detection_limit || a.interval_kind === "source_conflict" || b.interval_kind === "source_conflict") return null;
  if (!Number.isFinite(a.min) || !Number.isFinite(b.min) || a.min !== a.max || b.min !== b.max) return null;
  if (a.flags?.includes("multi") || b.flags?.includes("multi")) return null;
  return [a.min!, b.min!];
}

export function evidenceExport(runs: SlimRun[], investigations: Investigation[], q: Query, tolerances: Tolerances,
  individual: boolean, dataset: { generated_at: string; sha256: string }, excludedInvestigation = "") {
  const pool = (individual ? individualRuns(runs) : runs).filter(r => r.investigation !== excludedInvestigation);
  const result = query(pool, investigations, q, tolerances, pool.length);
  return {
    schema_version: 1, excluded_investigation: excludedInvestigation || null, method_version: METHOD_VERSION, dataset,
    query: q, tolerances: { ...Object.fromEntries(Object.entries(NUMERIC_AXES).map(([k, v]) => [k, v.tol])), ...tolerances },
    scope: individual ? "individual tests and test points" : "all granularities, including summaries and envelopes",
    limitations: "Search overlap is not physical equivalence, safety, certification or a partial-gravity prediction. Missing conditions are unknown. Ranges are reported intervals, not statistical uncertainty. Summary rows are not independent tests. No model-readiness claim is made.",
    counts: result.counts,
    investigations: investigations.filter(i => [...result.match, ...result.partial, ...result.near].some(v => v.run.investigation === i.id)),
    records: [...result.match, ...result.partial, ...result.near].map(v => ({ tier: v.tier, axes: v.axes, run: v.run })),
  };
}
