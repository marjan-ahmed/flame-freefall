"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { useState } from "react";
import { Menu, X, Flame, Search } from "lucide-react";

const links = [["/", "Overview"], ["/explore/", "Explore data"], ["/chat/", "Research assistant"], ["/docs/", "System of Record"]] as const;

export function WorkspaceNav({ title = "Flame in Freefall" }: { title?: string }) {
  const pathname = usePathname();
  const [open, setOpen] = useState(false);
  return <header className="atlas-nav">
    <div className="atlas-nav-inner">
      <Link href="/" className="atlas-brand"><Flame size={26} aria-hidden="true" /><span>{title}<small>Microgravity combustion research</small></span></Link>
      <nav aria-label="Workspace" className="atlas-desktop-nav">{links.map(([href, label]) => <Link key={href} href={href} aria-current={(href === "/" ? pathname === "/" : pathname.startsWith(href.slice(0, -1))) ? "page" : undefined}>{label}</Link>)}</nav>
      <Link className="atlas-search" href="/docs/"><Search size={17} /><span>Browse record</span></Link>
      <button className="atlas-menu" aria-label={open ? "Close navigation" : "Open navigation"} aria-expanded={open} onClick={() => setOpen(!open)}>{open ? <X /> : <Menu />}</button>
    </div>
    {open && <nav aria-label="Mobile workspace" className="atlas-mobile-nav">{links.map(([href, label]) => <Link href={href} key={href} aria-current={(href === "/" ? pathname === "/" : pathname.startsWith(href.slice(0, -1))) ? "page" : undefined} onClick={() => setOpen(false)}>{label}</Link>)}</nav>}
  </header>;
}
