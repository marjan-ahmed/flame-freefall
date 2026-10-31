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

  return <section className="research-entry">
    <div className="research-intro">
      <span className="research-label"><span /> NASA microgravity combustion</span>
      <h1>Find the evidence.<br />Understand fire in space.</h1>
      <p>Explore NASA microgravity combustion research. Find relevant tests, compare measured outcomes, and follow each result to its source.</p>
      <div className="research-actions">
        <Link href="/explore/" className="research-primary">Explore test data <ArrowUpRight size={18} /></Link>
        <Link href="/chat/" className="research-secondary flame-blue-action">Ask a research question <ArrowUpRight size={18} /></Link>
      </div>
      <div className="research-paths">
        <Link href="/explore/?fuel_family=n-heptane"><FlaskConical size={20} /><span>Start with an experiment<small>Students · begin with droplet experiments</small></span></Link>
        <Link href="/docs/"><BookOpen size={20} /><span>Read investigation reports<small>Faculty · read the governed investigations</small></span></Link>
        <Link href="/explore/?individual=1"><ChartNoAxesCombined size={20} /><span>Compare and export tests<small>Researchers & engineers · filter and export</small></span></Link>
      </div>
    </div>
    <div className="experiment-directory">
      <div className="directory-heading"><div><span>Experiment directory</span><h2>Browse investigations</h2></div><span className="directory-count">{investigations.length}<small>investigations</small></span></div>
      <label className="directory-search"><Search size={18} /><input value={search} onChange={e => setSearch(e.target.value)} placeholder="Search investigations…" aria-label="Search investigations" /></label>
      <div className="directory-filters" role="group" aria-label="Filter by geometry"><button aria-pressed={!geometry} onClick={() => setGeometry("")}>All</button>{Object.entries(GEOMETRY_LABEL).map(([key,label]) => <button key={key} aria-pressed={geometry === key} onClick={() => setGeometry(key)}>{label}</button>)}</div>
      <div className="directory-results" aria-live="polite">
        {filtered.length ? filtered.map(i => <Link key={i.id} href={`/explore/${i.id}/`} className="directory-row"><div><strong>{i.name}</strong><span>{i.full_name ?? GEOMETRY_LABEL[i.geometry_class]}</span></div><div className="directory-volume"><span>{i.runs.toLocaleString("en-US")} records</span></div><ArrowUpRight size={16} /></Link>) : <p className="directory-empty">No investigations match. Try another name or choose All.</p>}
      </div>
      <p className="directory-note">Counts include indexed table records, summaries, and planned envelopes. Record counts are not independent test counts.</p>
    </div>
  </section>;
}
