# Terminal Prompts

Use these prompts in a command‑line or batch processing environment to aggregate data and manage multiple files at once.

## Tracker Compilation Prompt

> **Objective:** Compile campaign and ad performance trackers.
>
> **Read:**
> - All ad files in `04_workspaces/ad-assembly/[run-folder]/`.
> - Tracking templates in `06_templates/`.
>
> **Tasks:**
> - For each ad, extract the platform, headline, CTA and canonical line.
> - Populate the **Campaign Master Tracker** with run details, including budgets and platform allocation.
> - Populate the **Ad Performance Tracker** with the ad specifics.
>
> **Output:** Tracker files saved in `04_workspaces/performance-tracking/[run-folder]/`.

## Metrics Aggregation Prompt

> **Objective:** Combine performance metrics across multiple ad sets or time periods.
>
> **Read:**
> - Existing tracker files with metrics and scores.
>
> **Tasks:**
> - Sum or average metrics (impressions, clicks, CTR, conversions, CPC, ROAS) across versions or time periods.
> - Update the master tracker with aggregated values.
> - Identify trends and anomalies.
>
> **Output:** Aggregated metrics and updated tracker files.

## Batch Optimisation Prompt

> **Objective:** Apply multiple optimisation recommendations at once.
>
> **Read:**
> - `optimisation-expansion-v*.md` files.
>
> **Tasks:**
> - Loop through A/B test recommendations and schedule them for execution.
> - Generate new ad versions or audience segments as specified.
> - Update the campaign plan and trackers accordingly.
>
> **Output:** Updated campaign assets, schedules and trackers reflecting the applied optimisations.
