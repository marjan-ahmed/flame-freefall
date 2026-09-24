// Condition query over the PSI run table — the TypeScript twin of
// system/chatkit-server/psi_query.py. The static site can't call the copilot's
// server, so the Explorer runs the same algorithm in the browser; both are held
// to the golden cases in psi-data/query-fixtures.json
// (system/site/lib/psi-query.test.ts). Change them together.
//
// Tiers: match (every requested axis reported and within tolerance), partial
// (every REPORTED axis within tolerance, but silent on at least one), near
// (closest of the rest). Categorical filters are hard; what they removed is
// reported as `relaxed`.

import type { Investigation, Measure, SlimRun } from "./psi-types";

export const NUMERIC_AXES = {
  o2_pct: { kind: "abs", tol: 1.5, unit: "%", label: "O₂" },
  flow_cm_s: { kind: "rel", tol: 0.3, unit: "cm/s", label: "Flow" },
  pressure_atm: { kind: "abs", tol: 0.1, unit: "atm", label: "Pressure" },
  thickness_mm: { kind: "rel", tol: 0.5, unit: "mm", label: "Thickness" },
  droplet_d0_mm: { kind: "rel", tol: 0.25, unit: "mm", label: "Droplet d₀" },
} as const;
export type NumericAxis = keyof typeof NUMERIC_AXES;
export const CATEGORICAL_AXES = ["fuel_family", "geometry_class", "flow_direction", "fuel_form", "investigation"] as const;
export type CategoricalAxis = (typeof CATEGORICAL_AXES)[number];

export type Query = Partial<Record<NumericAxis, number>> & Partial<Record<CategoricalAxis, string>>;

const MISSING_PENALTY = 1.5;
const GRANULARITY_RANK: Record<string, number> = { test: 0, "test-point": 0, day: 1, summary: 1, envelope: 2 };

export type AxisResult =
  | { status: "not_reported" }
  | { status: "within" | "outside"; raw: string; min: number; max: number; unit?: string; distance: number; flags?: string[] };

export type RunView = {
  run: SlimRun;
  tier: "match" | "partial" | "near";
  distance: number;
  axes: Partial<Record<NumericAxis, AxisResult>>;
};

export type CoverageAxis =
  | { reported_by: 0; of: number; statement: string }
  | { reported_by: number; of: number; min: number; max: number; target_in_range: boolean };

export type Coverage = {
  investigation: string;
  investigation_id: string;
  geometry_class: string;
  runs: number;
  axes: Partial<Record<NumericAxis, CoverageAxis>>;
};

export type QueryResult = {
  query: Query;
  counts: { match: number; partial: number; near_pool: number };
  match: RunView[];
  partial: RunView[];
  near: RunView[];
  coverage: Coverage[];
  relaxed: { fuel_family: string; investigation: string; runs: number }[];
  geometry_classes: string[];
};

type InvIndex = Record<string, Investigation>;

function catValue(run: SlimRun, key: CategoricalAxis, invs: InvIndex): string | null {
  if (key === "investigation") return run.investigation;
  if (key === "geometry_class") return invs[run.investigation]?.geometry_class ?? null;
  const c = run.conditions[key] as { value?: unknown } | undefined;
  return c && typeof c.value === "string" ? c.value : null;
}

function catMatch(run: SlimRun, key: CategoricalAxis, want: string, invs: InvIndex): boolean {
  if (key === "investigation") {
    const inv = invs[run.investigation];
    return want === inv.id.toLowerCase() || want === inv.name.toLowerCase();
  }
  const have = (catValue(run, key, invs) ?? "").toLowerCase();
  return key === "fuel_family" ? have.startsWith(want) : have === want;
}

function measureOf(run: SlimRun, axis: NumericAxis): Measure | undefined {
  const m = run.conditions[axis] as Measure | undefined;
  return m && typeof m.min === "number" ? m : undefined;
}

function normDistance(axis: NumericAxis, target: number, m: Measure | undefined, tol: number): number | null {
  if (!m || m.min === undefined || m.max === undefined) return null;
  const kind = NUMERIC_AXES[axis].kind;
  const scale = kind === "rel" && target ? tol * Math.abs(target) : tol;
  let d: number;
  if ((m.flags ?? []).includes("multi") && m.values?.length) {
    d = Math.min(...m.values.map((v) => Math.abs(v - target)));
  } else {
    d = m.min <= target && target <= m.max ? 0 : Math.min(Math.abs(target - m.min), Math.abs(target - m.max));
  }
  return scale ? d / scale : d === 0 ? 0 : Infinity;
}

const cmp = (a: string, b: string) => (a < b ? -1 : a > b ? 1 : 0);

export function query(
  runs: SlimRun[],
  investigations: Investigation[],
  q: Query,
  tolerances: Partial<Record<NumericAxis, number>> = {},
  nearLimit = 10,
): QueryResult {
  const invs: InvIndex = Object.fromEntries(investigations.map((i) => [i.id, i]));
  const tol = Object.fromEntries(
    (Object.keys(NUMERIC_AXES) as NumericAxis[]).map((k) => [k, tolerances[k] ?? NUMERIC_AXES[k].tol]),
  ) as Record<NumericAxis, number>;
  const numQ = (Object.keys(NUMERIC_AXES) as NumericAxis[])
    .filter((k) => q[k] !== undefined && q[k] !== null && !Number.isNaN(q[k]))
    .map((k) => [k, Number(q[k])] as const);
  const catQ = CATEGORICAL_AXES.filter((k) => q[k]).map((k) => [k, String(q[k]).toLowerCase()] as const);

  type Hit = { score: number; run: SlimRun; axes: RunView["axes"] };
  const matched: Hit[] = [];
  const partial: Hit[] = [];
  const near: Hit[] = [];
  const relaxed = new Map<string, { fuel_family: string; investigation: string; runs: number }>();
  const considered = new Set<string>();

  for (const run of runs) {
    const catOk = catQ.every(([k, v]) => catMatch(run, k, v, invs));
    const axes: RunView["axes"] = {};
    const dists: number[] = [];
    const missing: NumericAxis[] = [];
    for (const [axis, target] of numQ) {
      const m = measureOf(run, axis);
      const d = normDistance(axis, target, m, tol[axis]);
      if (d === null || !m) {
        missing.push(axis);
        axes[axis] = { status: "not_reported" };
        continue;
      }
      dists.push(d);
      axes[axis] = {
        status: d <= 1 ? "within" : "outside",
        raw: m.raw,
        min: m.min!,
        max: m.max!,
        unit: m.unit,
        distance: Math.round(d * 1000) / 1000,
        ...(m.flags?.length ? { flags: m.flags } : {}),
      };
    }
    const within = dists.every((d) => d <= 1);
    if (!catOk) {
      if (numQ.length && within && !missing.length) {
        const fam = catValue(run, "fuel_family", invs) ?? "unassigned";
        const name = invs[run.investigation].name;
        const key = `${fam}\u0000${name}`;
        const e = relaxed.get(key) ?? { fuel_family: fam, investigation: name, runs: 0 };
        e.runs += 1;
        relaxed.set(key, e);
      }
      continue;
    }
    considered.add(run.investigation);
    const score = Math.sqrt(dists.reduce((s, d) => s + d * d, 0) + MISSING_PENALTY ** 2 * missing.length);
    if (!numQ.length) matched.push({ score: 0, run, axes });
    else if (within && !missing.length) matched.push({ score, run, axes });
    else if (within && dists.length) partial.push({ score, run, axes });
    else near.push({ score, run, axes });
  }

  const order = (a: Hit, b: Hit) =>
    (GRANULARITY_RANK[a.run.granularity] ?? 9) - (GRANULARITY_RANK[b.run.granularity] ?? 9) ||
    a.score - b.score ||
    cmp(a.run.id, b.run.id);
  matched.sort(order);
  partial.sort(order);
  near.sort(order);
  const view = (tier: RunView["tier"]) => (h: Hit): RunView => ({
    run: h.run,
    tier,
    distance: Math.round(h.score * 1000) / 1000,
    axes: h.axes,
  });

  return {
    query: { ...Object.fromEntries(numQ), ...Object.fromEntries(catQ) } as Query,
    counts: { match: matched.length, partial: partial.length, near_pool: near.length },
    match: matched.map(view("match")),
    partial: partial.map(view("partial")),
    near: near.slice(0, nearLimit).map(view("near")),
    coverage: coverage(runs, invs, numQ, catQ, considered),
    // Python's Counter.most_common: by count, ties in first-seen order (sort is stable).
    relaxed: [...relaxed.values()].sort((a, b) => b.runs - a.runs),
    geometry_classes: [...new Set([...matched, ...partial].map((h) => invs[h.run.investigation].geometry_class))].sort(cmp),
  };
}

function coverage(
  runs: SlimRun[],
  invs: InvIndex,
  numQ: (readonly [NumericAxis, number])[],
  catQ: (readonly [CategoricalAxis, string])[],
  considered: Set<string>,
): Coverage[] {
  const byInv = new Map<string, SlimRun[]>();
  for (const r of runs) {
    if (!considered.has(r.investigation)) continue;
    if (!catQ.every(([k, v]) => catMatch(r, k, v, invs))) continue;
    byInv.set(r.investigation, [...(byInv.get(r.investigation) ?? []), r]);
  }
  return [...byInv.entries()]
    .sort((a, b) => cmp(invs[a[0]].name, invs[b[0]].name))
    .map(([invId, rs]) => {
      const axes: Coverage["axes"] = {};
      for (const [axis, target] of numQ) {
        const ms = rs.map((r) => measureOf(r, axis)).filter((m): m is Measure => !!m);
        if (!ms.length) {
          const settings =
            axis === "flow_cm_s"
              ? [...new Set(rs.flatMap((r) => Object.keys(r.conditions).filter((k) => k.startsWith("flow_setting"))))].sort(cmp)
              : [];
          axes[axis] = {
            reported_by: 0,
            of: rs.length,
            statement: "not reported" + (settings.length ? ` (only as control-panel settings: ${settings.join(", ")})` : ""),
          };
          continue;
        }
        const lo = Math.min(...ms.map((m) => m.min!));
        const hi = Math.max(...ms.map((m) => m.max!));
        axes[axis] = { reported_by: ms.length, of: rs.length, min: lo, max: hi, target_in_range: lo <= target && target <= hi };
      }
      return {
        investigation: invs[invId].name,
        investigation_id: invId,
        geometry_class: invs[invId].geometry_class,
        runs: rs.length,
        axes,
      };
    });
}

/** The query as URL search params (what the copilot's "Open in Explorer" link carries). */
export function queryFromParams(p: URLSearchParams): Query {
  const q: Query = {};
  for (const k of Object.keys(NUMERIC_AXES) as NumericAxis[]) {
    const v = p.get(k);
    if (v !== null && v !== "" && !Number.isNaN(Number(v))) q[k] = Number(v);
  }
  for (const k of CATEGORICAL_AXES) {
    const v = p.get(k);
    if (v) q[k] = v;
  }
  return q;
}

export function queryToParams(q: Query): URLSearchParams {
  const p = new URLSearchParams();
  for (const [k, v] of Object.entries(q)) if (v !== undefined && v !== null && v !== "") p.set(k, String(v));
  return p;
}
