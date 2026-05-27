# VS Code Prompts

These prompts are intended for use in an integrated development environment (IDE) such as VS Code.  They support focused content creation and editing within a specific context of the SignalBeast system.

## Context‑Specific Content Creation Prompt

> **Objective:** Generate or edit files within a single context.
>
> **Read:**
> - The context definition (`context.md`) and workflow (`workflow.md`) for the current context in `03_contexts/[context-name]/`.
> - All relevant input files in `04_workspaces/[context-name]/[run-folder]/`.
>
> **Tasks:**
> - Follow the steps outlined in the workflow to generate or edit the required files.
> - Use the naming conventions defined in `00_router/naming-conventions.md`.
> - Ensure outputs are saved in the correct workspace subfolder.
>
> **Output:** One or more completed Markdown files representing the deliverables for the current context (e.g. summaries, highlights, platform drafts, trackers, automation plans).

## Platform Drafting Prompt

> **Objective:** Produce platform‑specific content drafts using the core assets.
>
> **Read:**
> - The content plan from the Platform Explosion thinking task.
> - The core assets (`summary.md`, `meta-description.md`, `key-highlights.md`).
> - Any platform guidelines stored in `02_system-definition/`.
>
> **Tasks:**
> - For each designated platform, write the drafts according to the plan (hooks, insights, transitions, CTA, hashtags, canonical line).
> - Save each draft in the appropriate workspace folder using the correct naming convention.
>
> **Output:** Complete platform drafts ready for review and logging.
