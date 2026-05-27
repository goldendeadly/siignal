# SignalBeast Master SOP

This SOP outlines the high‑level process for running a SignalBeast session. The structure parallels the Blogzilla system but reflects the unique phases of the SignalBeast engine (context decoder, core generation, platform explosion, tracking & canon, signal expansion, automation suggestions and recursion engine).

## Step‑by‑Step Execution

1. **Prepare Inputs**
   - Place the source blog post, keyword or idea into `07_inputs/source-blogs/` or `07_inputs/keywords/`.
   - Create a run brief in `07_inputs/run-briefs/` with resonance mode, core intent, niche and recursion amplification setting.
2. **Route the Task**
   - Use `00_router/Claude.md` to determine which context handles the current phase.
3. **Context Decoder**
   - Enter the `context-decoder` to analyse tone, audience intent, emotional frequency, conversion goals and SEO clusters (primary keyword, LSI terms, long‑tail variants, related questions). Produce a canonical statement and an initial SEO supercluster grid.
4. **Core Generation**
   - Use `core-generation` to produce a summary, meta description and modular highlights from the source.
5. **Platform Explosion**
   - In `platform-explosion`, generate 100+ platform‑specific outputs based on the supercluster grid, resonance mode and CTA tiers. Include platform publication matrix and recursion flags.
6. **Tracking & Canon**
   - In `tracking-canon`, log each output’s metadata: platform, format, keywords, CTA, canonical line, publication target and resonance score. Update master trackers and create a content matrix.
7. **Signal Expansion**
   - Enter `signal-expansion` to propose new topics, collaborations/backlinks, lead magnets and suggestions for expanded or adjacent niches.
8. **Automation Suggestions**
   - Use `automation-suggestions` to recommend workflow automations (e.g. Zapier flows, template updates) and assign tasks to tools or VAs.
9. **Recursion Engine**
   - If recursion amplification is enabled, use `recursion-engine` to mutate selected outputs using commands like `/mutate`, `/threadcast`, `/glyphseed`, `/storybind`, `/promptforge`, `/recur100`. Document the new assets and update the tracking tables accordingly.
10. **Finalise and Archive**
   - Move completed and approved outputs from `04_workspaces` to `08_outputs/`. Save trackers and expansion logs. Archive the run folder in `09_archive/`.

## Roles and Responsibilities

- **Signal Operator** – orchestrates the phases, runs prompts and ensures outputs meet the criteria.
- **Router** – directs tasks to appropriate contexts based on the current phase.
- **Tracker Maintainer** – updates content master tracker, platform outputs tracker and analytics.
- **Automation Manager** – sets up and maintains automations and recursion commands.

## Tips

- Always refer to the `context.md` and `workflow.md` files in each context before starting tasks; they contain detailed instructions and expected outputs.
- Use naming conventions to keep files discoverable and maintain consistency across runs.
- When enabling recursion amplification, limit the number of recursion loops per run to avoid exponential output proliferation.

This SOP provides the framework for operating SignalBeast. Refer to `06_templates/` for trackers and handoff templates, and `05_prompts/` for prompt guidance.