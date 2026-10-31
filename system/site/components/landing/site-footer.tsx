import type { ReactElement } from "react";

import Link from "next/link";

export function SiteFooter({ title }: { title: string }): ReactElement {
  return (
    <footer className="border-t border-border/60">
      <div className="mx-auto flex max-w-5xl flex-col gap-3 px-4 py-8 text-sm text-muted-foreground sm:flex-row sm:items-center sm:justify-between sm:px-6">
        <div className="space-y-1">
          <p className="font-medium text-foreground">{title} by Team Code Nashai</p>
          <p>Built for NASA Space Apps Challenge 2026, &ldquo;Flame in Freefall&rdquo; track.</p>
        </div>
        <div className="flex flex-wrap gap-5">
          <Link href="/chat/" className="transition-colors hover:text-foreground">
            AI assistant
          </Link>
          <Link href="/docs/" className="transition-colors hover:text-foreground">
            System of Record
          </Link>
        </div>
      </div>
    </footer>
  );
}
