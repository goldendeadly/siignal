# Blogzilla Content Engine

Blogzilla is a reusable AI‑workspace system for turning a single blog post, keyword, or idea into a multi‑platform content ecosystem. It applies a structured workflow—analysis, modular generation, platform adaptation, amplification, tracking and automation—so that the same source material can be repurposed and expanded across many channels while preserving SEO signals, tone coherence and canonical links.

## Purpose

* Convert one source blog or idea into a consistent, SEO‑compounding set of assets.
* Produce summaries, highlights, modular snippets, and platform‑specific posts for channels such as X/Twitter, LinkedIn, Instagram, YouTube, Quora, Facebook, Pinterest, Medium, Substack, Blogger and Dev.to.
* Capture metadata (keywords, tone, resonance mode, CTA tier) and feed it into a tracker so future runs can build on past results.
* Suggest expansion opportunities—new topics, collaborations, backlinks, lead magnets and automations—to keep the content engine evergreen.

## Inputs

- **Source blog post, URL or idea** – the raw content to be repurposed.
- **Resonance mode** – chosen tone calibration (Authority, Emotional, Technical, Viral or Educational).
- **Core intent** – e.g. SEO dominance, lead generation, thought leadership or audience growth.
- **Niche/domain** – context for keyword and audience mapping.
- **Optional recursion setting** – whether to re‑run the engine on its own outputs.

## Outputs

- 2–3 sentence summary and 150–160 character meta description.
- 5–10 key highlights tagged as frameworks, principles, statistics, provocations or meta‑insights.
- Platform‑specific assets (threads, carousels, videos, posts, reels, answers, pins, articles, emails, prompts).
- Canonical/backlink statements and hashtag sets.
- Tracking tables (content master tracker, platform outputs, analytics & memory feedback, expansion & collaboration).
- Expansion suggestions (new topics, collaborators, backlinks, lead magnet ideas, automation improvements).

## Constraints and Rules

* Preserve canonical consistency—every output must reference the original blog and maintain tone coherence.
* Adapt outputs to each platform’s length, style and CTA requirements.
* Separate source material from generated outputs; do not overwrite the original.
* Derive context areas from the workflow rather than inventing arbitrary names.
* Use explicit naming conventions so files are predictable and machine‑findable.
* Optimize routing to ensure the AI reads only the files relevant to the current task.

## Folder Structure

The system follows a layered architecture: **router** (Layer 1) defines the system description, context definitions and naming rules; **context areas** (Layer 2) encapsulate the tasks at each stage; and **workspaces** (Layer 3) hold working files and outputs. A full folder blueprint is provided in `00_router/Claude.md` and the system definition files under `02_system-definition`.