import type { ReactElement } from "react";

import Link from "next/link";

import { Button } from "@/components/ui/button";

/** The landing page's own slim chrome: a wordmark, the record, and the one
 * action that matters. Not a link farm — two destinations, not a nav bar
 * pretending to organize five. */
export function SiteHeader({ title }: { title: string }): ReactElement {
  return (
    <header className="border-b border-white/10 bg-slate-950 text-slate-100">
      <nav className="mx-auto flex max-w-6xl items-center justify-between gap-4 px-4 py-3.5 sm:px-6">
        <Link href="/" className="inline-flex items-center gap-3 font-display text-base font-semibold tracking-tight">
          <span className="grid size-7 place-items-center border border-orange-400/60 text-xs text-orange-300" aria-hidden="true">F</span>
          {title}
        </Link>
        <div className="flex items-center gap-5">
          <Link href="/explore/" className="hidden text-sm text-slate-300 transition-colors hover:text-white sm:inline">
            Explore PSI data
          </Link>
          <Link href="/docs/" className="hidden text-sm text-slate-300 transition-colors hover:text-white sm:inline">
            System of Record
          </Link>
          <Button asChild size="sm" className="bg-orange-400 text-slate-950 hover:bg-orange-300">
            <Link href="/chat/">Ask the assistant</Link>
          </Button>
        </div>
      </nav>
    </header>
  );
}
