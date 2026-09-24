import { notFound } from "next/navigation";

import { psiInvestigations, rawBundle } from "@/lib/psi-data";

export const revalidate = false;

/** Source cells exactly as written, per investigation (`<id>.json`), keyed by
 * run id — loaded only when a reader opens a run in the Explorer. */
export function generateStaticParams(): { file: string }[] {
  return psiInvestigations().map((i) => ({ file: `${i.id}.json` }));
}

export async function GET(_request: Request, { params }: { params: Promise<{ file: string }> }): Promise<Response> {
  const { file } = await params;
  const id = file.replace(/\.json$/, "");
  if (!psiInvestigations().some((i) => i.id === id)) notFound();
  return Response.json(rawBundle(id));
}
