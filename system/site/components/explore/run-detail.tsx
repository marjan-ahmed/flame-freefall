"use client";

import { useEffect, useState, type ReactElement } from "react";

import type { Investigation, Measure, SlimRun } from "@/lib/psi-types";

import { CONDITION_LABEL, FLAG_LABEL, conditionText, isCat, outcomeText, QUANTITY_LABEL } from "./format";

type RawBundle = Record<string, Record<string, string>[]>;
const rawCache = new Map<string, Promise<RawBundle>>();

function loadRaw(basePath: string, investigation: string): Promise<RawBundle> {
  const key = investigation;
  if (!rawCache.has(key)) {
    rawCache.set(
      key,
      fetch(`${basePath}/psi/raw/${investigation}.json`).then((r) => {
        if (!r.ok) throw new Error(String(r.status));
        return r.json() as Promise<RawBundle>;
      }),
    );
  }
  return rawCache.get(key)!;
}

function sourceLabel(run: SlimRun, i: number, inv: Investigation | undefined): string {
  const s = run.sources[i];
  if (!s) return `source ${i}`;
  if (s.kind === "report") return `${s.title ?? inv?.citation?.title ?? s.doc} — ${s.table}`;
  return `${s.dataset} · ${s.file}${s.sheet ? ` [${s.sheet}]` : ""}${s.row ? ` · line ${s.row}` : ""}`;
}

export function RunDetail({
  run,
  investigation,
  basePath,
  onClose,
}: {
  run: SlimRun;
  investigation: Investigation | undefined;
  basePath: string;
  onClose?: () => void;
}): ReactElement {
  const [raw, setRaw] = useState<Record<string, string>[] | null>(null);
  const [rawError, setRawError] = useState(false);
  useEffect(() => {
    let live = true;
    setRaw(null);
    setRawError(false);
    loadRaw(basePath, run.investigation)
      .then((b) => live && setRaw(b[run.id] ?? []))
      .catch(() => live && setRawError(true));
    return () => {
      live = false;
    };
  }, [basePath, run.id, run.investigation]);

  const conditions = Object.entries(run.conditions).filter(([k]) => k !== "gravity");

  return (
    <article className="min-w-0 border border-border border-t-2 border-t-orange-400 bg-card p-4 text-sm [overflow-wrap:anywhere]" aria-label={`Run ${run.id}`}>
      <header className="flex items-start justify-between gap-3">
        <div>
          <p className="text-xs uppercase tracking-wide text-muted-foreground">
            {investigation?.name} · {run.granularity === "test" ? "individual test" : run.granularity}
            {run.date ? ` · ${run.date}` : ""}
          </p>
          <h3 className="font-mono text-lg font-semibold">{run.id}</h3>
        </div>
        {onClose && (
          <button type="button" onClick={onClose} className="rounded-md border px-2 py-1 text-xs hover:bg-accent">
            Close
          </button>
        )}
      </header>

      <section className="mt-3">
        <h4 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Sources</h4>
        <ol className="mt-1 list-decimal space-y-1 pl-5">
          {run.sources.map((s, i) => (
            <li key={i}>
              {s.kind === "report" ? (
                <>
                  {s.url ? (
                    <a href={s.url} className="text-primary underline underline-offset-2" target="_blank" rel="noreferrer">
                      {s.title ?? s.url}
                    </a>
                  ) : (
                    (s.title ?? s.doc)
                  )}{" "}
                  — {s.table}
                  {s.line ? (
                    <>
                      , as reproduced in the governed record{" "}
                      <a
                        href={`${basePath}/docs/${(s.doc ?? "").replace(/^knowledge\//, "")}/`}
                        className="text-primary underline underline-offset-2"
                      >
                        {s.doc}
                      </a>
                    </>
                  ) : (
                    <span className="block text-xs text-muted-foreground">
                      extracted verbatim from the converted report text
                      {s.via ? (
                        <>
                          {" "}
                          (<span className="font-mono">{s.via}</span>)
                        </>
                      ) : null}{" "}
                      — checked against it, not yet reviewed by a person
                    </span>
                  )}
                  {s.descriptor && !s.url ? (
                    <span className="block text-xs text-muted-foreground">{s.descriptor}</span>
                  ) : null}
                  {s.scope ? <span className="block text-xs text-muted-foreground">{s.scope}: inherited apparatus metadata, not test-specific conditions</span> : null}
                </>
              ) : (
                <>
                  NASA PSI {s.dataset}: <span className="font-mono text-xs">{s.file}</span>
                  {s.sheet ? ` [${s.sheet}]` : ""}
                  {s.row ? `, line ${s.row}` : ""}
                </>
              )}
            </li>
          ))}
        </ol>
      </section>

      {!!run.conflicts?.length && (
        <section className="mt-4 rounded-lg border border-red-300 bg-red-50 p-3 dark:border-red-900 dark:bg-red-950/40">
          <h4 className="text-xs font-semibold uppercase tracking-wide text-red-900 dark:text-red-200">Sources disagree</h4>
          <p className="mt-1 text-xs text-red-900/80 dark:text-red-200/80">
            Both values are kept. Neither is chosen; the query treats the run as spanning both.
          </p>
          <ul className="mt-2 space-y-1">
            {run.conflicts.map((c, i) => (
              <li key={i}>
                <span className="font-medium">{CONDITION_LABEL[c.field] ?? c.field.replace("outcome:", "")}</span>:{" "}
                {c.values.map((v, j) => (
                  <span key={j}>
                    {j > 0 && " vs "}
                    <span className="font-mono">{v.raw}</span>{" "}
                    <span className="text-xs text-muted-foreground">({sourceLabel(run, v.source, investigation)})</span>
                  </span>
                ))}
              </li>
            ))}
          </ul>
        </section>
      )}

      <section className="mt-4">
        <h4 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Results</h4>
        {run.outcomes.length ? (
          <table className="mt-1 w-full text-xs">
            <tbody>
              {run.outcomes.map((o, i) => (
                <tr key={i} className="border-b last:border-0 align-top">
                  <td className="py-1 pr-2 text-muted-foreground">{QUANTITY_LABEL[o.quantity] ?? o.quantity}</td>
                  <td className="py-1 pr-2 font-semibold">{outcomeText(o)}</td>
                  <td className="py-1 text-muted-foreground">
                    {o.measure && o.measure.raw !== outcomeText(o) ? <>cell “{o.measure.raw}” · </> : null}
                    source {o.source + 1}
                    {o.confirmed_by?.length ? ` · confirmed by source ${o.confirmed_by.map((c) => c + 1).join(", ")}` : ""}
                    {o.note ? ` · ${o.note}` : ""}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <p className="mt-1 text-xs italic text-muted-foreground">No results recorded in these sources.</p>
        )}
      </section>

      <section className="mt-4">
        <h4 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Conditions</h4>
        <table className="mt-1 w-full text-xs">
          <tbody>
            {conditions.map(([k, c]) => {
              const flags = isCat(c) ? [] : ((c as Measure).flags ?? []).filter((f) => !f.startsWith("from_source") && !f.startsWith("confirmed_by"));
              const confirmed = !isCat(c) && ((c as Measure).flags ?? []).some((f) => f.startsWith("confirmed_by"));
              return (
                <tr key={k} className="border-b last:border-0 align-top">
                  <td className="py-1 pr-2 text-muted-foreground">{CONDITION_LABEL[k] ?? k.replaceAll("_", " ")}</td>
                  <td className="py-1 pr-2 font-medium">{conditionText(c)}</td>
                  <td className="py-1 text-muted-foreground">
                    {!isCat(c) && (c as Measure).raw !== conditionText(c) ? <>cell “{(c as Measure).raw}” </> : null}
                    {flags.map((f) => (
                      <span key={f} className="mr-1 inline-block rounded bg-muted px-1">
                        {FLAG_LABEL[f] ?? f.replaceAll("_", " ")}
                      </span>
                    ))}
                    {confirmed && <span className="text-emerald-700 dark:text-emerald-400">✓ 2 sources</span>}
                    {isCat(c) && c.basis ? <span className="block italic">basis: {c.basis}</span> : null}
                    {isCat(c) && c.source !== undefined ? <span className="block">source {c.source + 1}: {sourceLabel(run, c.source, investigation)}</span> : null}
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </section>

      {!!run.notes?.length && (
        <section className="mt-4">
          <h4 className="text-xs font-semibold uppercase tracking-wide text-muted-foreground">Notes</h4>
          <ul className="mt-1 list-disc pl-5 text-xs">
            {run.notes.map((n, i) => (
              <li key={i}>{n}</li>
            ))}
          </ul>
        </section>
      )}

      <details className="mt-4">
        <summary className="cursor-pointer text-xs font-semibold uppercase tracking-wide text-muted-foreground">
          Source cells, exactly as written
        </summary>
        {rawError && <p className="mt-1 text-xs text-muted-foreground">Could not load source cells.</p>}
        {!raw && !rawError && <p className="mt-1 text-xs text-muted-foreground">Loading…</p>}
        {raw?.map((cells, i) => (
          <div key={i} className="mt-2 min-w-0 overflow-x-auto">
            <p className="text-[11px] text-muted-foreground">{sourceLabel(run, i, investigation)}</p>
            <table className="mt-1 w-full table-fixed text-[11px]">
              <tbody>
                {Object.entries(cells).map(([k, v]) => (
                  <tr key={k} className="border-b last:border-0 align-top">
                    <td className="py-0.5 pr-2 text-muted-foreground">{k}</td>
                    <td className="py-0.5 font-mono">{v}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        ))}
      </details>
    </article>
  );
}
