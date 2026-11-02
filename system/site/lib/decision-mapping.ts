import { readFileSync } from "node:fs";
import path from "node:path";
import { parse } from "yaml";
import type { Assignment } from "./decision.ts";
import type { Investigation } from "./psi-types.ts";

export function checkMapping(assignments: Assignment[], invs: Investigation[], root: string) {
  const seen = new Set<string>();
  for (const a of assignments) {
    if (!invs.some(i => i.id === a.investigation)) throw new Error(`Unknown investigation: ${a.investigation}`);
    if (!["prevention", "detection", "suppression"].includes(a.job) || !["direct", "indirect"].includes(a.relevance)) throw new Error("Invalid classification");
    const key = `${a.investigation}/${a.job}`;
    if (seen.has(key)) throw new Error(`Duplicate assignment: ${key}`);
    seen.add(key);
    if (!/^knowledge\/[a-z0-9/-]+$/.test(a.doc)) throw new Error("Invalid document path");
    const text = readFileSync(path.join(root, `${a.doc}.md`), "utf8");
    const match = text.match(/^---\r?\n([\s\S]*?)\r?\n---\r?\n([\s\S]*)$/);
    if (!match || parse(match[1]).status !== "stable") throw new Error(`Document is not stable: ${a.doc}`);
    const norm = (s: string) => s.replace(/\s+/g, " ").trim();
    if (!a.quote.trim() || !norm(match[2]).includes(norm(a.quote))) throw new Error(`Unsupported quote: ${key}`);
    for (const e of a.evidence ?? []) if (!["instrument", "report-only-agent"].includes(e.kind) || !e.quote.trim() || !norm(match[2]).includes(norm(e.quote))) throw new Error(`Unsupported evidence excerpt: ${key}`);
    if (!a.checked_by.startsWith("process:") || !/^\d{4}-\d\d-\d\dT.*(?:Z|[+-]\d\d:\d\d)$/.test(a.checked_at) || !Number.isFinite(Date.parse(a.checked_at))) throw new Error("Automated check identity and timestamp required");
  }
  for (const job of ["prevention", "detection", "suppression"]) if (!assignments.some(a => a.job === job)) throw new Error(`No supported mapping for ${job}`);
  return assignments;
}
