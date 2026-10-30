import { createHash } from "node:crypto";
import { readFileSync } from "node:fs";
import path from "node:path";

import { projectRoot } from "./shared";
import type { Investigation, RawBundle, Run, SlimRun, SlimSource } from "./psi-types";

// The PSI run table is a GENERATED build artifact (system/psi-ingest →
// psi-data/derived/), not authored content: nothing here writes it, and the
// site holds no copy of it — every build reads it fresh, like the record.
const derived = path.join(projectRoot, "psi-data", "derived");

let cache: { runs: Run[]; investigations: Investigation[]; generatedAt: string } | null = null;

function load() {
  if (cache) return cache;
  const runsFile = JSON.parse(readFileSync(path.join(derived, "runs.json"), "utf8")) as {
    generated_at: string;
    runs: Run[];
  };
  const invFile = JSON.parse(readFileSync(path.join(derived, "investigations.json"), "utf8")) as {
    investigations: Investigation[];
  };
  cache = { runs: runsFile.runs, investigations: invFile.investigations, generatedAt: runsFile.generated_at };
  return cache;
}

export function psiInvestigations(): Investigation[] {
  return load().investigations;
}

export function psiDatasetHash(): string {
  return createHash("sha256").update(readFileSync(path.join(derived, "runs.json"))).digest("hex");
}

export function psiGeneratedAt(): string {
  return load().generatedAt;
}

export function psiIngestReport(): Record<string, unknown> {
  return JSON.parse(readFileSync(path.join(derived, "ingest-report.json"), "utf8")) as Record<string, unknown>;
}

/** Every run without its raw cells, and with report citations reduced to a
 * key into the investigation's citation (the title/URL live there once). */
export function slimRuns(): SlimRun[] {
  return load().runs.map(({ raw: _raw, sources, ...rest }) => ({
    ...rest,
    sources,
  }));
}

/** The raw cells for one investigation's runs, keyed by run id — fetched only
 * when a reader opens a run. */
export function rawBundle(investigation: string): RawBundle {
  const out: RawBundle = {};
  for (const r of load().runs) if (r.investigation === investigation) out[r.id] = r.raw;
  return out;
}

export function runsFor(investigation: string): Run[] {
  return load().runs.filter((r) => r.investigation === investigation);
}
