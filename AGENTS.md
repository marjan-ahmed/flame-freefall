# AGENTS.md

The working contract for this Knowledge System of Record. CLAUDE.md points
here; every coding agent reads this file first.

## This instance: Flame in Freefall

This is a KSoR instance for **Flame in Freefall** — a governed,
citation-backed corpus of NASA microgravity combustion investigations
(BASS-II, SAFFIRE, FLEX, ACME) and the fire-safety standards and
decadal-survey research priorities that frame them (NASA-STD-6001B, Liao et
al., Miller et al., "Thriving in Space"). Built for NASA Space Apps 2026's
"Flame in Freefall" challenge track. Everything below this section is the
generic KSoR framework contract; this section is what's specific to this
corpus.

There is no unit-test suite here — this is a content corpus, not an
application. The closest things to tests:

- `npm run check` validates the entire record (frontmatter, citation
  linkage, filenames, links).
- `node .agents/skills/add-sources/verify.mjs <extraction.txt> <knowledge-doc.md>`
  validates ONE document: every number/date/proper-noun-run in its body must
  appear in the raw source extraction it's cited from. Run this after editing
  any file under `knowledge/investigations/` or `knowledge/foundations/`.

**Folder layout encodes comparability, not just topic.** Under
`knowledge/investigations/`, each subfolder is a *geometry class* —
`solid-fuel/` (BASS-II, SAFFIRE), `droplet-combustion/` (FLEX),
`gaseous-flames/` (ACME) — because two investigations are only honestly
comparable if they share a geometry class. Every investigation document also
carries a custom `geometry_class:` frontmatter key for the same reason.
`knowledge/foundations/` holds narrative-only context (the standard and the
three decadal-survey papers) with no `geometry_class` key and no numeric
structured-facts tables.

**One footnote definition per source, not per claim.** The format checker
(rule `ksor-footnote-unkeyed`) requires every footnote LABEL to exactly equal
a `sources[].id` declared in that document's frontmatter — a document with
one source may have only ONE footnote definition, however many claims it
backs. Each document's single footnote is itemized internally by section
(`§1.2: "quote..." §1.4: "quote..."`) rather than split into per-claim
footnotes. Keep citation density to roughly **one reference per paragraph**,
not per sentence — GFM renders every reference to a shared footnote as its
own numbered backlink arrow (↩ ↩2 ↩3…), and citing every sentence
individually produces a long, broken-looking wall of arrows at the bottom of
the page on the rendered site.

**Raw PDF extractions live outside `knowledge/`, as verification ground
truth.** `investigation_reports/_converted/` and
`narrative_reports/_converted/` hold the full text of every source PDF,
converted via the `pdf-to-markdown` skill. These are scratch/staging files
(not part of the governed record) — `verify.mjs` checks a `knowledge/`
document's claims against them. When a SAFFIRE claim needs two sources
reconciled, the combined check file is
`investigation_reports/_converted/saffire-combined.extracted.md`.

**Corpus state: everything is still `draft`.** All 8 knowledge documents are
`status: draft` pending a human quote-verification pass (nothing reaches
`stable` until every extracted quote is checked against its source PDF page
by a person). A plain `npm run build` therefore publishes zero documents —
`llms.txt`, the search index, and the site's document pages are all empty by
design, not broken. Use `KSOR_DRAFTS=show npm run build` to preview the
pipeline against draft content without approving anything.

**Two project-scoped subagents handle PDF work**, in `.claude/agents/`:
`pdf-to-markdown.md` (converts a PDF to a saved `.md` file via the installed
Nutrient `pdf-to-markdown` skill) and `pdf-reader.md` (reads/answers
questions about a PDF in-conversation without writing any file). The
installed skill itself lives in `.agents/skills/pdf-to-markdown/`, mirrored
byte-identically into `.claude/skills/pdf-to-markdown/` — the format checker
enforces this mirror (a real file copy, not a symlink — this Windows/git
setup stores symlinks as plain text, which the checker treats as missing),
edit the `.agents/skills/` copy and re-sync, never edit the
`.claude/skills/` copy directly.

## The two worlds

| Path          | What it is                                           |
| ------------- | ----------------------------------------------------- |
| `knowledge/`  | **the record** — governed markdown, the product        |
| `system/`     | **the system** — all code that serves the record       |
| `instance.md` | what this SoR is authoritative for; its body is the MCP server's system prompt. `name:` is the machine identity, `title:` the display title — both read at build/serve start, so restart `npm run dev` after changing either |

The record survives the system: `knowledge/` must stay readable and complete
even if `system/` is deleted. The system reads the record; the record never
references the system.

Authority lives in `.ksor/governance.yaml`: the audiences a document may
name (`public` is implicit), who may approve a document to `stable`, and who
may take one down. Takedowns are an append-only ledger in
`.ksor/takedowns.yaml`, written only by `ksor takedown`. Display names for
actors (so a page reads "Owner · Bashir Aziz" instead of "Owner ·
human:bashiraziz") live in `.ksor/people.yaml` — presentation only, grants no
authority, and is not cross-checked against governance.yaml (a person who
leaves the authority list is still the recorded approver of what they
approved).

## Critical rules

1. **The site never contains authored content.** Knowledge goes in
   `knowledge/`, always. Never create markdown, MDX, or content pages inside
   `system/site` — the site _renders_ the record, it never _holds_ it.
2. **`knowledge/` is CommonMark `.md` only.** No `.mdx`, no `meta.json`, no
   framework files. A document must read cleanly in any markdown viewer.
3. **Never edit generated files** — `system/site/.source/`, `.next/`, `out/`,
   `system/site/.staged-knowledge/`, lockfiles by hand.

## Commands (run at the repo root)

```sh
npm install     # once (also fetches the pinned `ksor` tool)
npm run dev         # the site, hot-reloading, at http://localhost:3000
npm run build       # static site into system/site/out/ — publishes ONLY status: stable
npm run check       # the format checker — run before handing off any knowledge change
```

## Serving to agents

`ksor serve` runs an MCP server over the record with cited retrieval and
honest abstention — not required for `npm run dev`, and **not wired up for
this project yet** (no `.env`, no database). `README.md` has the full
runbook (Neon/Postgres setup, embedding key, `npm run provision` /
`refresh` / `serve`, calibrating the abstention gate with
`npx ksor calibrate`, deployment). Worth knowing without reading it:

- **Serving does not publish.** `npm run refresh` publishes (builds +
  ingests the record); `npm run serve` just opens the door on whatever was
  last published.
- **`ksor serve` refuses to boot unauthenticated.** Local needs
  `KSOR_AUTH=disabled-local` in `.env`; public needs real SSO variables or
  an explicit `KSOR_AUTH=disabled-public`.
- **`system/gateways/content.ts`** is this record's MCP tool registration —
  deletable, ordinary `registerTool` + zod — except its `FLOOR` text (tells a
  connecting agent corpus content is untrusted and how to read an
  abstention), which the door checks for at boot and refuses to start
  without.

## Withdrawing a document

```sh
npx ksor takedown --instance instance.md --actor human:you <stable-id> --reason "..."
npx ksor takedown --instance instance.md --list      # what is currently denied
```

The stable id is `knowledge/<path-without-.md>`. `--actor` must be an actor
`.ksor/governance.yaml`'s `takedown_authorities` names. The MCP door stops
serving a taken-down document immediately (it reads the ledger); the site
stops at its next build — rebuild and redeploy after a takedown.

## Publishing

`npm run build` runs `ksor build` first (regenerates every `index.md`, checks
the record, writes `build.lock.json` — commit it), then builds the static
site. A checker refusal stops the build before anything is written.

**Nothing the owner writes publishes until approved.** A new document is
`status: draft`, admitted to zero surfaces (no page, no sidebar row, no
`llms.txt` entry) — `npm run dev` shows it, marked, which is what the preview
is for. `KSOR_DRAFTS=show npm run build` previews a draft-only record's
pipeline (marked `noindex`) without approving anything — a review link,
never a way to ship.

## Writing knowledge

- One document per file under `knowledge/`; the path is the document's
  identity and its URL — ascii lowercase, digits, hyphens; no spaces; never
  both `foo.md` and a folder `foo/`. `title:` carries the real name; the
  filename is the address, not the name. Every folder's `index.md` is
  GENERATED by `ksor build` — never edit one; a folder's own introduction is
  a named document inside it (e.g. `overview.md`). `log.md` and `README.md`
  are reserved names.
- `title:` IS the rendered page heading — never repeat it as an `# h1` in the
  body; quote any value containing a colon.
- **Required frontmatter on every document**: `type` (`Document` unless it's
  a `Policy`, `Procedure`, `Control`, `Standard`, `Definition`,
  `Decision Record`, `Example` or `Attested Computation` — those reserved
  types also require `sources` and `ksor.owner`), `title`, `description`
  (one sentence), `status` (`draft | stable | deprecated`), and
  `ksor.audience` (a list — `[public]`, or an audience registered in
  `.ksor/governance.yaml`; never omitted, never inferred).
- **`stable` additionally requires** `generated: { by, at }` and
  `ksor.approval: { by, at }` by an actor the policy authorises, with
  `generated.at` no later than the approval. `generated.at` dates the TEXT:
  edit a stable document's body without moving this stamp past the edit and
  `ksor build`/`ksor ingest` refuse `ksor-generated-stale`. A `deprecated`
  document carries `ksor.deprecated: { by, at }` and usually
  `ksor.superseded_by: <id>` (a `stable` document every reader of this one
  may read, or `ksor-supersession-strands` refuses it).
- **Optional keys**: `order` (reading position — also decides where a folder
  sits, by its lowest-order document), `sources` (`{ id, resource, title }`,
  cited in the body as GFM footnotes `[^id]` — **the footnote label must be
  the source's `id`, exactly**, see "This instance" above), `verified`
  (`[{ by, at }]` — sets trust tier: none → unverified, machine actor →
  machine-confirmed, any `human:` → human-reviewed), `stale_after`,
  `ksor.effective_from`. Actors are `human:<id>`, `process:<id>` or
  `<producer>/<version>`. Every timestamp is ISO 8601 with an offset, never a
  bare date. Unknown keys are preserved unless one edit from a profile key
  (fails open — a near-miss like `stale_afer:` is refused, not kept).
- `ksor.audience` gates readers: a viewer's list always includes `public`,
  and a document is visible when the two overlap. Every identifier but
  `public` must be registered in `.ksor/governance.yaml`. `npm run check`
  refuses any link, `superseded_by`, or summary that reaches a document not
  every reader of the source may read (`ksor-link-widens`).
  **Publication, not authorship: anyone who can clone the repo reads every
  document regardless of frontmatter** — if someone must not read a document
  and can clone, the answer is a second repository.
- Images/assets live in `knowledge/` beside the document that uses them; a
  relative link must never leave `knowledge/`.
- **Study attachments** — a document may carry `<doc>.summary.md` (a second
  tab), `<doc>.slides.yaml` or `<doc>.slides.url:` (a presentation),
  `<doc>.flashcards.yaml` (a recall deck), and `<doc>.quiz.yaml` (a
  multiple-choice check). Each is *part of its document* — no URL, no
  sidebar row, no `llms.txt` entry, takes its audience/takedown from its
  parent — and may only say what the document says (never a second source).
  `npm run build` audits a quiz for answer-position/length bias and refuses
  one a reader could pass without reading. Ask your coding agent to
  generate/update these from the document rather than hand-writing them.
- **Formatting extras this corpus doesn't currently use**: tabbed code
  blocks (`` ```lang tab="X" tab-group="Y" ``` `` for the same instruction
  per tool) and embeds (`[label](page.sim.html "embed")` for a running
  page/simulation). GitHub-style callouts (`> [!NOTE]`, `[!IMPORTANT]`, etc.)
  ARE used here, for geometry-class and source-caveat notices. All are plain
  CommonMark that degrades gracefully everywhere else the record is read.
- Copy load-bearing values (numbers, thresholds, dates) exactly from their
  source, name the source in `sources`, and cite it with a GFM footnote.
- **The record says only what its source says.** A gap is an open question
  written into the document — never filled from general knowledge. Two
  sources that disagree stay two cited statements — flag the disagreement,
  never silently choose. That boundary is the product.

### Structuring the record

A folder per topic; its `index.md` is GENERATED — a folder's own
introduction is a named document inside it. Sidebar position is the governed
`order:` key: documents that declare it come first (ascending), the rest
follow in name order; folders sit in that SAME list, positioned by the
`order:` of the documents inside them. One `order:` drives every
surface — sidebar, `llms.txt`, the MCP `outline` tool.

## Skills

- `.agents/skills/intake-interview/` — first run: interview the owner and
  write `instance.md` together.
- `.agents/skills/add-sources/` — turn what the owner has into governed
  knowledge (a document, a page, notes, or something they tell you nobody
  wrote down).
- `.agents/skills/format-checker/` — the rules above, as a program;
  `npm run check` runs it.

## Customizing the site

You own `system/site/` outright. Cheapest seams: display title/description
in `instance.md`; accent color in `system/site/app/global.css`
(`--primary`); logo/favicon at `system/site/app/icon.png`; components via
`npx shadcn@latest add <name>`. Anything deeper is an ordinary Next.js app —
the only rule that survives customization is critical rule 1.

## What this project owns

Everything. The scaffold was emitted by `ksor init` and belongs to this
repository outright — change anything in `system/` deliberately; the
knowledge in `knowledge/` was always yours.
