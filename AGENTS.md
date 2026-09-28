# AGENTS.md

The working contract for this Knowledge System of Record. CLAUDE.md points
here; every coding agent reads this file first.

## This instance: Flame in Freefall

A KSoR instance for **Flame in Freefall** (NASA Space Apps 2026): a governed,
citation-backed record of NASA microgravity combustion investigations, a
unified table of their PSI test data, and a chatbot that answers from both.
Three parts, one rule: every number shown traces to a PSI table line, a
report table or a governed document, and the model never states values itself.

| Part | Where | What it is |
| --- | --- | --- |
| The record | `knowledge/` | 20 governed docs, all `stable`, each with a `.summary.md`. The 12 approved 2026-09-24 (BASS, BASS-II requirements, FLEX-2, CFI, ACME BRE, ACME s-Flame, SPICE, SAME, SAME-R, `data-sources/` ×3) carry no `verified:` stamp yet; all 20 are now ingested into the MCP door (generation 7, sentence-transformers/all-MiniLM-L6-v2 embeddings) |
| The test data | `psi-data/` + `system/psi-ingest/` | 20 PSI experimental tables → 1,948 normalized run records (`psi-data/derived/runs.json`) |
| The chatbot | `system/chatkit-server/` (FastAPI, Groq) + `system/site/` (ChatKit UI) | answers through ChatKit **widgets**; the site also hosts a linked Explorer at `/explore` |

Everything below "The two worlds" is the generic KSoR contract.

### Commands

```sh
npm run check                                   # the record's format checker (CI: Validate)
npm run build                                   # ksor build + static site (CI: Deploy Pages)
node .agents/skills/add-sources/verify.mjs <extraction> <knowledge-doc.md>   # one doc vs its source text

cd system/psi-ingest
uv run psi-ingest        # raw PSI + knowledge tables + extractions -> psi-data/derived/*.json (+ copy to chatkit-server/data/)
uv run psi-extract       # converted report text -> psi-data/extracted/report-outcomes.csv
uv run psi-inventory     # raw-file inventory -> psi-data/derived/source-inventory.md
uv run pytest            # ingest invariants; single test: uv run pytest tests/test_ingest.py -k conflicts

cd system/chatkit-server
uv run uvicorn main:app --port 8000        # chat backend (needs GROQ_API_KEY in the repo-root .env)
GROQ_API_KEY=dummy uv run pytest           # query + widget tests, no network
uv run python tests/gen_query_fixtures.py  # regenerate golden query cases after an intentional change

cd system/site
npm run test:psi         # TypeScript query parity against the same golden cases
```

After changing ingest rules or data: `psi-ingest`, then regenerate fixtures,
then run all three test suites. `psi-data/derived/`,
`psi-data/query-fixtures.json` and `system/chatkit-server/data/` are
generated and committed; never hand-edit them.

### Architecture of the test data and chatbot

- **Ingest** (`system/psi-ingest/psi_ingest/`): one adapter per PSI file
  (`adapters/solid|droplet|gaseous|smoke.py`) maps its columns onto a `Run`
  (`model.py`). `units.py` parses cells into a `Measure` that ALWAYS keeps the
  raw cell and flags any interpretation; unreadable cells become null plus a
  flag, never a guess. `reports.py` then joins per-test tables from
  `knowledge/` docs and verified PDF extractions, recording source
  disagreements as `conflicts` (both values kept, the interval widened,
  nothing chosen). `registry.yaml` holds investigation identity only;
  citations are read from each doc's `sources:` frontmatter.
- **Query** (`system/chatkit-server/psi_query.py`): tiers `match` / `partial`
  (within tolerance on every axis it reports, silent on one) / `near`, plus
  per-investigation coverage and `relaxed` (same conditions, other
  materials). Categorical filters are hard. `rank()` aggregates match/partial
  runs per material (n, min, median, max, every contributing run id) within
  ONE geometry class (`RANKABLE` names which (class, quantity) pairs have
  enough data — never ranks across classes). `readiness()` reports
  match/partial/near coverage per geometry class near a named mission
  atmosphere (`psi_atmospheres.py`: `iss`/`gateway`/`lunar`, each preset's
  numbers copied from a governed doc and checked verbatim by
  `tests/test_atmospheres.py`), paired with governed-doc quotes from
  `psi-data/findings.yaml` (also checked verbatim, by
  `tests/test_findings.py`). **Twin implementation** of `query()`/`rank()` in
  `system/site/lib/psi-query.ts` (atmospheres twinned in
  `psi-atmospheres.ts`): change both together; `psi-data/query-fixtures.json`
  pins them to identical output. `readiness()` has no TS twin — the
  dashboard's mission-readiness cards (`system/site/lib/dashboard-data.ts`)
  compute coverage directly from the twinned `query()` instead, so there is
  no third reimplementation of the match/partial/near tiers. A tolerance
  boundary is inclusive on both sides (`TOLERANCE_EPS`, both twins — plain
  float division can land a query's own axis a hair past `1.0`); a near-tier
  run reporting NONE of the query's axes never outranks one that reports the
  axis however far off (`NO_AXES_REPORTED_SCORE`). Investigation names
  (`query()`'s `investigation` filter, `compare_investigations`,
  `results_data`/`plot_results`) all resolve through one function,
  `_investigation_ids`/`investigationIds`: exact id/name, then family prefix
  ("SAFFIRE" → every SAFFIRE), then hyphen-insensitive, then a **one-way**
  roman-numeral alias (a real name's own trailing numeral, e.g. `BASS-II`,
  answers to an arabic query `"BASS 2"` — never the reverse, so a query that
  itself types a roman numeral, e.g. `"SAFFIRE-II"`, is never aliased onto
  the arabic-named `SAFFIRE-2`). Every outcome `compact()` hands the model
  carries its own source tag (`fmt_sourced_outcome`; a run's `conflicts` via
  `sourced_conflicts`) — never a single per-run citation, which used to get
  copied as the source of a value from a different table entirely — and
  `_shrink_to_budget()` trims the longest outcome strings, never a whole run
  first, until the payload provably fits, rather than trusting one pinned
  query shape to represent every shape.
- **Chat** (`system/chatkit-server/`): see `main.py` for implementation. Seven
  PSI tools (`query_test_runs`, `show_gap_map`, `compare_investigations`,
  `show_test_details`, `plot_results`, `rank_results`, `show_mission_readiness`)
  wrapped by `_guarded` for error capture; widgets built in `psi_widgets.py`;
  button actions in `main.py` `action()` (no model call). `TurnGuard` enforces
  citation integrity and run-id cross-checks. Narrative answers via MCP door
  (`HANDBOOK_MCP_URL`); PSI tools are local.
- **Dashboard** (`system/site/app/(home)/page.tsx`): a server-rendered band
  above the chat — coverage heatmaps per geometry class
  (`components/dashboard/heatmap.tsx`) and mission-readiness cards
  (`components/dashboard/readiness-cards.tsx`), both fed by
  `lib/dashboard-data.ts`. Same O₂/pressure bins and color scale as the
  chat's gap map (`--heat-0`…`--heat-4` in `app/global.css`), so the two
  surfaces read as one system.
- **Deploys**: the site is a static export on GitHub Pages
  (`KSOR_BASE_PATH=/flame-freefall`). The chat backend
  (`flame-freefall-site`) and MCP door (`flame-freefall-mcp`) are Vercel
  projects that redeploy on every push to `main`.

### Rules and gotchas specific to this repo

- **`CLAUDE.md` must stay exactly `@AGENTS.md`** (rule `ksor-pointer-changed`).
  Project memory goes here, never there.
- **Folder = geometry class = comparability.** `investigations/` subfolders
  are `solid-fuel/`, `droplet-combustion/`, `gaseous-flames/` and
  `smoke-aerosol/` (heated, non-burning samples); every investigation doc
  carries a matching `geometry_class:` key. The chatbot and Explorer warn when
  results span classes. `foundations/` and `data-sources/` are narrative, with
  no `geometry_class`.
- **One footnote per source.** Every footnote label must equal a
  `sources[].id` (rule `ksor-footnote-unkeyed`), and that one footnote is
  itemized internally (`§1.2: "quote..." §1.4: "quote..."`). Cite about once
  per paragraph: GFM renders each reference as its own ↩ backlink.
- **Verify against source text, not memory.** Extractions are verification
  ground truth, not part of the record: `investigation_reports/_converted/`,
  `narrative_reports/_converted/`, `psi-data/derived/report-extractions/`
  (the PSI report PDFs), and `psi-data/derived/source-inventory.md` (for
  `data-sources/` docs). For a multi-source doc, concatenate its extractions
  into one scratch file and verify against that. `verify.mjs` cannot see
  numbers written as words; count those by hand.
- **Mission-atmosphere presets and mission-readiness findings are the same
  rule, enforced by pytest instead of `verify.mjs`.** `psi_atmospheres.py`
  (ISS/Gateway/Lunar O₂ %/pressure) and `psi-data/findings.yaml` (the
  governed-doc quotes the readiness view shows beside a coverage gap) each
  carry a `quote` checked verbatim (whitespace-normalized) against its `doc`
  by `tests/test_atmospheres.py` / `tests/test_findings.py`. Editing either
  file's numbers or quotes without updating the source citation fails that
  test — don't loosen it to make a new preset or finding pass.
- **Editing a `stable` doc's body forces re-approval**: `generated.at` must
  move past the edit, and `stable` needs an approval no earlier than it. Add a
  sibling draft instead, as `bass-ii-requirements.md` does. Never record an
  approval the owner didn't give.
- **Report quirks are recorded, not fixed.** When a source contradicts itself
  (SPICE: 52 vs 55 smoke points) or a column's meaning is ambiguous (SAME's
  diameter columns; BASS-II "Air display" panel readings with no unit), keep
  both readings and write an Open question. BASS-II flow velocities in cm/s
  exist only in report Tables 5.1 and 7.1 and in the test video; never
  convert panel readings.
- **Never make the model retype numbers.** Tool replies give it compact,
  already-formatted values and forbid restating per-cell counts, merging runs'
  values, or writing button labels; each rule came from a live error. Groq's
  free tier allows 8000 tokens per minute, so tool replies stay small — not
  just for one pinned query shape (a test enforces the size of `compact()`
  for a wide, untuned query too, since a per-outcome citation tag can, for a
  query with many long free-text outcomes and little repetition to compress
  away, still push a narrower-tested payload over budget; `compact()`'s
  `_shrink_to_budget()` is the hard guarantee, not the test alone).
- **Not everything belongs in the system prompt.** An instruction is a
  request, not a guarantee — it will be followed inconsistently across
  models, fallbacks, and repeated calls to the same model. Before adding or
  editing any instruction in `main.py` (`BASE_INSTRUCTIONS`,
  `WITH_TOOLS_INSTRUCTIONS`, `WITHOUT_TOOLS_INSTRUCTIONS`) or a tool's
  `description_override`/`_reply()` text in `psi_tools.py`, ask: *if the
  model silently ignored this exact sentence on some fraction of calls,
  would anything actually break?* If yes, it needs a code-level guarantee,
  not better wording — a citation, id, unit conversion, aggregate, tier
  label, or set-difference the model is told to state or compute is a
  candidate for moving into `psi_query.py`/`psi_widgets.py` (precomputed
  into the tool's payload) or into a `RunHooks`/`on_tool_end` callback that
  renders from the tool's own JSON, independent of what the model's text
  says — the pattern already proven for narrative citations (`_cite_sources`
  in `main.py`) and for `cite_run_ids=False` on tools whose payload carries
  no per-run id. Prompt text stays fine for genuinely linguistic choices:
  prose length, tone, which 2-3 results to mention, whether a caveat reads
  well. It is not fine for anything with a right answer a human could check
  against source data.
- **`psi-data/raw/matrices/BASS Test Matrix 050213.xlsx` contains
  credentials.** It is gitignored and no tool ever opens it.
- **ChatKit widgets** use the directly-constructed classes (deprecated but
  supported). `ListView` is root-only, so it can't nest inside a `Card`.

- **Subagents in `.claude/agents/`**: two PDF agents (`pdf-to-markdown.md`
  converts to a saved `.md` via the Nutrient skill; `pdf-reader.md` answers
  in-conversation) and a QA/release-gate suite of nine specialists —
  `reliability-regression`, `data-forensics`, `numerical-accuracy`,
  `grounding-provenance`, `citation-verifier`, `chatbot-qa`, `red-team`,
  `cross-layer-consistency`, `code-quality` — coordinated by
  `qa-orchestrator`, which together answer one question: does a value or
  citation the chatbot/dashboard shows actually trace to governed data,
  never the model's invention or a code bug. Each specialist's own `.md`
  documents its method. A confirmed, still-open defect they find is pinned
  as `pytest.mark.xfail(strict=True, reason="...")` in a
  `system/*/tests/test_qa_*.py` file (never edit `psi-data/raw/**`,
  `knowledge/**`, or a generated file to make one pass) — the suite stays
  green while the defect exists, and turns red (`XPASS`) the moment a fix
  lands, which is the cue to remove that marker, not soften it. Skills live
  in `.agents/skills/`, mirrored byte-identically into `.claude/skills/` as a
  real copy, not a symlink (the checker enforces it). Edit `.agents/skills/`
  and re-copy.

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
honest abstention — not required for `npm run dev`. For this project it is
deployed on Vercel (`flame-freefall-mcp`, backed by Neon Postgres), and the
chat backend reaches it through `HANDBOOK_MCP_URL`. `README.md` has the
deployment table and quick start. Worth knowing:

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
