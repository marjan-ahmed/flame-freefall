"use client";

import type { ReactElement } from "react";

import { cn } from "@/lib/utils";
import { NUMERIC_AXES, type NumericAxis, type RunView } from "@/lib/psi-query";
import type { Investigation } from "@/lib/psi-types";

import { fmt, isCat, outcomeText, QUANTITY_LABEL } from "./format";

const OUTCOME_ORDER = [
  "spread_rate", "burning_rate_k", "burning_rate_k_hot", "burning_rate_k_cool", "extinction_diameter",
  "extinction_diameter_hot", "end_mode", "test_end", "ignited", "hot_ignition", "cool_flame", "burn_time",
  "spread_extent", "peak_heat_release", "flames_ignited", "weight_loss_rate",
];

export function citationLine(view: RunView["run"], investigations: Record<string, Investigation>): string {
  const inv = investigations[view.investigation];
  const parts = view.sources.map((s) =>
    s.kind === "report"
      ? `${s.title ?? inv?.citation?.title ?? s.doc} — ${s.table}`
      : `${s.dataset} ${s.file}${s.sheet ? ` [${s.sheet}]` : ""}${s.row ? ` line ${s.row}` : ""}`,
  );
  return [...new Set(parts)].join(" · ");
}

export function RunCard({
  view,
  investigations,
  color,
  selected,
  onSelect,
  targetFlow,
}: {
  view: RunView;
  investigations: Record<string, Investigation>;
  color: string;
  selected: boolean;
  onSelect: (id: string) => void;
  targetFlow?: number;
}): ReactElement {
  const { run } = view;
  const inv = investigations[run.investigation];
  const fuel = run.conditions.fuel;
  const outcomes = [...run.outcomes]
    .sort((a, b) => {
      const ra = OUTCOME_ORDER.indexOf(a.quantity);
      const rb = OUTCOME_ORDER.indexOf(b.quantity);
      const byQ = (ra < 0 ? 99 : ra) - (rb < 0 ? 99 : rb);
      if (byQ || targetFlow === undefined) return byQ;
      return Math.abs((a.at?.flow_cm_s ?? Infinity) - targetFlow) - Math.abs((b.at?.flow_cm_s ?? Infinity) - targetFlow);
    })
    .slice(0, 3);

  return (
    <button
      type="button"
      onClick={() => onSelect(run.id)}
      className={cn(
        "w-full rounded-lg border bg-card p-3 text-left transition-colors hover:border-primary/60",
        selected && "border-primary ring-2 ring-primary/20",
      )}
    >
      <div className="flex flex-wrap items-center gap-2">
        <span className="inline-block size-2.5 shrink-0 rounded-full" style={{ background: color }} aria-hidden />
        <span className="font-mono text-sm font-semibold">{run.id}</span>
        <span className="rounded-full bg-secondary px-2 py-0.5 text-xs">{inv?.name}</span>
        {run.granularity !== "test" && run.granularity !== "test-point" && (
          <span className="rounded-full bg-amber-100 px-2 py-0.5 text-xs text-amber-900 dark:bg-amber-950 dark:text-amber-200">
            {run.granularity === "day" ? "daily summary" : run.granularity === "summary" ? "per-fuel summary" : "planned envelope"}
          </span>
        )}
        {!!run.conflicts?.length && (
          <span className="rounded-full bg-red-100 px-2 py-0.5 text-xs text-red-900 dark:bg-red-950 dark:text-red-200">
            sources disagree ({run.conflicts.length})
          </span>
        )}
        {run.sources.some((s) => s.kind === "report") && (
          <span className="rounded-full border px-2 py-0.5 text-xs text-muted-foreground">+ NASA report</span>
        )}
      </div>
      {isCat(fuel) && <p className="mt-1 truncate text-xs text-muted-foreground">{fuel.value}</p>}
      <dl className="mt-2 flex flex-wrap gap-x-4 gap-y-1 text-xs">
        {(Object.entries(view.axes) as [NumericAxis, RunView["axes"][NumericAxis]][]).map(([axis, a]) => (
          <div key={axis} className="flex gap-1">
            <dt className="text-muted-foreground">{NUMERIC_AXES[axis].label}</dt>
            <dd
              className={cn(
                "font-medium",
                a?.status === "within" && "text-emerald-700 dark:text-emerald-400",
                a?.status === "outside" && "text-amber-700 dark:text-amber-400",
                a?.status === "not_reported" && "italic text-muted-foreground",
              )}
            >
              {a?.status === "not_reported"
                ? "not reported"
                : `${a && "raw" in a ? a.raw : ""}${a && "unit" in a && a.unit && !a.raw.includes(a.unit) ? ` ${a.unit}` : ""}`}
              {a && "flags" in a && a.flags?.includes("sources_disagree") ? " ⚠" : ""}
            </dd>
          </div>
        ))}
      </dl>
      {outcomes.length > 0 && (
        <ul className="mt-2 space-y-0.5 text-xs">
          {outcomes.map((o, i) => (
            <li key={i}>
              <span className="text-muted-foreground">{QUANTITY_LABEL[o.quantity] ?? o.quantity}: </span>
              <span className="font-semibold">{outcomeText(o)}</span>
              {o.confirmed_by?.length ? <span className="text-emerald-700 dark:text-emerald-400"> ✓ 2 sources</span> : null}
            </li>
          ))}
        </ul>
      )}
      <p className="mt-2 line-clamp-2 text-[11px] text-muted-foreground">{citationLine(run, investigations)}</p>
      {view.tier === "near" && (
        <p className="mt-1 text-[11px] text-muted-foreground">distance {fmt(view.distance)} tolerances</p>
      )}
    </button>
  );
}
