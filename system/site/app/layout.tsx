import localFont from "next/font/local";
import { RootProvider } from "fumadocs-ui/provider/next";
import "./global.css";
import type { Metadata } from "next";
import { appTitle } from "@/lib/shared";
import { basePath, badgeByUrl } from "@/lib/source";
import { readStageManifest } from "@/lib/stage-manifest";
import KsorSearchDialog from "@/components/search-dialog";

// The variable font is bundled locally, including its OFL license.
const atlasFont = localFont({ src: "../public/fonts/plus-jakarta-sans.ttf", variable: "--font-atlas", display: "swap" });

export const metadata: Metadata = {
  // Resolves relative openGraph/twitter image URLs (e.g. the home page's
  // "icon.png") against the site's one published address, in dev too —
  // without it Next falls back to localhost and warns on every build.
  metadataBase: new URL("https://marjan-ahmed.github.io/flame-freefall/"),
  title: {
    default: appTitle,
    template: `%s | ${appTitle}`,
  },
  description: "The Knowledge System of Record for humans and AI agents.",
  // A build that shows drafts (`KSOR_DRAFTS=show`) is a preview, and a static
  // site's pages are open-web artefacts: it says so to every crawler rather
  // than letting a draft be indexed under the record's name (build spec §3).
  ...(readStageManifest().drafts === "shown" ? { robots: { index: false, follow: false } } : {}),
};

export default function Layout({ children }: LayoutProps<"/">) {
  return (
    <html lang="en" suppressHydrationWarning>
      <body className={`${atlasFont.variable} flex flex-col min-h-screen`}>
        {/* Which documents carry a badge, for the search dialog — it
            runs in the browser over a static index that has no field for it.
            Delivered in the document rather than as a dialog prop because
            RootProvider types `options` against the SHIPPED dialog's props, and
            casting that away would hide a real break the day those props move.
            `<` is escaped: a title or route is authored content, and closing
            this tag early would be script injection from the record. */}
        <script
          type="application/json"
          id="ksor-statuses"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify(badgeByUrl()).replaceAll("<", "\\u003c"),
          }}
        />
        <RootProvider
          search={{
            // Static search: the browser downloads the index that
            // app/api/search exports at build time (staticGET) and runs
            // Orama client-side — no server needed, so search keeps
            // working on any static host.
            //
            // Our own dialog, composed from the shell's primitives, so a
            // withdrawn document is marked in the RESULTS too — the last
            // surface where it looked identical to the one that replaced it,
            // and the one whose snippet quotes its obsolete figures.
            SearchDialog: KsorSearchDialog,
            options: { api: `${basePath}/api/search` },
          }}
        >
          {children}
        </RootProvider>
      </body>
    </html>
  );
}
