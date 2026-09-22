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
          label: "BASS-II flame spread",
          prompt: "What did BASS-II find about flame spread over solid fuel?",
        },
        {
          label: "SAFFIRE vs BASS-II",
          prompt: "How does SAFFIRE differ from BASS-II?",
        },
        {
          label: "NASA-STD-6001B",
          prompt: "What does NASA-STD-6001B require for fire safety certification?",
        },
        {
          label: "FLEX droplet results",
          prompt: "Summarize FLEX's droplet combustion results.",
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
    <div className="flex h-screen w-full flex-col">
      <ChatKit control={control} className="min-h-0 flex-1" />
      {/* The assistant answers from — and cites — the governed record, but
          nothing on this screen otherwise says that record is browsable on
          its own. This strip is the human path to it: verify a citation,
          or just read past what a chat answer summarized (user's call,
          2026-09-22). */}
      {/* Plain gray/white, not the site's --ksor-cover-* tokens — those flip
          with the site's dark mode, but the chat above is forced light
          (2026-09-22), and this strip sits directly under it. */}
      <div className="flex shrink-0 items-center justify-center border-t border-gray-200 bg-gray-50 px-4 py-2 text-xs">
        <Link
          href="/docs"
          className="text-[#1d4ed8] underline-offset-2 hover:underline"
        >
          Browse the governed record — every cited source, in full →
        </Link>
      </div>
    </div>
  );
}
