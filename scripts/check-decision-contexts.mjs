import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { parse } from "yaml";
import { checkMapping } from "../system/site/lib/decision-mapping.ts";
const root = new URL("../", import.meta.url);
const mapping = parse(readFileSync(new URL("psi-data/decision-contexts.yaml", root), "utf8"));
const investigations = JSON.parse(readFileSync(new URL("psi-data/derived/investigations.json", root), "utf8")).investigations;
checkMapping(mapping.assignments, investigations, fileURLToPath(root));
console.log(`Decision mapping v${mapping.version}: ${mapping.assignments.length} supported assignments; automated source-text checking only.`);
for (const job of ["prevention", "detection", "suppression"]) {
  console.log(`${job}: unclassified = ${investigations.filter(i => !mapping.assignments.some(a => a.investigation === i.id && a.job === job)).map(i => i.id).sort().join(", ")}`);
}
