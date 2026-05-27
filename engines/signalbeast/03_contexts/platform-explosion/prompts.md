# Platform Explosion Prompts

These prompts help guide the AI in creating platform‑specific outputs from the core assets.  Use them for thinking, file editing and batch processing within the **Platform Explosion** context.

## Thinking Task Prompt

> **Task:** Plan the platform‑specific content strategy.
>
> **Read:**
> - `summary.md`, `meta-description.md`, `key-highlights.md` from the core-generation phase.
> - The context analysis file for tone, keywords and audience.
> - Any platform SOPs or guidelines available in `01_source-material/`.
>
> **Steps:**
> - Identify which platforms are relevant for this run.
> - For each platform, outline the number of posts, their structure (e.g. hook + insights + CTA for Twitter; article + two posts for LinkedIn), and the CTA tier to be used.
> - Decide on hashtag sets or keyword phrases tailored to each platform.
> - Note any additional requirements such as video length or slide count.
>
> **Output:** A short content plan summarising the intended outputs per platform, including key structural elements and CTA tiering.

## File Editing Task Prompt

> **Task:** Generate the platform‑specific drafts.
>
> **Read:**
> - The content plan from the thinking task.
> - Core assets (summary, meta description, highlights).
> - Platform guidelines.
>
> **Steps:**
> - For each platform, write the required posts or scripts according to the plan.
> - Incorporate resonance mode cues, keyword/hashtag layering and canonical lines.
> - Vary the CTA across drafts (soft → engagement → conversion).
> - Save each draft as a Markdown file in `04_workspaces/platform-explosion/[run-folder]/` following the naming conventions.
>
> **Output:** Completed Markdown drafts for each platform with clear section headings and CTA markers.

## Folder Processing Task Prompt

> **Task:** Batch‑process highlights into platform drafts.
>
> **Read:**
> - `key-highlights.md` from the core-generation workspace.
>
> **Steps:**
> - For repetitive platforms like Twitter and Instagram, loop through each highlight and generate a corresponding tweet or carousel slide.
> - Apply the same structure to all items in a list (e.g. 7 tweets or 7 carousel scripts), ensuring each is unique but consistent.
> - After generating content for one highlight across all platforms, move to the next highlight.

> **Output:** A batch of drafts covering all highlights across selected platforms, stored in the run workspace.
