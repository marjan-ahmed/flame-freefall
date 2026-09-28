import type { ReactElement } from "react";

import type { Metadata } from "next";
import Link from "next/link";

import { FlameComparison } from "@/components/landing/flame-comparison";
import { Heatmap, HeatmapLegend } from "@/components/dashboard/heatmap";
import { ReadinessCards } from "@/components/dashboard/readiness-cards";
import { Button } from "@/components/ui/button";
import {
  atmosphereMarkers,
  dashboardTotals,
  geometryHeatmaps,
  missionReadinessSummary,
  totalCoverageGaps,
} from "@/lib/dashboard-data";
import { appDescription, appTitle } from "@/lib/shared";

const SITE_URL = "https://marjan-ahmed.github.io/flame-freefall/";

export const metadata: Metadata = {
  title: "AI-Powered Fire Safety Insights from Microgravity Combustion",
  description:
    "A governed, citation-backed record of NASA's microgravity combustion research, an AI assistant that answers only " +
    "from it, and a live dashboard showing exactly where 1,948 PSI test records do — and don't — cover the atmospheres " +
    "proposed for the ISS, the Lunar Gateway and a Lunar surface habitat.",
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
    title: "Flame in Freefall — AI-Powered Fire Safety Insights from Microgravity Combustion",
    description:
      "Where NASA's microgravity combustion data reaches, and where it doesn't — cited, computed, and answerable in a " +
      "five-second chat message.",
    url: SITE_URL,
    siteName: appTitle,
    images: [{ url: "icon.png", width: 512, height: 512, alt: `${appTitle} icon` }],
    type: "website",
  },
  twitter: {
    card: "summary",
    title: "Flame in Freefall — AI-Powered Fire Safety Insights from Microgravity Combustion",
    description: "A governed, citation-backed record of NASA's microgravity combustion research, and where it does and doesn't reach.",
  },
};

/**
 * The root `/` — the landing page. Built around the one fact the whole
 * project rests on: a flame in microgravity is a different SHAPE, not just
 * a curiosity — no buoyancy means no upward pull, so it burns as a sphere
 * instead of a teardrop, which is why ground-certified materials (NASA-
 * STD-6001B, tested at 1g) can't be assumed safe off Earth. That fact opens
 * the page instead of a decorative hero graphic. Two real destinations
 * follow — the assistant and the governed record — then the live coverage
 * data that backs every claim on the page.
 *
 * Server component throughout: it reads instance.md and psi-data/derived/
 * at build time (lib/shared, lib/dashboard-data) — no client JS ships here
 * beyond the two heatmap SVGs' native <title> tooltips.
 */
export default function HomePage(): ReactElement {
  const totals = dashboardTotals();
  const heatmaps = geometryHeatmaps();
  const markers = atmosphereMarkers();
  const readiness = missionReadinessSummary();
  const totalGaps = totalCoverageGaps(heatmaps, readiness);

  return (
    <>
      <Hero />
      <NumberStrip totals={totals} />
      <Destinations />
      <EvidenceSection heatmaps={heatmaps} markers={markers} readiness={readiness} totalGaps={totalGaps} />
      <TrustSection />
      <ClosingCta description={appDescription} />
    </>
  );
}

// ── Hero ─────────────────────────────────────────────────────────────────

function Hero(): ReactElement {
  return (
    <section className="mx-auto grid max-w-5xl gap-10 px-4 py-16 sm:px-6 sm:py-20 lg:grid-cols-[1.1fr_0.9fr] lg:items-center lg:py-24">
      <div className="ksor-fade-up">
        <h1 className="font-display text-4xl font-semibold tracking-tight text-balance sm:text-5xl">
          AI-powered fire safety insights from microgravity combustion
        </h1>
        <p className="mt-5 max-w-xl text-lg text-muted-foreground">
          A candle flame on Earth is pulled into a teardrop by buoyancy. Without gravity, there&apos;s nothing for hot
          gas to rise into — the same flame burns as a sphere. Spacecraft materials are certified against the first
          shape. This record and assistant exist because NASA needs to know what the second one actually does.
        </p>
        <div className="mt-8 flex flex-col gap-3 sm:flex-row">
          <Button asChild size="lg">
            <Link href="/chat/">Ask the assistant</Link>
          </Button>
          <Button asChild size="lg" variant="outline">
            <Link href="/docs/">Browse the System of Record</Link>
          </Button>
        </div>
      </div>
      <div className="ksor-fade-up ksor-fade-up-delay-1">
        <FlameComparison />
      </div>
    </section>
  );
}

// ── Number strip ─────────────────────────────────────────────────────────

function NumberStrip({ totals }: { totals: ReturnType<typeof dashboardTotals> }): ReactElement {
  const stats: { n: number; label: string }[] = [
    { n: totals.investigations, label: "investigations" },
    { n: totals.runs, label: "run-table rows, every granularity" },
    { n: totals.tests, label: "of those, single-test rows" },
    { n: totals.withOutcomes, label: "with measured results" },
    { n: totals.reportConfirmed, label: "report-confirmed" },
    { n: totals.conflicts, label: "conflicts flagged, not hidden" },
  ];
  return (
    <section className="border-y border-border/60">
      <dl className="mx-auto flex max-w-5xl flex-wrap justify-between gap-x-6 gap-y-3 px-4 py-5 text-sm sm:px-6">
        {stats.map((s) => (
          <div key={s.label} className="flex items-baseline gap-1.5">
            <dd className="font-medium tabular-nums">{s.n.toLocaleString("en-US")}</dd>
            <dt className="text-muted-foreground">{s.label}</dt>
          </div>
        ))}
      </dl>
    </section>
  );
}

// ── Two destinations ─────────────────────────────────────────────────────

function Destinations(): ReactElement {
  const assistantCapabilities: { term: string; body: string }[] = [
    { term: "Evidence, tiered", body: "at-conditions, partial and nearest tests — never one number picked and passed off as the answer." },
    { term: "Gap map", body: "O₂ × flow bands shaded by test count, so an untested condition is visible, not silent." },
    { term: "Ranking", body: "materials ranked by a measured result within one geometry class — median, range, every run id." },
    { term: "Mission readiness", body: "how much data exists near a named mission atmosphere, with a citation on why a gap matters." },
    { term: "Compare & chart", body: "investigations side by side, or a result plotted against a condition." },
  ];
  const recordPrinciples: { term: string; body: string }[] = [
    { term: "draft → stable", body: "nothing publishes until a named approver signs off, with a timestamp." },
    { term: "cited, always", body: "every claim carries a footnote back to a report, table or workbook." },
    { term: "gaps stay gaps", body: "a hole in a source is an open question, never filled by inference." },
    { term: "append-only takedowns", body: "a withdrawn document stops serving immediately, through an auditable ledger." },
  ];
  return (
    <section className="mx-auto max-w-5xl px-4 py-16 sm:px-6">
      <div className="grid gap-12 lg:grid-cols-[1.2fr_1fr]">
        <div className="border-t border-border pt-6">
          <h2 className="font-display text-2xl font-semibold tracking-tight">The AI assistant</h2>
          <p className="mt-2 max-w-lg text-muted-foreground">
            Ask by conditions, by material, or by mission atmosphere. Every answer renders from a tool&apos;s own JSON
            result — the model writes a short summary of what&apos;s on screen and is told never to retype or merge a
            value.
          </p>
          <dl className="mt-6 space-y-4">
            {assistantCapabilities.map((c) => (
              <div key={c.term} className="flex flex-col gap-0.5 sm:flex-row sm:gap-3">
                <dt className="shrink-0 text-sm font-medium sm:w-40">{c.term}</dt>
                <dd className="text-sm text-muted-foreground">{c.body}</dd>
              </div>
            ))}
          </dl>
          <Button asChild className="mt-6">
            <Link href="/chat/">Start chatting</Link>
          </Button>
        </div>

        <div className="border-t border-border pt-6">
          <h2 className="font-display text-2xl font-semibold tracking-tight">The System of Record</h2>
          <p className="mt-2 text-muted-foreground">
            20 documents covering every investigation, report, table and workbook this project touches. A governance
            model a shared doc or a wiki doesn&apos;t have.
          </p>
          <dl className="mt-6 space-y-4">
            {recordPrinciples.map((c) => (
              <div key={c.term}>
                <dt className="text-sm font-medium">{c.term}</dt>
                <dd className="text-sm text-muted-foreground">{c.body}</dd>
              </div>
            ))}
          </dl>
          <Button asChild variant="outline" className="mt-6">
            <Link href="/docs/">Browse the record</Link>
          </Button>
        </div>
      </div>
    </section>
  );
}

// ── Evidence: the live coverage data ─────────────────────────────────────

function EvidenceSection({
  heatmaps,
  markers,
  readiness,
  totalGaps,
}: {
  heatmaps: ReturnType<typeof geometryHeatmaps>;
  markers: ReturnType<typeof atmosphereMarkers>;
  readiness: ReturnType<typeof missionReadinessSummary>;
  totalGaps: ReturnType<typeof totalCoverageGaps>;
}): ReactElement {
  return (
    <section className="border-y border-border/60 bg-muted/20">
      <div className="mx-auto max-w-5xl px-4 py-16 sm:px-6">
        <h2 className="font-display text-2xl font-semibold tracking-tight">Where the evidence actually reaches</h2>
        <p className="mt-2 max-w-2xl text-muted-foreground">
          NASA-STD-6001B certifies materials at 20.9% O₂ and 1 atmosphere. The atmospheres proposed for a Lunar habitat
          run up to 34% oxygen at reduced pressure, and NASA&apos;s own decadal-survey research says those atmospheres
          &ldquo;will likely require the retest of many materials.&rdquo; Below is what the PSI data actually covers
          near each proposed atmosphere — computed from the 1,948-record test table, not estimated.
        </p>

        {totalGaps.length > 0 ? (
          <div className="ksor-caution mt-6 rounded-lg border border-l-4 px-4 py-3 text-sm">
            <span className="font-medium">
              {totalGaps.map((g) => g.label).join(" and ")}: zero coverage, full stop.
            </span>{" "}
            No run in {totalGaps.length === 1 ? "that class" : "those classes"} reports both O₂% and pressure — not
            at conditions, not partial, not near, at any of the three mission atmospheres below. That gap sits
            inside the grid underneath; it deserves to be read before it, not inside it.
          </div>
        ) : null}

        <div className="mt-8 rounded-none border border-border bg-card">
          <div className="flex items-center justify-between border-b border-border px-4 py-2.5">
            <span className="font-mono text-xs text-muted-foreground">psi-data/derived/runs.json → coverage by O₂ × pressure</span>
          </div>
          <div className="grid gap-x-6 gap-y-5 p-4 sm:grid-cols-2 sm:p-6">
            {heatmaps.map((h) => (
              <Heatmap key={h.geometryClass} heatmap={h} markers={markers} />
            ))}
          </div>
          <div className="border-t border-border px-4 py-3 sm:px-6">
            <HeatmapLegend />
          </div>
        </div>

        <h3 className="mt-10 text-lg font-medium">Mission readiness</h3>
        <p className="mt-1 text-sm text-muted-foreground">
          &ldquo;Covered&rdquo; means at least one test matches or partially matches that atmosphere — it never means safe.
        </p>
        <div className="mt-4">
          <ReadinessCards readiness={readiness} />
        </div>
      </div>
    </section>
  );
}

// ── Trust ────────────────────────────────────────────────────────────────

function TrustSection(): ReactElement {
  const items = [
    "Numbers come only from tools — the model never states a value that wasn't returned by data.",
    "A ranking is a computed median over every contributing run, never a guess, and every run id is kept.",
    "A mission-readiness finding is a citation checked verbatim against its source document by an automated test.",
    "An empty result (“no test at these conditions”) is shown as an answer, not papered over.",
    "Source disagreements are flagged and both values kept — never silently resolved.",
    "A failed lookup forces an honest “I can't check that right now” in code, regardless of what the model wrote.",
  ];
  return (
    <section className="mx-auto max-w-5xl px-4 py-16 sm:px-6">
      <h2 className="font-display text-2xl font-semibold tracking-tight">Architecture over prompting</h2>
      <p className="mt-2 max-w-2xl text-muted-foreground">
        This isn&apos;t a wrapped LLM with a system prompt telling it to &ldquo;be accurate.&rdquo; Every line below is
        enforced in code against every reply.
      </p>
      <ul className="mt-6 max-w-2xl divide-y divide-border border-t border-border">
        {items.map((text) => (
          <li key={text} className="py-3 text-sm text-muted-foreground">
            {text}
          </li>
        ))}
      </ul>
    </section>
  );
}

// ── Closing CTA ──────────────────────────────────────────────────────────

function ClosingCta({ description }: { description: string | null }): ReactElement {
  return (
    <section className="border-t border-border/60 bg-muted/20">
      <div className="mx-auto max-w-3xl px-4 py-16 text-center sm:px-6">
        <h2 className="font-display text-3xl font-semibold tracking-tight">Ready to see where the data reaches?</h2>
        {description ? <p className="mt-3 text-muted-foreground">{description}</p> : null}
        <div className="mt-7 flex flex-col items-center justify-center gap-3 sm:flex-row">
          <Button asChild size="lg">
            <Link href="/chat/">Ask the assistant</Link>
          </Button>
          <Button asChild size="lg" variant="outline">
            <Link href="/docs/">Browse the System of Record</Link>
          </Button>
        </div>
      </div>
    </section>
  );
}
