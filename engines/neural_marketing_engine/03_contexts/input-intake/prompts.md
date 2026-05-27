# Input Intake Prompts

Use these prompts as guidance when executing tasks within the input‑intake context.

## Thinking Prompt

> **Question:** What information do I need to start a new run and is anything missing from the run brief?
>
> **Action:** Review the run brief and ensure that niche, offer, avatar, tone, outcome and SEO intent are all specified.  Note any gaps and decide whether to request additional information or proceed with assumptions.

## File Editing Prompt

> **Task:** Create or validate the run brief for a new campaign.
>
> **Steps:**
> 1. Use the run brief template in `06_templates/` as a guide.
> 2. Populate all required fields.
> 3. Save the run brief as `[run-slug]-runbrief-intake-v1.md` in the new run folder inside `04_workspaces/input-intake/`.
> 4. If clarifications were needed, document them in a notes file (optional).

## Folder Processing Prompt

> **Task:** Initialise the workspace for a new run.
>
> **Steps:**
> 1. Derive the run slug from the niche and offer.
> 2. Create the run folder using the date and run slug pattern.
> 3. Copy the validated run brief into this folder.
> 4. Confirm that the folder and file names follow the naming conventions.