"use client";
import type { Investigation, SlimRun } from "@/lib/psi-types";
import { compareRuns, COMPARISON_VARIED_AXES } from "@/lib/psi-comparison";
import { CONDITION_LABEL, QUANTITY_LABEL, outcomeText, measureText } from "./format";
import type { Measure } from "@/lib/psi-types";

export function RunComparison({ records, investigations, dataset, onRemove, onInspect, selectedQuantity, setSelectedQuantity, varied, setVaried }: {
  records: SlimRun[]; investigations: Record<string, Investigation>;
  dataset: { generated_at: string; sha256: string }; onRemove: (id: string) => void; onInspect: (id: string) => void;
  selectedQuantity: string; setSelectedQuantity: (q: string) => void; varied: string; setVaried: (axis: string) => void;
}) {
  const quantities = [...new Set(records.flatMap(r => r.outcomes.map(o => o.quantity)))];
  const quantity = selectedQuantity || quantities[0] || "unreported";
  const assessment = records.length === 2 ? compareRuns(records[0], records[1], investigations, quantity, varied || null) : null;
  const download = () => {
    const blob = new Blob([JSON.stringify({ schema_version: 1, dataset, assessment, records }, null, 2)], { type: "application/json" });
    const url = URL.createObjectURL(blob); const a = document.createElement("a");
    a.href = url; a.download = "flame-freefall-comparison.json"; a.click(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  return <section className="min-w-0 rounded border border-border bg-card p-4 sm:p-5" aria-labelledby="comparison-heading">
    <h2 id="comparison-heading" className="font-display text-lg">Compare selected tests</h2>
    <p className="mt-1 text-sm text-muted-foreground">Select two tests. A shared geometry class alone does not establish comparability.</p>
    <ul className="mt-3 space-y-2">{records.map(r => <li key={r.id} className="flex flex-wrap items-center gap-2 text-sm">
      <button className="break-all text-primary underline" onClick={() => onInspect(r.id)}>{r.id}</button>
      <button className="rounded border px-2 py-1" onClick={() => onRemove(r.id)}>Remove <span className="sr-only">{r.id}</span></button>
    </li>)}</ul>
    {!assessment ? <p className="mt-3 text-sm">Open another test and add it to this comparison.</p> : <>
      <div className="mt-4 flex flex-wrap gap-3 text-sm">
        <label className="min-w-0 max-w-full">Outcome<select className="ml-2 min-w-0 max-w-full rounded border bg-background px-2 py-1" value={quantity} onChange={e => setSelectedQuantity(e.target.value)}>
          {!quantities.includes(quantity) && <option value={quantity}>{QUANTITY_LABEL[quantity] ?? quantity} (not reported)</option>}
          {quantities.map(q => <option key={q} value={q}>{QUANTITY_LABEL[q] ?? q}</option>)}
        </select></label>
        <label className="min-w-0 max-w-full">Intentionally varied condition<select className="ml-2 min-w-0 max-w-full rounded border bg-background px-2 py-1" value={varied} onChange={e => setVaried(e.target.value)}>
          <option value="">None</option>{varied && !COMPARISON_VARIED_AXES.includes(varied) && <option value={varied}>{varied} (unsupported)</option>}{COMPARISON_VARIED_AXES.map(k => <option key={k} value={k}>{CONDITION_LABEL[k] ?? k}</option>)}
        </select></label>
      </div>
      <p className="mt-4 border-l-2 border-primary bg-muted px-3 py-2 text-sm" role="status">
        {assessment.status === "insufficient_metadata" ? "Insufficient metadata for a condition-matched comparison." : assessment.status === "different_conditions"
          ? "Other conditions differ; this is not an isolated comparison." : assessment.status === "controlled_difference"
          ? "Reported metadata supports a descriptive comparison of the selected varied condition." : "Reported conditions match for a descriptive comparison."}
      </p>
      <div className="mt-3 overflow-x-auto"><table className="w-full min-w-[560px] text-sm">
        <caption className="sr-only">Condition, method, and outcome checks for selected tests</caption>
        <thead><tr className="border-b text-left"><th scope="col" className="p-2">Check</th><th scope="col" className="p-2">First test</th><th scope="col" className="p-2">Second test</th><th scope="col" className="p-2">Result</th></tr></thead>
        <tbody>{assessment.checks.map(c => <tr key={c.field} className="border-b align-top">
          <th scope="row" className="p-2 text-left font-medium">{CONDITION_LABEL[c.field] ?? QUANTITY_LABEL[c.field.replace("outcome:", "")] ?? c.field.replaceAll("_", " ")}</th>
          <td className="p-2">{c.left == null ? "not reported" : typeof c.left.value === "number" ? measureText(c.left as Measure) : c.left.raw}</td>
          <td className="p-2">{c.right == null ? "not reported" : typeof c.right.value === "number" ? measureText(c.right as Measure) : c.right.raw}</td>
          <td className="p-2">{c.status.replaceAll("-", " ")}</td>
        </tr>)}</tbody>
      </table></div>
      <div className="mt-3 grid gap-2 text-sm sm:grid-cols-2">{assessment.outcomes.map((o, i) => <p key={i}>{records[i].id}: {o ? outcomeText(o) : "No single unambiguous outcome at these settings"}</p>)}</div>
      <p className="mt-3 text-xs leading-5 text-muted-foreground">{assessment.limitations}</p>
      <button className="mt-3 rounded border px-3 py-2 text-sm" onClick={download}>Export comparison JSON</button>
    </>}
  </section>;
}
