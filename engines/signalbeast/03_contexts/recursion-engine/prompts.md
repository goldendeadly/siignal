# Recursion Engine Prompts

These prompts guide the AI through selecting assets, choosing commands and generating mutated outputs in the **Recursion Engine** phase.

## Thinking Task Prompt

> **Task:** Plan the recursion strategy for extending the content set.
>
> **Read:**
> - All existing output files from the current run.
> - The **Recursion Pathways** table (if any previous recursions were performed).
> - The expansion recommendations to recall suggested transformations.
>
> **Steps:**
> - Identify which assets have the strongest potential for mutation (e.g. high engagement, adaptable formats).
> - Select the recursion commands that will produce the most value (e.g. `/threadcast` for turning a paragraph into a Twitter thread).
> - Decide how many new pieces you aim to generate and which platforms they will target.
>
> **Output:** A plan specifying assets to mutate, commands to use and expected platforms or formats for the new outputs.

## File Editing Task Prompt

> **Task:** Execute a recursion command and create a new asset.
>
> **Read:**
> - The plan from the thinking task.
> - The original asset file to be mutated.
>
> **Steps:**
> - Apply the selected command (e.g. `/mutate`, `/threadcast`, `/glyphseed`) to the content of the original file.
> - Write the resulting content according to the target platform’s conventions.
> - Include a CTA and the canonical line.
> - Save the new content to `04_workspaces/recursion-engine/[run-folder]/` following the naming convention `[topic]-[new-format]-[platform]-v1.md`.
> - Update the **Recursion Pathways** table with details of the transformation.
>
> **Output:** A new content file and an updated pathways record documenting the recursion.

## Folder Processing Task Prompt

> **Task:** Batch‑mutate multiple assets.
>
> **Read:**
> - A list of assets selected for mutation.
> - The commands to apply to each asset.
>
> **Steps:**
> - For each asset, apply the designated command and generate the mutated output.
> - Save each new file to the recursion engine workspace with correct naming conventions.
> - Append all transformations to the **Recursion Pathways** table.

> **Output:** A batch of new assets derived via recursion and a comprehensive pathways table.
