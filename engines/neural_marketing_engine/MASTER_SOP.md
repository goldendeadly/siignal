# Neural Marketing Engine v1 – Master SOP

This Standard Operating Procedure describes how to run the Neural Marketing Engine from beginning to end.  It is designed to be used by a single AI agent following a deterministic workflow.

## Roles

* **Operator (AI)** – executes every step according to the router and context instructions.
* **Strategist (optional)** – reviews the outputs and may provide feedback; not required for core operation.

## High‑Level Steps

1. **Setup & Intake**
   1. Collect or create a **run brief** using `06_templates/run-brief-template.md`.  Fill in all required fields (niche, offer, avatar, tone, outcome, SEO intent).  Save it as `[run-slug]-runbrief-intake-v1.md` in `07_inputs/run-briefs/`.
   2. Place any supporting materials (research notes, competitor examples) in `01_source-material/notes/`.

2. **Input Intake Context**
   1. Open `03_contexts/input-intake/context.md` and read its purpose and expected outputs.
   2. Open `03_contexts/input-intake/workflow.md` and follow the steps to normalise and validate the run brief.  Ensure no required field is missing.
   3. Save the processed brief in `04_workspaces/input-intake/` and mark the task complete.

3. **Strategy Modelling Context**
   1. Read `03_contexts/strategy-modeling/context.md` and its workflow.  Use the templates in `06_templates/` (avatar map, offer architecture, SEO intent) to create a comprehensive strategy model.
   2. Populate avatar psychology (demographics, pains, desires), offer positioning, tone guidelines (conscious frequency), desired outcome mapping and a keyword cluster based on SEO intent.
   3. Save the strategy model as `[run-slug]-strategy-model-core-v1.md` in `04_workspaces/strategy-modeling/`.

4. **Blog Generation Context**
   1. From the strategy model, generate **seven blog titles**.  Save them as `[run-slug]-blog-titles-generation-v1.md`.
   2. Choose (or solicit a choice) the most appropriate title.  Then write a full blog post (1,500–2,500 words) adhering to the tone and outcome specified.  Save as `[run-slug]-blog-post-generation-v1.md`.
   3. Store both files in `04_workspaces/blog-generation/` until final packaging.

5. **Signal Expansion Context**
   1. Read the blog post and strategy model.
   2. Use `06_templates/social-signal-template.md` to create multi‑platform social content (threads, carousels, scripts) tailored to each platform’s norms.  Include hooks, insights, CTAs and appropriate hashtags.
   3. Save as `[run-slug]-social-signal-expansion-v1.md` in `04_workspaces/signal-expansion/`.

6. **Conversion Assets Context**
   1. Using the strategy model and blog post, craft a set of ad copies (e.g. three variations per platform) and a landing page draft.  Follow the structure in `06_templates/conversion-assets-template.md` (headline, sub‑head, problem/promise sections, CTA stack, form section, etc.).
   2. Save the ad copy set as `[run-slug]-ad-copy-conversion-v1.md` and the landing page draft as `[run-slug]-landing-page-conversion-v1.md` in `04_workspaces/conversion-assets/`.

7. **Optimisation & Recursion (Optional)**
   1. If performance data or stakeholder feedback is available (CTR, engagement, conversions), place it in `07_inputs/feedback-inputs/`.
   2. Enter the `optimization-recursion` context.  Analyse the feedback using `03_contexts/optimization-recursion/workflow.md` and make revisions to the blog post, social assets, ads and landing page.  Increment version numbers accordingly (e.g. `v2`).  Save revisions in the same workspace.

8. **Packaging & Delivery**
   1. Once all assets are approved, enter the `packaging-output` context.  Use `06_templates/output-index-template.md` to create an index of all outputs.
   2. Copy final versions from each workspace into `08_outputs/final-delivery/`, maintaining naming conventions.
   3. Create an output index file `[run-slug]-output-index-final-v1.md` listing all deliverables, their locations, and a summary.

9. **Archive**
   1. Move the completed run folder inside `04_workspaces/` into `09_archive/old-runs/` when the client confirms delivery.
   2. Store outdated assets or revisions in `09_archive/superseded-assets/`.

## Principles

* **Follow the router** – Always consult `00_router/Claude.md` for routing rules.
* **Stay context aware** – Work only inside the current context and its workspace.  Do not edit files in other contexts.
* **Use naming conventions** – Predictable file names allow the AI to locate and update files automatically.
* **Document everything** – If a run decision is ambiguous or requires judgement, write a note in the workspace.
* **Iterate deliberately** – Only enter optimisation when performance feedback exists; otherwise move on to packaging.