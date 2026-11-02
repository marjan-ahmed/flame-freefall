/** Source-linked executable walkthroughs. These are engineering cases, not expert adjudication. */
import assert from "node:assert/strict";
import { readFileSync, writeFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { fileURLToPath } from "node:url";
import { resolve } from "node:path";
import { parse } from "yaml";
import { defaults, decisionExport } from "../system/site/lib/decision.ts";
import { comparisonAudit } from "../system/site/lib/psi-comparison.ts";
import { observationRelationshipSummary } from "../system/site/lib/observation-relationships.ts";
const root = fileURLToPath(new URL("../", import.meta.url));
const read = p => readFileSync(resolve(root, p), "utf8");
const raw = read("psi-data/derived/runs.json"), bundle = JSON.parse(raw), runs = bundle.runs;
const investigations = JSON.parse(read("psi-data/derived/investigations.json")).investigations;
const invs = Object.fromEntries(investigations.map(i => [i.id, i]));
const assignments = parse(read("psi-data/decision-contexts.yaml")).assignments;
const dataset = { generated_at: bundle.generated_at, sha256: createHash("sha256").update(raw).digest("hex") };
const index = Object.fromEntries(runs.map(r => [r.id, r]));
const norm = s => s.replace(/\s+/g, " ").trim();
const cases = [];
function check(id, question, task, forbidden, fn) {
  try { cases.push({ id, question, task, forbidden_inferences: forbidden, passed: true, observed: fn() }); }
  catch (error) { cases.push({ id, question, task, forbidden_inferences: forbidden, passed: false, failure: error.message }); }
}
check("prevention-lunar", "Which experiments inform a material study near the proposed Lunar atmosphere?", "Shortlist direct SAFFIRE evidence and indirect BRE evidence; explain the retrieval sensitivity and next source checks.", ["A full atmosphere match establishes material safety", "BRE is a measured solid specimen", "Microgravity validates Lunar gravity"], () => {
  const state = { ...defaults(), question: "Which experiments inform a material study near the proposed Lunar atmosphere?", shortlist: "saffire-iv-vi,acme-bre", quantity: "spread_rate" };
  const out = decisionExport(runs, investigations, assignments, state, dataset, bundle.generated_at);
  assert.equal(out.dossier.entries.length, 2);
  assert.equal(out.sensitivity[0].investigations.find(i => i.id === "saffire-iv-vi").full, 0);
  assert.equal(out.sensitivity.find(w => w.label === "Double oxygen tolerance").investigations.find(i => i.id === "saffire-iv-vi").full, 1);
  assert.ok(out.dossier.entries.find(e => e.id === "acme-bre").next_steps.some(s => s.code === "EMULATOR"));
  const audit = comparisonAudit(index["saffire-iv-vi:VI-3"], index["saffire-iv-vi:VI-4"], invs, "max_temp_sfu_outlet");
  assert.deepEqual(audit.sourced_outcomes.map(o => o.outcome.measure.value), [77, 57]);
  assert.ok(audit.sourced_outcomes.every(o => o.source.table === "Table 2"));
  assert.equal(audit.assessment.can_compare, false);
  return { selected_ids: out.dossier.selected_ids, sensitivity: out.sensitivity, audit_status: audit.assessment.status, audit_source: audit.sourced_outcomes.map(o => o.source), next_steps: audit.next_steps };
});
check("detection-observations", "Which smoke observations and instrument channels inform an early-warning study?", "Inspect SAME-R relationships and source columns; explain why an identifier group is not a replicate count.", ["Every suffix denotes an aged sample", "All observations are independent tests", "Instrument voltage is calibrated smoke concentration"], () => {
  const smoke = runs.filter(r => r.investigation === "same-r");
  const summary = observationRelationshipSummary(smoke);
  assert.equal(summary.observations, 109);
  assert.equal(summary.resolved_identifier_groups, 65);
  assert.ok(summary.ambiguous_observations > 0);
  assert.equal(index["PSI-101:SAME #51a"].observation_relationship.role, "unspecified");
  assert.equal(index["PSI-101:SAME #61a"].observation_relationship.role, "aged");
  const record = smoke.find(r => r.outcomes.some(o => o.quantity === "iss_detector_scatter_volts" && o.metadata?.instrument));
  assert.ok(record);
  const outcome = record.outcomes.find(o => o.quantity === "iss_detector_scatter_volts");
  const meta = outcome.metadata.instrument, source = record.sources[meta.source];
  assert.equal(source.sheet, "Reduced Data with ISS Det");
  assert.ok(source.quote.includes("ISS Detector Scatter (volts)"));
  assert.equal(outcome.metadata.measurement_method, undefined);
  return { identifier_summary: summary, example_record_id: record.id, instrument: meta, source, calibration: "unknown", independence: "unknown" };
});
check("suppression-methods", "What supports comparison of FLEX burning-rate measurements under different conditions?", "Inspect the selected outcome method and source definition, then explain the remaining comparison blockers.", ["One campaign method applies to every outcome", "An extrapolated extinction diameter is an exact measured point", "The catalog identifies a universally best suppressant"], () => {
  const a = index["PSI-69:FLEX-001"], b = index["PSI-69:FLEX-002"];
  const rate = b.outcomes.find(o => o.quantity === "burning_rate_k");
  assert.equal(rate.measure.value, 0.6);
  assert.equal(rate.measure.unit, "mm²/s");
  for (const field of ["instrument", "measurement_method"]) {
    const metadata = rate.metadata[field], source = b.sources[metadata.source];
    assert.ok(norm(source.quote).includes(norm(metadata.quote)));
    assert.ok(norm(read(source.via)).includes(norm(metadata.quote)));
  }
  const audit = comparisonAudit(a, b, invs, "burning_rate_k");
  assert.ok(audit.assessment.checks.filter(c => ["instrument", "measurement_method"].includes(c.field)).every(c => c.status === "match"));
  assert.equal(audit.assessment.can_compare, false);
  assert.equal(b.outcomes.find(o => o.quantity === "extinction_diameter").metadata?.measurement_method, undefined);
  return { record_ids: [a.id, b.id], metadata: rate.metadata, comparison_status: audit.assessment.status, blockers: audit.assessment.unknown_or_conflicted, differences: audit.assessment.differences, next_steps: audit.next_steps };
});
const report = { checked_at: new Date().toISOString(), dataset, passed: cases.every(c => c.passed), cases,
  limitations: "Executable internal source/data checks. No researcher was observed; no independent relevance labels, acceptance, safety validation or treatment effect is established." };
writeFileSync(resolve(root, "research/research-scenario-verification.json"), JSON.stringify(report, null, 2) + "\n");
const reviewTemplate = { dataset, status: "awaiting_independent_review", reviewer: null, reviewed_at: null,
  instructions: "Complete the tasks without assuming the application is correct. Record source IDs, applicability limits and next evidence to obtain. Expected automated outputs are in a separate engineering report, not independent ground truth.",
  tasks: cases.map(({ id, question, task }) => ({ id, question, task, researcher_answer: null, cited_sources: null, unsupported_inferences: null, completion_seconds: null, task_completed: null })),
  approval: null };
// A later engineering run must never erase a researcher's answers or rebind
// their review to a new dataset. Existing packets retain their original hash.
try {
  writeFileSync(resolve(root, "research/researcher-review-packet.json"), JSON.stringify(reviewTemplate, null, 2) + "\n", { flag: "wx" });
} catch (error) {
  if (error.code !== "EEXIST") throw error;
  console.log("Existing researcher review packet preserved, including its original dataset identity.");
}
console.log(JSON.stringify({ passed: report.passed, cases: cases.map(c => ({ id: c.id, passed: c.passed, failure: c.failure })), independent_review: "not performed" }, null, 2));
process.exitCode = report.passed ? 0 : 1;
