import { ATMOSPHERES, ATM_PER_KPA } from "./psi-atmospheres.ts";
import { query, type Query, type RunView } from "./psi-query.ts";
import { evidenceExport, evidenceParams, individualRuns, type Tolerances } from "./evidence-method.ts";
import type { Investigation, SlimRun } from "./psi-types.ts";
import { observationRelationshipSummary } from "./observation-relationships.ts";

export type Job = "prevention" | "detection" | "suppression";
export type Assignment = { investigation: string; job: Job; relevance: "direct" | "indirect"; doc: string; quote: string; rationale?: string; checked_by: string; checked_at: string; evidence?: { kind: "instrument" | "report-only-agent"; quote: string }[] };
export const ORDERING = "Implement direct before indirect; within each class use descending full count, partial count and individual records with cited outcomes, then ascending ID. With no atmosphere constraints, omit the first two sort keys. Keep unclassified investigations alphabetic and publication-only evidence separate and unranked.";
export const LIMITATIONS = "Internal review only. Sparse pressure coverage and missing atmosphere metadata limit matching. No safety or gravity-equivalence validation. Coverage does not establish safety, certification or suitability. Indexed observations are not necessarily independent experimental replicates. Compare outcomes only within one geometry class.";
export const CONVERSION = "Preset pressures retain the existing four-decimal-atmosphere stored values. Custom pressure and pressure tolerances in kPa multiply by ATM_PER_KPA = 1 / 101.325 without additional rounding. Flow tolerances are relative fractions (at zero target, absolute cm/s), as in query(). Outcome-at-flow values and control settings never supply the condition axis.";
export const fields = ["o2_pct", "pressure_kpa", "flow_cm_s", "tol_o2", "tol_pressure_kpa", "tol_flow", "fuel_family", "geometry_class", "question", "shortlist", "quantity"] as const;
export type State = Record<typeof fields[number], string> & { job: string; scenario: string; atmosphere: string; browse: string };
export function defaults(job = "prevention", scenario = "lunar"): State {
  const a = ATMOSPHERES[scenario];
  return { job, scenario, atmosphere: job === "detection" ? "0" : "1", browse: job === "detection" ? "1" : "0",
    o2_pct: a ? String(a.o2_pct) : "", pressure_kpa: a ? String(parseFloat(a.pressure_source_value)) : "", flow_cm_s: "",
    tol_o2: "1.5", tol_pressure_kpa: String(0.1 / ATM_PER_KPA), tol_flow: "0.3", fuel_family: "", geometry_class: "", question: "", shortlist: "", quantity: "" };
}
export function restore(p: URLSearchParams): State {
  const s = defaults(p.get("job") ?? "prevention", p.get("scenario") ?? "lunar");
  for (const k of Object.keys(s) as (keyof State)[]) if (p.has(k)) s[k] = p.get(k)!;
  return s;
}
export function stateParams(s: State) { return new URLSearchParams(Object.entries(s)); }
export function validate(s: State) {
  const errors: Partial<Record<keyof State, string>> = {};
  if (s.question.length > 1200) errors.question = "Keep the research question within 1200 characters.";
  if (!["prevention", "detection", "suppression"].includes(s.job)) errors.job = "Choose a research job.";
  if (!["iss", "gateway", "lunar", "rover", "spacesuit", "mars", "custom"].includes(s.scenario)) errors.scenario = "Choose a scenario.";
  if (s.geometry_class && !["solid-fuel", "droplet-combustion", "gaseous-flames", "smoke-aerosol"].includes(s.geometry_class)) errors.geometry_class = "Choose an indexed geometry.";
  for (const k of ["atmosphere", "browse"] as const) if (!["0", "1"].includes(s[k])) errors[k] = "Choose yes or no.";
  const q: Query = {}, tol: Tolerances = {};
  const parse = (k: keyof State, max = Infinity, positive = false) => {
    if (!s[k].trim()) return undefined;
    const n = Number(s[k]);
    if (!Number.isFinite(n) || n < 0 || n > max || (positive && n === 0)) { errors[k] = `Enter a finite ${positive ? "positive" : "non-negative"} number${max < Infinity ? ` no greater than ${max}` : ""}.`; return undefined; }
    return n;
  };
  const o = parse("o2_pct", 100), p = parse("pressure_kpa", Infinity, true), f = parse("flow_cm_s");
  const ot = parse("tol_o2", 100), pt = parse("tol_pressure_kpa"), ft = parse("tol_flow");
  if (s.atmosphere === "1") {
    if (o !== undefined) q.o2_pct = o;
    if (p !== undefined) {
      const a = ATMOSPHERES[s.scenario];
      // Preserve preset rounding only while the displayed value remains unchanged.
      q.pressure_atm = a && s.pressure_kpa === String(parseFloat(a.pressure_source_value)) ? a.pressure_atm : p * ATM_PER_KPA;
    }
  }
  if (f !== undefined) q.flow_cm_s = f;
  if (ot !== undefined) tol.o2_pct = ot;
  if (pt !== undefined) tol.pressure_atm = pt * ATM_PER_KPA;
  if (ft !== undefined) tol.flow_cm_s = ft;
  if (s.fuel_family.trim()) q.fuel_family = s.fuel_family.trim();
  if (s.geometry_class) q.geometry_class = s.geometry_class;
  const conditioned = [q.o2_pct, q.pressure_atm, q.flow_cm_s].some(n => n !== undefined);
  if (!conditioned && s.browse !== "1") errors.browse = "Enter conditions or explicitly choose unconstrained browsing.";
  return { errors, q, tol, conditioned };
}
export type Bucket = "full" | "partial" | "outside-only" | "outside-plus-missing" | "none-reported" | "unconditioned";
export function bucket(v: RunView): Bucket {
  const a = Object.values(v.axes);
  if (!a.length) return "unconditioned";
  const missing = a.filter(x => x.status === "not_reported").length;
  if (missing === a.length) return "none-reported";
  if (a.some(x => x.status === "outside")) return missing ? "outside-plus-missing" : "outside-only";
  return missing ? "partial" : "full";
}
export function decide(runs: SlimRun[], invs: Investigation[], assignments: Assignment[], s: State) {
  const input = validate(s);
  if (Object.keys(input.errors).length) throw new Error("Invalid decision inputs");
  const result = query(runs, invs, input.q, input.tol, runs.length);
  const views = [...result.match, ...result.partial, ...result.near];
  const accepted = new Set(views.map(v => v.run.id));
  const hasNumeric = (r: SlimRun, k: string) => typeof (r.conditions[k] as { min?: unknown } | undefined)?.min === "number";
  const rows = invs.filter(i => !s.geometry_class || i.geometry_class === s.geometry_class).map(i => {
    const records = views.filter(v => v.run.investigation === i.id).map(v => ({ ...v, bucket: bucket(v) }));
    const individual = records.filter(v => ["test", "test-point"].includes(v.run.granularity));
    const mapping = assignments.find(a => a.investigation === i.id && a.job === s.job);
    const counts = Object.fromEntries((["full", "partial", "outside-only", "outside-plus-missing", "none-reported", "unconditioned"] as Bucket[]).map(b => [b, individual.filter(v => v.bucket === b).length])) as Record<Bucket, number>;
    const missing = Object.fromEntries(["o2_pct", "pressure_atm", "flow_cm_s"].map(k => [k, individual.filter(v => !hasNumeric(v.run, k)).length]));
    return { investigation: i, mapping, tags: assignments.filter(a => a.investigation === i.id).map(a => a.job), records, counts, missing,
      individual: individual.length, nonIndividual: records.length - individual.length,
      citedOutcomes: individual.filter(v => v.run.outcomes.some(o => (!s.quantity || o.quantity === s.quantity) && !!v.run.sources[o.source])).length,
      measurements: [...new Set(individual.flatMap(v => v.run.outcomes.map(o => o.quantity)))].sort(),
      observation_relationships: observationRelationshipSummary(individual.map(v => v.run)),
      controlOnly: individual.filter(v => !hasNumeric(v.run, "flow_cm_s") && Object.keys(v.run.conditions).some(k => k.startsWith("flow_setting"))).length,
      conflicts: records.filter(v => v.run.conflicts?.length).length };
  });
  const cmp = (a: string, b: string) => a < b ? -1 : a > b ? 1 : 0;
  rows.sort((a, b) => {
    const cls = (r: typeof a) => r.mapping ? r.mapping.relevance === "direct" ? 0 : 1 : 2;
    if (cls(a) !== cls(b)) return cls(a) - cls(b);
    if (!a.mapping) return cmp(a.investigation.name, b.investigation.name) || cmp(a.investigation.id, b.investigation.id);
    const atmosphereConstrained = input.q.o2_pct !== undefined || input.q.pressure_atm !== undefined;
    return (atmosphereConstrained ? b.counts.full - a.counts.full || b.counts.partial - a.counts.partial : 0) || b.citedOutcomes - a.citedOutcomes || cmp(a.investigation.id, b.investigation.id);
  });
  return { ...input, rows, relaxed: result.relaxed, categoricalExcludedIds: runs.filter(r => !accepted.has(r.id)).map(r => r.id) };
}
export function explorerLink(s: State, ids: string[]) {
  const { q, tol } = validate(s), p = evidenceParams(q, tol, false);
  if (ids.length === 1) p.set("run", ids[0]);
  else ids.slice(0, 2).forEach(id => p.append("compare", id));
  return `/explore/?${p}`;
}

/** Availability sensitivity only: no physical equivalence or outcome pooling. */
export function sensitivity(runs: SlimRun[], invs: Investigation[], assignments: Assignment[], s: State) {
  const input = validate(s);
  if (Object.keys(input.errors).length) return [];
  const selected = new Set(s.shortlist.split(",").filter(Boolean));
  const windows = [{ label: "Current window", state: s },
    ...(input.q.pressure_atm === undefined ? [] : [{ label: "Half pressure tolerance", state: { ...s, tol_pressure_kpa: String((input.tol.pressure_atm ?? 0.1) / ATM_PER_KPA / 2) } }]),
    ...(input.q.o2_pct === undefined ? [] : [{ label: "Double oxygen tolerance", state: { ...s, tol_o2: String(Math.min(100, (input.tol.o2_pct ?? 1.5) * 2)) } }])];
  return windows.map(w => ({ label: w.label, query: validate(w.state).q, tolerances: validate(w.state).tol,
    investigations: decide(runs, invs, assignments, w.state).rows.filter(r => selected.size ? selected.has(r.investigation.id) : r.mapping).map(r => ({ id: r.investigation.id, geometry: r.investigation.geometry_class, full: r.counts.full, incomplete: r.counts.partial })) }));
}

export function dossier(runs: SlimRun[], invs: Investigation[], assignments: Assignment[], s: State) {
  const d = decide(runs, invs, assignments, s);
  const ids = [...new Set(s.shortlist.split(",").filter(Boolean))].sort();
  const unknown = ids.filter(id => !invs.some(i => i.id === id));
  const excluded = ids.filter(id => !d.rows.some(r => r.investigation.id === id));
  return { question: s.question.trim() || "Research question not supplied", measurement: s.quantity || "All recorded outcomes", selected_ids: ids,
    selection_warnings: [...unknown.map(id => `Unknown investigation: ${id}`), ...excluded.filter(id => !unknown.includes(id)).map(id => `Outside the geometry filter: ${id}`)],
    entries: d.rows.filter(r => ids.includes(r.investigation.id)).map(r => ({ id: r.investigation.id, name: r.investigation.name, geometry: r.investigation.geometry_class,
      classification: r.mapping ?? null, buckets: r.counts, missing: r.missing, conflicts: r.conflicts, measurement_records: r.citedOutcomes,
      record_ids: r.records.map(v => v.run.id), observation_relationships: r.observation_relationships,
      next_steps: [
        ...(!r.mapping ? [{ code: "UNCLASSIFIED", text: "Inspect the investigation objective before asserting relevance to this job." }] : []),
        ...(r.conflicts ? [{ code: "SOURCE_CONFLICT", text: "Inspect both retained source values before quantitative use." }] : []),
        ...(Object.values(r.missing).some(n => n > 0) ? [{ code: "MISSING_CONDITIONS", text: "Inspect linked sources for missing conditions; do not infer values from apparatus capability or a different test." }] : []),
        ...(r.counts["outside-only"] + r.counts["outside-plus-missing"] > 0 ? [{ code: "OUTSIDE_WINDOW", text: "Inspect original conditions and sensitivity before choosing comparison candidates. Widening a search does not change an experiment." }] : []),
        ...(s.quantity && !r.citedOutcomes ? [{ code: "MEASUREMENT_GAP", text: "The selected measurement has no cited individual outcomes in this selection; inspect the publication separately." }] : []),
        ...(r.investigation.id === "acme-bre" ? [{ code: "EMULATOR", text: "Emulator, not a solid sample. Inspect the emulation assumptions before transfer to real materials." }] : []),
        { code: "COMPARISON_AUDIT", text: "Audit fuel, specimen, apparatus, instrument, method and outcome conditions before a condition-matched claim." },
      ] })) };
}
export function decisionExport(runs: SlimRun[], invs: Investigation[], assignments: Assignment[], s: State,
  dataset: { generated_at: string; sha256: string }, generatedAt = new Date().toISOString()) {
  const d = decide(runs, invs, assignments, s);
  return { schema: "fire-safety-decision", schema_version: 2, method_version: "decision-dossier-v2", generated_at: generatedAt,
    review: "internal review only", limitations: LIMITATIONS, conversion_policy: CONVERSION, state: s,
    condition_state: d.conditioned ? "conditioned" : "unconditioned", ordering: ORDERING,
    ordered_ids: d.rows.map(r => r.investigation.id), classification_version: 1, classification: assignments, rows: d.rows,
    dossier: dossier(runs, invs, assignments, s), sensitivity: sensitivity(runs, invs, assignments, s),
    independent_review: { status: "not_reviewed", reviewer: null, reviewed_at: null, source_checks: null, unsupported_inferences: null, task_completion_seconds: null,
      instructions: "A researcher should independently check source applicability, missing conditions, interpretation and next steps. Blank fields are not an approval or a passing result." },
    non_finite_distances: d.rows.flatMap(r => r.records.flatMap(v => Object.entries(v.axes).flatMap(([axis, a]) => a.status !== "not_reported" && !Number.isFinite(a.distance) ? [{ run_id: v.run.id, axis, distance: String(a.distance), reason: "Nonzero difference with zero tolerance; JSON numeric distance is null." }] : []))),
    categorical_excluded_ids: d.categoricalExcludedIds, relaxed: d.relaxed,
    publication_only: ["knowledge/literature/luci-rotating-rocket", "knowledge/literature/daft-cabin-aerosol", "knowledge/investigations/droplet-combustion/flex-2-cool-flame-results"],
    evidence: evidenceExport(runs, invs, d.q, d.tol, false, dataset) };
}
