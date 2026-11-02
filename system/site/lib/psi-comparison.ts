import type { Investigation, Measure, Outcome, SlimRun } from "./psi-types.ts";

export const COMPARISON_VERSION = "comparability-v2";
const BASE = ["fuel_family", "fuel", "gravity", "flow_direction", "apparatus", "confinement", "instrument", "measurement_method"];
const AXES: Record<string, string[]> = {
  "solid-fuel": ["o2_pct", "pressure_atm", "flow_cm_s", "fuel_form"],
  "droplet-combustion": ["o2_pct", "pressure_atm", "droplet_d0_mm"],
  "gaseous-flames": ["o2_pct", "pressure_atm", "fuel_flow_mg_s", "nozzle_diameter_mm", "flame_type"],
  "smoke-aerosol": ["flow_cm_s", "rt_r0", "duration_s", "net_aging_s"],
};
const DIMENSIONS = ["thickness_mm", "width_cm", "length_cm", "diameter_mm", "nozzle_diameter_mm", "fuel_fraction_pct", "oxidizer_stream_o2_pct", "duct_width_cm", "duct_height_cm", "duct_length_cm"];
const COMPOSITION = ["diluent", "n2_pct", "co2_pct", "he_pct", "ambient_fuel_pct", "oxidizer_flow_mg_s", "ambient_temperature_k"];
export const COMPARISON_VARIED_AXES = [...DIMENSIONS, "o2_pct", "pressure_atm", "flow_cm_s", "droplet_d0_mm", "fuel_flow_mg_s"];
type Value = { value: number | string | null; raw: string; unit?: string | null; uncertainty?: Measure["uncertainty"]; source?: number; quote?: string };
export type ComparisonCheck = { field: string; left: Value | null; right: Value | null; status: string };

function value(c: Record<string, unknown> | undefined): Value | null {
  if (!c) return null;
  const v = c.value;
  if (typeof v === "string") return { value: v, unit: null, raw: String(c.raw ?? v) };
  if (typeof v !== "number" || !Number.isFinite(v) || (c.min ?? v) !== (c.max ?? v) || c.detection_limit || (c.flags as string[] | undefined)?.some(f => ["multi", "source_definition_unresolved"].includes(f)))
    return { value: null, raw: String(c.raw ?? "not reported"), unit: (c.unit ?? null) as string | null };
  return { value: v as number, unit: (c.unit ?? null) as string | null, raw: String(c.raw ?? v),
    ...(c.uncertainty ? { uncertainty: c.uncertainty as Measure["uncertainty"] } : {}) };
}

function methodValue(run: SlimRun, outcome: Outcome | null, field: string): Value | null {
  const c = outcome?.metadata?.[field];
  if (!outcome?.metadata || !(field in outcome.metadata)) return value(run.conditions[field] as unknown as Record<string, unknown>);
  if (!c || !Number.isInteger(c.source) || c.source < 0 || typeof c.quote !== "string" || !c.quote.trim()) return null;
  const source = run.sources[c.source];
  const norm = (s: string) => s.replace(/\s+/g, " ").trim();
  if (!source || typeof source.quote !== "string" || !["report", "psi-workbook"].includes(source.kind) || !norm(source.quote).includes(norm(c.quote))) return null;
  const parsed = value(c as unknown as Record<string, unknown>);
  return parsed ? { ...parsed, source: c.source, quote: c.quote } : null;
}

export function compareRuns(left: SlimRun, right: SlimRun, investigations: Record<string, Investigation>, quantity: string, variedAxis: string | null = null) {
  const lc = left.conditions, rc = right.conditions;
  const selected = [left, right].map(r => { const matches = r.outcomes.filter(o => o.quantity === quantity); return matches.length === 1 ? matches[0] : null; });
  const lg = investigations[left.investigation].geometry_class, rg = investigations[right.investigation].geometry_class;
  const fields = [...new Set([...BASE, ...(AXES[lg] ?? []), ...(AXES[rg] ?? []), ...[...DIMENSIONS, ...COMPOSITION].filter(k => k in lc || k in rc)])];
  if (lg === "solid-fuel" && !fields.some(k => ["thickness_mm", "diameter_mm"].includes(k))) fields.push("thickness_mm");
  if (lg === "solid-fuel" || rg === "solid-fuel") {
    const forms = [lc, rc].map(c => String(c.fuel_form?.value ?? "").toLowerCase());
    for (const k of (forms.every(f => ["rod", "sphere"].includes(f)) ? ["diameter_mm"] : ["thickness_mm", "width_cm", "length_cm"]))
      if (!fields.includes(k)) fields.push(k);
  }
  const checks: ComparisonCheck[] = [];
  function check(field: string, a: Value | null, b: Value | null, conflict = false) {
    let status = conflict ? "source-conflict" : "unknown";
    if (!conflict && a?.value != null && b?.value != null) {
      const equal = typeof a.value === "string" && typeof b.value === "string" ? a.value.trim().toLowerCase() === b.value.trim().toLowerCase() : a.value === b.value;
      if (typeof a.value === "string" || field === "rt_r0" || field.startsWith("outcome_at:") || (a.unit && b.unit))
        status = equal && (a.unit ?? null) === (b.unit ?? null) ? "match" : "different";
      if (typeof a.value !== "string" && (a.unit ?? null) !== (b.unit ?? null)) status = "unknown";
    }
    checks.push({ field, left: a, right: b, status });
  }
  check("geometry_class", value({ value: lg }), value({ value: rg }));
  const granularity = (r: SlimRun) => ["test", "test-point"].includes(r.granularity) ? "individual" : r.granularity;
  check("record_type", value({ value: granularity(left) }), value({ value: granularity(right) }));
  const conflicts = new Set([...(left.conflicts ?? []), ...(right.conflicts ?? [])].map(c => c.field));
  for (const field of fields) check(field,
    ["instrument", "measurement_method"].includes(field) ? methodValue(left, selected[0], field) : value(lc[field] as unknown as Record<string, unknown>),
    ["instrument", "measurement_method"].includes(field) ? methodValue(right, selected[1], field) : value(rc[field] as unknown as Record<string, unknown>), conflicts.has(field));
  check(`outcome:${quantity}`, value(selected[0]?.measure as unknown as Record<string, unknown>), value(selected[1]?.measure as unknown as Record<string, unknown>), conflicts.has(`outcome:${quantity}`));
  for (const axis of [...new Set(selected.flatMap(o => Object.keys(o?.at ?? {})))].sort()) {
    check(`outcome_at:${axis}`, value({ value: (selected[0]?.at as Record<string, number> | undefined)?.[axis] }), value({ value: (selected[1]?.at as Record<string, number> | undefined)?.[axis] }));
  }
  const blockers = checks.filter(c => ["unknown", "source-conflict"].includes(c.status)).map(c => c.field);
  if (lg !== rg) blockers.push("geometry_class");
  if (left.id === right.id) blockers.push("same_record");
  if (variedAxis !== null && !COMPARISON_VARIED_AXES.includes(variedAxis)) blockers.push("invalid_varied_axis");
  const differences = checks.filter(c => c.status === "different" && !c.field.startsWith("outcome:")).map(c => c.field);
  if ([left, right].some(r => !["test", "test-point"].includes(r.granularity))) blockers.push("non_individual_record");
  if (selected[0]?.measure && selected[1]?.measure && (selected[0].measure.unit ?? null) !== (selected[1].measure.unit ?? null)) blockers.push("outcome_unit");
  const unexplained = differences.filter(f => f.replace(/^outcome_at:/, "") !== variedAxis);
  return { method_version: COMPARISON_VERSION, left_id: left.id, right_id: right.id, quantity, varied_axis: variedAxis, checks,
    unknown_or_conflicted: blockers, differences, can_compare: blockers.length === 0 && unexplained.length === 0,
    status: blockers.length ? "insufficient_metadata" : unexplained.length ? "different_conditions" : differences.length ? "controlled_difference" : "condition_matched",
    outcomes: selected as (Outcome | null)[], limitations: "Descriptive comparison only. Missing metadata blocks a condition-matched claim; reported ranges are not uncertainty intervals. No statistical-significance, predictive or safety claim." };
}

/** A useful research result even when equivalence cannot be established.
 * This audit preserves the strict comparison assessment: observing two sourced
 * outcomes is distinct from attributing their difference to one condition.
 */
export function comparisonAudit(left: SlimRun, right: SlimRun, investigations: Record<string, Investigation>, quantity: string, variedAxis: string | null = null) {
  const assessment = compareRuns(left, right, investigations, quantity, variedAxis);
  const setup = assessment.checks.filter(c => !c.field.startsWith("outcome:"));
  const shared = setup.filter(c => c.status === "match");
  const differences = setup.filter(c => c.status === "different");
  const missing = assessment.checks.filter(c => c.status === "unknown");
  const conflicts = assessment.checks.filter(c => c.status === "source-conflict");
  const sourcedOutcomes = [left, right].map((run, i) => {
    const outcome = assessment.outcomes[i];
    const source = outcome && Number.isInteger(outcome.source) ? run.sources?.[outcome.source] ?? null : null;
    return { run_id: run.id, outcome, source_index: outcome?.source ?? null, source };
  });
  const steps: { code: string; fields: string[]; text: string }[] = [];
  if (missing.length) steps.push({ code: "INSPECT_MISSING_METADATA", fields: missing.map(c => c.field), text: "Inspect the linked original sources for these missing or ambiguous fields. The source may not contain the value; do not fill it by inference." });
  if (conflicts.length) steps.push({ code: "REVIEW_RETAINED_CONFLICTS", fields: conflicts.map(c => c.field), text: "Inspect both retained source values before using the disputed field." });
  const unexplained = differences.filter(c => c.field.replace(/^outcome_at:/, "") !== variedAxis);
  if (unexplained.length) steps.push({ code: "MULTIPLE_SETUP_DIFFERENCES", fields: unexplained.map(c => c.field), text: "These recorded conditions differ beyond the nominated varied condition. Their effects cannot be isolated by this pair." });
  if (assessment.unknown_or_conflicted.some(f => ["geometry_class", "same_record", "non_individual_record", "invalid_varied_axis"].includes(f)))
    steps.push({ code: "REVIEW_SELECTION", fields: assessment.unknown_or_conflicted.filter(f => ["geometry_class", "same_record", "non_individual_record", "invalid_varied_axis"].includes(f)), text: "Choose distinct individual records in one geometry class and a supported varied condition before considering a matched comparison." });
  const bothSourced = sourcedOutcomes.every(o => o.outcome && o.source);
  if (!bothSourced) steps.push({ code: "INSPECT_OUTCOME_SOURCES", fields: [`outcome:${quantity}`], text: "One or both records lack a single selected outcome with a valid source index. Inspect the original records; no missing outcome or citation is supplied." });
  steps.push({ code: "DESCRIPTIVE_ONLY", fields: [], text: "Use this audit to explain shared evidence, setup differences and the remaining source checks. It does not estimate a treatment effect, statistical significance, material safety or gravity equivalence." });
  return { method_version: "comparison-audit-v1", assessment,
    research_result: bothSourced ? "Two source-linked outcomes are available for inspection. Shared facts and recorded differences are separated below; the strict comparability assessment still applies." : "The audit identifies recorded facts and the source checks needed before comparing the selected outcomes.",
    shared_facts: shared, recorded_differences: differences, missing_or_ambiguous: missing, conflicted_checks: conflicts,
    retained_conflicts: [left, right].flatMap(run => (run.conflicts ?? []).map(c => ({ run_id: run.id, ...c }))),
    sourced_outcomes: sourcedOutcomes, next_steps: steps,
    limitations: "An evidence audit is not a controlled experiment. Shared recorded fields do not establish equivalence; unrecorded details remain unknown. No subtraction, ratio, causal effect or safety ranking is inferred from this pair." };
}
