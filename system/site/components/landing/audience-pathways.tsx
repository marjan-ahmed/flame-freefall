import Link from "next/link";
import type { ReactElement } from "react";

const PATHS = [
  {
    audience: "For students",
    title: "Start with a test question",
    text: "Change a condition, inspect matching runs, and follow a result back to its source.",
    href: "/explore/?o2_pct=15&flow_cm_s=10&fuel_family=PMMA",
    action: "Open the worked query",
    code: "LEARN / 01",
  },
  {
    audience: "For professors",
    title: "Choose investigations for class",
    text: "Browse by fuel geometry and use the governed records to frame a comparison or discussion.",
    href: "/explore/investigations/",
    action: "Browse investigations",
    code: "TEACH / 02",
  },
  {
    audience: "For researchers",
    title: "Trace a pattern to its evidence",
    text: "Filter runs, plot outcomes against conditions, and export a cited evidence bundle.",
    href: "/explore/?o2_pct=30&pressure_atm=0.55&individual=1",
    action: "Explore PSI data",
    code: "RESEARCH / 03",
  },
  {
    audience: "For aerospace teams",
    title: "Inspect mission-condition coverage",
    text: "See where indexed tests overlap a proposed atmosphere, with geometry and gaps visible.",
    href: "/#lunar-evidence",
    action: "View coverage evidence",
    code: "MISSION / 04",
  },
] as const;

export function AudiencePathways(): ReactElement {
  return (
    <section className="dark border-y border-white/10 bg-background text-foreground">
      <div className="mx-auto max-w-6xl px-4 py-14 sm:px-6 sm:py-16">
        <div className="grid gap-10 lg:grid-cols-[0.7fr_1.3fr] lg:gap-16">
          <div>
            <p className="text-sm font-medium text-orange-300">Use the evidence your way</p>
            <h2 className="mt-3 max-w-sm font-display text-3xl font-semibold tracking-tight text-balance sm:text-4xl">
              One archive. Different points of entry.
            </h2>
            <p className="mt-4 max-w-sm leading-6 text-slate-300">
              Follow a guided question, prepare a class discussion, compare measurements, or look at mission-condition coverage.
            </p>
          </div>
          <div className="grid border-l border-white/15 sm:grid-cols-2">
            {PATHS.map((path) => (
              <Link
                key={path.code}
                href={path.href}
                className="group border-b border-r border-t border-white/15 px-4 py-5 outline-none transition-colors hover:bg-white/[0.04] focus-visible:bg-white/[0.06] sm:p-5"
              >
                <span className="font-mono text-[10px] text-slate-400">{path.code}</span>
                <span className="mt-3 block text-sm font-medium text-orange-200">{path.audience}</span>
                <span className="mt-1 block font-display text-xl font-semibold group-hover:text-white">{path.title}</span>
                <span className="mt-2 block text-sm leading-5 text-slate-300">{path.text}</span>
                <span className="mt-5 inline-flex items-center gap-2 text-sm font-medium text-white underline decoration-orange-400/70 underline-offset-4 group-hover:decoration-orange-300">
                  {path.action}<span aria-hidden="true">↗</span>
                </span>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </section>
  );
}
