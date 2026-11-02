"use client";
import type { Investigation, SlimRun } from "@/lib/psi-types";
import { comparisonAudit, COMPARISON_VARIED_AXES } from "@/lib/psi-comparison";
import { CONDITION_LABEL, QUANTITY_LABEL, outcomeText, measureText } from "./format";
import type { Measure } from "@/lib/psi-types";

export function RunComparison({ records, investigations, dataset, onRemove, onInspect, selectedQuantity, setSelectedQuantity, varied, setVaried }: {
  records: SlimRun[]; investigations: Record<string, Investigation>;
  dataset: { generated_at: string; sha256: string }; onRemove: (id: string) => void; onInspect: (id: string) => void;
  selectedQuantity: string; setSelectedQuantity: (q: string) => void; varied: string; setVaried: (axis: string) => void;
}) {
  const quantities = [...new Set(records.flatMap(r => r.outcomes.map(o => o.quantity)))];
  const quantity = selectedQuantity || quantities[0] || "unreported";
  const audit = records.length === 2 ? comparisonAudit(records[0], records[1], investigations, quantity, varied || null) : null;
  const assessment = audit?.assessment ?? null;
  const fieldLabel = (field: string) => CONDITION_LABEL[field] ?? QUANTITY_LABEL[field.replace("outcome:", "")] ?? field.replaceAll("_", " ");
  const download = () => {
    const blob = new Blob([JSON.stringify({ schema_version: 1, dataset, assessment, records, audit }, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob); const a = document.createElement("a");
    a.href = url; a.download = "flame-freefall-comparison.json"; a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return <section className="min-w-0 rounded border border-border bg-card p-4 sm:p-5" aria-labelledby="comparison-heading">
    <h2 id="comparison-heading" className="font-display text-lg">Compare selected tests</h2>
    <p className="mt-1 text-sm text-muted-foreground">Audit two records: inspect their source-linked outcomes, shared facts, setup differences and missing evidence. A shared geometry class alone does not establish comparability.</p>
    <ul className="mt-3 space-y-2">{records.map(r => <li key={r.id} className="flex flex-wrap items-center gap-2 text-sm">
      <button className="break-all text-primary underline" onClick={() => onInspect(r.id)}>{r.id}</button>
      <button className="rounded border px-2 py-1" onClick={() => onRemove(r.id)}>Remove <span className="sr-only">{r.id}</span></button>
    </li>)}</ul>
    {!assessment || !audit ? <p className="mt-3 text-sm">Open another test and add it to this comparison.</p> : <>
      <div className="mt-4 flex flex-wrap gap-3 text-sm">
        <label className="min-w-0 max-w-full">Outcome<select className="ml-2 min-w-0 max-w-full rounded border bg-background px-2 py-1" value={quantity} onChange={e => setSelectedQuantity(e.target.value)}>
          {!quantities.includes(quantity) && <option value={quantity}>{QUANTITY_LABEL[quantity] ?? quantity} (not reported)</option>}
          {quantities.map(q => <option key={q} value={q}>{QUANTITY_LABEL[q] ?? q}</option>)}
        </select></label>
        <label className="min-w-0 max-w-full">Intentionally varied condition<select className="ml-2 min-w-0 max-w-full rounded border bg-background px-2 py-1" value={varied} onChange={e => setVaried(e.target.value)}>
          <option value="">None</option>{varied && !COMPARISON_VARIED_AXES.includes(varied) && <option value={varied}>{varied} (unsupported)</option>}{COMPARISON_VARIED_AXES.map(k => <option key={k} value={k}>{CONDITION_LABEL[k] ?? k}</option>)}
        </select></label>
      </div>
      <h3 className="mt-5 font-medium">Comparison audit</h3>
      <p className="mt-2 text-sm">{audit.research_result}</p>
      <div className="mt-3 grid gap-4 sm:grid-cols-2">{audit.sourced_outcomes.map((entry, i) => <div key={entry.run_id} className="rounded border border-border p-3 text-sm">
        <p className="font-medium">{entry.run_id}</p>
        <p className="mt-2">{QUANTITY_LABEL[quantity] ?? quantity}: {entry.outcome ? outcomeText(entry.outcome) : "No single unambiguous outcome recorded"}</p>
        {Object.entries(entry.outcome?.metadata ?? {}).map(([field, meta]) => <details key={field} className="mt-2"><summary>{field.replaceAll("_", " ")}: {meta.value} (this outcome only)</summary><p>{meta.quote}</p><p>{meta.basis} · source index {meta.source}</p></details>)}
        {entry.outcome?.note && <p className="mt-2 text-xs leading-5 text-muted-foreground">{entry.outcome.note}</p>}
        <p className="mt-2">{entry.source ? <>{entry.source.url ? <a className="text-primary underline" href={entry.source.url}>Original outcome source</a> : <a className="text-primary underline" href={`#comparison-sources-${i}`}>Outcome source descriptor</a>} · source index {entry.source_index}{entry.source.table && ` · ${entry.source.table}`}{entry.source.line != null && ` · governed line ${entry.source.line}`}</> : "Outcome source not resolved; inspect the record before use."}</p>
      </div>)}</div>
      <div className="mt-4 grid gap-4 text-sm sm:grid-cols-2">
        {[
          { title: "Shared recorded facts", checks: audit.shared_facts },
          { title: "Recorded setup differences", checks: audit.recorded_differences },
          { title: "Missing or ambiguous fields", checks: audit.missing_or_ambiguous },
          { title: "Conflicted fields", checks: audit.conflicted_checks },
        ].map(({ title, checks }) => <div key={title}><h4 className="font-medium">{title}</h4><p className="mt-1 text-muted-foreground">{checks.length ? checks.map(c => fieldLabel(c.field)).join(", ") : "None identified in this audit."}</p></div>)}
      </div>
      <p className="mt-4 border-l-2 border-primary bg-muted px-3 py-2 text-sm" role="status">
        {assessment.status === "insufficient_metadata" ? "Insufficient metadata for a condition-matched comparison." : assessment.status === "different_conditions"
          ? "Other conditions differ; this is not an isolated comparison." : assessment.status === "controlled_difference"
          ? "Reported metadata supports a descriptive comparison of the selected varied condition." : "Reported conditions match for a descriptive comparison."}
      </p>
      <details className="mt-3"><summary className="cursor-pointer text-sm font-medium">Inspect every condition, method and outcome check</summary><div className="mt-3 overflow-x-auto"><table className="w-full min-w-[560px] text-sm">
        <caption className="sr-only">Condition, method, and outcome checks for selected tests</caption>
        <thead><tr className="border-b text-left"><th scope="col" className="p-2">Check</th><th scope="col" className="p-2">First test</th><th scope="col" className="p-2">Second test</th><th scope="col" className="p-2">Result</th></tr></thead>
        <tbody>{assessment.checks.map(c => <tr key={c.field} className="border-b align-top">
          <th scope="row" className="p-2 text-left font-medium">{CONDITION_LABEL[c.field] ?? QUANTITY_LABEL[c.field.replace("outcome:", "")] ?? c.field.replaceAll("_", " ")}</th>
          <td className="p-2">{c.left == null ? "not reported" : typeof c.left.value === "number" ? measureText(c.left as Measure) : c.left.raw}</td>
          <td className="p-2">{c.right == null ? "not reported" : typeof c.right.value === "number" ? measureText(c.right as Measure) : c.right.raw}</td>
          <td className="p-2">{c.status.replaceAll("-", " ")}</td>
        </tr>)}</tbody>
      </table></div></details>
      {audit.retained_conflicts.length > 0 && <div className="mt-4"><h3 className="font-medium">Retained source disagreements</h3><ul className="mt-2 space-y-2 text-sm">{audit.retained_conflicts.map((c, i) => <li key={i}>{c.run_id} · {fieldLabel(c.field)}: {c.values.map(v => `source ${v.source}: ${v.raw}`).join("; ")}</li>)}</ul></div>}
      <h3 className="mt-5 font-medium">What to do next</h3><ul className="mt-2 space-y-3 text-sm">{audit.next_steps.map(step => <li key={step.code}><p>{step.text}</p>{step.fields.length > 0 && <p className="mt-1 text-xs text-muted-foreground">Fields: {step.fields.map(fieldLabel).join(", ")}</p>}{["INSPECT_MISSING_METADATA", "REVIEW_RETAINED_CONFLICTS", "INSPECT_OUTCOME_SOURCES"].includes(step.code) && <a className="mt-1 inline-block text-primary underline" href="#comparison-original-sources">Inspect original sources</a>}</li>)}</ul>
      <details id="comparison-original-sources" className="mt-5"><summary className="cursor-pointer text-sm font-medium">Original sources and record inspection</summary><div className="mt-3 grid gap-4 text-sm sm:grid-cols-2">{records.map((run, i) => <div id={`comparison-sources-${i}`} key={run.id}><h4 className="font-medium">{run.id}</h4><button className="my-2 text-primary underline" onClick={() => onInspect(run.id)}>Inspect record and raw cells</button><ol start={0} className="list-decimal space-y-2 pl-5">{run.sources.map((source, sourceIndex) => <li key={sourceIndex} className="break-words">{source.url ? <a className="text-primary underline" href={source.url}>{source.title || source.url}</a> : source.descriptor || source.file || source.title || "Source descriptor unavailable"}{source.table && ` · ${source.table}`}{source.row != null && ` · row ${source.row}`}{source.sheet && ` · sheet ${source.sheet}`}{source.line != null && ` · governed line ${source.line}`}{source.scope && ` · ${source.scope}`}</li>)}</ol></div>)}</div></details>
      <p className="mt-3 text-xs leading-5 text-muted-foreground">{audit.limitations}</p>
      <p className="mt-3 text-xs leading-5 text-muted-foreground">{assessment.limitations}</p>
      <button className="mt-3 rounded border px-3 py-2 text-sm" onClick={download}>Export comparison JSON</button>
    </>}
  </section>;
}
