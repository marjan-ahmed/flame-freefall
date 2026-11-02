"use client";

import Link from "next/link";
import Image from "next/image";
import { usePathname } from "next/navigation";
import { useState } from "react";
import { Menu, X } from "lucide-react";
import { ThemeToggle } from "@/components/theme-toggle";
import siteLogo from "@/app/icon.png";

const links = [["/", "Dashboard"], ["/decide/", "Find relevant evidence"], ["/explore/", "Test explorer"], ["/chat/", "Ask a question"], ["/docs/", "Source library"]] as const;

export function WorkspaceNav({ title = "Flame in Freefall" }: { title?: string }) {
  const pathname = usePathname();
  const [open, setOpen] = useState(false);
  return <header className="atlas-nav"><a className="sr-only focus:not-sr-only" href={pathname.startsWith('/docs') ? '#nd-page' : '#workspace-content'}>Skip to content</a>
    <div className="atlas-nav-inner">
      <Link href="/" className="atlas-brand"><Image src={siteLogo} alt="" width={36} height={36} className="atlas-brand-logo" priority /><span>{title}<small>Microgravity combustion research</small></span></Link>
      <nav aria-label="Workspace" className="atlas-desktop-nav">{links.map(([href, label]) => <Link key={href} href={href} aria-current={(href === "/" ? pathname === "/" : pathname.startsWith(href.slice(0, -1))) ? "page" : undefined}>{label}</Link>)}</nav>
      <Link className="atlas-current-section" href={links.find(([href]) => href !== "/" && pathname.startsWith(href.slice(0, -1)))?.[0] ?? "/"}>
        {links.find(([href]) => href !== "/" && pathname.startsWith(href.slice(0, -1)))?.[1] ?? "Dashboard"}
      </Link>
      <ThemeToggle />
      <button className="atlas-menu" aria-label={open ? "Close navigation" : "Open navigation"} aria-expanded={open} onClick={() => setOpen(!open)}>{open ? <X /> : <Menu />}</button>
    </div>
    {open && <nav aria-label="Mobile workspace" className="atlas-mobile-nav">{links.map(([href, label]) => <Link href={href} key={href} aria-current={(href === "/" ? pathname === "/" : pathname.startsWith(href.slice(0, -1))) ? "page" : undefined} onClick={() => setOpen(false)}>{label}</Link>)}</nav>}
  </header>;
}
