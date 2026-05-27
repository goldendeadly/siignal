# Neural Marketing Engine v1

## Purpose

The **Neural Marketing Engine** is a modular, AI‑driven system for turning a few structured marketing inputs into a complete marketing ecosystem.  It takes six core variables—**niche/industry**, **offer/product**, **core avatar**, **conscious frequency** (tone/resonance), **primary outcome/transformation**, and **SEO intent**—and converts them into:

* a set of seven compelling blog titles;
* a long‑form blog post optimised for the chosen avatar and outcome;
* a multi‑platform social signal (threads, carousels, short videos, etc.);
* ad copy sets with tiered calls‑to‑action;
* a landing page draft with coherent messaging and CTA stacking; and
* optional iterative improvements driven by performance feedback.

The system is designed to be reused across different industries and offers.  By following the provided router, contexts and naming conventions, a single AI can navigate the entire workflow without needing multiple agents or human intervention.

## Inputs

The engine relies on a concise run brief containing:

1. **Niche/Industry** – e.g. “roofing”, “nutrition coaching”, “AI software”, etc.
2. **Offer/Product** – a description of the product or service being promoted.
3. **Core Avatar** – demographic and psychographic profile of the ideal customer.
4. **Conscious Frequency / Tone** – a resonance setting describing how the messaging should feel (e.g. educational, persuasive, emotional, technical).
5. **Primary Outcome** – the transformation or result the customer seeks.
6. **SEO Intent** – the overarching search intent (informational, transactional, comparison, etc.) and seed keywords.

Optional inputs include competitor examples, existing research notes and past performance feedback.

## Outputs

When run end‑to‑end, the engine will produce:

* **Strategy model** – a consolidated document describing avatar psychology, offer framing, tone guidelines, outcome mapping and keyword cluster.
* **Blog titles** – seven candidate titles derived from the strategy model.
* **Long‑form blog post** – one full post (1500–2500 words) based on the selected title.
* **Social signal** – a collection of posts, captions and scripts for major platforms (Twitter/X, LinkedIn, Instagram, YouTube, etc.) derived from the blog.
* **Conversion assets** – ad copy sets and a landing page draft tailored to the avatar and offer.
* **Feedback revisions** – updated versions of the above assets if optimisation is run.
* **Delivery package** – a final index file and organised folder of all outputs ready for hand‑off.

## Structure

The engine uses three layers:

**Layer 1 – Router**

* `00_router/` contains files that describe the system, map tasks to contexts, and define naming conventions.  The router routes incoming tasks (e.g. “generate blog titles”) to the appropriate context.

**Layer 2 – Context Areas**

* `03_contexts/` holds one folder per context, each with its own `context.md`, `workflow.md` and `prompts.md`.  These documents tell the AI what the context does, what files to read and ignore, how to perform the work, and what outputs to produce.

**Layer 3 – Workspaces**

* `04_workspaces/` mirrors the context structure.  During a run, the AI writes intermediate files inside the workspace folders.  Once complete, final versions are moved to `08_outputs/` and the run can be archived.

Additional layers store source material (`01_source-material/`), system definition (`02_system-definition/`), reusable prompts (`05_prompts/`), templates (`06_templates/`), structured inputs (`07_inputs/`), outputs (`08_outputs/`), and archives (`09_archive/`).

## Usage

1. **Prepare a run brief** in `07_inputs/run-briefs/` using the run brief template.
2. **Route the task** using `00_router/Claude.md` to determine the correct context.
3. **Enter the context** and follow the instructions in its `workflow.md`.  Create or update files in the corresponding workspace folder.
4. **Repeat** for each stage (strategy modelling, blog generation, signal expansion, conversion assets, etc.).
5. **Optional optimisation**: if performance data is available, run the optimisation recursion context to refine the outputs.
6. **Package the results** using the packaging context.  Move final files to `08_outputs/final-delivery/` and archive old runs as needed.

Always adhere to the naming conventions so the AI can locate and update files automatically.