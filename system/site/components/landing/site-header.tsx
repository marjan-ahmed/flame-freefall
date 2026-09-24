import type { ReactElement } from "react";

import Link from "next/link";

import { Button } from "@/components/ui/button";

/** The landing page's own slim chrome: a wordmark, the record, and the one
 * action that matters. Not a link farm — two destinations, not a nav bar
 * pretending to organize five. */
export function SiteHeader({ title }: { title: string }): ReactElement {
  return (
    <header className="border-b border-border/60">
      <nav className="mx-auto flex max-w-5xl items-center justify-between gap-4 px-4 py-4 sm:px-6">
        <Link href="/" className="font-display text-base font-semibold tracking-tight">
          {title}
        </Link>
        <div className="flex items-center gap-5">
          <Link href="/docs/" className="hidden text-sm text-muted-foreground transition-colors hover:text-foreground sm:inline">
            System of Record
          </Link>
          <Button asChild size="sm">
            <Link href="/chat/">Ask the assistant</Link>
          </Button>
        </div>
      </nav>
    </header>
  );
}
