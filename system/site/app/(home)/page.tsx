import type { ReactElement } from "react";

import { appTitle } from "@/lib/shared";

import { ChatInterface } from "./components/chat-interface";

/**
 * The root `/` — a full-screen OpenAI ChatKit interface, in place of the
 * record's cover (2026-09-22, owner's call: ChatKit owns sessions, history
 * and streaming, so it replaces the front door rather than sitting beside
 * it).
 *
 * Server component on purpose: `appTitle` reads instance.md via `lib/shared`,
 * which touches `node:fs` and cannot enter the client bundle — the actual
 * ChatKit hook/component lives in the client-only `ChatInterface` below,
 * which receives the title as a plain string prop.
 */
export default function HomePage(): ReactElement {
  return <ChatInterface title={appTitle} />;
}
