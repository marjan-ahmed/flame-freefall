import Link from "next/link";
import type { ReactNode } from "react";

import { appTitle } from "@/lib/shared";

// The Explorer's own chrome: a slim bar linking the three ways into the same
// evidence — ask the copilot, query the test table, read the governed record.
export default function Layout({ children }: { children: ReactNode }) {
  return (
    <div className="min-h-screen bg-background text-foreground">
      <header className="border-b border-white/10 bg-slate-950 text-slate-100">
        <nav className="mx-auto flex max-w-[1400px] flex-wrap items-center gap-x-6 gap-y-2 px-4 py-3 text-sm">
          <Link href="/explore/" className="inline-flex items-center gap-3 font-display text-base font-semibold">
            <span className="grid size-7 place-items-center border border-orange-400/60 text-xs text-orange-300" aria-hidden="true">F</span>
            {appTitle}
          </Link>
          <div className="flex flex-wrap gap-4">
            <Link href="/" className="text-slate-400 hover:text-white">
              Home
            </Link>
            <Link href="/chat/" className="text-slate-400 hover:text-white">
              Ask the copilot
            </Link>
            <Link href="/explore/" className="font-medium text-orange-300">
              Test-data explorer
            </Link>
            <Link href="/explore/investigations/" className="text-slate-400 hover:text-white">
              Investigations
            </Link>
            <Link href="/docs/" className="text-slate-400 hover:text-white">
              System of Record
            </Link>
          </div>
        </nav>
      </header>
      <main className="mx-auto max-w-[1400px] px-4 py-6">{children}</main>
    </div>
  );
}
