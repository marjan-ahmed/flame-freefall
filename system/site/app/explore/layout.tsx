import Link from "next/link";
import type { ReactNode } from "react";

import { appTitle } from "@/lib/shared";

// The Explorer's own chrome: a slim bar linking the three ways into the same
// evidence — ask the copilot, query the test table, read the governed record.
export default function Layout({ children }: { children: ReactNode }) {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <header className="border-b">
        <nav className="mx-auto flex max-w-[1400px] flex-wrap items-center gap-x-6 gap-y-2 px-4 py-3 text-sm">
          <Link href="/explore/" className="font-display text-base font-semibold">
            {appTitle}
          </Link>
          <div className="flex flex-wrap gap-4">
            <Link href="/" className="text-muted-foreground hover:text-foreground">
              Ask the copilot
            </Link>
            <Link href="/explore/" className="font-medium text-foreground">
              Test-data explorer
            </Link>
            <Link href="/explore/investigations/" className="text-muted-foreground hover:text-foreground">
              Investigations
            </Link>
            <Link href="/docs/" className="text-muted-foreground hover:text-foreground">
              System of Record
            </Link>
          </div>
        </nav>
      </header>
      <main className="mx-auto max-w-[1400px] px-4 py-6">{children}</main>
    </div>
  );
}
