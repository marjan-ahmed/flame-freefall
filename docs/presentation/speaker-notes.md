# Flame Freefall speaker notes

## Slide 1

I am Muhammad Marjan Ahmed, the solo builder behind Code Nashai. Flame Freefall combines an AI-powered research chatbot with a traceable evidence workbench across prevention, detection and suppression. Ask questions in natural language, inspect source-linked test results and research documents, then use the workbench to compare and export evidence. This is an independent challenge response, not NASA-approved safety software.

## Slide 2

The challenge is not simply finding a paper. An engineer needs to know whether its experiment supports the question being asked. The AI chatbot provides a natural-language entry point into cited research and structured test tools. The evidence workbench then exposes conditions, missing fields and transfer limits. Microgravity findings do not automatically validate Lunar-gravity behavior.

## Slide 3

The chatbot and evidence workbench are complementary interfaces to the project. Ask the chatbot to find tests, explain cited research, show plots or audit records. In the workbench, explicitly set conditions, shortlist investigations and export a reproducible dossier. This does not claim that a chat conversation automatically becomes a dossier. The screenshot is an actual saved local capture of the dossier UI. The deterministic Explorer works without an AI service.

## Slide 4

The displayed prompt is an example of an explicit natural-language condition search, not a transcript of a newly recorded provider session. The chatbot can render test-search widgets with conditions and source records. Continue the research in the workbench, where SAFFIRE IV–VI provides direct solid-fuel evidence and BRE offers indirect condensed-fuel emulation. Doubling the oxygen search tolerance admits one full SAFFIRE record in the saved engineering scenario. These are separate chat and workbench capabilities, not an automatic end-to-end handoff.

## Slide 5

The chatbot has a two-record comparison tool; the Explorer provides a detailed audit interface. The source-backed example shows outlet temperatures from SAFFIRE Table 2 and the reasons a condition-matched comparison is blocked. Missing metadata and differing conditions remain visible. We do not subtract the temperatures or attribute their difference to specimen configuration. Source: https://ntrs.nasa.gov/citations/20240002981

## Slide 6

The AI-powered chatbot is built with ChatKit, FastAPI and an agent with eight local PSI tools plus cited narrative retrieval through MCP. Features include natural-language test searches, gap maps, investigation comparisons, individual test details, plots, ordering eligible measurements, atmosphere coverage and two-record comparison audits. PSI numerical answers are rendered by deterministic widgets rather than model-generated numerical prose. Ambiguous condition requests can require explicit Explorer controls. The dataset contains 1,951 indexed records, of which 1,838 are test or test-point records; these are not proven independent replicates. No universal answer accuracy, safety prediction or best-material claim is asserted.

## Slide 7

Flame Freefall combines an AI research companion, an Explorer and reproducible evidence dossiers. It is designed to help researchers find and inspect applicable evidence before the next study. The next milestone is observed task completion with researchers and independent domain review. Team: Code Nashai. Solo builder: Muhammad Marjan Ahmed. No measured time-saving or safety-qualification claim is asserted.
