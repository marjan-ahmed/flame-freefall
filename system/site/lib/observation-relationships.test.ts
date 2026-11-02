import assert from "node:assert/strict";
import { test } from "node:test";
import { observationRelationshipSummary } from "./observation-relationships.ts";
import type { ObservationRelationship, SlimRun } from "./psi-types.ts";

test("source identifier grouping counts observations without claiming independent tests", () => {
  const relation: ObservationRelationship = { method_version: "same-r-source-identifiers-v1", basis: "source identifier grouping", source: 0, source_field: "SAME Test #", source_label: "51", description: "baseline", role: "unspecified", role_basis: "Description only", base_test_number: "51", material: "Kapton", group_id: "same-r:Kapton:51", independence: "unknown", status: "identifier_grouped", related_source_labels: ["51", "51a"] };
  const run: SlimRun = { id: "a", investigation: "same-r", label: "51", granularity: "test", date: null, conditions: {}, outcomes: [], sources: [], observation_relationship: relation };
  const unresolved = { ...relation, status: "ambiguous_identifier" as const, group_id: null };
  const summary = observationRelationshipSummary([run, { ...run, id: "b" }, { ...run, id: "c", observation_relationship: unresolved }, { ...run, id: "d", observation_relationship: unresolved }, { ...run, id: "e", observation_relationship: undefined }]);
  assert.equal(summary.observations, 4);
  assert.equal(summary.resolved_identifier_groups, 1);
  assert.equal(summary.ambiguous_observations, 2);
  assert.equal(summary.unclassified_observations, 1);
  assert.equal(summary.independence, "unknown");
  assert.match(summary.limitation, /No observations are merged/);
});
