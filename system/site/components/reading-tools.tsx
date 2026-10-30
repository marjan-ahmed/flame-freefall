"use client";
import { useState } from "react";
export function ReadingTools() {
  const [large, setLarge] = useState(false);
  const [copied, setCopied] = useState(false);
  return <div className="atlas-reading-tools" aria-label="Reading tools">
    <span>Reading workspace</span>
    <button aria-pressed={large} onClick={() => { setLarge(!large); document.documentElement.classList.toggle("atlas-large-reading", !large); }}>Aa · {large ? "Standard text" : "Larger text"}</button>
    <button onClick={() => window.print()}>Print</button>
    <button onClick={async () => { try { await navigator.clipboard.writeText(window.location.href); setCopied(true); } catch { setCopied(false); } }}>{copied ? "Link copied" : "Copy link"}</button>
  </div>;
}
