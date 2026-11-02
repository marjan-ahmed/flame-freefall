import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { compareRuns } from "./psi-comparison.ts";
import type { SlimRun } from "./psi-types.ts";

const fixtures = JSON.parse(readFileSync(new URL("../../../psi-data/query-fixtures.json", import.meta.url), "utf8"));
function pair() {
  const c = structuredClone(fixtures.comparison_cases[0]);
  for (const r of [c.left, c.right] as SlimRun[]) {
    r.sources = [{ kind: "report", quote: "Camera and front tracking were used." }];
    delete r.conditions.instrument; delete r.conditions.measurement_method;
    r.outcomes[0].metadata = Object.fromEntries([['instrument', 'camera'], ['measurement_method', 'front tracking']].map(([field, value]) => [field, { value, source: 0, quote: "Camera and front tracking were used." }]));
  }
  return c;
}
test("source-indexed method metadata applies to the selected outcome, not every outcome", () => {
  const c = pair();
  assert.equal(compareRuns(c.left, c.right, c.investigations, c.quantity).can_compare, true);
  for (const r of [c.left, c.right]) r.outcomes.push({ quantity: 'burn_time', source: 0, measure: { value: 1, min: 1, max: 1, raw: '1', unit: 's' } });
  const other = compareRuns(c.left, c.right, c.investigations, 'burn_time');
  assert.ok(other.unknown_or_conflicted.includes('instrument'));
  assert.ok(other.unknown_or_conflicted.includes('measurement_method'));
});
test("unsupported method sources cannot be rescued by campaign-wide categories", () => {
  for (const source of [-1, 99, true]) {
    const c = pair();
    c.left.conditions.instrument = { value: 'camera' };
    c.left.outcomes[0].metadata.instrument.source = source;
    assert.ok(compareRuns(c.left, c.right, c.investigations, c.quantity).unknown_or_conflicted.includes('instrument'));
  }
  const c = pair();
  c.left.outcomes[0].metadata.measurement_method.quote = 'unsupported';
  assert.ok(compareRuns(c.left, c.right, c.investigations, c.quantity).unknown_or_conflicted.includes('measurement_method'));
});

test("real FLEX methods resolve only for burning rate, with equivalence still blocked", () => {
  const root = new URL('../../../', import.meta.url);
  const runs = JSON.parse(readFileSync(new URL('psi-data/derived/runs.json', root), 'utf8')).runs as SlimRun[];
  const invs = Object.fromEntries(JSON.parse(readFileSync(new URL('psi-data/derived/investigations.json', root), 'utf8')).investigations.map((i: { id: string }) => [i.id, i]));
  const left = runs.find(r => r.id === 'PSI-69:FLEX-001')!, right = runs.find(r => r.id === 'PSI-69:FLEX-002')!;
  const rates = compareRuns(left, right, invs, 'burning_rate_k');
  for (const field of ['instrument', 'measurement_method']) {
    const check = rates.checks.find(c => c.field === field)!;
    assert.equal(check.status, 'match');
    for (const [r, c] of [[left, check.left], [right, check.right]] as const) assert.ok(r.sources[c!.source!].quote!.includes(c!.quote!));
  }
  assert.equal(rates.can_compare, false);
  assert.ok(compareRuns(left, right, invs, 'extinction_diameter').unknown_or_conflicted.includes('measurement_method'));
});
