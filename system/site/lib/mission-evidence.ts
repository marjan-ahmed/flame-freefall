// A small, reproducible case study for the home page. It is intentionally
// computed through the same query() implementation as the Explorer, rather
// than copying a dashboard number into prose. If the derived PSI table
// changes, the finding changes with it and its test asks us to review the
// judge-facing claim.

import { ATMOSPHERES } from "./psi-atmospheres";
import { psiInvestigations, slimRuns } from "./psi-data";
import { query, type RunView } from "./psi-query";

export type MissionEvidenceSlice = {
  match: number;
  partial: number;
  representative: RunView | null;
};

export type LunarEvidenceBrief = {
  atmosphere: (typeof ATMOSPHERES)["lunar"];
  gaseous: MissionEvidenceSlice;
  solid: MissionEvidenceSlice;
};

function sliceFor(geometry_class: "gaseous-flames" | "solid-fuel"): MissionEvidenceSlice {
  const atmosphere = ATMOSPHERES.lunar;
  const result = query(slimRuns(), psiInvestigations(), {
    o2_pct: atmosphere.o2_pct,
    pressure_atm: atmosphere.pressure_atm,
    geometry_class,
  });
  // A representative is evidence navigation only, never a stand-in for the
  // count. Prefer fully specified evidence, then partial, then the nearest
  // measured condition when the honest result is a gap.
  return {
    match: result.counts.match,
    partial: result.counts.partial,
    representative: result.match[0] ?? result.partial[0] ?? result.near[0] ?? null,
  };
}

export function lunarEvidenceBrief(): LunarEvidenceBrief {
  return {
    atmosphere: ATMOSPHERES.lunar,
    gaseous: sliceFor("gaseous-flames"),
    solid: sliceFor("solid-fuel"),
  };
}
