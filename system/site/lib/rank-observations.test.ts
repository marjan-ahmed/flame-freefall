import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { rank } from "./psi-query.ts";
import type { Investigation, SlimRun } from "./psi-types.ts";

const root = new URL("../../../", import.meta.url);
const runs: SlimRun[] = JSON.parse(readFileSync(new URL("psi-data/derived/runs.json", root), "utf8")).runs;
const investigations: Investigation[] = JSON.parse(readFileSync(new URL("psi-data/derived/investigations.json", root), "utf8")).investigations;

test("real CFI-G temperature records remain separate observations despite equal recorded setup", () => {
  const ids = ["PSI-159:21265 F3", "PSI-159:21265 F4"];
  const selected = runs.filter(r => ids.includes(r.id));
  assert.equal(selected.length, 2);
  assert.ok(selected.every(r => !r.conditions.instrument));
  const result = rank(selected, investigations, {}, "peak_burner_temp_c", "gaseous-flames");
  assert.ok(!("error" in result));
  assert.equal(result.mode, "individual_observations");
  assert.equal(result.rows.length, 2);
  assert.deepEqual(result.rows.map(r => r.runs[0]).sort(), [...ids].sort());
  for (const row of result.rows) {
    assert.equal(row.n, 1);
    assert.equal(row.row_kind, "individual_observation");
    assert.equal(row.comparison_status, "not_audited");
    const original = selected.find(r => r.id === row.runs[0])!;
    const outcome = original.outcomes.find(o => o.quantity === "peak_burner_temp_c")!;
    assert.equal(row.value, outcome.measure!.value);
    assert.equal(row.raw, outcome.measure!.raw);
    assert.equal(row.source_index, outcome.source);
  }
});

test("an incomplete shared setup cannot produce pooled material estimates", () => {
  const original = structuredClone(runs.find(r => r.id === "PSI-159:21265 F3")!);
  const other = structuredClone(original);
  other.id += "-another-test";
  original.conditions = other.conditions = { fuel_family: { value: "butane" } };
  const result = rank([original, other], investigations, {}, "peak_burner_temp_c", "gaseous-flames");
  assert.ok(!("error" in result));
  assert.equal(result.rows.length, 2);
  assert.ok(result.rows.every(r => r.n === 1));
  assert.match(result.method, /no pooled material estimates/);
});

test("missing outcome units are excluded and incompatible units do not share value ordering", () => {
  const original = structuredClone(runs.find(r => r.id === "PSI-159:21265 F3")!);
  const missing = structuredClone(original), other = structuredClone(original);
  missing.id += "-unknown-unit";
  delete missing.outcomes.find(o => o.quantity === "peak_burner_temp_c")!.measure!.unit;
  other.id += "-kelvin";
  Object.assign(other.outcomes.find(o => o.quantity === "peak_burner_temp_c")!.measure!, { value: 300, min: 300, max: 300, unit: "K" });
  const result = rank([original, missing, other], investigations, {}, "peak_burner_temp_c", "gaseous-flames");
  assert.ok(!("error" in result));
  assert.equal(result.excluded.missing_outcome_unit, 1);
  assert.equal(result.rows.length, 2);
  assert.deepEqual(result.rows.map(r => r.unit), result.rows.map(r => r.unit).sort());
});
