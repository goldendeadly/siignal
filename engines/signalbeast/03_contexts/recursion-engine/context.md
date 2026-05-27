# Recursion Engine Context

## Purpose

The **Recursion Engine** context enables SignalBeast to generate additional or mutated outputs from existing assets.  It leverages the engine’s command set (e.g. `/mutate`, `/threadcast`, `/glyphseed`, `/storybind`, `/promptforge`, `/recur100`, `/mapout`) to expand the content footprint and breathe new life into existing insights.  This represents Phase 7 of the SignalBeast framework.

## Read First

- All platform outputs produced earlier in the run.
- The expansion recommendations (topics, collaborators, lead magnets, system improvements).
- The automation plan if it includes recursion triggers.

## Use This Context For

- Executing specific commands to mutate outputs into new formats or tones (e.g. converting a paragraph into a tweet thread or a graphic).
- Generating new prompts or meta‑prompts (e.g. using `/promptforge` to turn a post into a reusable prompt template).
- Creating visual representations or story‑based adaptations of existing content (e.g. `/glyphseed` or `/storybind`).
- Running a full secondary round of content generation on the same source with an adjusted SEO cluster (`/recur100`).

## Ignore

- Initial generation of platform outputs (handled in earlier phases).
- Expansion planning and automation design (handled in other contexts).

## Expected Outputs

- New or mutated content pieces stored in the run workspace with appropriate naming conventions (e.g. `[topic]-mutated-thread-v1.md`).
- A **Recursion Pathways** table listing which command was used, on which asset, and what output was produced.
- Updated tracking entries reflecting the additional outputs.
