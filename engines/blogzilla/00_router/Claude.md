# Blogzilla Router

This router describes the Blogzilla system, defines the core context areas and naming rules, and provides routing instructions for common tasks.

## System Description

Blogzilla is a recursive content repurposing engine. It ingests a single blog post, keyword or idea and transforms it into a multi‑platform content ecosystem while preserving SEO structure, canonical consistency and brand tone. The engine operates through a sequence of contexts: source capture, analysis, core content generation, platform adaptation, amplification & expansion, tracking & memory, and automation & deployment.

## Folder Map

- `00_router/` – router description, routing table and naming conventions.
- `01_source-material/` – reference documents: engine specs, action trees, SOPs, research notes, prompts, examples.
- `02_system-definition/` – high‑level system definition files: overview, goals, rules, workflow map and output catalogue.
- `03_contexts/` – one subfolder per context (source‑intake, context‑analysis, core‑generation, platform‑generation, amplification‑expansion, tracking‑memory, automation‑deployment). Each contains `context.md`, `workflow.md` and `prompts.md`.
- `04_workspaces/` – active workspaces for each context; new run folders live here until final outputs are moved.
- `05_prompts/` – prompt templates separated by interface (desktop, VS Code, terminal) and by task type (thinking, file editing, folder processing).
- `06_templates/` – reusable templates such as trackers, output catalogues, weekly review, master handoff and content master tracker.
- `07_inputs/` – incoming materials: source blogs, URLs, keywords, run briefs and resonance modes.
- `08_outputs/` – completed outputs: summaries, platform assets, trackers, distribution plans, feedback digests, expansion ideas.
- `09_archive/` – retired runs and superseded materials.

## Context Definitions

| Context | Purpose | Examples of tasks |
| --- | --- | --- |
| **source‑intake** | Capture the source, assign resonance mode and intent, create the run folder. | Register blog/link, pick resonance mode and core intent, create run brief. |
| **context‑analysis** | Analyse tone, audience intent, conversion goal and SEO cluster; produce canonical statement and keyword map. | Determine tone, audience, conversion goal; map primary and LSI keywords; suggest long‑tail variants and related questions. |
| **core‑generation** | Generate summary, meta description and key highlights tagged by type. | Write 2–3 sentence summary, 150–160 character meta description, extract 5–10 highlights. |
| **platform‑generation** | Adapt the core assets into platform‑specific outputs with appropriate tone, length and CTA. | Generate tweets, LinkedIn posts, Instagram carousels, YouTube scripts, Quora answers, Medium/Substack articles, etc. |
| **amplification‑expansion** | Identify new topics, collaboration or backlink opportunities, lead magnet ideas and automation suggestions. | Suggest five new blog ideas, three collaboration/backlink opportunities, one lead magnet, one automation improvement. |
| **tracking‑memory** | Track outputs and performance, record lessons learned and plan next iterations. | Update trackers, log analytics and reflections, identify top‑performing content. |
| **automation‑deployment** | Plan publishing cadence, schedule posts, prepare VA/Canva guidance and integrate automation. | Create deployment plan, schedule posts, prepare design instructions, set up automation triggers. |

## Routing Instructions

When deciding where to send a task, match the task description against the context definitions above. Use the following mapping:

* **Source intake tasks** such as adding a new blog, choosing resonance mode or creating a run brief → **source‑intake**.
* **Analysis tasks** such as tone decoding, audience intent, keyword mapping or canonical statements → **context‑analysis**.
* **Summary and highlight creation** → **core‑generation**.
* **Generating platform‑specific posts, carousels, scripts, articles or answers** → **platform‑generation**.
* **Finding new topics, collaborations, backlinks, magnets or automation improvements** → **amplification‑expansion**.
* **Updating trackers, logging analytics, writing reflection notes or calculating performance** → **tracking‑memory**.
* **Preparing publishing schedules, instructions for VAs/designers, or automation flows** → **automation‑deployment**.

Always place outputs in the matching workspace first (e.g. `04_workspaces/platform‑generation/run‑…/`) and move them to `08_outputs/` only when final. Follow the naming conventions defined below.

## Naming Rules

Refer to `00_router/naming-conventions.md` for the full naming guidelines. Use predictable, kebab‑cased file names and version numbers so the system can locate files automatically. Run folders follow the pattern `run‑YYYY‑MM‑DD‑slug/` and file names follow `[topic]‑[asset]‑[platform]‑[status]‑v[number].md`.