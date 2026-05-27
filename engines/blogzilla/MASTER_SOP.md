# Blogzilla Master SOP

This master standard operating procedure (SOP) outlines the high‑level workflow for running a Blogzilla content engine session. It assumes the folder structure described in `00_router/Claude.md` and uses the defined contexts to guide tasks through the system.

## Step‑by‑Step Execution

1. **Prepare Inputs**
   - Place the source blog post, URL, or idea into `07_inputs/source-blogs/` or record the keyword/idea in `07_inputs/keywords/`.
   - Create a run brief in `07_inputs/run-briefs/` summarising the topic, resonance mode, core intent, niche and any special constraints.

2. **Route the Task**
   - Consult `00_router/Claude.md` to determine which context handles the next action.
   - Each context has its own `context.md`, `workflow.md`, and `prompts.md` files; read those before starting work.

3. **Source Intake**
   - Enter the `source-intake` context to register the source, assign resonance mode and core intent, and create a dedicated run folder (`04_workspaces/source-intake/run‑YYYY‑MM‑DD‑slug/`).

4. **Context Analysis**
   - Move to `context-analysis` to decode tone, audience intent, emotional frequency, conversion goal and SEO cluster. Record the primary keyword, LSI terms, long‑tail variants, related questions and canonical statement.

5. **Core Generation**
   - In `core-generation`, generate a concise summary, a meta description, and 5–10 highlights tagged by type (framework, principle, statistic, provocation, meta‑insight). Save them into the run workspace.

6. **Platform Generation**
   - Enter `platform-generation` and produce platform‑specific outputs for each active channel. Follow the guidelines in `workflow.md` to ensure length, tone, CTA tier and canonical/backlink structure are correct. Save drafts into the appropriate `04_workspaces/platform-generation/run‑…/` folder.

7. **Amplification & Expansion**
   - In `amplification-expansion`, review the outputs and suggest new blog topics, collaboration or backlink opportunities, a lead magnet idea and an automation or system improvement.

8. **Tracking & Memory**
   - Switch to `tracking-memory` to update tracker tables with the outputs, performance metrics and lessons learned. This context collects analytics and prepares reflection notes for future runs.

9. **Automation & Deployment**
   - Finally, use `automation-deployment` to plan publishing cadence, schedule posts, prepare VA/Canva guidance, and integrate with automation tools. Create a deployment sheet and handoff instructions.

10. **Finalise and Archive**
   - When all outputs are approved, move the completed files from `04_workspaces` to `08_outputs/` (e.g. `08_outputs/summaries/`, `08_outputs/platform-assets/`, etc.).
   - Archive the run folder into `09_archive/` when the cycle is complete and update status fields in trackers.

## Roles and Responsibilities

- **Operator/Analyst** – reads the context files, runs the prompts, edits files and ensures outputs meet quality standards.
- **Router** – the system file that directs tasks to contexts; use it as your map.
- **Tracker Maintainer** – updates spreadsheets or Airtable trackers with the results and performance metrics.
- **VA/Design Assistant** – uses deployment instructions to produce visuals (e.g., carousels in Canva) and schedule posts.

## Tips

- Always read the `context.md` and `workflow.md` before starting tasks in a new context; they define the scope and prevent confusion.
- Use the naming conventions in `00_router/naming-conventions.md` so files can be found automatically by the AI.
- When in doubt, add a comment or TODO to document assumptions rather than guessing; the system is designed to be iterative.

This SOP provides the scaffold for operating Blogzilla. Specific prompts and templates live under `05_prompts/` and `06_templates/` and should be consulted during execution.