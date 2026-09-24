import type { ReactElement } from "react";

import { fmt } from "@/components/explore/format";
import { O2_BINS, PRESSURE_BINS, type AtmosphereMarker, type ClassHeatmap } from "@/lib/dashboard-data";

// The dashboard's hero: one small O2 x pressure grid per geometry class, so
// "where does the data reach" is visible with no typing. Same bins and the
// same five-step color scale as the chat's gap map (system/chatkit-server/
// psi_widgets.py O2_BINS / SHADES, mirrored in app/global.css --heat-*), so
// this and the chat read as one system. Plain SSR'd SVG: no client JS, no
// chart library — a <title> gives every cell and marker a native tooltip.

const CELL = 20;
const GAP = 2;
const LABEL_W = 46;

function shadeVar(n: number): string {
  if (n === 0) return "var(--heat-0)";
  if (n < 3) return "var(--heat-1)";
  if (n < 10) return "var(--heat-2)";
  if (n < 30) return "var(--heat-3)";
  return "var(--heat-4)";
}

function binLabel([lo, hi]: [number, number], first: boolean, last: boolean): string {
  if (first) return `<${fmt(hi, 3)}`;
  if (last) return `≥${fmt(lo, 3)}`;
  return `${fmt(lo, 3)}–${fmt(hi, 3)}`;
}

export function Heatmap({ heatmap, markers }: { heatmap: ClassHeatmap; markers: AtmosphereMarker[] }): ReactElement {
  const cols = O2_BINS.length;
  const rows = PRESSURE_BINS.length;
  const w = LABEL_W + cols * (CELL + GAP);
  const h = rows * (CELL + GAP) + 16;
  const coveredCells = heatmap.grid.flat().filter((n) => n > 0).length;

  return (
    <figure className="min-w-0">
      <figcaption className="mb-1 flex items-baseline justify-between gap-2">
        <span className="text-sm font-medium">{heatmap.label}</span>
        <span className="text-xs text-muted-foreground">
          {coveredCells}/{cols * rows} cells tested
        </span>
      </figcaption>
      <svg viewBox={`0 0 ${w} ${h}`} width="100%" role="img" aria-label={`${heatmap.label}: test coverage by O2 and pressure`}>
        {/* rows: pressure bands, low at the bottom */}
        {PRESSURE_BINS.map((pb, yi) => {
          const rowIndex = rows - 1 - yi; // draw high pressure at top
          const y = rowIndex * (CELL + GAP);
          return (
            <g key={yi}>
              <text x={LABEL_W - 6} y={y + CELL / 2 + 4} textAnchor="end" fontSize={9} fill="var(--muted-foreground)">
                {binLabel(pb, yi === 0, yi === rows - 1)}
              </text>
              {O2_BINS.map((ob, xi) => {
                const n = heatmap.grid[yi]?.[xi] ?? 0;
                const isMarker = markers.some((m) => m.xBin === xi && m.yBin === yi);
                return (
                  <rect
                    key={xi}
                    x={LABEL_W + xi * (CELL + GAP)}
                    y={y}
                    width={CELL}
                    height={CELL}
                    rx={3}
                    fill={shadeVar(n)}
                    stroke={isMarker ? "var(--primary)" : "var(--border)"}
                    strokeWidth={isMarker ? 2 : 1}
                  >
                    <title>
                      {`${heatmap.label}: O₂ ${binLabel(ob, xi === 0, xi === cols - 1)}%, pressure ${binLabel(pb, yi === 0, yi === rows - 1)} atm\n${n} test${n === 1 ? "" : "s"}${
                        isMarker
                          ? "\n" + markers.filter((m) => m.xBin === xi && m.yBin === yi).map((m) => m.label).join(", ")
                          : ""
                      }`}
                    </title>
                  </rect>
                );
              })}
            </g>
          );
        })}
        <text x={LABEL_W} y={h - 2} fontSize={9} fill="var(--muted-foreground)">
          {"O₂ (%) →"}
        </text>
      </svg>
    </figure>
  );
}

export function HeatmapLegend(): ReactElement {
  const steps: [string, string][] = [
    ["var(--heat-0)", "0 (gap)"],
    ["var(--heat-1)", "1–2"],
    ["var(--heat-2)", "3–9"],
    ["var(--heat-3)", "10–29"],
    ["var(--heat-4)", "30+"],
  ];
  return (
    <div className="flex flex-wrap items-center gap-3 text-xs text-muted-foreground">
      <span>Tests per cell:</span>
      {steps.map(([color, label]) => (
        <span key={label} className="flex items-center gap-1">
          <span className="inline-block h-3 w-3 rounded-sm border border-border" style={{ background: color }} />
          {label}
        </span>
      ))}
      <span className="flex items-center gap-1">
        <span className="inline-block h-3 w-3 rounded-sm border-2" style={{ borderColor: "var(--primary)" }} />
        mission atmosphere
      </span>
    </div>
  );
}
