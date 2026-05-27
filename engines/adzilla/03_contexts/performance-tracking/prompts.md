# Performance Tracking Prompts

Prompts to support logging metrics and capturing insights in the Performance Tracking context.

## Thinking Task Prompt

> **Task:** Plan the performance tracking process.
>
> **Read:**
> - Ad files generated in the Ad Assembly phase.
> - The targeting plan for audience and budget context.
> - Tracking templates in `06_templates/`.
>
> **Steps:**
> - Determine which metrics will be collected for each platform and how frequently.
> - Decide on the formula or weighting to calculate a performance score.
> - Plan how to record qualitative feedback (comments, sentiment) alongside numerical metrics.
>
> **Output:** A tracking plan summarising metrics, collection frequency, scoring method and qualitative notes.

## File Editing Task Prompt

> **Task:** Populate the trackers and write reflections.
>
> **Read:**
> - Current metrics from advertising platform dashboards.
> - Tracker files (`tracker-[product]-campaign-v1.md`, `tracker-[product]-ads-v1.md`).
>
> **Steps:**
> - Enter metrics into the appropriate fields for each ad.
> - Calculate performance scores and record them.
> - Write a concise reflection summarising what worked and what didn’t, linking to specific ads or audiences.
> - Save the updated trackers and reflections document in `04_workspaces/performance-tracking/[run-folder]/`.

> **Output:** Updated trackers and a reflection document with key insights.

## Folder Processing Task Prompt

> **Task:** Aggregate metrics across multiple periods or experiments.
>
> **Read:**
> - All tracker files (`tracker-[product]-ads-v*.md`) from the run.
>
> **Steps:**
> - Combine metrics from multiple versions or periods; calculate cumulative metrics (total impressions, total conversions, average CPC, overall ROAS).
> - Update the master tracker with the aggregated data.
> - Highlight trends (e.g. improving CTR over time, declining conversions after budget changes).

> **Output:** An aggregated metrics document and an updated master tracker.
