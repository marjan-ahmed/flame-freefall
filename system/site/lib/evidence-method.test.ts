import assert from "node:assert/strict";
import { test } from "node:test";
import { readFileSync } from "node:fs";
import { evidenceExport, evidenceParams, pairedPoint, tolerancesFromParams } from "./evidence-method.ts";
import type { SlimRun } from "./psi-types.ts";

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

test("heatmap pairs never invent midpoints or combinations from marginal ranges", () => {
  const r = { granularity: "test", conditions: { o2_pct: { raw: "34", min: 34, max: 34 }, pressure_atm: { raw: "0.5", min: .5, max: .5 } } } as SlimRun;
  assert.deepEqual(pairedPoint(r, "o2_pct", "pressure_atm"), [34, .5]);
  assert.equal(pairedPoint({ ...r, granularity: "day" }, "o2_pct", "pressure_atm"), null);
  assert.equal(pairedPoint({ ...r, conditions: { ...r.conditions, o2_pct: { raw: "30-34", min: 30, max: 34 } } }, "o2_pct", "pressure_atm"), null);
  assert.equal(pairedPoint({ ...r, conflicts: [{ field: "o2_pct", values: [] }] }, "o2_pct", "pressure_atm"), null);
});
