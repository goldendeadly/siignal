# Core Generation Prompts

Use the following prompts to guide the AI through the tasks required in the **Core Generation** phase.  Each section specifies what to read, the objectives, and the expected outputs.

## Thinking Task Prompt

> **Task:** Convert the contextual analysis into modular core assets.
>
> **Read:**
> - `context-analysis-v1.md` from the run workspace.
> - The original source material if further clarity is needed.
>
> **Steps:**
> - Write a succinct summary (2–3 sentences) capturing the source’s key idea and tone.
> - Compose a meta description (150–160 characters) that incorporates the primary keyword.
> - Extract 5–10 standalone highlights; write them as short, punchy statements and tag each appropriately (Framework, Principle, Statistic, Provocation or Meta‑Insight).
>
> **Output:** A short report outlining the summary, meta description and list of highlights with tags.  Note any ambiguity or missing details.

## File Editing Task Prompt

> **Task:** Create the core asset files.
>
> **Read:**
> - The draft report from the thinking task.
>
> **Steps:**
> - Write `summary.md` with the finalized 2–3 sentence summary.
> - Write `meta-description.md` with the final meta description.
> - Write `key-highlights.md` as a bullet list with each highlight followed by its tag in brackets (e.g. “Insight about systems thinking (Principle)”).
> - Save these files to `04_workspaces/core-generation/[run-folder]/`.
>
> **Output:** The three completed Markdown files in the core-generation workspace.

## Folder Processing Task Prompt

> **Task:** Batch‑process multiple summaries or highlight sets if the run includes multiple source posts or ideas.
>
> **Read:**
> - All `context-analysis-v1.md` files in the current run folder (if multiple sources were decoded).
>
> **Steps:**
> - Combine the summaries into a single coherent summary highlighting the unified topic.
> - Merge meta descriptions, ensuring primary keywords from each source appear naturally within a 150–160 character limit.  If this cannot be done cleanly, generate separate meta descriptions.
> - Consolidate all highlights into one list, retaining tags, and remove duplicates.
>
> **Output:** A combined set of core assets reflecting all sources in the run.
