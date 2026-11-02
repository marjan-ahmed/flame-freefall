import { readFileSync } from "node:fs";
import path from "node:path";
import { parse } from "yaml";
import { DecisionView } from "@/components/decide/decision-view";
import { checkMapping } from "@/lib/decision-mapping";
import { psiInvestigations } from "@/lib/psi-data";
import { projectRoot } from "@/lib/shared";
import { basePath } from "@/lib/source";
import { WorkspaceNav } from "@/components/workspace-nav";
import type { Assignment } from "@/lib/decision";

export const metadata = { title: "Find relevant evidence" };
export default function DecidePage() {
  const investigations = psiInvestigations();
  const mapping = parse(readFileSync(path.join(projectRoot, "psi-data/decision-contexts.yaml"), "utf8"));
  const assignments = checkMapping(mapping.assignments as Assignment[], investigations, projectRoot);
  return <><WorkspaceNav /><main id="workspace-content" className="mx-auto max-w-6xl px-4 py-8 sm:px-6"><DecisionView investigations={investigations} assignments={assignments} basePath={basePath} /></main></>;
}
