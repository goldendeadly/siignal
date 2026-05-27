# Blog Generation Prompts

## Thinking Prompt

> **Question:** What headline ideas will grab the avatar’s attention and signal the transformation promised by the offer?
>
> **Action:** Review the avatar’s pains and desires from the strategy model.  Brainstorm a variety of headlines (how‑to, secrets, contrarian angles, numbered lists).  Check each for clarity, relevance and keyword inclusion.  Rank or select the best one.

## File Editing Prompt

> **Task:** Write the full blog post based on the chosen title.
>
> **Steps:**
> 1. Outline the structure: introduction, problem explanation, solution demonstration, evidence/proof, conclusion and CTA.
> 2. Draft each section using the tone and outcome guidelines.  Incorporate the primary keyword and LSI terms naturally.
> 3. Keep paragraphs short (2–4 sentences), use subheadings and bullet points for readability.
> 4. Save as `[run-slug]-blog-post-generation-v1.md` in the current run’s blog generation folder.

## Folder Processing Prompt

> **Task:** Organise titles and blog files.
>
> **Steps:**
> 1. Ensure the titles file and blog post file are saved in the `04_workspaces/blog-generation/` directory.
> 2. If a selection note exists, include it next to the titles list.
> 3. Copy final versions to `08_outputs/blog-assets/` when moving to packaging.