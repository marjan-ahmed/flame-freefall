import type { ReactElement } from "react";

/**
 * The hero's visual: the one fact the whole project rests on. A candle
 * flame on Earth is a teardrop because buoyant convection pulls hot,
 * lighter gas upward past cooler air. Without gravity there's no "up" for
 * hot gas to rise into — a flame burns as a slow, near-spherical, often
 * blue diffusion ball instead. That single shape difference is why a
 * material NASA certifies at 1g can behave completely differently on a
 * spacecraft, and it's the reason this project exists. Real subject matter,
 * not a decorative gradient.
 */
export function FlameComparison(): ReactElement {
  return (
    <svg viewBox="0 0 420 220" className="mx-auto w-full max-w-md" role="img" aria-labelledby="flame-comparison-title">
      <title id="flame-comparison-title">
        A candle flame on Earth tapers into a teardrop, pulled upward by buoyant convection. In quiescent microgravity a candle flame can approach a spherical shape; imposed ventilation changes its shape.
      </title>
      <defs>
        <radialGradient id="earthFlame" cx="50%" cy="78%" r="65%">
          <stop offset="0%" stopColor="#fef3c7" />
          <stop offset="45%" stopColor="var(--heat-3)" />
          <stop offset="100%" stopColor="var(--heat-4)" />
        </radialGradient>
        <radialGradient id="microFlame" cx="46%" cy="46%" r="58%">
          <stop offset="0%" stopColor="#dbeafe" />
          <stop offset="55%" stopColor="#7fb0f9" />
          <stop offset="100%" stopColor="var(--primary)" />
        </radialGradient>
      </defs>

      <g transform="translate(70 30)">
        <path
          d="M 40 150 C 8 120 8 78 40 40 C 55 20 30 8 40 0 C 62 10 78 34 72 62 C 90 84 88 122 40 150 Z"
          fill="url(#earthFlame)"
        />
        <text x="40" y="185" textAnchor="middle" className="fill-foreground text-[13px] font-medium">
          On Earth
        </text>
        <text x="40" y="203" textAnchor="middle" className="fill-muted-foreground text-[11px]">
          buoyancy pulls it into a teardrop
        </text>
      </g>

      <g transform="translate(240 30)">
        <circle cx="48" cy="72" r="52" fill="url(#microFlame)" className="ksor-flame-drift" />
        <text x="48" y="185" textAnchor="middle" className="fill-foreground text-[13px] font-medium">
          In microgravity
        </text>
        <text x="48" y="203" textAnchor="middle" className="fill-muted-foreground text-[11px]">
          no buoyancy, no &ldquo;up&rdquo; — it burns as a sphere
        </text>
      </g>
    </svg>
  );
}
