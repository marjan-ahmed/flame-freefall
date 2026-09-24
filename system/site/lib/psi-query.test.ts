// Parity with system/chatkit-server/psi_query.py: both implementations must
// reproduce psi-data/query-fixtures.json exactly. Run: npm run test:psi
// (node's built-in runner + type stripping; no test framework dependency).

import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import path from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

import { query, rank, type Query } from "./psi-query.ts";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../../..");
const read = (p: string) => JSON.parse(readFileSync(path.join(root, p), "utf8"));
const runs = read("psi-data/derived/runs.json").runs;
const investigations = read("psi-data/derived/investigations.json").investigations;
const { cases, rank_cases } = read("psi-data/query-fixtures.json") as {
  cases: { name: string; query: Query; tolerances: Record<string, number> | null; expect: Record<string, unknown> }[];
  rank_cases: {
    name: string;
    query: Query;
    quantity: string;
    geometry_class: string;
    direction: "asc" | "desc";
    expect: Record<string, unknown>;
  }[];
};

for (const c of cases) {
  test(c.name, () => {
    const r = query(runs, investigations, c.query, c.tolerances ?? {});
    const got = {
      counts: r.counts,
      match_ids: r.match.slice(0, 15).map((v) => v.run.id),
      partial_ids: r.partial.slice(0, 15).map((v) => v.run.id),
      near_ids: r.near.slice(0, 5).map((v) => v.run.id),
      coverage: Object.fromEntries(
        r.coverage.map((cv) => [
          cv.investigation_id,
          Object.fromEntries(
            Object.entries(cv.axes).map(([k, a]) => [k, "target_in_range" in a! ? a.target_in_range : null]),
          ),
        ]),
      ),
      relaxed: r.relaxed,
    };
    assert.deepEqual(got, c.expect);
  });
}

for (const c of rank_cases) {
  test(c.name, () => {
    const r = rank(runs, investigations, c.query, c.quantity, c.geometry_class, c.direction);
    if ("error" in r) throw new Error(r.error);
    const got = {
      total_ranked: r.total_ranked,
      rows: r.rows.map((row) => ({ fuel_family: row.fuel_family, n: row.n, min: row.min, median: row.median, max: row.max })),
      untested: r.untested,
    };
    assert.deepEqual(got, c.expect);
  });
}
