import type { Metadata } from "next";
import { Suspense, type ReactElement } from "react";

import { Explorer } from "@/components/explore/explorer";
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
      <section className="mb-6">
        <h1 className="font-display text-3xl tracking-tight sm:text-4xl">Every microgravity fire test, one question away</h1>
        <p className="mt-2 max-w-3xl text-muted-foreground">
          {totals.investigations} NASA investigations, each published in its own table, format and units — normalized into one record per
          test, with the original cell kept beside every value. Ask for a set of conditions and get the tests run there, the tests that come
          close, and what nobody has tested yet. Nothing on this page is generated: every number traces to a PSI table line or a NASA report.
        </p>
        <dl className="mt-4 grid grid-cols-2 gap-3 sm:grid-cols-3 lg:grid-cols-6">
          <Figure n={totals.investigations} label="investigations" />
          <Figure n={tests} label="individual tests & test points" />
          <Figure n={totals.runs - tests} label="daily summaries & planned envelopes" />
          <Figure n={totals.runs_with_outcomes} label="with measured results" />
          <Figure n={totals.runs_with_report_data} label="cross-checked against a NASA report" />
          <Figure n={totals.conflicts} label="source disagreements, flagged not hidden" />
        </dl>
      </section>
      <Suspense fallback={<p className="text-sm text-muted-foreground">Loading…</p>}>
        <Explorer investigations={investigations} basePath={basePath} />
      </Suspense>
    </>
  );
}

function Figure({ n, label }: { n: number; label: string }): ReactElement {
  return (
    <div className="rounded-lg border bg-card p-3">
      <dt className="text-xs text-muted-foreground">{label}</dt>
      <dd className="font-display text-2xl">{n.toLocaleString("en-US")}</dd>
    </div>
  );
}
