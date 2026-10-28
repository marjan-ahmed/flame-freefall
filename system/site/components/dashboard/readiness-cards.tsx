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
        const evidenceHref = `/explore/?o2_pct=${r.atmosphere.o2_pct}&pressure_atm=${r.atmosphere.pressure_atm}`;
        return (
          <div key={r.atmosphere.id} className="rounded-lg border bg-card p-3">
            <div className="flex items-baseline justify-between gap-2">
              <span className="text-sm font-medium">{r.atmosphere.label}</span>
              <span className="text-xs text-muted-foreground">
                {covered}/{r.classes.length} classes with evidence
              </span>
            </div>
            <p className="mt-1 text-xs text-muted-foreground">
              {`${r.atmosphere.o2_pct}% O₂ · ${r.atmosphere.pressure_atm.toFixed(2)} atm (cell ${r.atmosphere.pressure_source_value})`}
            </p>
            <ul className="mt-2 flex flex-wrap gap-1.5">
              {r.classes.map((c) => (
                <li
                  key={c.geometryClass}
                  className={"rounded-full border px-2 py-0.5 text-xs " + (c.covered ? "ksor-coverage-ok" : "ksor-coverage-gap")}
                  title={`${c.match} at conditions, ${c.partial} partial`}
                >
                  {c.label} {c.covered ? `(${c.match + c.partial})` : "— gap"}
                </li>
              ))}
            </ul>
            <Link href={evidenceHref} className="mt-3 inline-block text-xs font-medium text-primary hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
              Inspect matching and partial evidence
            </Link>
          </div>
        );
      })}
    </div>
  );
}
