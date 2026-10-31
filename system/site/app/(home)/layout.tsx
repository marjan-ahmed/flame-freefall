import type { ReactNode } from "react";

import { SiteFooter } from "@/components/landing/site-footer";
import { SiteHeader } from "@/components/landing/site-header";
import { appTitle } from "@/lib/shared";

// The root `/` is the landing page (2026-09-25 decision, replacing the
// full-screen ChatKit interface this route group carried before): a judge or
// researcher lands somewhere that explains what the product is and offers
// three clear destinations — the AI assistant (now at /chat), the Test-data
// Explorer, and the System of Record — rather than an empty chat composer.
// No chatkit.js here: nothing on this page loads the widget.
export default function Layout({ children }: LayoutProps<"/">) {
  return (
    <div className="flex min-h-screen flex-col bg-background text-foreground">
      <SiteHeader title={appTitle} />
      <main id="workspace-content" className="flex-1">{children}</main>
      <SiteFooter title={appTitle} />
    </div>
  );
}
