import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { compareRuns } from "./psi-comparison.ts";

const fixtures = JSON.parse(readFileSync(new URL("../../../psi-data/query-fixtures.json", import.meta.url), "utf8"));
assert.ok(fixtures.comparison_cases?.length >= 16, "Comparison parity fixtures must be regenerated");
for (const c of fixtures.comparison_cases) {
  test(`comparison parity: ${c.name}`, () => {
    // JSON removes optional undefined properties just as the exported payload does.
    const got = JSON.parse(JSON.stringify(compareRuns(c.left, c.right, c.investigations, c.quantity, c.varied_axis)));
    assert.deepEqual(got, c.expect);
    assert.equal(got.status, c.status);
  });
}
