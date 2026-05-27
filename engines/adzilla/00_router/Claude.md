# AdZilla Router

## System Description

AdZilla is an AI‑assisted advertising engine that converts an offer into multi‑channel ad campaigns.  It provides a structured environment for analysing your product, generating value propositions, crafting channel‑specific ads, planning targeting, tracking performance, and optimising and expanding campaigns.  The router helps you understand the folder structure, context definitions, naming conventions and routing rules.

## Folder Map

- `00_router/` – Contains the router description (this file), the routing table and naming conventions.
- `01_source-material/` – Storage for reference documents such as platform guidelines, compliance checklists, example ads and SOPs.
- `02_system-definition/` – High‑level system overview, workflow map, goals and rules.
- `03_contexts/` – Contains subfolders for each context area (offer-intake, market-analysis, creative-generation, ad-assembly, targeting-plan, performance-tracking, optimisation-expansion).  Each subfolder includes `context.md`, `workflow.md` and `prompts.md`.
- `04_workspaces/` – Active work directories for each context.  When you start a run, create a folder under the appropriate context for that run.
- `05_prompts/` – Generic prompts for desktop, IDE and terminal environments.
- `06_templates/` – Templates for run briefs, trackers, plans, expansion ideas and handoff documents.
- `07_inputs/` – Where you place run briefs, offer details, audience descriptions and other input files.
- `08_outputs/` – The destination for final campaign assets, performance reports and summary documents.
- `09_archive/` – Storage for completed runs and outdated materials.

## Context Definitions

- **offer-intake** – Gather and document offer details, marketing objectives, target audience, resonance mode and platform selections.
- **market-analysis** – Analyse the audience persona, competitor landscape, regulatory environment and brand voice.  Identify benefits and differentiators.
- **creative-generation** – Produce value propositions, benefit bullets, hooks and taglines tailored to the resonance mode.
- **ad-assembly** – Compose channel‑specific ads (headline, body copy, CTA, creative note) for each selected platform.
- **targeting-plan** – Design audience segmentation, geographic targeting, budget allocations and scheduling for each ad platform.
- **performance-tracking** – Record performance metrics, update trackers, reflect on results and maintain canonical lines.
- **optimisation-expansion** – Suggest A/B tests, retargeting strategies, cross‑selling opportunities and automation improvements.

## Routing Instructions

| Task Description | Context |
|---|---|
| Define a new campaign run, collect offer details and set objectives | `offer-intake` |
| Analyse the audience persona and competitor landscape | `market-analysis` |
| Craft value propositions, benefit bullets, hooks and taglines | `creative-generation` |
| Generate ads for Facebook, Instagram, Google Ads, LinkedIn, YouTube, TikTok or other platforms | `ad-assembly` |
| Plan audience targeting, budgets, schedules and segments | `targeting-plan` |
| Log ads, update performance metrics, compute ROI and reflect on results | `performance-tracking` |
| Recommend A/B tests, retargeting campaigns, cross‑selling, lookalike audiences and automations | `optimisation-expansion` |

## Naming Rules

Naming conventions ensure that files are predictable and machine‑readable.

- **Run Folders:** `run-[YYYY-MM-DD]-[product-slug]` (e.g. `run-2026-03-13-solar-panels`).  Create these inside the `04_workspaces/[context]/` directory.
- **Ad Files:** `[product]-[platform]-ad-[status]-v[number].md` (e.g. `solar-panels-facebook-ad-draft-v1.md`).  Status could be `draft`, `review`, `final`, etc.
- **Value Proposition Files:** `[product]-value-propositions-v[number].md`.
- **Targeting Plan Files:** `[product]-targeting-plan-v[number].md`.
- **Tracker Files:** `tracker-[product]-campaign-v[number].md` for the master tracker and `tracker-[product]-ads-v[number].md` for individual ads.
- **Expansion Files:** `[product]-optimisation-expansion-v[number].md`.

Follow these naming conventions to allow automated scripts to find and update files correctly.
