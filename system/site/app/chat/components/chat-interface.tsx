"use client";

import { useEffect, useState, type ReactElement } from "react";

import Link from "next/link";
import { WorkspaceNav } from "@/components/workspace-nav";
import { BookOpen, Database, Home, X } from "lucide-react";

import { ChatKit, useChatKit } from "@openai/chatkit-react";

/**
 * `api.url` points at the Python ChatKit backend in `system/chatkit-server`
 * (FastAPI + openai-chatkit + openai-agents, answering via Groq's
 * openai/gpt-oss-120b). In production, this is set via NEXT_PUBLIC_CHATKIT_API_URL.
 * For local development, it defaults to http://localhost:8000/chatkit.
 */
export function ChatInterface({ title }: { title: string }): ReactElement {
  const [isMobile, setIsMobile] = useState(false);
  const [mobileNavOpen, setMobileNavOpen] = useState(false);
  const apiUrl = process.env.NEXT_PUBLIC_CHATKIT_API_URL || "http://localhost:8000/chatkit";
  const domainKey = process.env.NEXT_PUBLIC_CHATKIT_DOMAIN_KEY || "local-dev";

  useEffect(() => {
    const media = window.matchMedia("(max-width: 767px)");
    const syncViewport = () => {
      setIsMobile(media.matches);
      if (!media.matches) setMobileNavOpen(false);
    };

    syncViewport();
    media.addEventListener("change", syncViewport);
    return () => media.removeEventListener("change", syncViewport);
  }, []);

  useEffect(() => {
    if (!mobileNavOpen) return;

    const closeOnEscape = (event: KeyboardEvent) => {
      if (event.key === "Escape") setMobileNavOpen(false);
    };
    window.addEventListener("keydown", closeOnEscape);
    return () => window.removeEventListener("keydown", closeOnEscape);
  }, [mobileNavOpen]);

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
        accent: { primary: "#087cb5", level: 1 }, // Shared flame-blue secondary accent; ChatKit owns its iframe theme.
      },
      typography: {
        baseSize: 16,
        fontFamily: '"Plus Jakarta Sans", system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif',
        fontFamilyMono: 'ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "DejaVu Sans Mono", "Courier New", monospace',
        fontSources: [
          {
            family: "Plus Jakarta Sans",
            src: typeof window === "undefined" ? "/fonts/plus-jakarta-sans.ttf" : `${window.location.origin}${window.location.pathname.replace(/chat\/?$/, "")}fonts/plus-jakarta-sans.ttf`,
            weight: 400,
            style: "normal",
            display: "swap",
          },
        ],
      },
    },
    // history: { enabled: true } below already gives ChatKit its own native
    // history-panel and new-chat header controls — a custom leftAction/
    // rightAction doing the same things just duplicated them (found live,
    // 2026-09-22). Pick one; native history wins since it's zero extra code.
    header: {
      enabled: true,
      title: { enabled: true, text: title },
      ...(isMobile && {
        leftAction: {
          icon: mobileNavOpen ? "sidebar-collapse-left" : "sidebar-open-left",
          onClick: () => setMobileNavOpen((open) => !open),
        },
      }),
    },
    startScreen: {
      greeting: "Which experiment would you like to understand?",
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
      tools: [
        {
          id: "query_test_runs",
          label: "Query Tests",
          shortLabel: "Query",
          placeholderOverride: "O₂ %, flow cm/s, pressure atm, fuel…",
          // Keep tool icons distinct and semantically aligned with each action.
          icon: "search",
          pinned: true,
        },
        {
          id: "show_gap_map",
          label: "Gap Map",
          shortLabel: "Gaps",
          placeholderOverride: "O₂ %, fuel, geometry…",
          icon: "maps",
          pinned: true,
        },
        {
          id: "compare_investigations",
          label: "Compare Investigations",
          shortLabel: "Compare",
          placeholderOverride: "Investigation names (optional)…",
          icon: "reload",
          pinned: false,
        },
        {
          id: "show_test_details",
          label: "Test Details",
          shortLabel: "Details",
          placeholderOverride: "Test ID (e.g. PSI-25:M18)…",
          icon: "document",
          pinned: false,
        },
        {
          id: "plot_results",
          label: "Plot Results",
          shortLabel: "Plot",
          placeholderOverride: "Quantity vs condition (e.g. spread_rate vs flow)…",
          icon: "chart",
          pinned: false,
        },
        {
          id: "rank_results",
          label: "Rank Materials",
          shortLabel: "Rank",
          placeholderOverride: "Geometry class, quantity, atmosphere…",
          icon: "notebook",
          pinned: false,
        },
        {
          id: "show_mission_readiness",
          label: "Mission Readiness",
          shortLabel: "Readiness",
          placeholderOverride: "Atmosphere: iss, gateway, or lunar…",
          icon: "clock",
          pinned: false,
        },
      ],
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
    <div className="relative flex h-dvh w-full flex-col">
      <WorkspaceNav title={title} />
      <div className="atlas-chat-workspace">
        <aside className="atlas-chat-rail">
          <p className="atlas-kicker">Research assistant</p>
          <h1>Follow a question to its evidence.</h1>
          <p>Ask about an investigation, compare test conditions, or inspect an individual result.</p>
          <div className="atlas-rail-section"><h2>Continue your research</h2>
            <Link href="/explore/">Explore the test table<span>Filter conditions and inspect source rows</span></Link>
            <Link href="/explore/investigations/">Browse investigations<span>Compare experimental geometry and coverage</span></Link>
            <Link href="/docs/">Read the source record<span>Open governed findings and source notes</span></Link>
          </div>
          <p className="atlas-rail-note">Use conversation history to return to a question. Source records remain available in the Explorer.</p>
        </aside>
        <div className="atlas-chat-canvas"><ChatKit control={control} className="h-full w-full" /></div>
      </div>
      {mobileNavOpen && (
        <div className="fixed inset-0 z-50 md:hidden">
          <button
            type="button"
            aria-label="Close navigation"
            className="absolute inset-0 bg-slate-950/35 backdrop-blur-[2px]"
            onClick={() => setMobileNavOpen(false)}
          />
          <aside
            role="dialog"
            aria-modal="true"
            aria-label="Mobile navigation"
            className="relative flex h-full w-[min(21rem,calc(100vw-2rem))] flex-col border-r border-slate-200 bg-white px-5 pb-[calc(env(safe-area-inset-bottom)+1.5rem)] pt-[calc(env(safe-area-inset-top)+1rem)] shadow-2xl"
          >
            <div className="flex items-center justify-between border-b border-slate-200 pb-5">
              <div>
                <p className="text-base font-semibold text-slate-950">Flame in Freefall</p>
                <p className="mt-1 text-xs text-slate-500">Research workspace</p>
              </div>
              <button
                type="button"
                aria-label="Close navigation"
                autoFocus
                className="flex size-10 items-center justify-center rounded-lg text-slate-600 transition-colors hover:bg-slate-100 hover:text-slate-950 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary"
                onClick={() => setMobileNavOpen(false)}
              >
                <X aria-hidden="true" size={20} />
              </button>
            </div>
            <nav aria-label="Primary" className="flex flex-col gap-1 pt-5">
              <Link
                href="/"
                onClick={() => setMobileNavOpen(false)}
                className="flex min-h-12 items-center gap-3 rounded-lg px-3 text-sm font-medium text-slate-800 transition-colors hover:bg-accent hover:text-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary"
              >
                <Home aria-hidden="true" className="text-slate-500" size={18} />
                Home
              </Link>
              <Link
                href="/docs"
                onClick={() => setMobileNavOpen(false)}
                className="flex min-h-12 items-center gap-3 rounded-lg px-3 text-sm font-medium text-slate-800 transition-colors hover:bg-accent hover:text-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary"
              >
                <BookOpen aria-hidden="true" className="text-slate-500" size={18} />
                System of Record
              </Link>
              <Link
                href="/explore/"
                onClick={() => setMobileNavOpen(false)}
                className="flex min-h-12 items-center gap-3 rounded-lg px-3 text-sm font-medium text-slate-800 transition-colors hover:bg-accent hover:text-primary focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-primary"
              >
                <Database aria-hidden="true" className="text-slate-500" size={18} />
                Test Data Explorer
              </Link>
            </nav>
          </aside>
        </div>
      )}
    </div>
  );
}
