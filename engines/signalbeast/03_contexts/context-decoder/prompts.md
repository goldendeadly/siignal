# Context Decoder Prompts

These prompts guide the AI through thinking, file editing, and folder processing tasks in the **Context Decoder** phase.  Each section specifies what to read, what to do, and what to produce.

## Thinking Task Prompt

> **Task:** Analyse the provided source blog post, keyword, or idea to decode its underlying context.
>
> **Read:**
> - The raw source file in `07_inputs/` (blog post, keyword or idea).
> - The run brief in `04_workspaces/source-intake/[run-folder]/run-brief.md`.
>
> **Steps:**
> - Identify the dominant tone (educational, emotional, technical, etc.).
> - Determine the target audience and primary intent (awareness, authority, leads, retention, etc.).
> - Extract the primary keyword and 3–5 LSI/secondary keywords; suggest long‑tail variants and related questions.
> - Recommend a publication frequency and content silo.
> - Draft a canonical statement referencing the original blog and domain.
>
> **Output:** Provide a concise plan summarising your findings, highlighting any missing information or assumptions to be confirmed.

## File Editing Task Prompt

> **Task:** Create a structured analysis file for the context decoding phase.
>
> **Read:**
> - Your notes from the thinking task.
>
> **Steps:**
> - Write a Markdown file (`context-analysis-v1.md`) capturing tone, audience, intent, keyword map, long‑tail variants, related questions, cadence, silo and canonical line.
> - Use bullet lists and short paragraphs; avoid long sentences in tables.
> - Save the file to `04_workspaces/context-decoder/[run-folder]/`.
>
> **Output:** A well‑structured `context-analysis-v1.md` ready for use in later phases.

## Folder Processing Task Prompt

> **Task:** Normalise multiple source inputs when more than one blog or idea is provided.
>
> **Read:**
> - All files in `07_inputs/source-blogs/`, `07_inputs/keywords/` or similar for the current run.
>
> **Steps:**
> - Compare multiple sources for tone, audience, intent and keywords.
> - Merge them into a single, cohesive analysis capturing shared themes and distinct nuances.
> - Save the merged analysis as `context-analysis-v1.md` in the workspace.
>
> **Output:** A single canonical analysis file reflecting the composite context across all inputs.
