import type { Metadata } from "next";
import Link from "next/link";
import { Suspense, type ReactElement } from "react";

import { Explorer } from "@/components/explore/explorer";
import { GEOMETRY_LABEL } from "@/components/explore/format";
import { psiIngestReport, psiInvestigations } from "@/lib/psi-data";
import { basePath } from "@/lib/source";

export const metadata: Metadata = {
  title: "Test-data explorer",
  description:
    "Query every NASA PSI microgravity-combustion test by O₂, flow, pressure and material — matches, near misses and untested gaps, each cited to its PSI table line or NASA report.",
};

type Totals = {
  runs: number;
  by_granularity: Record<string, number>;
  investigations: number;
  runs_with_outcomes: number;
  runs_with_report_data: number;
  conflicts: number;
  rows_read: number;
};

type Completeness = { by_geometry: Record<string, {
  records: number;
  records_with_numeric_outcomes: number;
  records_with_source_processed_outcomes: number;
  conditions_reported_by: Record<"o2_pct" | "pressure_atm" | "flow_cm_s", number>;
}> };

export default function ExplorePage(): ReactElement {
  const investigations = psiInvestigations();
  const { totals, completeness } = psiIngestReport() as { totals: Totals; completeness: Completeness };
  const tests = (totals.by_granularity.test ?? 0) + (totals.by_granularity["test-point"] ?? 0);
  return (
    <>
      <section className="relative -mx-4 mb-8 overflow-hidden bg-muted/40 px-4 py-8 text-foreground sm:px-6 sm:py-10">
        <div className="pointer-events-none absolute inset-0 opacity-40" aria-hidden="true">
          <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.04)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.04)_1px,transparent_1px)] bg-[size:36px_36px] [mask-image:linear-gradient(to_right,black,transparent)]" />
          <div className="absolute -right-20 -top-36 size-96 rounded-full border border-slate-500/30" />
          <div className="absolute -right-8 -top-24 size-72 rounded-full border border-slate-500/20" />
        </div>
        <div className="relative mx-auto max-w-6xl">
        <p className="mb-2 flex items-center gap-2 text-sm font-medium text-primary"><span className="size-2 rounded-full bg-primary" /> PSI test-data explorer</p>
        <h1 className="max-w-3xl font-display text-3xl tracking-tight text-balance sm:text-5xl">Find the tests that can answer your question</h1>
        <p className="mt-2 max-w-3xl text-muted-foreground">
          {totals.investigations} NASA investigations, each published in its own table, format and units — indexed with original cells and source references.
          Search reported conditions, inspect incomplete or outside-window records, and identify gaps in this collection.
          Values and derived views come from deterministic processing; the interface does not establish absence of research beyond this index.
        </p>
        <dl className="mt-6 grid grid-cols-2 divide-x divide-y divide-border border-y border-border sm:grid-cols-3 lg:grid-cols-6 lg:divide-y-0">
          <Figure n={totals.investigations} label="investigations" />
          <Figure n={tests} label="individual tests & test points" />
          <Figure n={totals.runs - tests} label="daily summaries & planned envelopes" />
          <Figure n={totals.runs_with_outcomes} label="with recorded outcomes" />
          <Figure n={totals.runs_with_report_data} label="with NASA report evidence" />
          <Figure n={totals.conflicts} label="source disagreements, flagged not hidden" />
        </dl>
        </div>
      </section>
      <section className="mb-8 border-y border-border py-4" aria-labelledby="geometry-heading">
        <div className="flex flex-wrap items-end justify-between gap-2">
          <div>
            <h2 id="geometry-heading" className="font-display text-lg font-semibold">Browse by fuel geometry</h2>
            <p className="mt-1 text-sm text-muted-foreground">Start within an experiment family. Select a group to filter the test table.</p>
          </div>
          <p className="text-xs text-muted-foreground">Rows include summaries and planned records; they are not all independent tests.</p>
        </div>
        <div className="mt-3 grid grid-cols-2 gap-px border border-border bg-border sm:grid-cols-4">
          {Object.entries(GEOMETRY_LABEL).map(([geometry, label]) => {
            const group = investigations.filter((i) => i.geometry_class === geometry);
            const records = group.reduce((total, i) => total + i.runs, 0);
            return (
              <a
                key={geometry}
                href={`${basePath}/explore/?geometry_class=${encodeURIComponent(geometry)}`}
                className="group bg-background p-3 outline-none transition-colors hover:bg-muted/60 focus-visible:ring-2 focus-visible:ring-inset focus-visible:ring-ring sm:p-4"
              >
                <span className="block text-xs text-muted-foreground">{group.length} investigations</span>
                <span className="mt-1 block font-medium group-hover:text-primary">{label}</span>
                <span className="mt-1 block font-mono text-sm tabular-nums text-muted-foreground">{records.toLocaleString("en-US")} table records</span>
              </a>
            );
          })}
        </div>
      </section>
      <details className="mb-8 rounded border border-border bg-card">
        <summary className="cursor-pointer px-4 py-3 font-medium">Data completeness and processing</summary>
        <div className="border-t border-border px-4 py-4">
          <p className="max-w-3xl text-sm leading-6 text-muted-foreground">
            Counts below cover the whole index, including summaries and planned envelopes. Numeric outcomes include
            source-processed workbook results. Availability is not an accuracy or safety score; missing values remain unknown.
          </p>
          <div className="mt-4 overflow-x-auto">
            <table className="w-full min-w-[640px] text-sm">
              <caption className="sr-only">Records with numeric outcomes and reported conditions, by geometry class</caption>
              <thead><tr className="border-b border-border text-left">
                <th scope="col" className="py-2 pr-4">Geometry</th>
                <th scope="col" className="py-2 pr-4">Records</th>
                <th scope="col" className="py-2 pr-4">Numeric outcomes</th>
                <th scope="col" className="py-2 pr-4">Source processed</th>
                <th scope="col" className="py-2 pr-4">O₂ reported</th>
                <th scope="col" className="py-2 pr-4">Pressure reported</th>
                <th scope="col" className="py-2">Flow reported</th>
              </tr></thead>
              <tbody>{Object.entries(completeness.by_geometry).map(([geometry, row]) => (
                <tr key={geometry} className="border-b border-border last:border-0 tabular-nums">
                  <th scope="row" className="py-3 pr-4 text-left font-medium">{GEOMETRY_LABEL[geometry] ?? geometry}</th>
                  <td className="py-3 pr-4">{row.records.toLocaleString("en-US")}</td>
                  <td className="py-3 pr-4">{row.records_with_numeric_outcomes.toLocaleString("en-US")}</td>
                  <td className="py-3 pr-4">{row.records_with_source_processed_outcomes.toLocaleString("en-US")}</td>
                  <td className="py-3 pr-4">{row.conditions_reported_by.o2_pct.toLocaleString("en-US")}</td>
                  <td className="py-3 pr-4">{row.conditions_reported_by.pressure_atm.toLocaleString("en-US")}</td>
                  <td className="py-3">{row.conditions_reported_by.flow_cm_s.toLocaleString("en-US")}</td>
                </tr>
              ))}</tbody>
            </table>
          </div>
          <p className="mt-3 max-w-3xl text-xs leading-5 text-muted-foreground">
            Source-processed records are a subset of numeric-outcome records, not additional tests. Each count uses
            the Records column as its denominator. Open a test to inspect its source cells and processing notes.
          </p>
        </div>
      </details>
      <Suspense fallback={<p className="text-sm text-muted-foreground">Loading…</p>}>
        <Explorer investigations={investigations} basePath={basePath} />
      </Suspense>
    </>
  );
}

function Figure({ n, label }: { n: number; label: string }): ReactElement {
  return (
    <div className="px-3 py-3 sm:px-4">
      <dt className="text-xs leading-4 text-muted-foreground">{label}</dt>
      <dd className="mt-1 font-display text-2xl font-semibold tabular-nums text-foreground">{n.toLocaleString("en-US")}</dd>
    </div>
  );
}
