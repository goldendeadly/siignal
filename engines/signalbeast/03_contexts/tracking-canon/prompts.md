# Tracking & Canon Prompts

The following prompts guide the AI in logging outputs and recording performance metrics in the **Tracking & Canon** context.

## Thinking Task Prompt

> **Task:** Plan the tracking and verification process for the current run.
>
> **Read:**
> - All platform drafts created in the Platform Explosion phase.
> - The tracker templates located in `06_templates/`.
> - The run brief and context analysis for context.
>
> **Steps:**
> - Determine how many outputs exist and categorise them by platform and asset type.
> - Identify the fields that need to be captured for each output (headline, hashtags, CTA, canonical link, publish date, etc.).
> - Decide on a consistent status framework (Idea, Draft, Review, Scheduled, Published, Archived).
> - Plan how analytics will be collected once the outputs are published.
>
> **Output:** A succinct plan for populating the trackers, including a list of all outputs and the fields to log.

## File Editing Task Prompt

> **Task:** Populate the tracking tables and verify canonical statements.
>
> **Read:**
> - The plan from the thinking task.
> - The draft outputs and canonical line template.
>
> **Steps:**
> - For each output, fill in the **Platform Outputs** table with platform, asset type, headline/hook, hashtags, CTA, canonical link, publish date and status.
> - Update the **Content Master Tracker** entry with details of the run, including summary, meta description, key highlights and keywords.
> - Check every output file to ensure the canonical line appears exactly as specified.
> - Record any missing or incorrect canonical statements and fix them.
> - Save the tracker files to `04_workspaces/tracking-canon/[run-folder]/`.
>
> **Output:** Completed trackers and confirmed canonical statements across all output files.

## Folder Processing Task Prompt

> **Task:** Aggregate performance metrics post‑publication.
>
> **Read:**
> - Engagement and analytics data from relevant platforms (e.g. Twitter/X, LinkedIn, YouTube, etc.).
> - The **Platform Outputs** table to match each output with its metrics.
>
> **Steps:**
> - For each published output, collect metrics such as impressions, click‑through rate, engagement rate, comments, shares and open rates.
> - Add these metrics to the **Analytics & Memory Feedback** table.
> - Write a short reflection on the performance of each platform and content type.
> - Identify the top‑performing outputs and note why they resonated.

> **Output:** An updated analytics file summarising metrics and lessons learned for the run.
