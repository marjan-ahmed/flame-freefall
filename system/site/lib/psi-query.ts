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
// Sentinel score for a near-tier run reporting NONE of the query's axes: it
// is not "near" in any measured sense and must sort after every run that
// reports the axis, however far off that reading is. Mirrors psi_query.py.
const NO_AXES_REPORTED_SCORE = 1e6;
// A target exactly one tolerance-width from a run's value must match from
// either side. Plain float division (e.g. (1.1-1.0)/0.1) can land a hair
// above 1.0, excluding it on one side only; this absorbs that noise without
// ever admitting a run genuinely outside tolerance. Mirrors psi_query.py.
const TOLERANCE_EPS = 1e-9;
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

// A trailing roman numeral, converted to its arabic digit -- so a real name
// ending in one ("BASS-II") also answers to an informally arabic-typed query
// ("BASS 2"). One-directional on purpose (see investigationIds): only ever
// applied to the CANDIDATE id/name, never to the query itself, so a query
// that itself uses a roman numeral ("SAFFIRE-II") is never treated as an
// alias of an arabic-named investigation (SAFFIRE-2) -- that is a genuinely
// wrong name, not an alias, and must stay unresolved. Mirrors psi_query.py.
const ROMAN_TO_ARABIC: Record<string, string> = {
  i: "1", ii: "2", iii: "3", iv: "4", v: "5", vi: "6", vii: "7", viii: "8", ix: "9", x: "10",
};
const TRAILING_NUMERAL_RE = new RegExp(
  "(" + Object.keys(ROMAN_TO_ARABIC).sort((a, b) => b.length - a.length).join("|") + ")$",
);
const alnum = (s: string) => s.toLowerCase().replace(/[^a-z0-9]/g, "");

/** Alphanumeric-only, with a trailing ROMAN numeral (only) converted to
 * arabic. A tail that's already a plain digit, or no numeral at all, is
 * returned as-is -- this never invents an arabic->roman direction. */
function numeralCanon(s: string): string {
  const base = alnum(s);
  const m = base.match(TRAILING_NUMERAL_RE);
  return m ? base.slice(0, m.index) + ROMAN_TO_ARABIC[m[1]] : base;
}

/** Investigation ids a user/model name resolves to. An exact id or name
 * match wins ("BASS" is BASS, not BASS-II); otherwise a family name matches
 * every member ("SAFFIRE" -> SAFFIRE-1/-2/-3/IV-VI); otherwise a
 * hyphen-insensitive exact match ("FLEX 2" -> FLEX-2); otherwise, if the
 * query itself ends in a plain arabic digit (never a roman numeral -- see
 * numeralCanon), a candidate whose OWN trailing roman numeral converts to
 * that digit ("BASS 2" -> BASS-II). Shared by query()'s investigation
 * filter -- see C7. */
export function investigationIds(name: string, invs: InvIndex): Set<string> {
  // A blank name resolves to nothing, never to "every investigation" (every
  // id/name trivially starts with ""). Mirrors psi_query.py.
  if (!name || !name.trim()) return new Set();
  const norm = (s: string) => s.toLowerCase().replace(/ /g, "").replace(/_/g, "-");
  const n = norm(name);
  const exact = new Set(Object.keys(invs).filter((i) => n === norm(i) || n === norm(invs[i].name)));
  if (exact.size) return exact;
  const prefix = new Set(
    Object.keys(invs).filter((i) => norm(i).startsWith(n) || norm(invs[i].name).startsWith(n)),
  );
  if (prefix.size) return prefix;
  const an = alnum(name);
  const alnumExact = new Set(Object.keys(invs).filter((i) => an === alnum(i) || an === alnum(invs[i].name)));
  if (alnumExact.size) return alnumExact;
  if (!/\d$/.test(an)) return new Set(); // query doesn't end in a plain digit: no roman-alias attempt
  return new Set(Object.keys(invs).filter((i) => an === numeralCanon(i) || an === numeralCanon(invs[i].name)));
}

function catMatch(run: SlimRun, key: CategoricalAxis, want: string, invs: InvIndex): boolean {
  if (key === "investigation") {
    return investigationIds(want, invs).has(run.investigation);
  }
  const have = (catValue(run, key, invs) ?? "").toLowerCase();
  if (key === "fuel_family") {
    // Prefix/family searches include blends only when explicitly requested.
    if (want.endsWith("*")) {
      const prefix = want.slice(0, -1).trim();
      return prefix.length > 0 && (have.startsWith(prefix) || have.split("/").some(part => part.trim().startsWith(prefix)));
    }
    if (want === "sibal") want = "sibal (cotton-fiberglass)";
  }
  return have === want;
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
        status: d <= 1 + TOLERANCE_EPS ? "within" : "outside",
        raw: m.raw,
        min: m.min!,
        max: m.max!,
        unit: m.unit,
        distance: Math.round(d * 1000) / 1000,
        ...(m.flags?.length ? { flags: m.flags } : {}),
      };
    }
    const within = dists.every((d) => d <= 1 + TOLERANCE_EPS);
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
    // A run reporting NONE of the query's axes has no measured information
    // about it at all -- it must never rank as "nearer" than a run that DOES
    // report an axis, however far off that value is.
    else near.push({ score: dists.length ? score : NO_AXES_REPORTED_SCORE, run, axes });
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

// Which (geometry class, quantity) pairs have enough numeric runs to rank —
// twin of RANKABLE in psi_query.py. Keep both in sync.
export const RANKABLE: Record<string, string[]> = {
  "solid-fuel": ["spread_rate"],
  "droplet-combustion": ["burning_rate_k", "extinction_diameter"],
  "gaseous-flames": ["burn_time", "peak_burner_temp_c"],
};

/** Explicit scalars only; never synthesize observations from ranges. */
function outcomeValue(o: import("./psi-types").Outcome): number | null {
  const m = o.measure;
  if (!m || m.detection_limit || m.flags?.includes("source_definition_unresolved")) return null;
  if (m.value !== undefined && m.value !== null && Number.isFinite(m.value) && !m.values?.length) {
    if ((m.min ?? m.value) === (m.max ?? m.value)) return m.value;
  }
  return null;
}

export type RankRow = {
  row_kind: "individual_observation";
  comparison_status: "not_audited";
  value: number;
  raw: string;
  source_index: number;
  fuel_family: string;
  n: number;
  min: number;
  max: number;
  median: number;
  unit?: string;
  runs: string[];
  investigations: string[];
  conditions: Record<string, unknown>;
};

export type RankResult =
  | { error: string; rankable: string[] }
  | {
      query: Query;
      quantity: string;
      geometry_class: string;
      direction: "asc" | "desc";
      rows: RankRow[];
      total_ranked: number;
      untested: string[];
      coverage: Coverage[];
      excluded: Record<string, number>;
      method: string;
      mode: "individual_observations";
      method_version: string;
    };

/** Sort individual observations within ONE geometry class. Full search
 * matches do not establish comparable setups or pooled material estimates.
 * TypeScript twin of psi_query.rank() — both are
 * pinned to psi-data/query-fixtures.json's rank_cases. */
export function rank(
  runs: SlimRun[],
  investigations: Investigation[],
  q: Query,
  quantity: string,
  geometryClass: string,
  direction: "asc" | "desc" = "desc",
  limit = 10,
): RankResult {
  const rankable = RANKABLE[geometryClass] ?? [];
  if (!rankable.includes(quantity)) {
    return { error: `${JSON.stringify(quantity)} is not a rankable result for ${JSON.stringify(geometryClass)}`, rankable };
  }
  if (q.geometry_class && q.geometry_class !== geometryClass) {
    return { error: "The requested geometry class conflicts with the ranking class; query unchanged.", rankable };
  }
  const invs: InvIndex = Object.fromEntries(investigations.map((i) => [i.id, i]));
  const fullQ: Query = { ...q, geometry_class: geometryClass };
  const result = query(runs, investigations, fullQ);

  const byMaterial = new Map<string, { run_id: string; investigation: string; fuel_family: string; conditions: Record<string, unknown>; value: number; raw: string; source_index: number; unit?: string }[]>();
  const excluded: Record<string, number> = { incomplete_conditions: result.partial.length };
  const exclude = (reason: string) => { excluded[reason] = (excluded[reason] ?? 0) + 1; };
  for (const tier of ["match"] as const) {
    for (const v of result[tier]) {
      if (!["test", "test-point"].includes(v.run.granularity)) { exclude("summary_or_envelope"); continue; }
      if (v.run.conflicts?.length) { exclude("source_conflict"); continue; }
      if (quantity === "burn_time" && v.run.outcomes.some((o) => ["hot_ignition", "ignited"].includes(o.quantity)
        && ["no", "no ignition", "false"].includes((o.text ?? "").trim().toLowerCase()))) {
        exclude("did_not_ignite"); continue;
      }
      // Keep at most one unambiguously selected observation per test.
      let candidates = (v.run.outcomes ?? []).filter((o) => o.quantity === quantity && outcomeValue(o) !== null);
      if (!candidates.length) { exclude("no_scalar_outcome"); continue; }
      candidates = candidates.filter(o => o.measure?.unit);
      if (!candidates.length) { exclude("missing_outcome_unit"); continue; }
      const requestedAxes = new Set(Object.keys(q).filter(k => k in NUMERIC_AXES));
      const distance = (axis: string, value: number) => normDistance(axis as NumericAxis, Number(q[axis as NumericAxis]), { min: value, max: value } as Measure, NUMERIC_AXES[axis as NumericAxis].tol)!;
      candidates = candidates.filter(o => Object.entries(o.at ?? {}).every(([axis, value]) =>
        !requestedAxes.has(axis) || (Number.isFinite(value) && distance(axis, value) <= 1 + TOLERANCE_EPS)));
      if (!candidates.length) { exclude("outcome_outside_query_window"); continue; }
      if (candidates.length > 1 && candidates.some(o => Object.keys(o.at ?? {}).some(axis => !requestedAxes.has(axis)))) {
        exclude("multiple_outcome_conditions"); continue;
      }
      const outcomeDistance = (o: (typeof candidates)[number]) => Object.entries(o.at ?? {}).reduce((sum, [axis, value]) =>
        sum + (requestedAxes.has(axis) ? distance(axis, value) : 0), 0);
      const bestDistance = Math.min(...candidates.map(outcomeDistance));
      const nearest = candidates.filter(o => Math.abs(outcomeDistance(o) - bestDistance) <= TOLERANCE_EPS);
      if (nearest.length !== 1) { exclude("ambiguous_outcome"); continue; }
      const chosen = nearest[0];
      const val = outcomeValue(chosen)!;
      const fam = (catValue(v.run, "fuel_family", invs) ?? "unassigned") as string;
      const conditions: Record<string, unknown> = {};
      for (const key of Object.keys(v.run.conditions).sort(cmp)) {
        const c = v.run.conditions[key];
        conditions[key] = typeof c.value === "string" ? c.value
          : Object.fromEntries(["value", "min", "max", "unit", "values", "flags", "uncertainty", "detection_limit", "interval_kind"].filter((k) => k in c).map((k) => [k, (c as Record<string, unknown>)[k]]));
      }
      if (chosen.at) conditions.outcome_at = chosen.at;
      // Equal recorded metadata, including equally missing fields, never
      // establishes physical equivalence. Each run remains one observation.
      const key = v.run.id;
      const list = [{ run_id: v.run.id, investigation: invs[v.run.investigation].name, fuel_family: fam, conditions, value: val,
        raw: chosen.measure!.raw, source_index: chosen.source, unit: chosen.measure?.unit }];
      byMaterial.set(key, list);
    }
  }

  const rows: RankRow[] = [];
  for (const entries of byMaterial.values()) {
    const vals = entries.map((e) => e.value).sort((a, b) => a - b);
    const n = vals.length;
    const median = n % 2 ? vals[(n - 1) / 2] : (vals[n / 2 - 1] + vals[n / 2]) / 2;
    rows.push({
      row_kind: "individual_observation", comparison_status: "not_audited",
      value: entries[0].value, raw: entries[0].raw, source_index: entries[0].source_index,
      // Legacy fields remain for export compatibility; n is always one.
      fuel_family: entries[0].fuel_family,
      n,
      min: Math.round(vals[0] * 10000) / 10000,
      max: Math.round(vals[n - 1] * 10000) / 10000,
      median: Math.round(median * 10000) / 10000,
      unit: entries[0].unit,
      runs: entries.map((e) => e.run_id).sort(cmp),
      conditions: entries[0].conditions,
      investigations: [...new Set(entries.map((e) => e.investigation))].sort(cmp),
    });
  }
  rows.sort((a, b) => cmp(a.unit ?? "", b.unit ?? "") || (direction === "desc" ? b.value - a.value : a.value - b.value) || cmp(a.fuel_family, b.fuel_family) || cmp(a.runs[0], b.runs[0]));

  // "Untested at these conditions" means no match/partial run at all under
  // this query's OWN filters (categorical + numeric) -- not "every family in
  // the geometry class" (which ignores the query's own fuel_family/etc.
  // filter, so a filtered-out family like SIBAL under fuel_family='PMMA'
  // would wrongly be called untested) and not "ranked" (a family can have
  // match/partial runs at these conditions that simply don't report THIS
  // quantity -- that is not the same as never having been tested here).
  const catQ = CATEGORICAL_AXES.filter((k) => fullQ[k]).map((k) => [k, String(fullQ[k]).toLowerCase()] as const);
  const candidateFamilies = new Set(
    runs
      .filter((r) => invs[r.investigation].geometry_class === geometryClass
        && catQ.every(([k, v]) => catMatch(r, k, v, invs)))
      .map((r) => (catValue(r, "fuel_family", invs) ?? "unassigned") as string),
  );
  const testedFamilies = new Set(
    (["match", "partial"] as const).flatMap((tier) =>
      result[tier].map((v) => (catValue(v.run, "fuel_family", invs) ?? "unassigned") as string)),
  );
  const untested = [...candidateFamilies].filter((f) => !testedFamilies.has(f)).sort(cmp);

  return {
    query: fullQ,
    quantity,
    geometry_class: geometryClass,
    direction,
    rows: rows.slice(0, limit),
    total_ranked: rows.length,
    excluded,
    mode: "individual_observations", method_version: "sorted-observations-v1",
    method: "Sorted individual observations, grouped by reported unit. One eligible scalar outcome per full-match test; no pooled material estimates. Recorded setups remain separate, missing metadata is unknown, and physical comparability is not established. Not a safety ranking.",
    untested,
    coverage: result.coverage,
  };
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
