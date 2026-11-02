import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { comparisonAudit, compareRuns } from "./psi-comparison.ts";
import type { Investigation, SlimRun } from "./psi-types.ts";

const root = new URL("../../../", import.meta.url);
const read = (p: string) => JSON.parse(readFileSync(new URL(p, root), "utf8"));
const runs: SlimRun[] = read("psi-data/derived/runs.json").runs;
const invs: Record<string, Investigation> = Object.fromEntries(read("psi-data/derived/investigations.json").investigations.map((i: Investigation) => [i.id, i]));
const example = read("system/chatkit-server/tests/comparison-audit-real-case.json");
const left = runs.find(r => r.id === example.left_id)!, right = runs.find(r => r.id === example.right_id)!;

test("real SAFFIRE audit yields source-checked research facts while matched comparison remains blocked", () => {
  const before = JSON.stringify([left, right]);
  const audit = comparisonAudit(left, right, invs, example.quantity);
  assert.equal(audit.assessment.status, "insufficient_metadata");
  assert.equal(audit.assessment.can_compare, false);
  assert.deepEqual(audit.assessment, compareRuns(left, right, invs, example.quantity));
  assert.deepEqual(audit.shared_facts.map(c => c.field), example.shared_fields);
  assert.deepEqual(audit.recorded_differences.map(c => c.field), example.different_fields);
  assert.deepEqual(audit.missing_or_ambiguous.map(c => c.field), example.missing_fields);
  assert.deepEqual(audit.next_steps.map(s => s.code), example.next_step_codes);
  assert.deepEqual(audit.sourced_outcomes.map(o => o.outcome?.measure?.value), example.outcome_values);
  assert.ok(audit.research_result.startsWith("Two source-linked outcomes"));
  assert.equal(JSON.stringify([left, right]), before, "audit must not enrich records by inference");
  const extraction = readFileSync(new URL(example.source_extraction, root), "utf8");
  for (const [i, entry] of audit.sourced_outcomes.entries()) {
    assert.equal(entry.source?.url, example.source_url);
    assert.equal(entry.source?.table, example.source_table);
    assert.equal(entry.source_index, 1);
    const label = [left.label, right.label][i];
    const row = [...extraction.matchAll(/<tr>([\s\S]*?)<\/tr>/g)].map(m => [...m[1].matchAll(/<td[^>]*>([\s\S]*?)<\/td>/g)].map(c => c[1].replace(/<[^>]*>/g, " ").trim())).find(c => c[0] === label)!;
    assert.equal(Number(row[7]), example.outcome_values[i], "selected temperature must match original Table 2 row");
  }
});

test("nominating one varied condition does not hide other differences or missing metadata", () => {
  const audit = comparisonAudit(left, right, invs, example.quantity, "pressure_atm");
  assert.equal(audit.assessment.can_compare, false);
  assert.deepEqual(audit.next_steps.find(s => s.code === "MULTIPLE_SETUP_DIFFERENCES")?.fields, ["fuel", "o2_pct"]);
  assert.ok(audit.next_steps.some(s => s.code === "INSPECT_MISSING_METADATA"));
});

test("audit retains both conflict readings and never repairs a missing outcome citation", () => {
  const changed = structuredClone(right);
  changed.conflicts = [{ field: "o2_pct", values: [{ source: 0, raw: "28.8" }, { source: 1, raw: "30" }] }];
  changed.outcomes.find(o => o.quantity === example.quantity)!.source = 999;
  const audit = comparisonAudit(left, changed, invs, example.quantity);
  assert.deepEqual(audit.retained_conflicts[0].values, changed.conflicts[0].values);
  assert.ok(audit.next_steps.some(s => s.code === "REVIEW_RETAINED_CONFLICTS"));
  assert.ok(audit.next_steps.some(s => s.code === "INSPECT_OUTCOME_SOURCES"));
  assert.equal(audit.sourced_outcomes[1].source, null);
  assert.equal(audit.assessment.can_compare, false);
  assert.ok(!audit.research_result.startsWith("Two source-linked outcomes"));
});

test("one-sided outcomes remain one-sided and do not produce an inferred difference", () => {
  const audit = comparisonAudit(left, right, invs, "smoke_threshold_crossing_time");
  assert.equal(audit.sourced_outcomes[0].outcome?.measure?.value, 981);
  assert.equal(audit.sourced_outcomes[1].outcome, null);
  assert.ok(audit.next_steps.some(s => s.code === "INSPECT_OUTCOME_SOURCES"));
  assert.equal("difference" in audit, false);
  assert.equal("ratio" in audit, false);
});
