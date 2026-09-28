import type { ReactElement } from "react";

import { appTitle } from "@/lib/shared";

import { ChatInterface } from "./components/chat-interface";

/**
 * `/chat` — the full-screen OpenAI ChatKit assistant. Moved here from the
 * root `/` (2026-09-25): the root is now the landing page that introduces
 * the three ways into the record (this assistant, the Test-data Explorer,
 * the System of Record) — a judge or researcher lands somewhere that
 * explains the product before being handed an empty composer.
 *
 * Server component on purpose: `appTitle` reads instance.md via `lib/shared`,
 * which touches `node:fs` and cannot enter the client bundle — the actual
 * ChatKit hook/component lives in the client-only `ChatInterface`, which
 * receives the title as a plain string prop.
 */
export default function ChatPage(): ReactElement {
  return <ChatInterface title={appTitle} />;
}
