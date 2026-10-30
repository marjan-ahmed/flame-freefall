import { WorkspaceNav } from "@/components/workspace-nav";
import Link from "next/link";
import type { ReactNode } from "react";

import { appTitle } from "@/lib/shared";

// The Explorer's own chrome: a slim bar linking the three ways into the same
// evidence — ask the copilot, query the test table, read the governed record.
export default function Layout({ children }: { children: ReactNode }) {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <WorkspaceNav title={appTitle} />
      <main className="mx-auto max-w-[1400px] px-4 py-6">{children}</main>
    </div>
  );
}
