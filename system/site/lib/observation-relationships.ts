import type { SlimRun } from "./psi-types.ts";

/** Counts source-identifier groups, never independent experimental replicates. */
export function observationRelationshipSummary(runs: SlimRun[]) {
  const linked = runs.filter(r => r.observation_relationship);
  return {
    observations: linked.length,
    resolved_identifier_groups: new Set(linked.flatMap(r => r.observation_relationship?.group_id ? [r.observation_relationship.group_id] : [])).size,
    ambiguous_observations: linked.filter(r => r.observation_relationship?.status === "ambiguous_identifier").length,
    unclassified_observations: runs.length - linked.length,
    independence: "unknown" as const,
    method_version: "same-r-source-identifiers-v1",
    limitation: "Identifier groups are derived from source test-number stems. They do not establish shared specimens, independent experiments or replicates. No observations are merged.",
  };
}
