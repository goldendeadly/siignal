# Packaging Output Prompts

## Thinking Prompt

> **Question:** Have all deliverables been generated and are you selecting the most recent version of each asset?  Are there any missing pieces or inconsistencies?
>
> **Action:** Review the workspaces and identify the latest version of each asset.  Ensure nothing has been overlooked.  Verify that version numbers are consistent and that no context has been skipped.

## File Editing Prompt

> **Task:** Create the output index.
>
> **Steps:**
> 1. Open the output index template.  List each asset with its type, file name, version and a one‑sentence description.
> 2. Include hyperlinks or relative paths to each file for easy navigation (optional).
> 3. Save the index as `[run-slug]-output-index-final-v1.md` in the final delivery folder.

## Folder Processing Prompt

> **Task:** Assemble the final delivery package.
>
> **Steps:**
> 1. Create a subfolder inside `08_outputs/final-delivery/` named after the run.
> 2. Copy the final versions of each asset into this folder.
> 3. Copy the output index into the same folder.
> 4. Move the run folder from the workspace to `09_archive/old-runs/` (optional step if archiving now).