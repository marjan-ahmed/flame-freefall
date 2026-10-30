import Link from "next/link";
import type { LunarEvidenceBrief } from "@/lib/mission-evidence";

export function LunarEvidenceBrief({ brief }: { brief: LunarEvidenceBrief }) {
  const { atmosphere, profiles, solidBoundary } = brief;
  function href(slice: typeof profiles[number]["slices"][number], profile: typeof profiles[number]) {
    const p = new URLSearchParams({ o2_pct: String(atmosphere.o2_pct), pressure_atm: String(atmosphere.pressure_atm),
      geometry_class: slice.geometry, tol_o2_pct: String(profile.o2), tol_pressure_atm: String(profile.pressure), individual: "1" });
    if (slice.emulator) p.set("investigation", "acme-bre");
    if (slice.key === "gaseous") p.set("exclude_investigation", "acme-bre");
    if (slice.representative) p.set("run", slice.representative.run.id);
    return `/explore/?${p}`;
  }
  return <section className="border-y border-border bg-muted/20" id="lunar-evidence">
    <div className="mx-auto max-w-5xl px-4 py-12 sm:px-6">
      <h2 className="font-display text-2xl font-semibold">What evidence overlaps a proposed Lunar atmosphere?</h2>
      <p className="mt-3 max-w-3xl text-muted-foreground">Target: {atmosphere.o2_pct}% O? and {atmosphere.pressure_source_value}.
        Change the search window and the answer changes. These are indexed individual tests and test points, not a measure of mission readiness.</p>
      <div className="mt-6 overflow-x-auto">
        <table className="w-full text-left text-sm">
          <caption className="pb-3 text-left text-muted-foreground">Each cell shows full matches / incomplete conditions. Select a cell to inspect sources. BRE is separate from the other gaseous tests here.</caption>
          <thead><tr className="border-b"><th className="p-3">Search window</th>{profiles[0].slices.map(s => <th key={s.key} className="p-3">{s.label}</th>)}</tr></thead>
          <tbody>{profiles.map(profile => <tr key={profile.label} className="border-b">
            <th scope="row" className="p-3 font-normal">{profile.label}<span className="block text-muted-foreground">?{profile.o2} O? points / ?{(profile.pressure * 101.325).toFixed(2)} kPa</span></th>
            {profile.slices.map(slice => <td key={slice.key} className="p-3"><Link className="inline-block rounded px-2 py-2 font-medium text-primary underline focus-visible:ring-2" href={href(slice, profile)} aria-label={`${profile.label}: ${slice.label}, ${slice.match} full, ${slice.partial} incomplete`}>{slice.match} / {slice.partial}</Link></td>)}
          </tr>)}</tbody>
        </table>
      </div>
      <div className="mt-6 grid gap-6 md:grid-cols-2">
        <div><h3 className="font-medium">A boundary independent of tolerances</h3>
          <p className="mt-2 text-sm text-muted-foreground">The maximum reported ambient O? among indexed individual solid-fuel records is {solidBoundary.maxO2 ?? "unknown"}%. {solidBoundary.reported} records report O?; {solidBoundary.missing} do not.
            This describes this collection, not all NASA experiments.</p>
          <p className="mt-2 text-sm">{solidBoundary.ids.map(id => <Link key={id} className="mr-3 text-primary underline" href={`/explore/?run=${encodeURIComponent(id)}`}>{id}</Link>)}</p>
        </div>
        <div><h3 className="font-medium">Relevant evidence is not always a solid sample</h3>
          <p className="mt-2 text-sm text-muted-foreground">BRE uses gaseous burners to emulate condensed fuels. Its indexed report examples are preliminary and incomplete as an inventory. They inform interpretation without becoming direct solid-material tests.</p>
          <Link className="mt-2 inline-block text-sm text-primary underline" href="/docs/investigations/gaseous-flames/acme-bre/">Read the BRE report evidence</Link>
        </div>
      </div>
      <p className="mt-6 max-w-3xl text-sm text-muted-foreground">Incomplete conditions are unknown. Atmosphere overlap does not establish equivalent fuel, flow, geometry or gravity. Microgravity observations do not validate Lunar-gravity predictions. A zero here is a search result within this index, not proof of safety or absence of research.</p>
      <Link className="mt-3 inline-block text-sm text-primary underline" href={`/docs/${atmosphere.doc.replace(/^knowledge\//, "").replace(/\.md$/, "")}/`}>Source of the proposed atmosphere</Link>
    </div>
  </section>;
}
