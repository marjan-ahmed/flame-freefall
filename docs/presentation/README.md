# Flame Freefall: seven-slide project demonstration

**Code Nashai — Muhammad Marjan Ahmed, solo builder.**

[View the PDF](flame-freefall-pitch.pdf) · [Download the editable PowerPoint](flame-freefall-pitch.pptx) · [Slide overview](contact-sheet.png) · [Speaker notes](speaker-notes.md)

The deck is self-contained: problem, AI research companion and evidence workbench,
actual product capture, worked demonstration, dedicated chatbot features,
NASA data, intended impact, next milestones and team. It is designed to be read without a
presenter. The PowerPoint retains editable text and vector shapes; only the
actual application capture is rasterized. The PDF has embedded fonts.

## Story and demonstration

1. Flame Freefall: an AI research companion for NASA combustion evidence.
2. The research problem and conversational access to source-backed evidence.
3. Ask in chat, investigate in the workbench, export a dossier.
4. An example chat question and the complementary Lunar workbench scenario.
5. Source-backed comparison tools and an actual SAFFIRE evidence audit.
6. Dedicated AI chatbot slide: cited document retrieval, test search, plots,
   gap maps, atmosphere coverage, comparisons and ordered measurements.
7. Combined research benefit, validation milestones and team.

The deck makes no measured time-saving, independent-review, safety-certification,
NASA-endorsement or Lunar-gravity prediction claim. Chat and workbench are
complementary interfaces; no automatic conversation-to-dossier handoff is claimed.
The presentation contains no repository URL or eligibility commentary.

## Evidence behind the slides

| Slides | Evidence |
| --- | --- |
| 1–2 | [Supplied challenge](../../challenge-details.md): synthesis, relevance, prevention, detection and suppression |
| 3 | Actual saved local browser capture, `.playwright-mcp/implemented-dossier-desktop.png`, cropped without altering UI text; [workflow report](../../research/implemented-improvements-2026-11-02.md). This capture predates subsequent source-method updates and is not deployment verification. |
| 4 | [Executable scenario](../../scripts/evaluate-research-scenarios.mjs), [saved results](../../research/research-scenario-verification.json), [relevance mapping](../../psi-data/decision-contexts.yaml) |
| 5 | [NASA SAFFIRE report](https://ntrs.nasa.gov/citations/20240002981), Table 2; source-indexed `max_temp_sfu_outlet` for `saffire-iv-vi:VI-3` and `VI-4`; [comparison audit](../../system/site/lib/psi-comparison.ts) |
| 6 | [Chat tools](../../system/chatkit-server/psi_tools.py), [widgets](../../system/chatkit-server/psi_widgets.py), [PSI response guard](../../system/chatkit-server/main.py), [dataset](../../psi-data/derived/runs.json); document count refers to 23 stable governed documents |
| 7 | [Researcher review packet](../../research/researcher-review-packet.json) remains awaiting review; validation milestones are future work |

No imagery was generated with AI. Diagrams, layout, copy and the generation script
were prepared with Codex assistance. The product uses optional AI conversation;
PSI measurement rendering and evidence classification are deterministic.

## Previous submissions and format research

Research performed 2026-11-02. The story structure takes a concrete user decision,
demonstrates the data-to-result path, and separates implemented work from intended
impact. These are editorial choices, not a claim to reproduce a winning formula.

- [NASA's 2024 winners](https://www.nasa.gov/learning-resources/stem-engagement-at-nasa/nasa-international-space-apps-challenge-announces-2024-global-winners/): reviewed the descriptions of 42 QuakeHeroes, Waterwise and NVS-knot. These communicate a specific task and use of agency data.
- [NVS-knot project submission](https://www.spaceappschallenge.org/nasa-space-apps-2024/find-a-team/nvs-knot/?tab=project): the indexed project text describes planting-risk decisions, its inputs and MVP, and supplies a [demo link](https://drive.google.com/file/d/10u8i69xK-b9ojl3y89R0_faH5hKe8Mqu/view). The linked demo was inaccessible in this environment; its footage was not reviewed.
- [42 QuakeHeroes project](https://www.spaceappschallenge.org/nasa-space-apps-2024/find-a-team/42-quakeheroes/?tab=project) and [project website](https://gabrielchayb.github.io/42-quake-heroes/): direct project-page retrieval failed and website text was unavailable. NASA's description supports discussion of the task, not a visual critique of the demo.
- [SunLock 2021 submission](https://2021.spaceappschallenge.org/challenges/statements/unlocking-the-secrets-of-the-sun/teams/sunlock/): reviewed indexed submission text, its user-facing purpose, prototype and demonstration links. Not used as scientific evidence or asserted to be a global winner.
- [Historical official submission guide, 2022](https://sa-2019.s3.amazonaws.com/media/documents/Space_Apps_2022_Project_Submission_Guide.pdf): the indexed excerpt specifies a public demo with seven slides or a 30-second video. This is historical format evidence, not confirmation of the 2026 rules.
- [Current submission guide URL](https://www.spaceappschallenge.org/resources/project-submission-guide/) returned an access error during research. The requested seven-slide format is implemented; final 2026 global format compliance is not independently established.

## Rebuild and inspect

Install `python-pptx`, `reportlab` and `Pillow` in a suitable Python environment,
then run from the repository root:

```sh
python scripts/build-pitch-deck.py
```

The script checks record counts and the two displayed source-indexed outcomes,
embeds speaker notes, checks text widths and emits seven PNG previews plus a
contact sheet. [Build receipt](build-receipt.json) records the dataset hash.
Arial fonts on Windows or Liberation Sans on Linux are supported. Inspect the
PowerPoint on the presentation device for font substitution; the PDF is the
fixed-layout delivery artifact.
