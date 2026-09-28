// One hue family per geometry class, one step per investigation inside it, so
// the coverage map reads by class first (the comparability unit) and by
// investigation second. Chosen to stay distinguishable on white and on the
// dark theme's near-black.

const FAMILIES: Record<string, string[]> = {
  "solid-fuel": ["#dc2626", "#ea580c", "#d97706", "#b91c1c", "#f97316", "#c2410c"],
  "droplet-combustion": ["#2563eb", "#0891b2", "#4f46e5"],
  "gaseous-flames": ["#16a34a", "#0d9488", "#65a30d", "#059669", "#15803d", "#84cc16", "#14b8a6", "#22c55e", "#047857"],
  "smoke-aerosol": ["#7c3aed", "#a855f7"],
};

export function colorMap(investigations: { id: string; geometry_class: string }[]): Record<string, string> {
  const used: Record<string, number> = {};
  const out: Record<string, string> = {};
  for (const inv of investigations) {
    const fam = FAMILIES[inv.geometry_class] ?? ["#64748b"];
    const i = used[inv.geometry_class] ?? 0;
    out[inv.id] = fam[i % fam.length];
    used[inv.geometry_class] = i + 1;
  }
  return out;
}
