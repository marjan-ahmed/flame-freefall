"use client";

import type { ReactElement } from "react";

import Link from "next/link";

import { ChatKit, useChatKit } from "@openai/chatkit-react";

/**
 * `api.url` points at the Python ChatKit backend in `system/chatkit-server`
 * (FastAPI + openai-chatkit + openai-agents, answering via Groq's
 * openai/gpt-oss-120b). In production, this is set via NEXT_PUBLIC_CHATKIT_API_URL.
 * For local development, it defaults to http://localhost:8000/chatkit.
 */
export function ChatInterface({ title }: { title: string }): ReactElement {
  const apiUrl = process.env.NEXT_PUBLIC_CHATKIT_API_URL || "http://localhost:8000/chatkit";
  const domainKey = process.env.NEXT_PUBLIC_CHATKIT_DOMAIN_KEY || "local-dev";
  const { control } = useChatKit({
    api: {
      url: apiUrl,
      domainKey: domainKey,
      // Required when composer.attachments is enabled. two_phase: the
      // backend hands back an upload URL (AttachmentStore.create_attachment),
      // the browser PUTs the bytes there, then the attachment id is attached
      // to the message. "hosted" (mentioned in ChatKit's newer docs) doesn't
      // exist on this installed version (@openai/chatkit-react 1.6.1) and is
      // for OpenAI's own hosted backend anyway, not this custom one.
      uploadStrategy: { type: "two_phase" },
    },
    history: {
      enabled: true,
      showDelete: true,
      showRename: true,
    },
    // Forced light — the site's own dark mode isn't reflected here on
    // purpose (user's call, 2026-09-22).
    theme: {
      colorScheme: "light",
      radius: "round",
      color: {
        accent: { primary: "#1d4ed8", level: 1 }, // --primary, light value
      },
    },
    // history: { enabled: true } below already gives ChatKit its own native
    // history-panel and new-chat header controls — a custom leftAction/
    // rightAction doing the same things just duplicated them (found live,
    // 2026-09-22). Pick one; native history wins since it's zero extra code.
    header: {
      enabled: true,
      title: { enabled: true, text: title },
    },
    startScreen: {
      greeting: "Hey! Nasa Researchers",
      // StartScreenPrompt is { label, prompt, icon? } — a bare string list
      // fails the same silent-blank-widget way `colorScheme: 'system'` did.
      prompts: [
        {
          label: "15% O₂, 10 cm/s, PMMA",
          prompt: "What do all the experiments say about PMMA burning at 15% O2 with a 10 cm/s flow?",
        },
        {
          label: "Where are the gaps?",
          prompt: "Show me the gap map for PMMA: which O2 and flow conditions has nobody tested?",
        },
        {
          label: "Spread rate vs flow",
          prompt: "Plot the flame spread rate against flow speed for opposed-flow PMMA tests.",
        },
        {
          label: "Low-pressure, high-O₂ tests",
          prompt: "Which tests were run near 30% O2 at about 0.55 atm, and what did they measure?",
        },
        {
          label: "SAFFIRE vs BASS-II fabric",
          prompt: "Compare SAFFIRE and BASS-II tests on cotton-fiberglass (SIBAL) fabric near 21% O2 and 20 cm/s.",
        },
        {
          label: "NASA-STD-6001B",
          prompt: "What does NASA-STD-6001B require for fire safety certification?",
        },
        {
          label: "Screen for a Lunar atmosphere",
          prompt:
            "NASA-STD-6001B says materials must be evaluated at the worst-case atmosphere they'll see. Is there PSI data " +
            "near the Lunar surface habitat atmosphere (34% O2, ~0.56 atm), and which solid-fuel materials rank fastest-" +
            "spreading there?",
        },
      ],
    },
    composer: {
      placeholder: `Ask ${title} a question…`,
      attachments: {
        enabled: true,
        maxSize: 20 * 1024 * 1024,
        maxCount: 3,
        accept: { "application/pdf": [".pdf"], "image/*": [".png", ".jpg", ".jpeg"] },
      },
    },
    // Temporary: diagnosing responses that stall after the reasoning step.
    onError: ({ error }) => {
      console.error("[chatkit] error", error);
    },
    onResponseStart: () => {
      console.log("[chatkit] response start");
    },
    onResponseEnd: () => {
      console.log("[chatkit] response end");
    },
  });

  return (
    <div className="relative flex h-screen w-full flex-col">
      {/* The assistant answers from — and cites — the governed record, but
          nothing else on this screen says that record is browsable on its
          own, or how to get back to the landing page. Top-right, left of
          ChatKit's own native history/new-chat icons — offset far enough
          (right-20) to clear that icon cluster rather than sit under it
          (user's call, 2026-09-22). Text only, no border/pill/background —
          a plain underlined link, ChatGPT-style. */}
      <div className="absolute right-20 top-4 z-10 flex gap-4 text-sm">
        <Link href="/" className="text-gray-900 underline underline-offset-4 hover:text-black">
          ← Home
        </Link>
        <Link href="/explore/" className="text-gray-900 underline underline-offset-4 hover:text-black">
          Test-data explorer
        </Link>
        <Link href="/docs" className="text-gray-900 underline underline-offset-4 hover:text-black">
          System of Record
        </Link>
      </div>
      <ChatKit control={control} className="h-full w-full" />
    </div>
  );
}
