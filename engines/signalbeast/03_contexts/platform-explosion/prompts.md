# Platform Explosion Prompts

These prompts help guide the AI in creating platform-specific outputs from the core assets. Use them for thinking, file editing and batch processing within the **Platform Explosion** context.

## Thinking Task Prompt

> **Task:** Plan the platform-specific content strategy using the Signal Storm Protocol.
>
> **Read:**
> - `summary.md`, `meta-description.md`, `key-highlights.md` from the core-generation phase.
> - The context analysis file for tone, keywords and audience.
> - Any platform SOPs or guidelines available in `01_source-material/`.
>
> **Steps:**
> - Identify which platforms are relevant for this run.
> - For each platform, plan the full Signal Storm output:
>   - **TikTok:** 7 concepts (hook + structure + CTA, 15-60s scripts)
>   - **YouTube Shorts:** 7 scripts (vertical, punch-first, pattern-interrupt)
>   - **YouTube Longform:** 1 outline (full script structure, 10-15 min)
>   - **Instagram:** 7 carousels (headline slide + 5-10 value slides + CTA)
>   - **Pinterest:** 1 board theme + 7 pin titles (evergreen, keyword-rich)
>   - **Twitter/X:** 7 tweets (short, punchy, viral-style, < 280 chars)
>   - **LinkedIn:** 1 thought-leadership post (authority-first, story-driven)
>   - **Facebook:** 7 posts (authority-style or emotive, community-building)
>   - **Reddit:** 2 threads (question/answer format, value-first, native tone)
>   - **Quora:** 3 answers (expert positioning, link-back to source)
>   - **Email:** 1 (personal story or CTA bridge)
>   - **Ad Copy:** 3 variants (cold traffic, retargeting, subconscious CTA)
>   - **Landing Page:** 1 (H1, subhead, bullets, social proof, CTA, form)
> - Decide on hashtag sets or keyword phrases tailored to each platform.
> - Assign CTA tiers across the 48+ assets (soft, medium, hard distribution).
> - Integrate LSI terms, symptom statements, and transformational visioning across all planned content.
>
> **Output:** A content plan summarising the intended 48+ outputs per platform, including structural elements, CTA tiering, and subconscious integration notes.

## File Editing Task Prompt

> **Task:** Generate the platform-specific drafts.
>
> **Read:**
> - The content plan from the thinking task.
> - Core assets (summary, meta description, highlights).
> - Platform guidelines.
>
> **Steps:**
> - For each platform, write the required posts or scripts according to the plan.
> - Adapt tone per platform:
>   - TikTok: Raw, authentic, pattern-interrupt (hook in first 1.5s)
>   - Instagram: Aspirational, visual-first, value-dense
>   - LinkedIn: Professional authority, data-backed
>   - Twitter/X: Provocative, concise, hot takes
>   - Facebook: Community, story-driven, longer form
>   - Reddit: Native, value-first, never promotional
>   - YouTube: Educational, personality-driven, strong intro
> - Incorporate resonance mode cues, keyword/hashtag layering and canonical lines.
> - Ensure no content repeats itself — each asset is unique, not a copy-paste resize.
> - Vary the CTA across drafts (soft, medium, hard).
> - Save each draft as a Markdown file in `04_workspaces/platform-explosion/[run-folder]/` following the naming conventions.
>
> **Output:** Completed Markdown drafts for each platform with clear section headings and CTA markers.

## Folder Processing Task Prompt

> **Task:** Batch-process highlights into platform drafts.
>
> **Read:**
> - `key-highlights.md` from the core-generation workspace.
>
> **Steps:**
> - For repetitive platforms like Twitter and Instagram, loop through each highlight and generate a corresponding tweet or carousel slide.
> - Apply the same structure to all items in a list (e.g. 7 tweets or 7 carousel scripts), ensuring each is unique but consistent.
> - After generating content for one highlight across all platforms, move to the next highlight.
> - Embed subconscious resolution language, LSI terms, and identity anchoring ("You are the type of person who...") naturally across all outputs.

> **Output:** A batch of drafts covering all highlights across selected platforms, stored in the run workspace.

## Recursion Loop (Post-Deployment)

> **Task:** Evolve the next Signal Storm based on performance feedback.
>
> **Read:**
> - Platform analytics (engagement, clicks, bounce rate, comment sentiment).
>
> **Steps:**
> - High-performing hooks: Amplify and create 3 more variants.
> - Low-performing formats: Swap style (e.g., authority to empathy).
> - Audience language: Inject their exact words into next-gen copy.
> - Platform winners: Double output volume on that channel.
>
> **Output:** An evolved content plan that is more aligned with audience response data.
