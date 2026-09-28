"use client";

import { useMemo, type ReactElement } from "react";

import { fmt } from "./format";

export type Span = { lo: number; hi: number; vals?: number[] };
export type Emphasis = "match" | "partial" | "near" | "other" | "dim";

export type Point = {
  id: string;
  x: Span;
  y: Span | null; // null → the run doesn't report this axis: drawn in the "not reported" strip
  color: string;
  emphasis: Emphasis;
  title: string;
};

type Props = {
  points: Point[];
  xLabel: string;
  yLabel: string;
  target?: { x?: number; y?: number; xTol?: [number, number]; yTol?: [number, number] };
  selected?: string | null;
  onSelect?: (id: string) => void;
  missingLabel?: string;
  height?: number;
};

const W = 760;
const M = { top: 16, right: 18, bottom: 44, left: 58 };
const STRIP = 34;

function niceTicks(lo: number, hi: number, n = 6): number[] {
  if (!(hi > lo)) return [lo];
  const raw = (hi - lo) / n;
  const pow = 10 ** Math.floor(Math.log10(raw));
  const step = [1, 2, 2.5, 5, 10].map((m) => m * pow).find((s) => s >= raw) ?? raw;
  const out: number[] = [];
  for (let v = Math.ceil(lo / step) * step; v <= hi + step * 1e-9; v += step) out.push(Number(v.toFixed(10)));
  return out;
}

function domain(values: number[], extra: (number | undefined)[]): [number, number] {
  const all = [...values, ...extra.filter((v): v is number => v !== undefined)];
  if (!all.length) return [0, 1];
  let lo = Math.min(...all);
  let hi = Math.max(...all);
  if (lo === hi) {
    lo -= Math.abs(lo) * 0.1 || 1;
    hi += Math.abs(hi) * 0.1 || 1;
  }
  const pad = (hi - lo) * 0.06;
  return [lo - pad, hi + pad];
}

const R: Record<Emphasis, number> = { match: 5.5, partial: 5, near: 4, other: 2.6, dim: 2 };

export function Scatter({
  points,
  xLabel,
  yLabel,
  target,
  selected,
  onSelect,
  missingLabel = "not reported",
  height = 380,
}: Props): ReactElement {
  const plotted = points.filter((p) => p.y);
  const strip = points.filter((p) => !p.y);
  const hasStrip = strip.length > 0;
  const H = height + (hasStrip ? STRIP : 0);
  const plotBottom = height - M.bottom;

  const [x0, x1] = useMemo(
    () => domain(points.flatMap((p) => [p.x.lo, p.x.hi]), [target?.x, ...(target?.xTol ?? [])]),
    [points, target],
  );
  const [y0, y1] = useMemo(
    () => domain(plotted.flatMap((p) => [p.y!.lo, p.y!.hi]), [target?.y, ...(target?.yTol ?? [])]),
    [plotted, target],
  );
  const sx = (v: number) => M.left + ((v - x0) / (x1 - x0)) * (W - M.left - M.right);
  const sy = (v: number) => plotBottom - ((v - y0) / (y1 - y0)) * (plotBottom - M.top);
  const xt = niceTicks(x0, x1);
  const yt = niceTicks(y0, y1, 5);

  // draw faint points first so emphasized ones sit on top
  const order: Emphasis[] = ["dim", "other", "near", "partial", "match"];
  const sorted = [...points].sort((a, b) => order.indexOf(a.emphasis) - order.indexOf(b.emphasis));
  const stripY = height + STRIP / 2 - 4;

  return (
    <svg viewBox={`0 0 ${W} ${H}`} className="h-auto w-full select-none" role="img" aria-label={`${yLabel} against ${xLabel}`}>
      {/* grid */}
      {xt.map((t) => (
        <g key={`x${t}`}>
          <line x1={sx(t)} x2={sx(t)} y1={M.top} y2={plotBottom} className="stroke-border" strokeWidth={1} />
          <text x={sx(t)} y={plotBottom + 16} textAnchor="middle" className="fill-muted-foreground text-[11px]">
            {fmt(t)}
          </text>
        </g>
      ))}
      {yt.map((t) => (
        <g key={`y${t}`}>
          <line x1={M.left} x2={W - M.right} y1={sy(t)} y2={sy(t)} className="stroke-border" strokeWidth={1} />
          <text x={M.left - 8} y={sy(t) + 4} textAnchor="end" className="fill-muted-foreground text-[11px]">
            {fmt(t)}
          </text>
        </g>
      ))}
      <text x={(M.left + W - M.right) / 2} y={plotBottom + 36} textAnchor="middle" className="fill-foreground text-[12px] font-medium">
        {xLabel}
      </text>
      <text
        transform={`translate(16 ${(M.top + plotBottom) / 2}) rotate(-90)`}
        textAnchor="middle"
        className="fill-foreground text-[12px] font-medium"
      >
        {yLabel}
      </text>

      {/* target + tolerance window */}
      {target?.xTol && target?.yTol && (
        <rect
          x={sx(target.xTol[0])}
          y={sy(target.yTol[1])}
          width={Math.max(0, sx(target.xTol[1]) - sx(target.xTol[0]))}
          height={Math.max(0, sy(target.yTol[0]) - sy(target.yTol[1]))}
          className="fill-primary/10 stroke-primary"
          strokeDasharray="4 3"
        />
      )}
      {target?.x !== undefined && (
        <line x1={sx(target.x)} x2={sx(target.x)} y1={M.top} y2={hasStrip ? H - 6 : plotBottom} className="stroke-primary" strokeDasharray="5 4" />
      )}
      {target?.y !== undefined && (
        <line x1={M.left} x2={W - M.right} y1={sy(target.y)} y2={sy(target.y)} className="stroke-primary" strokeDasharray="5 4" />
      )}

      {hasStrip && (
        <g>
          <rect x={M.left} y={height + 2} width={W - M.left - M.right} height={STRIP - 8} className="fill-muted" rx={4} />
          <text x={W - M.right - 6} y={height + 13} textAnchor="end" className="fill-muted-foreground text-[10px]">
            {missingLabel}
          </text>
        </g>
      )}

      {sorted.map((p) => {
        const r = R[p.emphasis];
        const sel = selected === p.id;
        const cx = sx((p.x.lo + p.x.hi) / 2);
        const common = {
          onClick: onSelect ? () => onSelect(p.id) : undefined,
          className: onSelect ? "cursor-pointer" : undefined,
        };
        const opacity = p.emphasis === "dim" ? 0.18 : p.emphasis === "other" ? 0.45 : 0.95;
        const fill = p.emphasis === "dim" ? "var(--muted-foreground)" : p.color;
        if (!p.y) {
          return (
            <g key={p.id} {...common} opacity={opacity}>
              <title>{p.title}</title>
              {p.x.hi > p.x.lo && <line x1={sx(p.x.lo)} x2={sx(p.x.hi)} y1={stripY} y2={stripY} stroke={fill} strokeWidth={1.5} />}
              <circle cx={cx} cy={stripY} r={Math.max(2, r - 1)} fill={p.emphasis === "partial" ? "var(--background)" : fill} stroke={fill} strokeWidth={p.emphasis === "partial" ? 2 : 0} />
              {sel && <circle cx={cx} cy={stripY} r={r + 4} fill="none" className="stroke-foreground" strokeWidth={2} />}
            </g>
          );
        }
        const ys = p.y.vals?.length ? p.y.vals : [(p.y.lo + p.y.hi) / 2];
        const cyMid = sy((p.y.lo + p.y.hi) / 2);
        return (
          <g key={p.id} {...common} opacity={opacity}>
            <title>{p.title}</title>
            {p.x.hi > p.x.lo && <line x1={sx(p.x.lo)} x2={sx(p.x.hi)} y1={cyMid} y2={cyMid} stroke={fill} strokeWidth={1.5} />}
            {p.y.hi > p.y.lo && <line x1={cx} x2={cx} y1={sy(p.y.lo)} y2={sy(p.y.hi)} stroke={fill} strokeWidth={1.5} />}
            {ys.map((yv, i) => (
              <circle
                key={i}
                cx={cx}
                cy={sy(yv)}
                r={r}
                fill={p.emphasis === "partial" ? "var(--background)" : fill}
                stroke={p.emphasis === "match" ? "var(--foreground)" : fill}
                strokeWidth={p.emphasis === "match" ? 1.2 : p.emphasis === "partial" ? 2 : 0}
              />
            ))}
            {sel && <circle cx={cx} cy={cyMid} r={r + 5} fill="none" className="stroke-foreground" strokeWidth={2} />}
          </g>
        );
      })}
    </svg>
  );
}
