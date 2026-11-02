// Parity with system/chatkit-server/psi_query.py: both implementations must
// reproduce psi-data/query-fixtures.json exactly. Run: npm run test:psi
// (node's built-in runner + type stripping; no test framework dependency).

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

import { query, rank, type Query } from "./psi-query.ts";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../../..");
const read = (p: string) => JSON.parse(readFileSync(path.join(root, p), "utf8"));
const runs = read("psi-data/derived/runs.json").runs;
const investigations = read("psi-data/derived/investigations.json").investigations;
const { cases, rank_cases } = read("psi-data/query-fixtures.json") as {
  cases: { name: string; query: Query; tolerances: Record<string, number> | null; expect: Record<string, unknown> }[];
  rank_cases: {
    name: string;
    query: Query;
    quantity: string;
    geometry_class: string;
    direction: "asc" | "desc";
    expect: Record<string, unknown>;
  }[];
};

test("pure fuels, explicit blends, and requested families have distinct populations", () => {
  const ids = (fuel_family: string) => new Set(query(runs, investigations, { fuel_family }).match.map(v => v.run.id));
  const pure = ids("n-dodecane");
  const blend = ids("n-dodecane/iso-dodecane");
  assert.ok(pure.size && blend.size);
  assert.ok([...pure].every(id => !blend.has(id)));
  assert.deepEqual(ids("n-dodecane*"), new Set([...pure, ...blend]));
  assert.equal(ids("*").size, 0);
  assert.deepEqual(ids("sibal"), ids("SIBAL (cotton-fiberglass)"));
  assert.deepEqual(ids("methane*"), new Set([...ids("methane"), ...ids("hydrogen/methane")]));
});

test("source quarantine excludes values from ranked aggregates", () => {
  const baseline = rank(runs, investigations, {}, "burning_rate_k", "droplet-combustion");
  assert.ok(!("error" in baseline));
  const record = structuredClone(runs.find((r: { id: string }) => r.id === baseline.rows[0].runs[0]));
  const before = rank([record], investigations, {}, "burning_rate_k", "droplet-combustion");
  assert.ok(!("error" in before) && before.total_ranked === 1);
  for (const outcome of record.outcomes) if (outcome.quantity === "burning_rate_k")
    outcome.measure.flags = [...(outcome.measure.flags ?? []), "source_definition_unresolved"];
  const after = rank([record], investigations, {}, "burning_rate_k", "droplet-combustion");
  assert.ok(!("error" in after) && after.total_ranked === 0);
});

test("ranking rejects censored points, contradictory outcome conditions and ambiguous sweeps", () => {
  const baseline = rank(runs, investigations, {}, "burning_rate_k", "droplet-combustion");
  assert.ok(!("error" in baseline));
  const sample = () => {
    const record = structuredClone(runs.find((r: { id: string }) => r.id === baseline.rows[0].runs[0]));
    record.outcomes = [record.outcomes.find((o: { quantity: string }) => o.quantity === "burning_rate_k")];
    return record;
  };
  const result = (record: ReturnType<typeof sample>, q: Query = {}) => {
    const r = rank([record], investigations, q, "burning_rate_k", "droplet-combustion");
    assert.ok(!("error" in r));
    return r;
  };
  const bounded = sample();
  bounded.outcomes[0].measure.detection_limit = { operator: "<", value: 1, raw: "<1" };
  assert.equal(result(bounded).total_ranked, 0);
  const unitless = sample();
  delete unitless.outcomes[0].measure.unit;
  assert.equal(result(unitless).excluded.missing_outcome_unit, 1);
  assert.ok("error" in rank(runs, investigations, { geometry_class: "solid-fuel" }, "burning_rate_k", "droplet-combustion"));
  const pressure = sample();
  pressure.conditions.pressure_atm = { value: 1, min: 1, max: 1, raw: "1", unit: "atm" };
  pressure.outcomes[0].at = { pressure_atm: .5 };
  assert.equal(result(pressure, { pressure_atm: 1 }).excluded.outcome_outside_query_window, 1);
  const duplicate = sample();
  duplicate.conditions.flow_cm_s = { value: 5, min: 5, max: 5, raw: "5", unit: "cm/s" };
  duplicate.outcomes[0].at = { flow_cm_s: 5 };
  duplicate.outcomes.push(structuredClone(duplicate.outcomes[0]));
  duplicate.outcomes[1].measure.value = 2;
  duplicate.outcomes[1].measure.min = 2;
  duplicate.outcomes[1].measure.max = 2;
  assert.equal(result(duplicate, { flow_cm_s: 5 }).excluded.ambiguous_outcome, 1);
  duplicate.outcomes.reverse();
  assert.equal(result(duplicate, { flow_cm_s: 5 }).excluded.ambiguous_outcome, 1);
  const sweep = sample();
  sweep.outcomes[0].at = { pressure_atm: .5 };
  sweep.outcomes.push(structuredClone(sweep.outcomes[0]));
  sweep.outcomes[1].at.pressure_atm = 1;
  assert.equal(result(sweep).excluded.multiple_outcome_conditions, 1);
  const original = sample(), uncertain = structuredClone(original);
  uncertain.id += "-uncertain";
  uncertain.conditions.pressure_atm.uncertainty = { kind: "reported", plus: .05, raw: "±0.05" };
  const strata = rank([original, uncertain], investigations, {}, "burning_rate_k", "droplet-combustion");
  assert.ok(!("error" in strata));
  assert.equal(strata.total_ranked, 2);
  assert.ok(strata.rows.every(row => row.n === 1));
});

for (const c of cases) {
  test(c.name, () => {
    const r = query(runs, investigations, c.query, c.tolerances ?? {});
    const got = {
      counts: r.counts,
      match_ids: r.match.slice(0, 15).map((v) => v.run.id),
      partial_ids: r.partial.slice(0, 15).map((v) => v.run.id),
      near_ids: r.near.slice(0, 5).map((v) => v.run.id),
      coverage: Object.fromEntries(
        r.coverage.map((cv) => [
          cv.investigation_id,
          Object.fromEntries(
            Object.entries(cv.axes).map(([k, a]) => [k, "target_in_range" in a! ? a.target_in_range : null]),
          ),
        ]),
      ),
      relaxed: r.relaxed,
    };
    assert.deepEqual(got, c.expect);
  });
}

for (const c of rank_cases) {
  test(c.name, () => {
    const r = rank(runs, investigations, c.query, c.quantity, c.geometry_class, c.direction);
    if ("error" in r) throw new Error(r.error);
    const got = {
      total_ranked: r.total_ranked,
      rows: r.rows.map((row) => ({ fuel_family: row.fuel_family, n: row.n, min: row.min, median: row.median, max: row.max })),
      untested: r.untested,
    };
    assert.deepEqual(got, c.expect);
  });
}
