# SignalBeast Router

This router defines the SignalBeast system, lists the context areas, sets naming rules and explains how to route tasks. Use it as your map when running the engine.

## System Description

SignalBeast is a GIGA‑prompt content deployment engine that transforms a source blog or idea into over 100 platform‑native assets. It operates through seven contexts: context decoder, core generation, platform explosion, tracking & canon, signal expansion, automation suggestions and recursion engine. The system also produces an SEO supercluster grid, a platform publication matrix and a self‑mutation feedback loop.

## Folder Map

- `00_router/` – router description, routing table and naming conventions.
- `01_source-material/` – reference documents, action trees, prompt examples, SOPs.
- `02_system-definition/` – system overview, goals, rules, workflow map and output catalogue.
- `03_contexts/` – subfolders for each context: `context-decoder`, `core-generation`, `platform-explosion`, `tracking-canon`, `signal-expansion`, `automation-suggestions`, `recursion-engine`. Each contains `context.md`, `workflow.md` and `prompts.md`.
- `04_workspaces/` – active workspaces for each context. New run folders live here until outputs are finalised.
- `05_prompts/` – desktop, VS Code and terminal prompt guides.
- `06_templates/` – tracker templates, run briefs, expansion logs, handoff forms.
- `07_inputs/` – incoming sources, keywords, run briefs and resonance modes.
- `08_outputs/` – final outputs, trackers, matrices, expansion suggestions and automation notes.
- `09_archive/` – archived run folders and superseded assets.

## Context Definitions

| Context | Purpose | Sample tasks |
| --- | --- | --- |
| **context‑decoder** | Analyse tone, audience intent, conversion goal and SEO clusters; produce canonical line and supercluster grid. | Identify tone and audience; map primary & LSI keywords; suggest long‑tail variants and questions; craft canonical statement. |
| **core‑generation** | Generate summary, meta description and modular highlights. | Write summary and meta description; extract and tag 5–10 highlights. |
| **platform‑explosion** | Produce 100+ platform‑native outputs across all selected channels. | Create threads, carousels, articles, scripts, pins, emails, prompts; assemble publication matrix; apply CTA tiering and resonance mode. |
| **tracking‑canon** | Log outputs, canonical links and performance metrics. | Update trackers; record platform, CTA, keyword usage, and resonance score for each asset; compile content matrices. |
| **signal‑expansion** | Suggest new topics, collaborations/backlinks, lead magnets and adjacent niches. | Generate 5 new blog topics; list 3 collaborators/backlinks; propose a lead magnet; note adjacent keywords. |
| **automation‑suggestions** | Recommend workflow automations and system improvements. | Identify processes to streamline; propose Zapier flows or scheduling scripts; assign tasks to VAs or tools. |
| **recursion‑engine** | Execute mutation commands and generate secondary outputs. | Run `/mutate`, `/threadcast`, `/glyphseed`, `/storybind`, `/promptforge`, `/recur100`; record new assets and update trackers. |

## Routing Instructions

Use the following mapping to send tasks to contexts:

* **Decoder tasks** (tone analysis, SEO mapping, canonical statement) → `context-decoder`.
* **Core generation tasks** (summary, meta, highlights) → `core-generation`.
* **Content explosion tasks** (creating threads, carousels, scripts, etc.) → `platform-explosion`.
* **Tracking tasks** (logging outputs, updating trackers, calculating resonance scores) → `tracking-canon`.
* **Expansion tasks** (new topics, collaborations, backlinks, lead magnets) → `signal-expansion`.
* **Automation tasks** (workflow improvements, scheduling recommendations) → `automation-suggestions`.
* **Recursion tasks** (mutating outputs, generating new variants) → `recursion-engine`.

Place outputs in the appropriate workspace under `04_workspaces/` first and move them to `08_outputs/` only when final. Follow the naming rules below.

## Naming Rules

See `00_router/naming-conventions.md` for full guidelines. Use kebab‑case and version numbers. Run folders follow `run‑YYYY‑MM‑DD‑slug/`; file names follow `[topic]‑[asset]‑[platform]‑[status]‑v[number].md`.