import type { ReactElement } from "react";

import Link from "next/link";

import type { LunarEvidenceBrief, MissionEvidenceSlice } from "@/lib/mission-evidence";

function explorerHref(brief: LunarEvidenceBrief, geometryClass: string, runId: string | undefined): string {
  const params = new URLSearchParams({
    o2_pct: String(brief.atmosphere.o2_pct),
    pressure_atm: String(brief.atmosphere.pressure_atm),
    geometry_class: geometryClass,
  });
  if (runId) params.set("run", runId);
  return `/explore/?${params.toString()}`;
}

function EvidenceCount({ slice, label }: { slice: MissionEvidenceSlice; label: string }): ReactElement {
  return (
    <p className="mt-3 text-sm text-muted-foreground">
      <span className="font-medium text-foreground">{slice.match}</span> at conditions and{" "}
      <span className="font-medium text-foreground">{slice.partial}</span> partial {label} records.
    </p>
  );
}

/**
 * The landing page's concrete scientific contribution. It compares coverage,
 * not flammability: geometry classes remain separate and the closest solid
 * run is shown as a near result, never promoted to a mission match.
 */
export function LunarEvidenceBrief({ brief }: { brief: LunarEvidenceBrief }): ReactElement {
  const gaseousRun = brief.gaseous.representative;
  const solidRun = brief.solid.representative;
  const sourceHref = "/docs/foundations/decadal-survey/miller-spacecraft-materials-fire-safety/";

  return (
    <section className="border-y border-border/60 bg-[linear-gradient(105deg,hsl(var(--muted)/0.58),transparent_62%)]">
      <div className="mx-auto max-w-5xl px-4 py-12 sm:px-6 sm:py-16">
        <div className="max-w-3xl">
          <h2 className="font-display text-2xl font-semibold tracking-tight">One Lunar scenario. Two evidence realities.</h2>
          <p className="mt-2 text-muted-foreground">
            This is a reproducible coverage comparison at the proposed Lunar-habitat atmosphere: {brief.atmosphere.o2_pct}% O₂ and{" "}
            {brief.atmosphere.pressure_source_value}. It asks what the table contains, not what is safe.
          </p>
        </div>

        <div className="mt-7 grid divide-y divide-border border border-border bg-card md:grid-cols-2 md:divide-x md:divide-y-0">
          <article className="p-5 sm:p-6">
            <p className="text-sm font-medium text-primary">Gaseous flames: evidence at the target</p>
            <EvidenceCount slice={brief.gaseous} label="gaseous-flame" />
            {gaseousRun ? (
              <p className="mt-4 text-sm text-muted-foreground">
                Representative at-condition record: <span className="font-medium text-foreground">{gaseousRun.run.id}</span>,{" "}
                {gaseousRun.run.conditions.fuel_family && "fuel family "}
                {typeof gaseousRun.run.conditions.fuel_family === "object" && "value" in gaseousRun.run.conditions.fuel_family
                  ? gaseousRun.run.conditions.fuel_family.value
                  : "not reported"}.
              </p>
            ) : null}
            <Link
              href={explorerHref(brief, "gaseous-flames", gaseousRun?.run.id)}
              className="mt-5 inline-block text-sm font-medium text-primary hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
            >
              Inspect the gaseous-flame records
            </Link>
          </article>

          <article className="p-5 sm:p-6">
            <p className="text-sm font-medium text-foreground">Solid fuels: a measured boundary, not coverage</p>
            <EvidenceCount slice={brief.solid} label="solid-fuel" />
            {solidRun ? (
              <p className="mt-4 text-sm text-muted-foreground">
                Closest returned record: <span className="font-medium text-foreground">{solidRun.run.id}</span> (SAFFIRE VI SIBAL fabric),
                at 31% O₂ and 54.1 kPa. It is a near result, so it does not fill the gap.
              </p>
            ) : null}
            <Link
              href={explorerHref(brief, "solid-fuel", solidRun?.run.id)}
              className="mt-5 inline-block text-sm font-medium text-primary hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring"
            >
              Inspect the solid-fuel boundary
            </Link>
          </article>
        </div>

        <div className="mt-5 grid gap-4 text-sm text-muted-foreground md:grid-cols-[1fr_auto] md:items-end">
          <p className="max-w-3xl">
            The finding is about evidence coverage only. These geometry classes are not comparable as material rankings, and microgravity
            tests do not establish behavior at Lunar gravity. NASA&apos;s Decadal Survey calls for further testing of real materials in
            reduced-gravity exploration atmospheres.
          </p>
          <Link href={sourceHref} className="font-medium text-primary hover:underline focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring">
            Read the governed NASA source
          </Link>
        </div>
      </div>
    </section>
  );
}
