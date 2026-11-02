import { ExperimentAtlas } from "@/components/landing/experiment-atlas";
import { psiInvestigations } from "@/lib/psi-data";
import type { Metadata } from "next";
import type { ReactElement } from "react";

import { Heatmap, HeatmapLegend } from "@/components/dashboard/heatmap";
import { LunarEvidenceBrief } from "@/components/dashboard/lunar-evidence-brief";
import { ReadinessCards } from "@/components/dashboard/readiness-cards";
import {
  atmosphereMarkers,
  geometryHeatmaps,
  missionReadinessSummary,
  totalCoverageGaps,
} from "@/lib/dashboard-data";
import { lunarEvidenceBrief } from "@/lib/mission-evidence";
import { appDescription, appTitle } from "@/lib/shared";
import { source } from "@/lib/source";
import { psiGeneratedAt, slimRuns } from "@/lib/psi-data";
import Link from "next/link";

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
  const heatmaps = geometryHeatmaps();
  const markers = atmosphereMarkers();
  const readiness = missionReadinessSummary();
  const totalGaps = totalCoverageGaps(heatmaps, readiness);
  const records = slimRuns();
  const outcomes = records.filter(r => r.outcomes.length > 0).length;
  const literature = [
    ["literature", "luci-rotating-rocket"],
    ["literature", "daft-cabin-aerosol"],
    ["investigations", "droplet-combustion", "flex-2-cool-flame-results"],
  ].flatMap(slug => { const page = source.getPage(slug); return page ? [page] : []; });

  return (
    <>
      <ExperimentAtlas investigations={psiInvestigations()} />

      <section className="mx-auto max-w-6xl border-y border-border px-4 py-10 sm:px-6" aria-labelledby="evidence-update-heading">
        <h2 id="evidence-update-heading" className="font-display text-2xl font-semibold">The current evidence record</h2>
        <p className="mt-3 max-w-3xl text-sm leading-6 text-muted-foreground">
          {records.length.toLocaleString("en-US")} indexed records; {outcomes.toLocaleString("en-US")} with recorded outcomes.
          Counts include planned envelopes and summaries, and measure availability rather than accuracy or safety.
          Dataset generated {new Date(psiGeneratedAt()).toISOString().slice(0, 10)}.
        </p>
        <div className="mt-4 flex flex-wrap gap-x-6 gap-y-3 text-sm">
          <Link className="text-primary underline" href="/decide/">Find relevant evidence</Link>
          <Link className="text-primary underline" href="/explore/?compare=saffire-iv-vi%3AVI-3&compare=saffire-iv-vi%3AVI-4&compare_quantity=max_temp_sfu_outlet">Worked audit: two SAFFIRE PMMA records</Link>
          <Link className="text-primary underline" href="/explore/?investigation=saffire-iv-vi&run=saffire-iv-vi%3AVI-3">Inspect SAFFIRE temperature, gas and smoke-threshold evidence</Link>
          <Link className="text-primary underline" href="/explore/?investigation=flex-2">Inspect FLEX-2 fuel envelopes and literature outcomes</Link>
        </div>
        {literature.length > 0 && <>
          <h3 className="mt-7 font-medium">Published literature beyond PSI test rows</h3>
          <p className="mt-2 text-sm text-muted-foreground">Campaign observations and rotating-platform results remain distinct from individual PSI tests.</p>
          <ul className="mt-4 grid gap-4 md:grid-cols-3">{literature.map(page => <li key={page.url} className="min-w-0 border-l-2 border-primary pl-4">
            <Link className="text-sm font-medium text-primary underline" href={page.url}>{page.data.title}</Link>
            <p className="mt-2 text-sm leading-6 text-muted-foreground">{page.data.description}</p>
          </li>)}</ul>
        </>}
      </section>

      <section className="bg-muted/40 text-foreground">
        <div className="mx-auto max-w-6xl px-4 py-14 sm:px-6 sm:py-16">
          <div className="grid gap-8 lg:grid-cols-[0.72fr_1.28fr] lg:items-end">
            <div>
              <p className="text-sm text-muted-foreground">Evidence coverage</p>
              <h2 className="mt-2 font-display text-3xl font-semibold tracking-tight">Where the data reaches</h2>
            </div>
            <p className="max-w-2xl text-sm leading-6 text-muted-foreground">
              Cells count indexed individual tests or test points that report both axes. Empty cells describe this index;
              they do not establish that no research exists. Compare within one geometry class.
            </p>
          </div>
          {totalGaps.length > 0 && (
            <p className="mt-6 border-l-2 border-primary bg-white/5 px-4 py-3 text-sm text-muted-foreground">
              {totalGaps.map((g) => g.label).join(" and ")}: no plottable O₂ and pressure pairs in the current index. Open the Explorer to inspect other reported conditions.
            </p>
          )}
          <div className="flame-blue-panel mt-8 border bg-background p-4 text-foreground sm:p-6">
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
          <p className="mt-2 max-w-3xl text-sm leading-6 text-muted-foreground">
            These counts show indexed condition overlap only. They do not establish material safety, mission readiness,
            certification, or behavior in partial gravity.
          </p>
          <div className="mt-4"><ReadinessCards readiness={readiness} /></div>
        </div>
      </section>

      <details className="research-detail">
        <summary>Case study: evidence near a proposed Lunar atmosphere<span>Inspect search windows, source records, and limitations</span></summary>
        <LunarEvidenceBrief brief={lunarEvidenceBrief()} />
      </details>

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
