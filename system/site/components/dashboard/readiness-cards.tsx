import type { ReactElement } from "react";

import Link from "next/link";

import type { ReadinessSummary } from "@/lib/dashboard-data";

// One card per named mission atmosphere: which geometry classes the PSI data
// actually covers there. Coverage is computed (the twinned query(), same as
// the chat's show_mission_readiness); nothing here states a safety
// conclusion — that's the chat's job, quoting the governed record.

export function ReadinessCards({ readiness }: { readiness: ReadinessSummary[] }): ReactElement {
  return (
    <div className="grid gap-3 sm:grid-cols-3">
      {readiness.map((r) => {
        const covered = r.classes.filter((c) => c.covered).length;
        const evidenceHref = `/explore/?o2_pct=${r.atmosphere.o2_pct}&pressure_atm=${r.atmosphere.pressure_atm}&individual=1`;
        return (
          <div key={r.atmosphere.id} className="border border-border border-t-2 border-t-primary bg-card p-4">
            <div className="flex items-start justify-between gap-3">
              <div>
                <span className="block text-xs text-muted-foreground">Named atmosphere</span>
                <span className="mt-1 block font-display text-lg font-semibold">{r.atmosphere.label}</span>
              </div>
              <div className="text-right">
                <span className="block font-mono text-lg font-medium tabular-nums">{covered}<span className="text-muted-foreground/60">/{r.classes.length}</span></span>
                <span className="block text-[11px] text-muted-foreground">classes with full matches</span>
              </div>
            </div>
            <p className="mt-1 text-xs text-muted-foreground">
              {`${r.atmosphere.o2_pct}% O₂ · ${r.atmosphere.pressure_atm.toFixed(2)} atm (cell ${r.atmosphere.pressure_source_value})`}
            </p>
            <ul className="mt-2 flex flex-wrap gap-1.5">
              {r.classes.map((c) => (
                <li
                  key={c.geometryClass}
                  className={"border px-2 py-1 text-xs " + (c.covered ? "ksor-coverage-ok" : "ksor-coverage-gap")}
                  title={`${c.match} at conditions, ${c.partial} partial`}
                >
                  {c.label} {c.covered ? `(${c.match + c.partial})` : "— gap"}
                </li>
              ))}
            </ul>
            <Link href={evidenceHref} className="mt-4 inline-block border-t border-border pt-3 text-xs font-medium text-primary hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
              Inspect matching and partial evidence
            </Link>
          </div>
        );
      })}
    </div>
  );
}
