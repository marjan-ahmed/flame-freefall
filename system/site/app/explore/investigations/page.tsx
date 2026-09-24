import type { Metadata } from "next";
import Link from "next/link";
import type { ReactElement } from "react";

import { GEOMETRY_LABEL, fmt } from "@/components/explore/format";
import { colorMap } from "@/components/explore/palette";
import { psiInvestigations } from "@/lib/psi-data";

export const metadata: Metadata = {
  title: "Investigations",
  description:
    "Every NASA PSI combustion investigation in the unified test table — what each tested, how much of it carries results, and where it is cited from.",
};

type Cov = { runs: number; min: number; max: number; unit: string };
const AXES = [
  ["o2_pct", "O₂"],
  ["flow_cm_s", "Flow"],
  ["pressure_atm", "Pressure"],
] as const;

export default function InvestigationsPage(): ReactElement {
  const all = psiInvestigations();
  const invs = all.filter((i) => i.runs > 0);
  const colors = colorMap(all);
  return (
    <>
      <h1 className="font-display text-3xl tracking-tight">Investigations</h1>
      <p className="mt-2 max-w-3xl text-muted-foreground">
        Grouped by geometry class, the unit within which results are comparable. Ranges are what the tables report, not what the hardware
        could do.
      </p>
      {Object.entries(GEOMETRY_LABEL).map(([g, label]) => {
        const group = invs.filter((i) => i.geometry_class === g);
        if (!group.length) return null;
        return (
          <section key={g} className="mt-8">
            <h2 className="font-display text-xl">{label}</h2>
            <div className="mt-3 grid gap-3 sm:grid-cols-2 xl:grid-cols-3">
              {group.map((i) => {
                const cov = i.coverage as Record<string, Cov>;
                return (
                  <Link
                    key={i.id}
                    href={`/explore/${i.id}/`}
                    className="rounded-xl border bg-card p-4 transition-colors hover:border-primary/60"
                  >
                    <div className="flex items-center gap-2">
                      <span className="inline-block size-3 rounded-full" style={{ background: colors[i.id] }} />
                      <span className="font-semibold">{i.name}</span>
                      {i.psi_id && <span className="ml-auto font-mono text-xs text-muted-foreground">{i.psi_id}</span>}
                    </div>
                    {i.full_name && <p className="mt-1 text-xs text-muted-foreground">{i.full_name}</p>}
                    <p className="mt-2 text-sm">
                      <strong>{i.runs}</strong> records
                      {Object.entries(i.granularity)
                        .filter(([k]) => k !== "test")
                        .map(([k, n]) => ` · ${n} ${k === "day" ? "daily summaries" : k === "envelope" ? "planned envelopes" : "test points"}`)}
                    </p>
                    <p className="text-xs text-muted-foreground">
                      {i.runs_with_outcomes} with results · {i.runs_with_report_data} cross-checked with a report
                      {i.conflicts ? ` · ${i.conflicts} disagreements` : ""}
                    </p>
                    <ul className="mt-2 space-y-0.5 text-xs">
                      {AXES.map(([k, label]) =>
                        cov[k] ? (
                          <li key={k}>
                            {label}: {fmt(cov[k].min)}–{fmt(cov[k].max)} {cov[k].unit}{" "}
                            <span className="text-muted-foreground">({cov[k].runs} records)</span>
                          </li>
                        ) : (
                          <li key={k} className="italic text-muted-foreground">
                            {label}: not reported
                          </li>
                        ),
                      )}
                    </ul>
                  </Link>
                );
              })}
            </div>
          </section>
        );
      })}
    </>
  );
}
