"use client";

import Link from "next/link";
import { useCallback, useEffect, useMemo, useState, type FormEvent, type ReactElement } from "react";
import { useSearchParams } from "next/navigation";

import { cn } from "@/lib/utils";
import {
  CATEGORICAL_AXES,
  NUMERIC_AXES,
  query as runQuery,
  queryFromParams,
  queryToParams,
  type NumericAxis,
  type Query,
  type QueryResult,
  type RunView,
} from "@/lib/psi-query";
import type { Investigation, Measure, SlimRun } from "@/lib/psi-types";

import { fmt, GEOMETRY_LABEL, isCat, QUANTITY_LABEL } from "./format";
import { colorMap } from "./palette";
import { RunCard } from "./run-card";
import { RunDetail } from "./run-detail";
import { Scatter, type Emphasis, type Point, type Span } from "./scatter";

const PRESETS: { label: string; hint: string; q: Query }[] = [
  { label: "15 % O₂ · 10 cm/s · PMMA", hint: "the challenge question", q: { o2_pct: 15, flow_cm_s: 10, fuel_family: "PMMA" } },
  { label: "Opposed flow over PMMA at 5 cm/s", hint: "BASS-II thick fuels", q: { flow_cm_s: 5, fuel_family: "PMMA", flow_direction: "opposed" } },
  { label: "30 % O₂ at 0.55 atm", hint: "exploration-atmosphere conditions", q: { o2_pct: 30, pressure_atm: 0.55 } },
  { label: "Cotton-fiberglass fabric in air at 20 cm/s", hint: "Saffire vs BASS", q: { o2_pct: 21, flow_cm_s: 20, fuel_family: "SIBAL" } },
  { label: "Heptane droplets, 15 % O₂", hint: "FLEX extinction", q: { o2_pct: 15, fuel_family: "n-heptane" } },
];

type Form = Record<NumericAxis | (typeof CATEGORICAL_AXES)[number], string>;
const EMPTY: Form = {
  o2_pct: "", flow_cm_s: "", pressure_atm: "", thickness_mm: "", droplet_d0_mm: "",
  fuel_family: "", geometry_class: "", flow_direction: "", fuel_form: "", investigation: "",
};
const toForm = (q: Query): Form => ({ ...EMPTY, ...Object.fromEntries(Object.entries(q).map(([k, v]) => [k, String(v)])) });
const fromForm = (f: Form): Query => queryFromParams(new URLSearchParams(Object.entries(f).filter(([, v]) => v !== "")));

function span(m: Measure | undefined): Span | null {
  if (!m || m.min === undefined || m.max === undefined) return null;
  return { lo: m.min, hi: m.max, vals: m.flags?.includes("multi") ? m.values : undefined };
}

function axisDisplay(m: Measure | undefined, axis: NumericAxis): string {
  if (!m || m.min === undefined || m.max === undefined) return "not reported";
  const unit = m.unit ?? NUMERIC_AXES[axis].unit;
  const convFlag = m.flags?.some((f) => f.startsWith("converted_from_")) ?? false;
  const moleFlag = m.flags?.includes("mole_fraction_to_pct") ?? false;
  if (convFlag || moleFlag) {
    if (m.min === m.max) return `${fmt(m.min)} ${unit} (cell ${m.raw})`;
    return `${fmt(m.min)}–${fmt(m.max)} ${unit} (cell ${m.raw})`;
  }
  return `${m.min === m.max ? fmt(m.min) : `${fmt(m.min)}–${fmt(m.max)}`}${unit ? ` ${unit}` : ""}`;
}

function describeQuery(q: Query): string {
  const bits: string[] = [];
  for (const k of Object.keys(NUMERIC_AXES) as NumericAxis[])
    if (q[k] !== undefined) bits.push(`${NUMERIC_AXES[k].label} ≈ ${fmt(q[k])} ${NUMERIC_AXES[k].unit}`);
  if (q.fuel_family) bits.push(q.fuel_family);
  if (q.flow_direction) bits.push(`${q.flow_direction} flow`);
  if (q.geometry_class) bits.push(GEOMETRY_LABEL[q.geometry_class] ?? q.geometry_class);
  if (q.investigation) bits.push(q.investigation);
  return bits.join(" · ") || "all tests";
}

/** The answer in one paragraph, computed — not generated. */
function Answer({ r, q }: { r: QueryResult; q: Query }): ReactElement {
  const { match, partial } = r.counts;
  const numeric = (Object.keys(NUMERIC_AXES) as NumericAxis[]).filter((k) => r.query[k] !== undefined);
  const missingAxes = [
    ...new Set(r.partial.flatMap((v) => numeric.filter((k) => v.axes[k]?.status === "not_reported"))),
  ].map((k) => NUMERIC_AXES[k].label.toLowerCase());
  const nearest = r.near[0];
  const outside = r.coverage.flatMap((c) =>
    Object.entries(c.axes)
      .filter(([, a]) => a && "target_in_range" in a && !a.target_in_range)
      .map(([k]) => `${c.investigation} (${NUMERIC_AXES[k as NumericAxis].label})`),
  );
  const conflicts = [...r.match, ...r.partial].filter((v) => v.run.conflicts?.length).length;
  return (
    <div className="rounded-xl border bg-card p-4">
      <p className="text-xs uppercase tracking-wide text-muted-foreground">What the PSI record says about</p>
      <p className="mt-0.5 font-display text-xl">{describeQuery(q)}</p>
      <div className="mt-3 flex flex-wrap gap-2 text-sm">
        <Stat n={match} label="at these conditions" tone={match ? "good" : "none"} />
        {numeric.length > 0 && <Stat n={partial} label={`partial (silent on ${missingAxes.join(", ") || "an axis"})`} tone={partial ? "info" : "none"} />}
        <Stat n={r.coverage.length} label="investigations searched" tone="none" />
        {conflicts > 0 && <Stat n={conflicts} label="with sources that disagree" tone="warn" />}
      </div>
      <ul className="mt-3 space-y-1 text-sm">
        {numeric.length > 0 && match === 0 && (
          <li>
            <strong>No test in these tables states all of these conditions.</strong>{" "}
            {partial > 0
              ? `${partial} test${partial > 1 ? "s" : ""} match every condition they do report, but don't report ${missingAxes.join(" or ")}.`
              : "Nothing matches even partially."}
          </li>
        )}
        {nearest && match < 3 && (
          <li>
            Nearest fully-reported test: <span className="font-mono">{nearest.run.id}</span> (
            {numeric
              .map((k) => {
                const a = nearest.axes[k];
                return a && "raw" in a ? `${NUMERIC_AXES[k].label} ${axisDisplay(a as any, k)}` : null;
              })
              .filter(Boolean)
              .join(", ")}
            ).
          </li>
        )}
        {outside.length > 0 && <li>Target outside the tested range of: {outside.join("; ")}.</li>}
        {r.geometry_classes.length > 1 && (
          <li className="text-amber-700 dark:text-amber-400">
            Evidence spans {r.geometry_classes.map((g) => GEOMETRY_LABEL[g] ?? g).join(" and ")} — compare outcomes only within one geometry class.
          </li>
        )}
        {r.relaxed.length > 0 && match === 0 && (
          <li className="text-muted-foreground">
            The same conditions were tested with other materials:{" "}
            {r.relaxed.slice(0, 4).map((x) => `${x.fuel_family} (${x.investigation}, ${x.runs})`).join("; ")}.
          </li>
        )}
      </ul>
    </div>
  );
}

function Stat({ n, label, tone }: { n: number; label: string; tone: "good" | "info" | "warn" | "none" }): ReactElement {
  return (
    <span
      className={cn(
        "rounded-full px-3 py-1",
        tone === "good" && "bg-emerald-100 text-emerald-900 dark:bg-emerald-950 dark:text-emerald-200",
        tone === "info" && "bg-sky-100 text-sky-900 dark:bg-sky-950 dark:text-sky-200",
        tone === "warn" && "bg-red-100 text-red-900 dark:bg-red-950 dark:text-red-200",
        tone === "none" && "bg-secondary text-secondary-foreground",
      )}
    >
      <strong>{n.toLocaleString("en-US")}</strong> {label}
    </span>
  );
}

export function Explorer({ investigations, basePath }: { investigations: Investigation[]; basePath: string }): ReactElement {
  const params = useSearchParams();
  const [runs, setRuns] = useState<SlimRun[] | null>(null);
  const [loadError, setLoadError] = useState(false);
  const [q, setQ] = useState<Query>(() => {
    const fromUrl = queryFromParams(new URLSearchParams(params.toString()));
    return Object.keys(fromUrl).length ? fromUrl : PRESETS[0].q;
  });
  const [form, setForm] = useState<Form>(() => toForm(q));
  const [selected, setSelected] = useState<string | null>(params.get("run"));
  const [tier, setTier] = useState<RunView["tier"]>("match");
  const [yAxis, setYAxis] = useState<"flow_cm_s" | "pressure_atm">("flow_cm_s");
  const [quantity, setQuantity] = useState("spread_rate");
  const [outcomeX, setOutcomeX] = useState<NumericAxis>("flow_cm_s");

  useEffect(() => {
    fetch(`${basePath}/psi/runs.json`)
      .then((r) => (r.ok ? r.json() : Promise.reject(r.status)))
      .then((d: { runs: SlimRun[] }) => setRuns(d.runs))
      .catch(() => setLoadError(true));
  }, [basePath]);

  const invIndex = useMemo(() => Object.fromEntries(investigations.map((i) => [i.id, i])), [investigations]);
  const colors = useMemo(() => colorMap(investigations), [investigations]);
  const result = useMemo(() => (runs ? runQuery(runs, investigations, q, {}, 25) : null), [runs, investigations, q]);
  const catOnly = useMemo(() => {
    if (!runs) return new Set<string>();
    const cq = Object.fromEntries(Object.entries(q).filter(([k]) => (CATEGORICAL_AXES as readonly string[]).includes(k))) as Query;
    return new Set(runQuery(runs, investigations, cq).match.map((v) => v.run.id));
  }, [runs, investigations, q]);
  const fuelFamilies = useMemo(() => {
    const c = new Map<string, number>();
    for (const r of runs ?? []) {
      const f = r.conditions.fuel_family;
      if (isCat(f)) c.set(f.value, (c.get(f.value) ?? 0) + 1);
    }
    return [...c.entries()].sort((a, b) => b[1] - a[1]);
  }, [runs]);

  // pick a sensible default tab whenever the result changes
  useEffect(() => {
    if (!result) return;
    setTier(result.counts.match ? "match" : result.counts.partial ? "partial" : "near");
  }, [result]);

  const apply = useCallback((next: Query) => {
    setQ(next);
    setForm(toForm(next));
    setSelected(null);
    const p = queryToParams(next).toString();
    window.history.replaceState(null, "", `${window.location.pathname}${p ? `?${p}` : ""}`);
  }, []);

  const onSubmit = (e: FormEvent) => {
    e.preventDefault();
    apply(fromForm(form));
  };

  const tierOf = useMemo(() => {
    const m = new Map<string, Emphasis>();
    if (!result) return m;
    for (const t of ["near", "partial", "match"] as const) for (const v of result[t]) m.set(v.run.id, t);
    return m;
  }, [result]);

  const emphasis = (id: string): Emphasis => tierOf.get(id) ?? (catOnly.has(id) ? "other" : "dim");

  const mapPoints: Point[] = useMemo(() => {
    if (!runs) return [];
    const out: Point[] = [];
    for (const r of runs) {
      const x = span(r.conditions.o2_pct as Measure | undefined);
      if (!x) continue;
      const y = span(r.conditions[yAxis] as Measure | undefined);
      out.push({
        id: r.id,
        x,
        y,
        color: colors[r.investigation],
        emphasis: emphasis(r.id),
        title: `${r.id} (${invIndex[r.investigation]?.name})\nO₂ ${axisDisplay(r.conditions.o2_pct as Measure | undefined, "o2_pct")}\n${
          y ? `${NUMERIC_AXES[yAxis].label} ${axisDisplay(r.conditions[yAxis] as Measure | undefined, yAxis)}` : `${NUMERIC_AXES[yAxis].label} not reported`
        }`,
      });
    }
    return out;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [runs, yAxis, colors, tierOf, catOnly]);

  const noO2 = runs ? runs.filter((r) => !span(r.conditions.o2_pct as Measure | undefined)).length : 0;

  const outcomeQuantities = useMemo(() => {
    const c = new Map<string, number>();
    for (const r of runs ?? [])
      if (catOnly.has(r.id)) for (const o of r.outcomes) if (o.measure?.min !== undefined) c.set(o.quantity, (c.get(o.quantity) ?? 0) + 1);
    return [...c.entries()].sort((a, b) => b[1] - a[1]);
  }, [runs, catOnly]);
  useEffect(() => {
    if (outcomeQuantities.length && !outcomeQuantities.some(([k]) => k === quantity)) setQuantity(outcomeQuantities[0][0]);
  }, [outcomeQuantities, quantity]);

  const outcomePoints: Point[] = useMemo(() => {
    const out: Point[] = [];
    for (const r of runs ?? []) {
      if (!catOnly.has(r.id)) continue;
      r.outcomes.forEach((o, i) => {
        if (o.quantity !== quantity || o.measure?.min === undefined) return;
        const atX = outcomeX === "flow_cm_s" && o.at?.flow_cm_s !== undefined ? { lo: o.at.flow_cm_s, hi: o.at.flow_cm_s } : null;
        const x = atX ?? span(r.conditions[outcomeX] as Measure | undefined);
        if (!x) return;
        const m = o.measure;
        out.push({
          id: `${r.id}#${i}`,
          x,
          y: { lo: m.min!, hi: m.max!, vals: m.value === undefined ? m.values : undefined },
          color: colors[r.investigation],
          emphasis: emphasis(r.id) === "dim" ? "other" : emphasis(r.id),
          title: `${r.id} (${invIndex[r.investigation]?.name})\n${QUANTITY_LABEL[quantity] ?? quantity}: ${o.measure?.raw ?? ""}${o.measure?.unit ? ` ${o.measure.unit}` : ""}`,
        });
      });
    }
    return out;
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [runs, catOnly, quantity, outcomeX, colors, tierOf]);
  const outcomeUnit = useMemo(() => {
    for (const r of runs ?? []) for (const o of r.outcomes) if (o.quantity === quantity && o.measure?.unit) return o.measure.unit;
    return "";
  }, [runs, quantity]);

  const selectedRun = runs?.find((r) => r.id === selected) ?? null;
  const tol = (k: NumericAxis, v?: number): [number, number] | undefined => {
    if (v === undefined) return undefined;
    const a = NUMERIC_AXES[k];
    const d = a.kind === "rel" ? a.tol * Math.abs(v) : a.tol;
    return [v - d, v + d];
  };

  return (
    <div className="grid gap-6 lg:grid-cols-[300px_minmax(0,1fr)]">
      {/* ── query panel ─────────────────────────────── */}
      <aside className="space-y-4 lg:sticky lg:top-4 lg:self-start">
        <form onSubmit={onSubmit} className="space-y-3 rounded-xl border bg-card p-4">
          <h2 className="font-display text-lg">Ask the data</h2>
          <p className="text-xs text-muted-foreground">Leave a field empty to not constrain it.</p>
          {(["o2_pct", "flow_cm_s", "pressure_atm"] as NumericAxis[]).map((k) => (
            <label key={k} className="block text-sm">
              <span className="text-muted-foreground">
                {NUMERIC_AXES[k].label} ({NUMERIC_AXES[k].unit}) · ±{NUMERIC_AXES[k].kind === "rel" ? `${NUMERIC_AXES[k].tol * 100}%` : `${NUMERIC_AXES[k].tol} ${NUMERIC_AXES[k].unit}`}
              </span>
              <input
                type="number"
                step="any"
                inputMode="decimal"
                value={form[k]}
                onChange={(e) => setForm({ ...form, [k]: e.target.value })}
                className="mt-1 w-full rounded-md border bg-background px-2 py-1.5"
              />
            </label>
          ))}
          <label className="block text-sm">
            <span className="text-muted-foreground">Fuel / material</span>
            <select
              value={form.fuel_family}
              onChange={(e) => setForm({ ...form, fuel_family: e.target.value })}
              className="mt-1 w-full rounded-md border bg-background px-2 py-1.5"
            >
              <option value="">any</option>
              {fuelFamilies.map(([f, n]) => (
                <option key={f} value={f}>
                  {f} ({n})
                </option>
              ))}
            </select>
          </label>
          <label className="block text-sm">
            <span className="text-muted-foreground">Geometry class</span>
            <select
              value={form.geometry_class}
              onChange={(e) => setForm({ ...form, geometry_class: e.target.value })}
              className="mt-1 w-full rounded-md border bg-background px-2 py-1.5"
            >
              <option value="">any</option>
              {Object.entries(GEOMETRY_LABEL).map(([k, v]) => (
                <option key={k} value={k}>
                  {v}
                </option>
              ))}
            </select>
          </label>
          <label className="block text-sm">
            <span className="text-muted-foreground">Flow direction</span>
            <select
              value={form.flow_direction}
              onChange={(e) => setForm({ ...form, flow_direction: e.target.value })}
              className="mt-1 w-full rounded-md border bg-background px-2 py-1.5"
            >
              <option value="">any</option>
              <option value="opposed">opposed</option>
              <option value="concurrent">concurrent</option>
              <option value="coflow">coflow</option>
            </select>
          </label>
          <label className="block text-sm">
            <span className="text-muted-foreground">Investigation</span>
            <select
              value={form.investigation}
              onChange={(e) => setForm({ ...form, investigation: e.target.value })}
              className="mt-1 w-full rounded-md border bg-background px-2 py-1.5"
            >
              <option value="">all</option>
              {investigations.map((i) => (
                <option key={i.id} value={i.id}>
                  {i.name}
                </option>
              ))}
            </select>
          </label>
          <div className="flex gap-2">
            <button type="submit" className="flex-1 rounded-md bg-primary px-3 py-2 text-sm font-medium text-primary-foreground hover:bg-primary/90">
              Search
            </button>
            <button type="button" onClick={() => setForm(EMPTY)} className="rounded-md border px-3 py-2 text-sm hover:bg-accent">
              Clear
            </button>
          </div>
        </form>
        <div className="rounded-xl border bg-card p-4">
          <h3 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Try</h3>
          <ul className="mt-2 space-y-1.5">
            {PRESETS.map((p) => (
              <li key={p.label}>
                <button type="button" onClick={() => apply(p.q)} className="text-left text-sm text-primary hover:underline">
                  {p.label}
                </button>
                <span className="block text-xs text-muted-foreground">{p.hint}</span>
              </li>
            ))}
          </ul>
        </div>
      </aside>

      {/* ── results ─────────────────────────────────── */}
      <div className="min-w-0 space-y-6">
        {loadError && <p className="rounded-lg border p-4 text-sm">Could not load the run table.</p>}
        {!runs && !loadError && <p className="rounded-lg border p-4 text-sm text-muted-foreground">Loading {investigations.reduce((s, i) => s + i.runs, 0).toLocaleString("en-US")} test records…</p>}
        {result && <Answer r={result} q={q} />}

        {result && (
          <section className="rounded-xl border bg-card p-4">
            <div className="flex flex-wrap items-end justify-between gap-3">
              <div>
                <h2 className="font-display text-lg">Coverage map</h2>
                <p className="text-xs text-muted-foreground">
                  Every test that reports O₂. Empty regions are conditions nobody has tested. Bars are ranges (O₂ drifting during a burn, flow swept);
                  stacked dots are one test run at several values. The dashed box is your tolerance window.
                </p>
              </div>
              <div className="flex rounded-md border p-0.5 text-xs">
                {(["flow_cm_s", "pressure_atm"] as const).map((k) => (
                  <button
                    key={k}
                    type="button"
                    onClick={() => setYAxis(k)}
                    className={cn("rounded px-2 py-1", yAxis === k ? "bg-primary text-primary-foreground" : "hover:bg-accent")}
                  >
                    O₂ × {NUMERIC_AXES[k].label.toLowerCase()}
                  </button>
                ))}
              </div>
            </div>
            <div className="mt-3">
              <Scatter
                points={mapPoints}
                xLabel="O₂ (%)"
                yLabel={`${NUMERIC_AXES[yAxis].label} (${NUMERIC_AXES[yAxis].unit})`}
                target={{
                  x: q.o2_pct,
                  y: q[yAxis],
                  xTol: tol("o2_pct", q.o2_pct),
                  yTol: tol(yAxis, q[yAxis]),
                }}
                selected={selected}
                onSelect={setSelected}
                missingLabel={`${NUMERIC_AXES[yAxis].label.toLowerCase()} not reported`}
              />
            </div>
            <Legend investigations={investigations} colors={colors} />
            <p className="mt-2 text-xs text-muted-foreground">
              {noO2.toLocaleString("en-US")} records don&apos;t report ambient O₂ (e.g. SPICE, SLICE, SAME, inverse flames whose O₂ is in the burner
              stream) and are searchable but not on this map.
            </p>
          </section>
        )}

        {result && (
          <section className="grid gap-4 xl:grid-cols-[minmax(0,1fr)_minmax(0,1fr)]">
            <div className="min-w-0">
              <div className="flex gap-1 rounded-lg border p-1 text-sm" role="tablist">
                {(["match", "partial", "near"] as const).map((t) => (
                  <button
                    key={t}
                    role="tab"
                    aria-selected={tier === t}
                    type="button"
                    onClick={() => setTier(t)}
                    className={cn("flex-1 rounded-md px-2 py-1.5", tier === t ? "bg-primary text-primary-foreground" : "hover:bg-accent")}
                  >
                    {t === "match" ? "At conditions" : t === "partial" ? "Partial" : "Nearest"}{" "}
                    <span className="opacity-80">({t === "near" ? result.near.length : result.counts[t]})</span>
                  </button>
                ))}
              </div>
              <p className="mt-2 text-xs text-muted-foreground">
                {tier === "match" && "Every condition you asked about is reported and within tolerance."}
                {tier === "partial" && "Within tolerance on everything the test reports — but it doesn't report at least one condition you asked about."}
                {tier === "near" && "Closest remaining tests, ranked by distance in tolerance units."}
              </p>
              <div className="mt-2 max-h-[70vh] space-y-2 overflow-y-auto pr-1">
                {result[tier].length === 0 && <p className="rounded-lg border p-4 text-sm text-muted-foreground">None.</p>}
                {result[tier].slice(0, 60).map((v) => (
                  <RunCard
                    key={v.run.id}
                    view={v}
                    investigations={invIndex}
                    color={colors[v.run.investigation]}
                    selected={selected === v.run.id}
                    onSelect={setSelected}
                    targetFlow={q.flow_cm_s}
                  />
                ))}
                {result[tier].length > 60 && (
                  <p className="text-xs text-muted-foreground">+ {result[tier].length - 60} more — narrow the query.</p>
                )}
              </div>
            </div>
            <div className="min-w-0">
              {selectedRun ? (
                <RunDetail run={selectedRun} investigation={invIndex[selectedRun.investigation]} basePath={basePath} onClose={() => setSelected(null)} />
              ) : (
                <div className="rounded-xl border border-dashed p-6 text-sm text-muted-foreground">
                  Select a test — in the list or on the map — to see every condition, result and source cell behind it.
                </div>
              )}
            </div>
          </section>
        )}

        {result && outcomeQuantities.length > 0 && (
          <section className="rounded-xl border bg-card p-4">
            <div className="flex flex-wrap items-end justify-between gap-3">
              <div>
                <h2 className="font-display text-lg">Results against conditions</h2>
                <p className="text-xs text-muted-foreground">
                  Measured results from tests passing your material / geometry filters. Where a test reports a result per flow setting, each is plotted at its own flow.
                </p>
              </div>
              <div className="flex flex-wrap gap-2 text-sm">
                <select value={quantity} onChange={(e) => setQuantity(e.target.value)} className="rounded-md border bg-background px-2 py-1">
                  {outcomeQuantities.map(([k, n]) => (
                    <option key={k} value={k}>
                      {QUANTITY_LABEL[k] ?? k} ({n})
                    </option>
                  ))}
                </select>
                <select value={outcomeX} onChange={(e) => setOutcomeX(e.target.value as NumericAxis)} className="rounded-md border bg-background px-2 py-1">
                  {(Object.keys(NUMERIC_AXES) as NumericAxis[]).map((k) => (
                    <option key={k} value={k}>
                      vs {NUMERIC_AXES[k].label.toLowerCase()}
                    </option>
                  ))}
                </select>
              </div>
            </div>
            {outcomePoints.length ? (
              <div className="mt-3">
                <Scatter
                  points={outcomePoints}
                  xLabel={`${NUMERIC_AXES[outcomeX].label} (${NUMERIC_AXES[outcomeX].unit})`}
                  yLabel={`${QUANTITY_LABEL[quantity] ?? quantity}${outcomeUnit ? ` (${outcomeUnit})` : ""}`}
                  target={{ x: q[outcomeX] }}
                  onSelect={(id) => setSelected(id.split("#")[0])}
                  height={320}
                />
              </div>
            ) : (
              <p className="mt-3 text-sm text-muted-foreground">No test reports both this result and this condition.</p>
            )}
          </section>
        )}

        {result && result.coverage.length > 0 && (
          <section className="rounded-xl border bg-card p-4">
            <h2 className="font-display text-lg">Coverage and gaps, by investigation</h2>
            <div className="mt-3 overflow-x-auto">
              <table className="w-full min-w-[560px] text-sm">
                <thead>
                  <tr className="border-b text-left text-xs uppercase tracking-wide text-muted-foreground">
                    <th className="py-2 pr-3">Investigation</th>
                    <th className="py-2 pr-3">Tests</th>
                    {(Object.keys(result.query) as string[])
                      .filter((k): k is NumericAxis => k in NUMERIC_AXES)
                      .map((k) => (
                        <th key={k} className="py-2 pr-3">
                          {NUMERIC_AXES[k].label} tested
                        </th>
                      ))}
                  </tr>
                </thead>
                <tbody>
                  {result.coverage.map((c) => (
                    <tr key={c.investigation_id} className="border-b last:border-0 align-top">
                      <td className="py-2 pr-3">
                        <span className="mr-2 inline-block size-2.5 rounded-full" style={{ background: colors[c.investigation_id] }} />
                        <Link href={`/explore/${c.investigation_id}/`} className="text-primary hover:underline">
                          {c.investigation}
                        </Link>
                        <span className="block text-xs text-muted-foreground">{GEOMETRY_LABEL[c.geometry_class]}</span>
                      </td>
                      <td className="py-2 pr-3">{c.runs}</td>
                      {(Object.keys(c.axes) as NumericAxis[]).map((k) => {
                        const a = c.axes[k]!;
                        return (
                          <td key={k} className="py-2 pr-3">
                            {"statement" in a ? (
                              <span className="italic text-muted-foreground">{a.statement}</span>
                            ) : (
                              <>
                                {fmt(a.min)}–{fmt(a.max)} {NUMERIC_AXES[k].unit}{" "}
                                <span className={a.target_in_range ? "text-emerald-700 dark:text-emerald-400" : "text-amber-700 dark:text-amber-400"}>
                                  {a.target_in_range ? "✓ covers target" : "✗ target outside"}
                                </span>
                                <span className="block text-xs text-muted-foreground">
                                  reported by {a.reported_by} of {a.of}
                                </span>
                              </>
                            )}
                          </td>
                        );
                      })}
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}
      </div>
    </div>
  );
}

function Legend({ investigations, colors }: { investigations: Investigation[]; colors: Record<string, string> }): ReactElement {
  const groups = Object.keys(GEOMETRY_LABEL).map((g) => ({ g, invs: investigations.filter((i) => i.geometry_class === g && i.runs > 0) }));
  return (
    <div className="mt-3 flex flex-wrap gap-x-6 gap-y-2 text-xs">
      {groups.map(({ g, invs }) => (
        <div key={g}>
          <p className="font-semibold text-muted-foreground">{GEOMETRY_LABEL[g]}</p>
          <div className="mt-1 flex flex-wrap gap-x-3 gap-y-1">
            {invs.map((i) => (
              <span key={i.id} className="inline-flex items-center gap-1">
                <span className="inline-block size-2.5 rounded-full" style={{ background: colors[i.id] }} />
                {i.name}
              </span>
            ))}
          </div>
        </div>
      ))}
      <div>
        <p className="font-semibold text-muted-foreground">Markers</p>
        <div className="mt-1 flex flex-wrap gap-x-3 gap-y-1">
          <span>● outlined — at conditions</span>
          <span>○ ring — partial</span>
          <span>• small — nearest</span>
          <span className="opacity-50">· faint — other tests</span>
        </div>
      </div>
    </div>
  );
}
