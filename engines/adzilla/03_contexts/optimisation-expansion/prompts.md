# Optimisation & Expansion Prompts

These prompts guide the creation of tests, retargeting strategies and automation recommendations in the Optimisation & Expansion context.

## Thinking Task Prompt

> **Task:** Generate improvement ideas based on performance data.
>
> **Read:**
> - The reflections document (`performance-reflections-v1.md`).
> - Tracker files with metrics and performance scores.
>
> **Steps:**
> - List the top‑performing ads, hooks, audiences and platforms.  Identify the factors contributing to success.
> - List underperforming elements and hypothesise why they didn’t work.
> - Brainstorm possible A/B test variants (headlines, CTAs, creatives, audiences).
> - Identify retargeting audiences and suggest tailored offers or messages for each.
> - Suggest cross‑sell/up‑sell ideas based on the product ecosystem.
> - Note any manual tasks that could be automated.
>
> **Output:** A brainstorming document summarising potential tests, retargeting strategies, cross‑sell opportunities and automation ideas.

## File Editing Task Prompt

> **Task:** Write the optimisation & expansion report.
>
> **Read:**
> - The brainstorming document.
>
> **Steps:**
> - Create `optimisation-expansion-v1.md` with sections for tests, retargeting, cross‑sell/up‑sell and automation recommendations.
> - For each recommendation, include the rationale, expected impact, and next steps.
> - Save the report to `04_workspaces/optimisation-expansion/[run-folder]/`.

> **Output:** A structured report to guide future campaign enhancements.

## Folder Processing Task Prompt

> **Task:** Consolidate multiple optimisation reports.
>
> **Read:**
> - All `optimisation-expansion-v*.md` files in the run workspace.
>
> **Steps:**
> - Merge recommendations, remove duplicates and prioritise based on potential impact.
> - Highlight any conflicting tests or suggestions for resolution.
> - Save a final version with the next version number.

> **Output:** A unified optimisation & expansion plan for the run.
