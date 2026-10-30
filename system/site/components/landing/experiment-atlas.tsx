"use client";
import { useState } from "react";
import Link from "next/link";
import { Search, ArrowUpRight, FlaskConical, BookOpen, ChartNoAxesCombined } from "lucide-react";
import type { Investigation } from "@/lib/psi-types";
import { GEOMETRY_LABEL } from "@/components/explore/format";

export function ExperimentAtlas({ investigations }: { investigations: Investigation[] }) {
  const [geometry, setGeometry] = useState("");
  const [search, setSearch] = useState("");
  const filtered = investigations.filter(i => (!geometry || i.geometry_class === geometry) && `${i.name} ${i.full_name ?? ""}`.toLowerCase().includes(search.toLowerCase()));
  const max = Math.max(1, ...investigations.map(i => i.runs));
  return <section className="research-entry">
    <div className="research-intro">
      <span className="research-label"><span /> NASA microgravity combustion</span>
      <h1>Flame in Freefall.<br />Understand fire beyond Earth.</h1>
      <p>Investigate NASA combustion experiments, compare test conditions, and trace fire-safety questions back to the evidence.</p>
      <div className="research-actions">
        <Link href="/explore/" className="research-primary">Open the research workspace <ArrowUpRight size={18} /></Link>
        <Link href="/chat/" className="research-secondary flame-blue-action">Ask the research assistant <ArrowUpRight size={18} /></Link>
      </div>
      <div className="combustion-identity">
        <svg viewBox="0 0 100 110" role="img" aria-label="Stylized flame emblem; illustrative, not experimental data">
          <defs>
            <linearGradient id="ember-mark" x1="0" y1="0" x2="0" y2="1">
              <stop stopColor="var(--flame-amber)"/><stop offset="0.55" stopColor="#db343d"/><stop offset="1" stopColor="var(--flame-blue)"/>
            </linearGradient>
            <linearGradient id="flame-core" x1="0" y1="0" x2="0" y2="1">
              <stop stopColor="#fff5de"/><stop offset="1" stopColor="var(--flame-blue)"/>
            </linearGradient>
          </defs>
          <path d="M53 5C65 32 85 39 85 66C85 90 69 103 49 103C26 103 13 87 16 66C19 49 31 38 35 24C37 42 43 48 47 50C55 38 60 25 53 5Z" fill="url(#ember-mark)"/>
          <path d="M49 57C60 70 66 76 63 87C60 98 43 101 36 89C30 79 39 67 49 57Z" fill="url(#flame-core)"/>
        </svg>
        <div><strong>Fire science. Space exploration.</strong><p>Compare investigations, inspect measured outcomes, and identify where indexed evidence is missing.</p></div>
      </div>
      <div className="research-paths">
        <Link href="/explore/?fuel_family=n-heptane"><FlaskConical size={20} /><span>Learn through a test<small>Students · begin with droplet experiments</small></span></Link>
        <Link href="/docs/"><BookOpen size={20} /><span>Prepare a class discussion<small>Faculty · read the governed investigations</small></span></Link>
        <Link href="/explore/?individual=1"><ChartNoAxesCombined size={20} /><span>Inspect the evidence<small>Researchers & engineers · filter and export</small></span></Link>
      </div>
    </div>
    <div className="experiment-directory">
      <div className="directory-heading"><div><span>Experiment directory</span><h2>Find your starting point</h2></div><span className="directory-count">{investigations.length}<small>investigations</small></span></div>
      <label className="directory-search"><Search size={18} /><input value={search} onChange={e => setSearch(e.target.value)} placeholder="Search investigations…" aria-label="Search investigations" /></label>
      <div className="directory-filters" role="group" aria-label="Filter by geometry"><button aria-pressed={!geometry} onClick={() => setGeometry("")}>All</button>{Object.entries(GEOMETRY_LABEL).map(([key,label]) => <button key={key} aria-pressed={geometry === key} onClick={() => setGeometry(key)}>{label}</button>)}</div>
      <div className="directory-results" aria-live="polite">
        {filtered.length ? filtered.map(i => <Link key={i.id} href={`/explore/${i.id}/`} className="directory-row"><div><strong>{i.name}</strong><span>{i.full_name ?? GEOMETRY_LABEL[i.geometry_class]}</span></div><div className="directory-volume"><span>{i.runs.toLocaleString("en-US")} records</span><div className="directory-track"><i style={{width: `${100*i.runs/max}%`}} /></div></div><ArrowUpRight size={16} /></Link>) : <p className="directory-empty">No investigations match. Try another name or choose All.</p>}
      </div>
      <p className="directory-note">Bars show indexed table records, including summaries and planned envelopes. Record counts are not independent test counts.</p>
    </div>
  </section>;
}
