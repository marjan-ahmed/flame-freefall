"use client";

import Link from "next/link";
import { useEffect, useMemo, useState, type ReactNode } from "react";
import { ATMOSPHERES } from "@/lib/psi-atmospheres";
import { CONVERSION, LIMITATIONS, ORDERING, decide, decisionExport, defaults, dossier, explorerLink, restore, sensitivity, stateParams, validate, type Assignment, type State } from "@/lib/decision";
import type { Investigation, SlimRun } from "@/lib/psi-types";
import { GEOMETRY_LABEL, QUANTITY_LABEL, outcomeText } from "@/components/explore/format";

type Dataset = { runs: SlimRun[]; generated_at: string; sha256: string };
const labels: Record<string, string> = { o2_pct: "Oxygen (%)", pressure_kpa: "Pressure (kPa)", flow_cm_s: "Reported flow (cm/s)", tol_o2: "Oxygen tolerance (percentage points)", tol_pressure_kpa: "Pressure tolerance (kPa)", tol_flow: "Flow tolerance (relative fraction)", fuel_family: "Material / fuel (exact, or trailing * for family)", geometry_class: "Geometry" };
const docHref = (doc: string) => `/docs/${doc.replace(/^knowledge\//, "")}/`;

function RecordDetails({ summary, children }: { summary: ReactNode; children: ReactNode }) {
  const [open, setOpen] = useState(false);
  return <details className="decision-record" onToggle={e => setOpen(e.currentTarget.open)}><summary>{summary}</summary>{open && children}</details>;
}

export function DecisionView({ investigations, assignments, basePath }: { investigations: Investigation[]; assignments: Assignment[]; basePath: string }) {
  const [s, setS] = useState(defaults());
  const [ready, setReady] = useState(false);
  const [dataset, setDataset] = useState<Dataset | null>(null);
  const [error, setError] = useState("");
  const [attempt, setAttempt] = useState(0);
  const [compare, setCompare] = useState<string[]>([]);
  const [share, setShare] = useState("");
  const [openInvestigations, setOpenInvestigations] = useState<string[]>([]);
  useEffect(() => {
    const read = () => { setS(restore(new URLSearchParams(window.location.search))); setReady(true); };
    read(); window.addEventListener("popstate", read);
    return () => window.removeEventListener("popstate", read);
  }, []);
  useEffect(() => {
    const controller = new AbortController();
    setError(""); setDataset(null);
    fetch(`${basePath}/psi/runs.json`, { signal: controller.signal }).then(r => { if (!r.ok) throw new Error(`HTTP ${r.status}`); return r.json(); }).then(d => {
      if (!Array.isArray(d.runs) || !d.sha256 || !d.generated_at) throw new Error("Invalid dataset");
      setDataset(d);
    }).catch(e => { if (e.name !== "AbortError") setError("The evidence dataset could not be loaded. Retry to inspect records and enable downloads."); });
    return () => controller.abort();
  }, [basePath, attempt]);
  const input = validate(s);
  const valid = !Object.keys(input.errors).length;
  const d = useMemo(() => dataset && valid ? decide(dataset.runs, investigations, assignments, s) : null, [dataset, valid, investigations, assignments, s]);
  const brief = useMemo(() => dataset && valid ? dossier(dataset.runs, investigations, assignments, s) : null, [dataset, valid, investigations, assignments, s]);
  const windows = useMemo(() => dataset && valid ? sensitivity(dataset.runs, investigations, assignments, s) : [], [dataset, valid, investigations, assignments, s]);
  const selected = new Set(s.shortlist.split(",").filter(Boolean));
  const quantities = [...new Set(dataset?.runs.flatMap(r => r.outcomes.map(o => o.quantity)) ?? [])].sort();
  const comparisonGeometry = compare.length ? investigations.find(i => i.id === dataset?.runs.find(r => r.id === compare[0])?.investigation)?.geometry_class : undefined;
  const update = (next: State) => {
    setS(next); setShare(""); setCompare([]);
    window.history.replaceState(null, "", `?${stateParams(next)}`);
  };
  const download = () => {
    if (!dataset || !d) return;
    const payload = decisionExport(dataset.runs, investigations, assignments, s, dataset);
    const url = URL.createObjectURL(new Blob([JSON.stringify(payload, null, 2)], { type: "application/json" }));
    const a = document.createElement("a"); a.href = url; a.download = "fire-safety-dossier-v2.json"; a.click();
    setTimeout(() => URL.revokeObjectURL(url), 1000);
  };
  const field = (key: keyof State) => <label key={key} className="decision-field" htmlFor={`decision-${key}`}>
    <span>{labels[key]}</span><input id={`decision-${key}`} inputMode={key === "fuel_family" ? "text" : "decimal"} value={s[key]} aria-invalid={!!input.errors[key]} aria-describedby={input.errors[key] ? `error-${key}` : undefined} onChange={e => update({ ...s, [key]: e.target.value })} />
    {input.errors[key] && <span id={`error-${key}`} className="text-destructive" role="alert">{input.errors[key]}</span>}
  </label>;
  return <div className="decision-view">
    <h1 className="font-display text-3xl font-semibold sm:text-4xl">Find relevant evidence</h1>
    <p className="mt-3 max-w-3xl text-muted-foreground">Choose a research job, inspect condition coverage and missing evidence, then export the source-linked selection. This is a deterministic evidence directory.</p>
    <p className="my-5 border-l-2 border-border pl-4 text-sm leading-6">{LIMITATIONS}</p>
    <div className="mb-5 flex flex-wrap gap-3" aria-label="Research starting points">
      <button className="decision-button" onClick={() => update({ ...defaults(), question: "Which solid-material experiments inform a study near the proposed Lunar atmosphere, and what limits their transfer?", quantity: "spread_rate" })}>Material evidence near a Lunar atmosphere</button>
      <button className="decision-button" onClick={() => update({ ...defaults("detection"), question: "Which smoke measurements and instrument evidence should inform an early-warning research study?", quantity: "iss_detector_scatter_volts" })}>Smoke measurement and instrument evidence</button>
      <button className="decision-button" onClick={() => update({ ...defaults("suppression", "custom"), atmosphere: "0", browse: "1", question: "Which droplet extinction measurements are available, and what must be checked before comparing gas-dilution conditions?", quantity: "extinction_diameter", geometry_class: "droplet-combustion" })}>Droplet extinction evidence</button>
    </div>
    <label className="decision-field mb-4" htmlFor="research-question"><span>Research question for the dossier</span><textarea id="research-question" value={s.question} maxLength={1200} rows={2} onChange={e => update({ ...s, question: e.target.value })} aria-invalid={!!input.errors.question} className="rounded border border-border bg-background p-3" /><small>Your question is recorded verbatim. Only the explicit controls below constrain the search; no AI assumptions are applied.</small>{input.errors.question && <span role="alert">{input.errors.question}</span>}</label>
    <fieldset className="decision-controls" disabled={!ready}><legend className="font-medium">Research job and scenario</legend>
      <div className="decision-grid">
        <label className="decision-field" htmlFor="decision-job"><span>Research job</span><select id="decision-job" aria-label="Research job" value={s.job} onChange={e => update({ ...defaults(e.target.value, s.scenario), fuel_family: s.fuel_family, geometry_class: s.geometry_class })}>
          {!["prevention", "detection", "suppression"].includes(s.job) && <option>{s.job}</option>}
          <option value="prevention">Prevention</option><option value="detection">Detection</option><option value="suppression">Suppression</option></select>{input.errors.job && <span role="alert">{input.errors.job}</span>}</label>
        <label className="decision-field" htmlFor="decision-scenario"><span>Scenario</span><select id="decision-scenario" aria-label="Scenario" value={s.scenario} onChange={e => update({ ...defaults(s.job, e.target.value), fuel_family: s.fuel_family, geometry_class: s.geometry_class })}>
          {!["iss", "gateway", "lunar", "rover", "spacesuit", "mars", "custom"].includes(s.scenario) && <option>{s.scenario}</option>}
          {Object.entries(ATMOSPHERES).map(([id, a]) => <option key={id} value={id}>{a.label}</option>)}
          {['rover', 'spacesuit', 'mars', 'custom'].map(id => <option key={id} value={id}>{id[0].toUpperCase() + id.slice(1)}</option>)}</select>{input.errors.scenario && <span role="alert">{input.errors.scenario}</span>}</label>
        <label className="decision-field" htmlFor="decision-atmosphere"><span>Apply atmosphere constraints</span><select id="decision-atmosphere" aria-label="Apply atmosphere constraints" value={s.atmosphere} onChange={e => update({ ...s, atmosphere: e.target.value })}>{!["0", "1"].includes(s.atmosphere) && <option>{s.atmosphere}</option>}<option value="0">No</option><option value="1">Yes</option></select>{input.errors.atmosphere && <span role="alert">{input.errors.atmosphere}</span>}</label>
      </div>
      <label className="decision-field mt-4" htmlFor="measurement-focus"><span>Measurement focus</span><select id="measurement-focus" value={s.quantity} onChange={e => update({ ...s, quantity: e.target.value })}><option value="">All recorded outcomes</option>{s.quantity && !quantities.includes(s.quantity) && <option value={s.quantity}>{s.quantity} (not indexed)</option>}{quantities.map(q => <option key={q} value={q}>{QUANTITY_LABEL[q] ?? q.replaceAll("_", " ")}</option>)}</select><small>Focus counts cited individual outcomes for this measurement. It does not remove records with missing measurements or change condition matching.</small></label>
      {ATMOSPHERES[s.scenario] ? <p className="text-sm leading-6"><Link href={docHref(ATMOSPHERES[s.scenario].doc)} className="underline text-primary">Preset source</Link>: “{ATMOSPHERES[s.scenario].quote}” Pressure stored as {ATMOSPHERES[s.scenario].pressure_atm} atm. Edited conditions are custom values.</p> : <p className="text-sm">This release supplies no cited numerical preset for this context. Enter conditions or explicitly choose unconstrained browsing.</p>}
      {s.job === "detection" && <p className="text-sm leading-6">Detection starts without atmosphere constraints. Missing atmosphere fields prevent matching; they do not make a detection investigation irrelevant. SAME and SAME-R remain in missing-evidence results when constraints are activated.</p>}
      <div className="decision-grid mt-4">{field("o2_pct")}{field("pressure_kpa")}{field("flow_cm_s")}{field("tol_o2")}{field("tol_pressure_kpa")}{field("tol_flow")}{field("fuel_family")}
        <label className="decision-field" htmlFor="decision-geometry_class"><span>Geometry</span><select id="decision-geometry_class" value={s.geometry_class} onChange={e => update({ ...s, geometry_class: e.target.value })}><option value="">All geometries (no cross-geometry outcome comparison)</option>{s.geometry_class && !investigations.some(i => i.geometry_class === s.geometry_class) && <option>{s.geometry_class}</option>}{[...new Set(investigations.map(i => i.geometry_class))].map(g => <option key={g} value={g}>{GEOMETRY_LABEL[g] ?? g}</option>)}</select>{input.errors.geometry_class && <span role="alert">{input.errors.geometry_class}</span>}</label>
      </div>
      <label className="my-3 flex items-center gap-2"><input type="checkbox" checked={s.browse === "1"} onChange={e => update({ ...s, browse: e.target.checked ? "1" : "0" })} />Browse without numeric constraints when none are supplied</label>
      {input.errors.browse && <p className="text-destructive" role="alert">{input.errors.browse}</p>}
      <details className="text-sm"><summary>Pressure conversion and flow interpretation</summary><p className="py-2 leading-6">{CONVERSION} Blank tolerance fields use the existing query defaults. Both query implementations read flow_cm_s only from record conditions. Panel settings are not velocities. Query distances are normalized tolerance distances, not inferred scalar measurements.</p></details>
    </fieldset>
    <div className="my-5 flex flex-wrap items-center gap-4"><button className="decision-button" disabled={!d} onClick={download}>Export evidence dossier</button><button className="decision-button" disabled={!ready} onClick={() => { const url = `${window.location.origin}${window.location.pathname}?${stateParams(s)}`; setShare(url); window.history.replaceState(null, "", url); }}>Create shareable URL</button>{compare.length === 2 && <Link className="underline text-primary" href={explorerLink(s, compare)}>Audit selected records in Explorer</Link>}</div>
    {share && <label className="decision-field">Shareable URL<input readOnly value={share} onFocus={e => e.target.select()} /></label>}
    {!dataset && !error && <p role="status">Loading evidence records…</p>}
    {error && <div role="alert"><p>{error}</p><button className="decision-button mt-3" onClick={() => setAttempt(a => a + 1)}>Retry loading evidence</button></div>}
    {d && <>
      <section aria-labelledby="dossier-heading" className="my-6 border border-border p-4">
        <h2 id="dossier-heading" className="text-xl font-semibold">Your evidence dossier</h2>
        <p className="my-2">{brief?.question}</p><p className="text-sm text-muted-foreground">Shortlist investigations below to record why they belong and what needs checking. The export includes the shortlist, sensitivity, source-linked records and complete query evidence as an audit appendix.</p>
        {brief?.selection_warnings.map(w => <p key={w} role="alert">{w}</p>)}
        {!brief?.entries.length && <p className="mt-3 text-sm">No investigations shortlisted yet. Expand an investigation and choose “Add to dossier”.</p>}
        {brief?.entries.map(entry => <article key={entry.id} className="mt-4 border-t border-border pt-4"><div className="flex items-center justify-between gap-3"><h3 className="font-semibold">{entry.name}</h3><button className="decision-button" onClick={() => update({ ...s, shortlist: [...selected].filter(id => id !== entry.id).join(",") })}>Remove {entry.name}</button></div><p className="my-2 text-sm">{GEOMETRY_LABEL[entry.geometry]} · {entry.classification?.relevance ?? "unclassified"} relevance · {entry.measurement_records} individual records with cited {s.quantity ? QUANTITY_LABEL[s.quantity] ?? s.quantity : "outcomes"}. Relevance is not evidence of safe performance.</p>
          <ul className="list-disc pl-5 text-sm">{entry.next_steps.map(step => <li key={step.code} className="my-2">{step.text}</li>)}</ul>
          {entry.classification && <Link className="text-sm underline text-primary" href={docHref(entry.classification.doc)}>Inspect the inclusion source</Link>}
        </article>)}
        {d.conditioned && <details className="mt-5"><summary>Sensitivity: does the evidence availability depend on the search window?</summary><p className="my-3 text-sm">These are retrieval alternatives, not safety margins. No experiment changes when a tolerance changes. Each geometry and investigation remains separate. {selected.size ? "Showing the shortlisted investigations." : "Showing classified investigations until you choose a shortlist."}</p><div className="overflow-x-auto"><table className="w-full text-left text-sm"><caption className="sr-only">Full and incomplete individual records under alternative retrieval tolerances</caption><thead><tr><th className="p-2">Investigation</th>{windows.map(w => <th key={w.label} className="p-2">{w.label}</th>)}</tr></thead><tbody>{windows[0]?.investigations.map(i => <tr key={i.id} className="border-t border-border"><th className="p-2">{investigations.find(v => v.id === i.id)?.name}<small className="block font-normal">{GEOMETRY_LABEL[i.geometry]}</small></th>{windows.map(w => { const c = w.investigations.find(v => v.id === i.id); return <td key={w.label} className="p-2">{c?.full ?? 0} full / {c?.incomplete ?? 0} incomplete</td>; })}</tr>)}</tbody></table></div></details>}
      </section>
      <h2 className="mt-8 text-xl font-semibold">Investigations and missing evidence</h2>
      <details className="my-3 text-sm"><summary>How investigations are ordered</summary><p className="mt-2 leading-6">{ORDERING}</p></details>
      {s.quantity && <p className="my-3 text-sm">The cited-outcome sort key uses only {QUANTITY_LABEL[s.quantity] ?? s.quantity}. Other quantities remain available for inspection.</p>}
      <p className="my-3 text-sm">{d.conditioned ? "Buckets count individual tests and test points only. Conflicts are overlays, including on full matches; inspect retained values before use." : "Unconditioned browsing: these records are not atmosphere evidence. Atmosphere buckets are suppressed."} Daily records, summaries and envelopes are shown separately. Relevance describes the job, not a safety ranking.</p>
      <p className="my-3 text-sm">Categorical filters excluded {d.categoricalExcludedIds.length} records (IDs retained in export). {d.rows.filter(r => r.mapping).length} investigations have a checked assignment for this job; other investigations remain unclassified.</p>
      {d.rows.filter(r => r.mapping).every(r => !r.counts.full && !r.counts.partial) && d.conditioned && <p className="border border-border p-3 text-sm">[NO_MATCH] No full or partial individual evidence among classified investigations in this selection. Explicitly change tolerances or material above to inspect alternatives. New tests may be needed; no matching evidence in this index does not establish absence of research.</p>}
      <div className="decision-table" aria-label="Investigations">
        <div className="decision-row decision-table-heading" aria-hidden="true"><span>Investigation / supported jobs</span><span>Relevance / geometry</span><span>Individual evidence</span><span>Missing metadata</span></div>
        {d.rows.map(row => <details key={row.investigation.id} className="decision-investigation" onToggle={e => { const open = e.currentTarget.open; setOpenInvestigations(ids => open ? [...new Set([...ids, row.investigation.id])] : ids.filter(id => id !== row.investigation.id)); }}>
          <summary className="decision-row"><span><strong>{row.investigation.name}</strong><small>Supported jobs: {row.tags.join(", ") || "Not yet classified"}</small></span><span>{row.mapping?.relevance ?? "Not yet classified"}<small>{GEOMETRY_LABEL[row.investigation.geometry_class] ?? row.investigation.geometry_class}</small>{row.investigation.id === "acme-bre" && <strong className="block">Emulator, not a solid sample.</strong>}</span><span>{d.conditioned ? `Full ${row.counts.full}; partial ${row.counts.partial}; outside-only ${row.counts["outside-only"]}; outside + missing ${row.counts["outside-plus-missing"]}; none reported ${row.counts["none-reported"]}` : `${row.individual} unconditioned records`}<small>{row.citedOutcomes} with cited outcomes; {row.nonIndividual} non-individual records</small></span><span>Oxygen: {row.missing.o2_pct}; pressure: {row.missing.pressure_atm}; flow: {row.missing.flow_cm_s}<small>{row.controlOnly} control-setting-only; {row.conflicts} records with conflicts</small></span></summary>
          {openInvestigations.includes(row.investigation.id) && <div className="decision-expanded">
            <button className="decision-button mb-4" aria-pressed={selected.has(row.investigation.id)} onClick={() => update({ ...s, shortlist: selected.has(row.investigation.id) ? [...selected].filter(id => id !== row.investigation.id).join(",") : [...selected, row.investigation.id].join(",") })}>{selected.has(row.investigation.id) ? "Remove from dossier" : "Add to dossier"}</button>
            <p className="mb-3 text-sm">Indexed measurement quantities: {row.measurements.map(q => QUANTITY_LABEL[q] ?? q.replaceAll("_", " ")).join(", ") || "None on individual records in this selection"}.</p>
            {row.observation_relationships.observations > 0 && <p className="my-3 border-l-2 border-border pl-3 text-sm">{row.observation_relationships.observations} source observations; {row.observation_relationships.resolved_identifier_groups} resolved source-identifier groups; {row.observation_relationships.ambiguous_observations} observations with ambiguous identifiers. Independence is unknown. {row.observation_relationships.limitation}</p>}
            {row.mapping ? <><p className="font-medium">Why included: {row.mapping.relevance} evidence for {s.job}</p><blockquote className="my-3 border-l-2 border-primary pl-3">{row.mapping.quote}</blockquote><p className="text-sm"><Link className="underline text-primary" href={docHref(row.mapping.doc)}>Inspect classification source</Link> · Automated text check: {row.mapping.checked_by}, {row.mapping.checked_at}. No independent relevance review.</p></> : <p>No source-checked assignment for this job in this release. No relevance inferred from the name or geometry.</p>}
            <p className="my-3 text-sm">[MISSING_FIELD] Inspect linked sources for missing metadata; the source may not contain the value. [CONFLICT] Inspect both retained values before use. [OUTSIDE_CONDITION] Outside records are comparison candidates; inspect original representations and normalized tolerance distance.</p>
            {row.mapping?.evidence?.map((e, ix) => <blockquote key={ix} className="my-3 border-l-2 border-border pl-3"><strong>{e.kind === "instrument" ? "Explicit instrument evidence" : "Report-only agent / objective evidence (not a per-test result)"}</strong><p>{e.quote}</p><Link className="underline text-primary" href={docHref(row.mapping!.doc)}>Inspect excerpt source</Link></blockquote>)}
            {row.mapping?.rationale && <p className="my-3 text-sm"><strong>Interpretation of relevance (internal, not independently reviewed):</strong> {row.mapping.rationale}</p>}
            {s.job === "detection" && <p className="my-3 text-sm">Sensors and instruments: shown only in explicit source excerpts or record metadata below. Unrecorded instrument metadata remains missing. Measurement quantities are listed with each outcome; their names do not supply instrument metadata.</p>}
            {s.job === "suppression" && <p className="my-3 text-sm">Structured agent evidence: only diluent / gas composition fields explicitly present in each record. Extinguishment quantities remain source-labeled outcomes below. Report-only agent or objective evidence stays in classification excerpts and linked reports; an objective is not a measured suppression result.</p>}
            {row.records.length === 0 && <p className="my-3">No records pass the categorical filters. Change material explicitly to inspect alternatives.</p>}
            {row.records.map(v => <RecordDetails key={v.run.id} summary={<>{v.run.id} — {v.bucket} — {v.run.granularity}{v.run.conflicts?.length ? " — conflict" : ""}</>}>
              <div className="py-3"><div className="flex flex-wrap gap-4"><Link className="underline text-primary" href={explorerLink(s, [v.run.id])}>Inspect record in Explorer</Link><label><input type="checkbox" disabled={!compare.includes(v.run.id) && (compare.length === 2 || (!!comparisonGeometry && comparisonGeometry !== row.investigation.geometry_class))} checked={compare.includes(v.run.id)} onChange={e => setCompare(ids => e.target.checked ? [...ids, v.run.id] : ids.filter(id => id !== v.run.id))} /> Select for pairwise comparison (one geometry only)</label></div>
                {Object.entries(v.axes).map(([axis, a]) => <p key={axis} className="mt-2 text-sm">{axis}: {a.status === "not_reported" ? "[MISSING_FIELD] Not reported" : `${a.status}; original: ${a.raw}; normalized tolerance distance: ${a.distance}`} </p>)}
                <h4 className="mt-4 font-medium">Reported conditions (control settings remain separate)</h4><dl className="decision-values">{Object.entries(v.run.conditions).map(([k, c]) => <div key={k}><dt>{k}</dt><dd>{"raw" in c && c.raw ? c.raw : "value" in c ? String(c.value) : "Not reported"}{k.startsWith("flow_setting") ? " (control setting, not cm/s)" : ""}</dd></div>)}</dl>
                <h4 className="mt-4 font-medium">Outcomes and source indexes</h4>{v.run.outcomes.length ? <ul className="list-disc pl-5">{v.run.outcomes.map((o, ix) => <li key={ix} className="py-1 text-sm">{o.quantity}: {outcomeText(o)} [source {o.source}]{o.at && `; outcome conditions: ${JSON.stringify(o.at)} (not the run condition axis)`}{Object.entries(o.metadata ?? {}).map(([field, meta]) => <details key={field}><summary>{field.replaceAll("_", " ")}: {meta.value} (this outcome only)</summary><p>{meta.quote}</p><p>{meta.basis} · source {meta.source}</p></details>)}</li>)}</ul> : <p className="text-sm">No structured outcomes recorded.</p>}
                {v.run.conflicts?.map((c, ix) => <div key={ix} className="my-3 border-l-2 border-border pl-3"><strong>[CONFLICT] {c.field}</strong>{c.values.map((x, j) => <p key={j}>Source {x.source}: {x.raw} {x.unit}</p>)}</div>)}
                <h4 className="mt-4 font-medium">Original sources</h4><ol start={0} className="list-decimal pl-5">{v.run.sources.map((src, ix) => <li key={ix} className="py-1 text-sm break-words">{src.url ? <a className="underline text-primary" href={src.url}>{src.title || src.url}</a> : src.descriptor || src.file || src.title || "Source descriptor unavailable"}{src.doc && <> · <Link className="underline text-primary" href={docHref(src.doc)}>Governed document</Link></>} {src.table && `Table ${src.table}`} {src.row != null && `row ${src.row}`} {src.line != null && `line ${src.line}`} {src.sheet && `sheet ${src.sheet}`}{src.quote && <blockquote>{src.quote}</blockquote>}</li>)}</ol>
              </div>
            </RecordDetails>)}
          </div>}
        </details>)}
      </div>
      <details className="my-5"><summary>Existing query relaxed results (other materials)</summary><pre className="overflow-auto py-3 text-xs">{JSON.stringify(d.relaxed, null, 2)}</pre></details>
    </>}
    <aside className="mt-8 border-t border-border pt-5"><h2 className="text-xl font-semibold">Publication-only evidence (unranked)</h2><p className="my-3 text-sm">These observations are outside individual PSI test ingestion and the investigation ordering.</p><ul className="flex flex-wrap gap-4"><li><Link className="underline text-primary" href="/docs/literature/luci-rotating-rocket/">LUCI rotating-platform observations</Link></li><li><Link className="underline text-primary" href="/docs/literature/daft-cabin-aerosol/">DAFT aerosol observations</Link></li><li><Link className="underline text-primary" href="/docs/investigations/droplet-combustion/flex-2-cool-flame-results/">FLEX-2 cool-flame publication supplement</Link></li></ul></aside>
  </div>;
}
