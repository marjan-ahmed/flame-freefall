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

export default function ExplorePage(): ReactElement {
  const investigations = psiInvestigations();
  const totals = (psiIngestReport() as { totals: Totals }).totals;
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
          {totals.investigations} NASA investigations, each published in its own table, format and units — normalized into one record per
          test, with the original cell kept beside every value. Ask for a set of conditions and get the tests run there, the tests that come
          close, and what nobody has tested yet. Nothing on this page is generated: every number traces to a PSI table line or a NASA report.
        </p>
        <dl className="mt-6 grid grid-cols-2 divide-x divide-y divide-border border-y border-border sm:grid-cols-3 lg:grid-cols-6 lg:divide-y-0">
          <Figure n={totals.investigations} label="investigations" />
          <Figure n={tests} label="individual tests & test points" />
          <Figure n={totals.runs - tests} label="daily summaries & planned envelopes" />
          <Figure n={totals.runs_with_outcomes} label="with measured results" />
          <Figure n={totals.runs_with_report_data} label="cross-checked against a NASA report" />
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
