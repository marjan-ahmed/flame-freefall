import assert from "node:assert/strict";
import { test } from "node:test";
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { parse } from "yaml";
import { ATMOSPHERES, ATM_PER_KPA } from "./psi-atmospheres.ts";
import { bucket, decide, decisionExport, defaults, dossier, explorerLink, restore, sensitivity, stateParams, validate, type Assignment } from "./decision.ts";
import { checkMapping } from "./decision-mapping.ts";
import { evidenceExport } from "./evidence-method.ts";
import { query } from "./psi-query.ts";
import type { Investigation, SlimRun } from "./psi-types.ts";

const root = new URL("../../../", import.meta.url);
const read = (p: string) => JSON.parse(readFileSync(new URL(p, root), "utf8"));
const runs: SlimRun[] = read("psi-data/derived/runs.json").runs;
const invs: Investigation[] = read("psi-data/derived/investigations.json").investigations;
const assignments: Assignment[] = parse(readFileSync(new URL("psi-data/decision-contexts.yaml", root), "utf8")).assignments;

test("real Lunar dossier retains the question, source-backed shortlist, missing evidence and sensitivity", () => {
  const s = { ...defaults(), question: "Which experiments should inform my exploration-atmosphere study?", shortlist: "saffire-iv-vi,acme-bre", quantity: "spread_rate" };
  assert.deepEqual(restore(stateParams(s)), s);
  const brief = dossier(runs, invs, assignments, s);
  assert.equal(brief.question, s.question);
  assert.equal(brief.entries.length, 2);
  const solid = brief.entries.find(e => e.id === "saffire-iv-vi")!;
  assert.equal(solid.buckets.full, 0);
  assert.ok(solid.next_steps.some(s => s.code === "OUTSIDE_WINDOW"));
  assert.ok(brief.entries.find(e => e.id === "acme-bre")!.next_steps.some(s => s.code === "EMULATOR"));
  const windows = sensitivity(runs, invs, assignments, s);
  assert.equal(windows[0].investigations.find(i => i.id === "saffire-iv-vi")!.full, 0);
  assert.equal(windows.find(w => w.label === "Double oxygen tolerance")!.investigations.find(i => i.id === "saffire-iv-vi")!.full, 1);
  assert.ok(windows.every(w => w.investigations.length === 2));
  const out = decisionExport(runs, invs, assignments, s, { generated_at: "fixture", sha256: "fixture" }, "fixture");
  for (const entry of out.dossier.entries) for (const id of entry.record_ids) assert.ok(out.evidence.records.some(v => v.run.id === id && v.run.sources.length > 0));
  assert.ok(dossier(runs, invs, assignments, { ...s, shortlist: "unknown" }).selection_warnings.some(w => w.includes("Unknown")));
});

test("measurement focus affects relevance availability without silently excluding records", () => {
  const all = decide(runs, invs, assignments, defaults("detection"));
  const focused = decide(runs, invs, assignments, { ...defaults("detection"), quantity: "iss_detector_scatter_volts" });
  assert.equal(focused.rows.reduce((n, r) => n + r.records.length, 0), runs.length);
  assert.equal(focused.rows.find(r => r.investigation.id === "same-r")!.citedOutcomes, 108);
  assert.ok(all.rows.find(r => r.investigation.id === "flex")!.citedOutcomes > 0);
  assert.equal(focused.rows.find(r => r.investigation.id === "flex")!.citedOutcomes, 0);
});

test("mapping checks stable sources, exact body quotes, identity, all jobs and duplicate membership", () => {
  assert.equal(checkMapping(assignments, invs, fileURLToPath(root)), assignments);
  for (const override of [{ investigation: "unknown" }, { quote: "Unsupported quotation" }, { doc: "knowledge/investigations/solid-fuel/bass-ii-requirements" }, { checked_by: "human:review-not-given" }]) {
    assert.throws(() => checkMapping([{ ...assignments[0], ...override }, ...assignments.slice(1)], invs, fileURLToPath(root)));
  }
  assert.throws(() => checkMapping([...assignments, assignments[0]], invs, fileURLToPath(root)), /Duplicate/);
  assert.throws(() => checkMapping(assignments.filter(a => a.job !== "suppression"), invs, fileURLToPath(root)), /No supported/);
});

test("defaults, explicit detection atmosphere activation and blank unprovided contexts", () => {
  assert.equal(validate(defaults()).q.pressure_atm, ATMOSPHERES.lunar.pressure_atm);
  const s = defaults("detection");
  assert.equal(validate(s).conditioned, false);
  const d = decide(runs, invs, assignments, s);
  for (const id of ["same", "same-r"]) {
    const row = d.rows.find(r => r.investigation.id === id)!;
    assert.equal(row.mapping?.job, "detection"); assert.ok(row.individual > 0);
    assert.ok(row.records.every(v => v.bucket === "unconditioned"));
    const activated = decide(runs, invs, assignments, { ...s, atmosphere: "1" }).rows.find(r => r.investigation.id === id)!;
    assert.ok(activated.records.some(v => v.bucket === "none-reported" || v.bucket === "partial" || v.bucket === "outside-plus-missing"));
  }
  for (const scenario of ["rover", "spacesuit", "mars", "custom"]) {
    const s = defaults("prevention", scenario);
    assert.equal(s.o2_pct, ""); assert.equal(s.pressure_kpa, ""); assert.ok(validate(s).errors.browse);
    assert.equal(validate({ ...s, browse: "1" }).conditioned, false);
  }
});

test("URL inputs survive invalid text; all state round trips; custom conversion does not round", () => {
  const s = { ...defaults(), pressure_kpa: "56.123456789", tol_pressure_kpa: "0.123456789", o2_pct: "NaN", flow_cm_s: "-1" };
  assert.deepEqual(restore(stateParams(s)), s);
  assert.ok(validate(s).errors.o2_pct); assert.ok(validate(s).errors.flow_cm_s);
  const good = validate({ ...s, o2_pct: "34", flow_cm_s: "5" });
  assert.equal(good.q.pressure_atm, Number(s.pressure_kpa) * ATM_PER_KPA);
  assert.equal(good.tol.pressure_atm, Number(s.tol_pressure_kpa) * ATM_PER_KPA);
  for (const id of Object.keys(ATMOSPHERES)) assert.equal(validate(defaults("prevention", id)).q.pressure_atm, ATMOSPHERES[id].pressure_atm);
  for (const [key, value] of [["o2_pct", "101"], ["pressure_kpa", "0"], ["tol_flow", "Infinity"], ["tol_o2", "-1"], ["job", "invalid"], ["scenario", "invalid"], ["geometry_class", "invalid"]]) assert.ok(Object.keys(validate({ ...defaults(), [key]: value }).errors).length);
});

test("five exhaustive buckets, discrete values, ranges, overlays, settings, near > 10 and granularity", () => {
  const base = runs.find(r => r.granularity === "test")!;
  const m = (min: number, max = min) => ({ min, max, raw: `${min} to ${max}` });
  const fixtures: SlimRun[] = [
    { ...base, id: "full", conditions: { o2_pct: m(34), pressure_atm: m(0.55) } },
    { ...base, id: "partial", conditions: { o2_pct: m(34) } },
    { ...base, id: "outside-only", conditions: { o2_pct: m(10), pressure_atm: m(1) } },
    { ...base, id: "outside-plus-missing", conditions: { o2_pct: m(10) } },
    { ...base, id: "none-reported", conditions: { flow_setting_air: m(34) } },
    { ...base, id: "range", conditions: { o2_pct: m(30, 40), pressure_atm: m(0.55) }, conflicts: [{ field: "o2_pct", values: [{ source: 0, raw: "30" }, { source: 1, raw: "40" }] }] },
    { ...base, id: "discrete", conditions: { o2_pct: { ...m(30, 40), flags: ["multi"], values: [30, 40] }, pressure_atm: m(0.55) } },
    ...Array.from({ length: 20 }, (_, i) => ({ ...base, id: `near-${i}`, conditions: { o2_pct: m(10) } })),
    { ...base, id: "summary", granularity: "summary", conditions: {} },
  ];
  const s = { ...defaults(), pressure_kpa: String(0.55 / ATM_PER_KPA) };
  const d = decide(fixtures, invs, assignments, s), r = d.rows.find(r => r.investigation.id === base.investigation)!;
  for (const name of ["full", "partial", "outside-only", "outside-plus-missing", "none-reported"]) assert.equal(r.records.find(v => v.run.id === name)!.bucket, name);
  assert.equal(r.records.find(v => v.run.id === "range")!.bucket, "full");
  assert.equal(r.records.find(v => v.run.id === "discrete")!.bucket, "outside-only");
  assert.equal(r.conflicts, 1); assert.equal(r.controlOnly, 1); assert.equal(r.nonIndividual, 1);
  assert.equal(Object.values(r.counts).reduce((a, b) => a + b), fixtures.length - 1);
  assert.equal(r.records.length, fixtures.length);
  assert.deepEqual(r.records.find(v => v.run.id === "range")!.run.conflicts, fixtures[5].conflicts);
  assert.equal(bucket(query(fixtures, invs, {}, {}, fixtures.length).match[0]), "unconditioned");
});

test("flow uses only condition axis; conversion tolerance boundaries remain inclusive", () => {
  const base = runs[0];
  const fixtures: SlimRun[] = [
    { ...base, id: "condition", conditions: { flow_cm_s: { min: 10, max: 10, raw: "10" } } },
    { ...base, id: "outcome", conditions: { flow_setting_air: { min: 10, max: 10, raw: "10" } }, outcomes: [{ quantity: "spread_rate", source: 0, at: { flow_cm_s: 10 } }] },
  ];
  const r = query(fixtures, invs, { flow_cm_s: 10 }, {}, fixtures.length);
  assert.equal(r.match[0].run.id, "condition"); assert.equal(r.near[0].axes.flow_cm_s?.status, "not_reported");
  const s = { ...defaults(), pressure_kpa: "60", tol_pressure_kpa: "10", o2_pct: "" };
  const q = validate(s);
  const edge = [{ ...base, conditions: { pressure_atm: { min: 70 * ATM_PER_KPA, max: 70 * ATM_PER_KPA, raw: "70 kPa" } } }];
  assert.equal(query(edge, invs, q.q, q.tol).match.length, 1);
  const zero = decisionExport(fixtures, invs, assignments, { ...defaults("detection"), flow_cm_s: "20", tol_flow: "0" }, { generated_at: "fixture", sha256: "fixture" });
  assert.equal(zero.non_finite_distances[0].distance, "Infinity");
  assert.equal(JSON.parse(JSON.stringify(zero)).non_finite_distances[0].distance, "Infinity");
});

test("global relevance ordering, deterministic ties, unclassified alphabetic and BRE separation", () => {
  for (const s of [defaults(), defaults("detection")]) {
    const d = decide(runs, invs, assignments, s);
    const classes = d.rows.map(r => !r.mapping ? 2 : r.mapping.relevance === "direct" ? 0 : 1);
    assert.deepEqual(classes, [...classes].sort());
    const names = d.rows.filter(r => !r.mapping).map(r => r.investigation.name);
    assert.deepEqual(names, [...names].sort());
    assert.deepEqual(d.rows.map(r => r.investigation.id), decide([...runs].reverse(), [...invs].reverse(), assignments, s).rows.map(r => r.investigation.id));
  }
  const empty = decide([], invs, assignments, defaults());
  assert.deepEqual(empty.rows.filter(r => r.mapping?.relevance === "direct").map(r => r.investigation.id), ["bass", "bass-ii", "saffire-1", "saffire-2", "saffire-iv-vi"]);
  assert.equal(empty.rows.find(r => r.investigation.id === "acme-bre")!.mapping!.relevance, "indirect");
  assert.equal(invs.find(i => i.id === "acme-bre")!.geometry_class, "gaseous-flames");
  const base = runs.find(r => r.granularity === "test" && r.outcomes.some(o => r.sources[o.source]))!;
  const flowOnly = decide([
    { ...base, id: "in-window", investigation: "bass", conditions: { flow_cm_s: { min: 10, max: 10, raw: "10" } } },
    ...["outside-a", "outside-b"].map(id => ({ ...base, id, investigation: "bass-ii", conditions: { flow_cm_s: { min: 100, max: 100, raw: "100" } } })),
  ], invs, assignments, { ...defaults(), atmosphere: "0", flow_cm_s: "10" });
  assert.equal(flowOnly.rows[0].investigation.id, "bass-ii", "Without atmosphere, cited-outcome count precedes full count even with flow enabled");
});

test("suppression distinguishes report-only objectives from structured record fields", () => {
  const d = decide(runs, invs, assignments, defaults("suppression"));
  assert.ok(d.rows.find(r => r.investigation.id === "bass")!.mapping!.evidence!.some(e => e.kind === "report-only-agent"));
  assert.ok(d.rows.find(r => r.investigation.id === "flex")!.records.some(v => v.run.conditions.diluent));
  assert.ok(d.rows.find(r => r.investigation.id === "bass")!.mapping!.quote.includes("no suppression result"));
});

test("full gaseous export is complete, reproducible, preserves evidence payload and Explorer links", t => {
  const s = { ...defaults(), geometry_class: "gaseous-flames" }, dataset = { generated_at: "fixture", sha256: "fixture" };
  const start = performance.now(), out = decisionExport(runs, invs, assignments, s, dataset, "2026-11-02T00:00:00Z");
  const json = JSON.stringify(out), duration = performance.now() - start;
  const gasIds = new Set(invs.filter(i => i.geometry_class === "gaseous-flames").map(i => i.id));
  assert.equal(out.evidence.records.length, runs.filter(r => gasIds.has(r.investigation)).length);
  assert.equal(out.rows.reduce((n, r) => n + r.records.length, 0), out.evidence.records.length);
  assert.deepEqual(out, decisionExport(runs, invs, assignments, s, dataset, "2026-11-02T00:00:00Z"));
  const q = validate(s);
  assert.deepEqual(out.evidence, evidenceExport(runs, invs, q.q, q.tol, false, dataset));
  assert.equal(new Set([...out.evidence.records.map(v => v.run.id), ...out.categorical_excluded_ids]).size, runs.length);
  assert.equal(out.evidence.records.length + out.categorical_excluded_ids.length, runs.length);
  assert.ok(out.evidence.records.every(v => v.run.sources.length));
  const p = new URL(explorerLink(s, ["acme-bre:19070D1", "acme-bre:19070K1"]), "https://example.org").searchParams;
  assert.equal(p.getAll("compare").length, 2); assert.equal(Number(p.get("pressure_atm")), ATMOSPHERES.lunar.pressure_atm);
  const u = decisionExport(runs, invs, assignments, defaults("detection"), dataset);
  assert.equal(u.condition_state, "unconditioned"); assert.ok(u.rows.every(r => r.records.every(v => v.bucket === "unconditioned")));
  t.diagnostic(`Gaseous export: ${out.evidence.records.length} records, ${Buffer.byteLength(json)} bytes, ${duration.toFixed(1)} ms including serialization`);
});
