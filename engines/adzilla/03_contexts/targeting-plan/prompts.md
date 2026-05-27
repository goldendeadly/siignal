# Targeting Plan Prompts

Prompts to support defining audience segments, budgets and schedules in the Targeting Plan context.

## Thinking Task Prompt

> **Task:** Plan the targeting strategy for the campaign.
>
> **Read:**
> - The run brief (budget, timeline, platforms).
> - `market-analysis-v1.md` for audience insights.
>
> **Steps:**
> - For each platform, describe who you want to reach based on demographics, interests and behaviours.
> - Suggest lookalike audiences or retargeting segments if applicable.
> - Allocate the budget proportionally across platforms and segments.
> - Determine the campaign schedule and dayparting.
> - Choose the optimization goal and bidding strategy.
>
> **Output:** An outline of audience segments, budgets, schedules and optimization goals for each platform.

## File Editing Task Prompt

> **Task:** Create the targeting plan file.
>
> **Read:**
> - The outline from the thinking task.
>
> **Steps:**
> - Write `targeting-plan-v1.md` with sections for each platform.
> - Under each platform, list audience segments (with criteria), geographic targeting, budget allocation, schedule and optimization goal.
> - Use bullet points and short phrases; avoid long sentences in tables.
> - Save the file to `04_workspaces/targeting-plan/[run-folder]/`.
>
> **Output:** A completed targeting plan file ready for execution.

## Folder Processing Task Prompt

> **Task:** Consolidate multiple targeting plans or update existing ones.
>
> **Read:**
> - All `targeting-plan-v*.md` files in the run workspace.
>
> **Steps:**
> - Merge similar audience segments and unify budget allocations.
> - Resolve conflicting schedules or overlapping audiences.
> - Produce a new version with updated recommendations.

> **Output:** A revised targeting plan file incorporating all feedback.
