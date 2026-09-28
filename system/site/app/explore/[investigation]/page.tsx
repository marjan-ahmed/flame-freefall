import type { Metadata } from "next";
import Link from "next/link";
import { notFound } from "next/navigation";
import type { ReactElement } from "react";

import { conditionText, GEOMETRY_LABEL, outcomeText, QUANTITY_LABEL } from "@/components/explore/format";
import { psiIngestReport, psiInvestigations, runsFor } from "@/lib/psi-data";
import type { Condition } from "@/lib/psi-types";

type Params = { params: Promise<{ investigation: string }> };

export function generateStaticParams(): { investigation: string }[] {
  return psiInvestigations()
    .filter((i) => i.runs > 0)
    .map((i) => ({ investigation: i.id }));
}

export async function generateMetadata({ params }: Params): Promise<Metadata> {
  const { investigation } = await params;
  const inv = psiInvestigations().find((i) => i.id === investigation);
  return { title: inv ? `${inv.name} test records` : "Investigation" };
}

type FileReport = {
  file: string;
  investigation: string;
  rows_read: number;
  runs_emitted: number;
  merged_into_previous: number;
  skipped: { row: number; reason: string }[];
  notes: string[];
};

const COLS = ["o2_pct", "flow_cm_s", "pressure_atm", "fuel", "flow_direction"] as const;
const COL_LABEL: Record<(typeof COLS)[number], string> = {
  o2_pct: "O₂",
  flow_cm_s: "Flow",
  pressure_atm: "Pressure",
  fuel: "Fuel / material",
  flow_direction: "Direction",
};

/** "exact duplicate of row 12" and "exact duplicate of row 40" are one reason. */
function reasonKey(reason: string): string {
  return reason.replace(/ (at|of) row \d+/, "").replace(/Flex Number \d+/, "Flex Number …");
}

export default async function InvestigationPage({ params }: Params): Promise<ReactElement> {
  const { investigation } = await params;
  const inv = psiInvestigations().find((i) => i.id === investigation);
  if (!inv) notFound();
  const runs = runsFor(inv.id);
  const files = ((psiIngestReport() as { files: FileReport[] }).files ?? []).filter((f) => f.investigation === inv.id);
  const cols = COLS.filter((c) => runs.some((r) => r.conditions[c]));
  const topQ = Object.keys(inv.outcome_quantities).slice(0, 2);

  return (
    <>
      <p className="text-sm text-muted-foreground">
        <Link href="/explore/investigations/" className="hover:underline">
          Investigations
        </Link>{" "}
        · {GEOMETRY_LABEL[inv.geometry_class]}
      </p>
      <h1 className="mt-1 font-display text-3xl tracking-tight">{inv.name}</h1>
      {inv.full_name && <p className="text-muted-foreground">{inv.full_name}</p>}

      <div className="mt-4 grid gap-4 lg:grid-cols-3">
        <section className="rounded-xl border bg-card p-4 text-sm">
          <h2 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Sources</h2>
          {inv.psi_id && (
            <p className="mt-1">
              NASA Physical Sciences Informatics dataset <strong>{inv.psi_id}</strong>
            </p>
          )}
          {inv.citation?.url && (
            <p className="mt-1">
              <a href={inv.citation.url} className="text-primary underline underline-offset-2" target="_blank" rel="noreferrer">
                {inv.citation.title}
              </a>
            </p>
          )}
          {inv.citation?.doc && (
            <p className="mt-1 text-xs text-muted-foreground">
              Governed record:{" "}
              <Link href={`/docs/${inv.citation.doc.replace(/^knowledge\//, "")}/`} className="text-primary hover:underline">
                {inv.citation.doc_title ?? inv.citation.doc}
              </Link>
            </p>
          )}
          <Link
            href={`/explore/?investigation=${inv.id}`}
            className="mt-3 inline-block rounded-md bg-primary px-3 py-1.5 text-primary-foreground"
          >
            Query these tests
          </Link>
        </section>

        <section className="rounded-xl border bg-card p-4 text-sm">
          <h2 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">How the table was read</h2>
          {files.map((f) => {
            const reasons = new Map<string, number>();
            for (const s of f.skipped) reasons.set(reasonKey(s.reason), (reasons.get(reasonKey(s.reason)) ?? 0) + 1);
            return (
              <div key={f.file} className="mt-2">
                <p className="break-all font-mono text-xs">{f.file}</p>
                <p className="text-xs">
                  {f.rows_read} rows read → {f.runs_emitted} records
                  {f.merged_into_previous ? `, ${f.merged_into_previous} continuation rows merged` : ""}
                  {f.skipped.length ? `, ${f.skipped.length} skipped` : ""}
                </p>
                {reasons.size > 0 && (
                  <ul className="mt-1 list-disc pl-4 text-xs text-muted-foreground">
                    {[...reasons.entries()].map(([r, n]) => (
                      <li key={r}>
                        {r} ({n})
                      </li>
                    ))}
                  </ul>
                )}
                {f.notes.map((n) => (
                  <p key={n} className="mt-1 text-xs text-muted-foreground">
                    {n}
                  </p>
                ))}
              </div>
            );
          })}
          {!files.length && <p className="mt-1 text-xs text-muted-foreground">Report tables only; no PSI experimental table.</p>}
        </section>

        <section className="rounded-xl border bg-card p-4 text-sm">
          <h2 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">What the records carry</h2>
          <p className="mt-1">
            {inv.runs} records · {inv.runs_with_outcomes} with results · {inv.runs_with_report_data} cross-checked with a report
            {inv.conflicts ? ` · ${inv.conflicts} source disagreements` : ""}
          </p>
          <ul className="mt-2 space-y-0.5 text-xs">
            {Object.entries(inv.outcome_quantities).map(([q, n]) => (
              <li key={q}>
                {QUANTITY_LABEL[q] ?? q}: {n}
              </li>
            ))}
          </ul>
          {inv.table_notes.length > 0 && (
            <>
              <h3 className="mt-3 text-xs font-semibold uppercase tracking-wide text-muted-foreground">The table&apos;s own notes</h3>
              <ul className="mt-1 list-disc space-y-1 pl-4 text-xs">
                {inv.table_notes.map((n) => (
                  <li key={n}>{n}</li>
                ))}
              </ul>
            </>
          )}
        </section>
      </div>

      <section className="mt-6 rounded-xl border bg-card p-4">
        <h2 className="font-display text-lg">All {runs.length} records</h2>
        <div className="mt-3 overflow-x-auto">
          <table className="w-full min-w-[720px] text-xs">
            <thead>
              <tr className="border-b text-left uppercase tracking-wide text-muted-foreground">
                <th className="py-2 pr-3">Record</th>
                {cols.map((c) => (
                  <th key={c} className="py-2 pr-3">
                    {COL_LABEL[c]}
                  </th>
                ))}
                {topQ.map((q) => (
                  <th key={q} className="py-2 pr-3">
                    {QUANTITY_LABEL[q] ?? q}
                  </th>
                ))}
                <th className="py-2 pr-3">Source</th>
              </tr>
            </thead>
            <tbody>
              {runs.map((r) => (
                <tr key={r.id} className="border-b align-top last:border-0">
                  <td className="py-1.5 pr-3">
                    <Link
                      href={`/explore/?investigation=${inv.id}&run=${encodeURIComponent(r.id)}`}
                      className="font-mono text-primary hover:underline"
                    >
                      {r.label}
                    </Link>
                    {r.conflicts?.length ? <span className="ml-1 text-red-700 dark:text-red-400" title="sources disagree">⚠</span> : null}
                    {r.date && <span className="block text-muted-foreground">{r.date}</span>}
                  </td>
                  {cols.map((c) => (
                    <td key={c} className="py-1.5 pr-3">
                      {r.conditions[c] ? conditionText(r.conditions[c] as Condition) : <span className="text-muted-foreground">—</span>}
                    </td>
                  ))}
                  {topQ.map((q) => {
                    const os = r.outcomes.filter((o) => o.quantity === q);
                    return (
                      <td key={q} className="py-1.5 pr-3">
                        {os.length ? os.map((o) => outcomeText(o)).join("; ") : <span className="text-muted-foreground">—</span>}
                      </td>
                    );
                  })}
                  <td className="py-1.5 pr-3 text-muted-foreground">
                    {[...new Set(r.sources.map((s) => (s.kind === "report" ? s.table : s.row ? `${s.dataset} l.${s.row}` : s.dataset)))].join(
                      " · ",
                    )}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
        <p className="mt-2 text-xs text-muted-foreground">Open a record to see its source cells exactly as written.</p>
      </section>
    </>
  );
}
