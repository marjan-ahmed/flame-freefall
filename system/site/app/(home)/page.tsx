import type { Metadata } from "next";
import type { ReactElement } from "react";
import Link from "next/link";

import { Heatmap, HeatmapLegend } from "@/components/dashboard/heatmap";
import { LunarEvidenceBrief } from "@/components/dashboard/lunar-evidence-brief";
import { ReadinessCards } from "@/components/dashboard/readiness-cards";
import { AudiencePathways } from "@/components/landing/audience-pathways";
import { FlameComparison } from "@/components/landing/flame-comparison";
import { Button } from "@/components/ui/button";
import {
  atmosphereMarkers,
  dashboardTotals,
  geometryHeatmaps,
  missionReadinessSummary,
  totalCoverageGaps,
} from "@/lib/dashboard-data";
import { lunarEvidenceBrief } from "@/lib/mission-evidence";
import { appDescription, appTitle } from "@/lib/shared";

const SITE_URL = "https://marjan-ahmed.github.io/flame-freefall/";

export const metadata: Metadata = {
  title: "Traceable NASA Combustion Evidence",
  description: appDescription ?? "A governed, citation-backed record of NASA microgravity combustion research and PSI test data.",
  keywords: [
    "NASA Space Apps 2026",
    "microgravity combustion",
    "spacecraft fire safety",
    "NASA-STD-6001B",
    "flame spread",
    "PSI archive",
    "AI research assistant",
  ],
  openGraph: {
    title: `${appTitle} — Traceable NASA Combustion Evidence`,
    description: "Explore NASA microgravity combustion investigations, PSI test data, and the conditions the evidence covers.",
    url: SITE_URL,
    siteName: appTitle,
    images: [{ url: "icon.png", width: 512, height: 512, alt: `${appTitle} icon` }],
    type: "website",
  },
  twitter: {
    card: "summary",
    title: `${appTitle} — Traceable NASA Combustion Evidence`,
    description: "A governed record of NASA microgravity combustion research, PSI test data, and its evidence limits.",
  },
};

export default function HomePage(): ReactElement {
  const totals = dashboardTotals();
  const heatmaps = geometryHeatmaps();
  const markers = atmosphereMarkers();
  const readiness = missionReadinessSummary();
  const totalGaps = totalCoverageGaps(heatmaps, readiness);

  return (
    <>
      <section className="dark relative isolate overflow-hidden bg-background text-foreground">
        <div className="absolute inset-0 -z-10 opacity-50" aria-hidden="true">
          <div className="absolute inset-0 bg-[radial-gradient(ellipse_at_78%_43%,rgba(29,78,216,0.22),transparent_42%)]" />
          <div className="absolute inset-0 bg-[linear-gradient(rgba(255,255,255,0.035)_1px,transparent_1px),linear-gradient(90deg,rgba(255,255,255,0.035)_1px,transparent_1px)] bg-[size:48px_48px] [mask-image:linear-gradient(to_bottom,black,transparent_88%)]" />
        </div>
        <div className="mx-auto grid max-w-6xl gap-10 px-4 pb-12 pt-14 sm:px-6 sm:pb-16 sm:pt-20 lg:grid-cols-[1.05fr_0.95fr] lg:items-center lg:gap-16 lg:pb-20 lg:pt-24">
          <div>
            <div className="flex items-center gap-3 text-xs font-medium text-slate-300">
              <span className="inline-block size-2 rounded-full bg-orange-400 shadow-[0_0_14px_rgba(251,146,60,.8)]" />
              <span>NASA PSI archive</span>
              <span className="text-slate-600">/</span>
              <span>Combustion research</span>
            </div>
            <h1 className="mt-6 max-w-2xl font-display text-4xl font-semibold leading-[1.04] tracking-tight text-balance sm:text-6xl">
              Fire behaves differently when there is no up.
            </h1>
            <p className="mt-6 max-w-xl text-base leading-7 text-slate-300 sm:text-lg">
              Explore the NASA investigations behind that change. Search their test conditions, inspect the source records,
              and see where the indexed evidence reaches.
            </p>
            <div className="mt-8 flex flex-wrap gap-3">
              <Button asChild size="lg" className="bg-orange-400 text-slate-950 hover:bg-orange-300">
                <Link href="/explore/">Open the test-data explorer</Link>
              </Button>
              <Button asChild size="lg" variant="outline" className="border-slate-600 bg-transparent text-slate-100 hover:bg-white/10 hover:text-white">
                <Link href="/chat/">Ask a research question</Link>
              </Button>
            </div>
            <p className="mt-5 text-xs text-slate-400">Every indexed value keeps a path to its PSI table line or NASA report.</p>
          </div>
          <div className="relative border border-white/10 bg-slate-950/30 px-2 py-6 sm:px-5">
            <div className="absolute left-0 top-0 h-8 w-px bg-orange-400" aria-hidden="true" />
            <div className="absolute left-0 top-0 h-px w-8 bg-orange-400" aria-hidden="true" />
            <p className="px-4 text-xs text-slate-400">A change in gravity changes the flame shape</p>
            <FlameComparison />
          </div>
        </div>
        <div className="border-t border-white/10">
          <dl className="mx-auto grid max-w-6xl grid-cols-2 divide-x divide-y divide-white/10 px-4 sm:grid-cols-3 sm:px-6 lg:grid-cols-6 lg:divide-y-0">
            <Metric n={totals.investigations} label="investigations" />
            <Metric n={totals.tests} label="individual tests & points" />
            <Metric n={totals.runs} label="total table records" />
            <Metric n={totals.withOutcomes} label="with recorded outcomes" />
            <Metric n={totals.reportConfirmed} label="report cross-checks" />
            <Metric n={totals.conflicts} label="source conflicts flagged" />
          </dl>
        </div>
      </section>

      <section className="mx-auto grid max-w-6xl gap-8 px-4 py-14 sm:px-6 sm:py-16 lg:grid-cols-[0.7fr_1.3fr] lg:gap-14">
        <div>
          <p className="text-sm font-medium text-primary">Choose your next move</p>
          <h2 className="mt-2 font-display text-3xl font-semibold tracking-tight">Three ways into the evidence</h2>
          <p className="mt-4 max-w-md leading-7 text-muted-foreground">
            Move from a question to a test record, or read the governed source material behind the data.
          </p>
        </div>
        <div className="grid divide-y divide-border border-y border-border sm:grid-cols-3 sm:divide-x sm:divide-y-0">
          <RouteLink href="/explore/" index="A" title="Search tests" text="Filter by atmosphere, flow, material, and geometry." />
          <RouteLink href="/chat/" index="B" title="Ask the copilot" text="Compare investigations and inspect evidence with citations." />
          <RouteLink href="/docs/" index="C" title="Read the record" text="Open governed investigation summaries and source notes." />
        </div>
      </section>

      <AudiencePathways />

      <section className="bg-slate-950 text-slate-100">
        <div className="mx-auto max-w-6xl px-4 py-14 sm:px-6 sm:py-16">
          <div className="grid gap-8 lg:grid-cols-[0.72fr_1.28fr] lg:items-end">
            <div>
              <p className="text-sm font-medium text-orange-300">Live PSI index</p>
              <h2 className="mt-2 font-display text-3xl font-semibold tracking-tight">Where the data reaches</h2>
            </div>
            <p className="max-w-2xl text-sm leading-6 text-slate-300">
              Cells count indexed individual tests or test points that report both axes. Empty cells describe this index;
              they do not establish that no research exists. Compare within one geometry class.
            </p>
          </div>
          {totalGaps.length > 0 && (
            <p className="mt-6 border-l-2 border-orange-400 bg-white/5 px-4 py-3 text-sm text-slate-200">
              {totalGaps.map((g) => g.label).join(" and ")}: no plottable O₂ and pressure pairs in the current index. Open the Explorer to inspect other reported conditions.
            </p>
          )}
          <div className="mt-8 border border-slate-700 bg-background p-4 text-foreground sm:p-6">
            <div className="flex flex-wrap items-center justify-between gap-2 border-b border-border pb-3">
              <h3 className="font-medium">Test coverage by oxygen and pressure</h3>
              <span className="font-mono text-[11px] text-muted-foreground">individual test records · indexed values</span>
            </div>
            <div className="grid gap-6 py-5 sm:grid-cols-2">
              {heatmaps.map((heatmap) => <Heatmap key={heatmap.geometryClass} heatmap={heatmap} markers={markers} />)}
            </div>
            <div className="border-t border-border pt-3"><HeatmapLegend /></div>
          </div>
          <h3 className="mt-10 font-display text-xl font-semibold">Mission atmosphere coverage</h3>
          <p className="mt-2 max-w-3xl text-sm leading-6 text-slate-300">
            These counts show indexed condition overlap only. They do not establish material safety, mission readiness,
            certification, or behavior in partial gravity.
          </p>
          <div className="mt-4"><ReadinessCards readiness={readiness} /></div>
        </div>
      </section>

      <LunarEvidenceBrief brief={lunarEvidenceBrief()} />

      <section className="mx-auto grid max-w-6xl gap-8 px-4 py-14 sm:px-6 sm:py-16 lg:grid-cols-[0.7fr_1.3fr]">
        <div>
          <p className="text-sm font-medium text-primary">A record you can audit</p>
          <h2 className="mt-2 font-display text-3xl font-semibold tracking-tight">Evidence before interpretation</h2>
          <p className="mt-4 max-w-md leading-7 text-muted-foreground">
            The interface keeps source disagreements, missing fields, and evidence limits visible so readers can inspect the record themselves.
          </p>
        </div>
        <ul className="divide-y divide-border border-y border-border">
          {[
            "Values remain connected to PSI rows and report tables.",
            "Unreported conditions stay unreported; the interface does not fill gaps by inference.",
            "Source disagreements retain both values and are flagged.",
            "Coverage means indexed overlap, not a safety conclusion.",
          ].map((item) => <li key={item} className="py-3 text-sm text-muted-foreground">{item}</li>)}
        </ul>
      </section>
    </>
  );
}

function Metric({ n, label }: { n: number; label: string }): ReactElement {
  return (
    <div className="px-3 py-4 sm:px-4">
      <dt className="text-xs leading-4 text-slate-400">{label}</dt>
      <dd className="mt-1 font-display text-2xl font-semibold tabular-nums text-white">{n.toLocaleString("en-US")}</dd>
    </div>
  );
}

function RouteLink({ href, index, title, text }: { href: string; index: string; title: string; text: string }): ReactElement {
  return (
    <Link href={href} className="group px-4 py-4 outline-none transition-colors hover:bg-muted/40 focus-visible:bg-muted/40 sm:px-5">
      <span className="font-mono text-xs text-primary">{index}</span>
      <span className="mt-3 block font-display text-lg font-semibold group-hover:text-primary">{title}</span>
      <span className="mt-1 block text-sm leading-5 text-muted-foreground">{text}</span>
    </Link>
  );
}
