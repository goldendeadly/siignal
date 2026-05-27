# Terminal Prompts

These prompts are designed for command‑line or batch processing environments.  Use them when aggregating data, generating tables, or performing bulk operations in SignalBeast.

## Tracker Compilation Prompt

> **Objective:** Compile and summarise all outputs and metrics into tracker files.
>
> **Read:**
> - All draft outputs stored in the current run’s workspace.
> - The tracking templates in `06_templates/`.
>
> **Tasks:**
> - For each output file, extract the platform, asset type, headline or hook, keywords/hashtags, CTA tier and canonical link.
> - Append this information to the **Platform Outputs** table.
> - Summarise high‑level details into the **Content Master Tracker**.
>
> **Output:** Updated tracker files saved to `04_workspaces/tracking-canon/[run-folder]/`.

## Metrics Aggregation Prompt

> **Objective:** Process performance metrics and calculate scores.
>
> **Read:**
> - Platform analytics data (from spreadsheets or APIs).
> - The **Platform Outputs** table to match metrics to assets.
>
> **Tasks:**
> - Combine metric values (impressions, CTR, engagement rate, open rate) with the corresponding output records.
> - Compute performance scores using the defined formula (e.g. `(CTR×0.4)+(Engagement×0.3)+(Opens×0.3)`).
> - Identify top‑performing platforms and outputs.
>
> **Output:** An updated **Analytics & Memory Feedback** table saved to `04_workspaces/tracking-canon/[run-folder]/`.

## Batch Recursion Prompt

> **Objective:** Perform recursion on multiple assets via command‑line.
>
> **Read:**
> - A list of asset IDs and corresponding recursion commands.
>
> **Tasks:**
> - Loop through each asset and apply the specified recursion command.
> - Save the mutated outputs with appropriate names.
> - Append entries to the **Recursion Pathways** table.
>
> **Output:** A set of mutated content files and an updated pathways table ready for review.
