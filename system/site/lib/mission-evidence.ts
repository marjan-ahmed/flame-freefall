import { ATMOSPHERES } from "./psi-atmospheres";
import { psiInvestigations, slimRuns } from "./psi-data";
import { query, type RunView } from "./psi-query";
import { individualRuns, type Tolerances } from "./evidence-method";
import type { Measure } from "./psi-types";

export type MissionEvidenceSlice = { match: number; partial: number; representative: RunView | null };
export function lunarEvidenceBrief() {
  const atmosphere = ATMOSPHERES.lunar;
  const invs = psiInvestigations();
  const runs = individualRuns(slimRuns());
  const categories = [
    { key: "solid", label: "Direct solid-fuel tests", geometry: "solid-fuel", emulator: false },
    { key: "emulator", label: "BRE condensed-fuel emulator", geometry: "gaseous-flames", emulator: true },
    { key: "gaseous", label: "Other gaseous-flame tests", geometry: "gaseous-flames", emulator: false },
  ];
  const windows = [
    { label: "Default search", o2: 1.5, pressure: 0.1 },
    { label: "Tighter pressure", o2: 1.5, pressure: 5 / 101.325 },
    { label: "Wider oxygen", o2: 3, pressure: 0.1 },
  ];
  const profiles = windows.map(window => ({
    ...window,
    slices: categories.map(category => {
      const pool = runs.filter(r => (r.investigation === "acme-bre") === category.emulator);
      const tolerances: Tolerances = { o2_pct: window.o2, pressure_atm: window.pressure };
      const q = { o2_pct: atmosphere.o2_pct, pressure_atm: atmosphere.pressure_atm, geometry_class: category.geometry };
      const r = query(pool, invs, q, tolerances);
      return { ...category, match: r.counts.match, partial: r.counts.partial,
        representative: r.match[0] ?? r.partial[0] ?? r.near[0] ?? null };
    }),
  }));
  const solids = runs.filter(r => invs.find(i => i.id === r.investigation)?.geometry_class === "solid-fuel");
  const reported = solids.filter(r => Number.isFinite((r.conditions.o2_pct as Measure)?.max));
  const maxO2 = reported.length ? Math.max(...reported.map(r => (r.conditions.o2_pct as Measure).max!)) : null;
  const boundaryIds = reported.filter(r => (r.conditions.o2_pct as Measure).max === maxO2).map(r => r.id);
  return { atmosphere, profiles, solidBoundary: { reported: reported.length, missing: solids.length - reported.length, maxO2, ids: boundaryIds } };
}
export type LunarEvidenceBrief = ReturnType<typeof lunarEvidenceBrief>;
