# Neural Marketing Engine v1 Router

## System Description

The Neural Marketing Engine is a strategy and funnel‑generation system that converts a structured marketing input into a complete modular marketing ecosystem.  It begins with six input variables—**niche/industry**, **offer/product**, **core avatar**, **conscious frequency** (resonance mode), **primary outcome/transformation** and **SEO intent**—and produces:

* seven blog title candidates;
* one long‑form blog post;
* a multi‑platform social signal (threads, carousels, scripts);
* an ad copy set and a landing page;
* optional iterative improvements based on performance data.

This router defines the folder map, context definitions and routing rules for the engine.  Always consult this file before starting a new task.

## Folder Map

* `00_router/` – system map, routing rules, naming logic
* `01_source-material/` – original prompts, research notes, reference documents
* `02_system-definition/` – overview, workflow map, rules, terminology, output definitions
* `03_contexts/` – context folders with their own instructions and prompts
* `04_workspaces/` – active work by context during a run
* `05_prompts/` – generic Desktop, VS Code and Terminal prompts
* `06_templates/` – reusable templates (run brief, avatar map, offer architecture, SEO intent, social signal, conversion assets, feedback loop, output index)
* `07_inputs/` – structured run inputs (run briefs, niche/offer inputs, avatar inputs, SEO inputs, feedback inputs)
* `08_outputs/` – generated outputs (strategy models, blog assets, social signal, conversion assets, recursion revisions, final delivery)
* `09_archive/` – completed or superseded runs

## Context Definitions

* **`input-intake`** – captures and normalises the full input block.  Produces a validated run brief ready for modelling.
* **`strategy-modeling`** – builds an integrated avatar, offer, tone and SEO model.  Produces a strategy model used by all downstream contexts.
* **`blog-generation`** – generates blog titles and the long‑form blog post based on the strategy model.
* **`signal-expansion`** – creates a multi‑platform social signal, including threads, carousels and short‑form scripts.
* **`conversion-assets`** – generates ad copy sets and a landing page draft, applying CTA layering and channel‑specific requirements.
* **`optimization-recursion`** – refines outputs based on feedback or performance data.  Produces revised assets with incremented version numbers.
* **`packaging-output`** – assembles all completed assets and creates a final delivery package and index.

## Routing Rules

If the task is:

* **Entering a new business / offer / avatar** → go to **`input-intake`**.
* **Clarifying messaging / transformation / avatar psychology** → go to **`strategy-modeling`**.
* **Creating blog titles or a blog post** → go to **`blog-generation`**.
* **Creating platform content outputs** → go to **`signal-expansion`**.
* **Creating ads or landing page copy** → go to **`conversion-assets`**.
* **Refining outputs based on performance data** → go to **`optimization-recursion`**.
* **Preparing final delivery files** → go to **`packaging-output`**.

## Output Rule

Work must be created inside the matching workspace first (`04_workspaces/[context]/`).  Once an output is approved, move the final version into the corresponding folder in `08_outputs/`.  Do not place unfinished files directly into `08_outputs/`.

## Execution Rule

Do **not** read the entire system unless necessary.  Route to the relevant context and use only the files required for the current task.  This keeps the AI focused and efficient.