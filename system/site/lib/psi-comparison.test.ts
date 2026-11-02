import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { test } from "node:test";
import { compareRuns } from "./psi-comparison.ts";

const fixtures = JSON.parse(readFileSync(new URL("../../../psi-data/query-fixtures.json", import.meta.url), "utf8"));
test("nonfinite measurements cannot establish comparability", () => {
  for (const invalid of [Infinity, NaN, true]) {
    const c = structuredClone(fixtures.comparison_cases[0]);
    for (const side of ["left", "right"]) Object.assign(c[side].conditions.pressure_atm, { value: invalid, min: invalid, max: invalid });
    const got = compareRuns(c.left, c.right, c.investigations, c.quantity);
    assert.equal(got.can_compare, false);
    assert.ok(got.unknown_or_conflicted.includes("pressure_atm"));
  }
});
assert.ok(fixtures.comparison_cases?.length >= 16, "Comparison parity fixtures must be regenerated");
for (const c of fixtures.comparison_cases) {
  test(`comparison parity: ${c.name}`, () => {
    // JSON removes optional undefined properties just as the exported payload does.
    const got = JSON.parse(JSON.stringify(compareRuns(c.left, c.right, c.investigations, c.quantity, c.varied_axis)));
    assert.deepEqual(got, c.expect);
    assert.equal(got.status, c.status);
  });
}
