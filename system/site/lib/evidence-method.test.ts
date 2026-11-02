import assert from "node:assert/strict";
import { test } from "node:test";
import { readFileSync } from "node:fs";
import { evidenceExport, evidenceParams, initialExplorerQuery, outcomeSeries, pairedPoint, tolerancesFromParams } from "./evidence-method.ts";
import type { Investigation, SlimRun } from "./psi-types.ts";

const root = new URL("../../../", import.meta.url);
const runs = JSON.parse(readFileSync(new URL("psi-data/derived/runs.json", root), "utf8")).runs;
const invs = JSON.parse(readFileSync(new URL("psi-data/derived/investigations.json", root), "utf8")).investigations;

test("evidence download contains all tiers without display truncation and preserves source payloads", () => {
  const data = evidenceExport(runs, invs, { o2_pct: 34, pressure_atm: 56.5 / 101.325 }, { pressure_atm: 5 / 101.325 }, false,
    { generated_at: "fixture", sha256: "fixture" });
  assert.equal(data.records.length, runs.length);
  assert.equal(new Set(data.records.map(r => r.run.id)).size, runs.length);
  assert.equal(data.records.filter(r => r.tier === "near").length, data.counts.near_pool);
  for (const item of data.records) assert.deepEqual(item.run, runs.find((r: SlimRun) => r.id === item.run.id));
  assert.equal(data.tolerances.pressure_atm, 5 / 101.325);
});

test("individual evidence exports exclude summaries and planned envelopes", () => {
  const data = evidenceExport(runs, invs, {}, {}, true, { generated_at: "fixture", sha256: "fixture" });
  assert.ok(data.records.length < runs.length);
  assert.ok(data.records.every(r => ["test", "test-point"].includes(r.run.granularity)));
});

test("tolerance URLs round-trip zero and reject non-finite or negative values", () => {
  assert.deepEqual(tolerancesFromParams(evidenceParams({ o2_pct: 34 }, { o2_pct: 0, pressure_atm: 5 / 101.325 }, true)),
    { o2_pct: 0, pressure_atm: 5 / 101.325 });
  assert.deepEqual(tolerancesFromParams(new URLSearchParams("tol_o2_pct=-1&tol_pressure_atm=Infinity&tol_flow_cm_s=")), {});
});

test("shared unconstrained and detail-only searches never acquire the default PMMA conditions", () => {
  const fallback = { o2_pct: 15, fuel_family: "PMMA" };
  assert.deepEqual(initialExplorerQuery(new URLSearchParams(), fallback), fallback);
  assert.deepEqual(initialExplorerQuery(evidenceParams({}, {}, false), fallback), {});
  assert.deepEqual(initialExplorerQuery(new URLSearchParams("run=bass:test-1"), fallback), {});
  assert.deepEqual(initialExplorerQuery(evidenceParams({ thickness_mm: 2, fuel_form: "sheet" }, { flow_cm_s: .1 }, true), fallback),
    { thickness_mm: 2, fuel_form: "sheet" });
});

test("outcome plots separate geometry and units and retain bounds only in source records", () => {
  const base = { id: "a", investigation: "solid", granularity: "test", conditions: {}, outcomes: [
    { quantity: "spread_rate", source: 0, measure: { raw: "1", min: 1, max: 1, unit: "mm/s" } },
  ] } as SlimRun;
  const records = [base,
    { ...base, id: "b", outcomes: [{ ...base.outcomes[0], measure: { raw: "1", min: 1, max: 1, unit: "cm/s" } }] },
    { ...base, id: "c", investigation: "droplet" },
    { ...base, id: "censored", outcomes: [{ ...base.outcomes[0], measure: { raw: "<1", min: 1, max: 1, unit: "mm/s", detection_limit: { operator: "<", value: 1, raw: "<1" } } }] },
    { ...base, id: "disputed", conflicts: [{ field: "spread_rate", values: [] }] },
    { ...base, id: "invalid", outcomes: [{ ...base.outcomes[0], measure: { raw: "?", min: Infinity, max: Infinity } }] },
  ] as SlimRun[];
  const invs = [{ id: "solid", geometry_class: "solid-fuel" }, { id: "droplet", geometry_class: "droplet-combustion" }] as Investigation[];
  const series = outcomeSeries(records, invs);
  assert.equal(series.length, 3);
  assert.deepEqual(series.flatMap(s => s.entries.map(e => e.run.id)).sort(), ["a", "b", "c"]);
  assert.equal(records.find(r => r.id === "censored")!.outcomes[0].measure!.detection_limit!.operator, "<");
});

test("real-data plotted series preserve every eligible source outcome in one dimensional group", () => {
  const series = outcomeSeries(runs, invs);
  assert.ok(series.length > 0);
  const seen = new Set<string>();
  for (const group of series) for (const entry of group.entries) {
    assert.equal((invs as Investigation[]).find(i => i.id === entry.run.investigation)!.geometry_class, group.geometry);
    assert.equal(entry.outcome.measure!.unit?.trim() || "unit not reported", group.unit);
    assert.ok(!seen.has(`${entry.run.id}:${entry.index}`));
    seen.add(`${entry.run.id}:${entry.index}`);
  }
});

test("heatmap pairs never invent midpoints or combinations from marginal ranges", () => {
  const r = { granularity: "test", conditions: { o2_pct: { raw: "34", min: 34, max: 34 }, pressure_atm: { raw: "0.5", min: .5, max: .5 } } } as SlimRun;
  assert.deepEqual(pairedPoint(r, "o2_pct", "pressure_atm"), [34, .5]);
  assert.equal(pairedPoint({ ...r, granularity: "day" }, "o2_pct", "pressure_atm"), null);
  assert.equal(pairedPoint({ ...r, conditions: { ...r.conditions, o2_pct: { raw: "30-34", min: 30, max: 34 } } }, "o2_pct", "pressure_atm"), null);
  assert.equal(pairedPoint({ ...r, conflicts: [{ field: "o2_pct", values: [] }] }, "o2_pct", "pressure_atm"), null);
});
