# System Overview – Neural Marketing Engine v1

The Neural Marketing Engine (NME) is a reusable AI workspace for designing, generating and optimising marketing funnels.  Starting from a short set of structured inputs (niche, offer, avatar, tone, outcome and SEO intent), the engine produces the core marketing assets needed to launch and iteratively refine a digital campaign.

## Inputs

1. **Run brief** – a completed run brief capturing the six core variables and any supplementary notes.
2. **Research notes** – optional supporting materials (competitor references, product specs, past analytics) placed in `01_source-material/`.
3. **Feedback** – optional performance data collected post‑launch to drive optimisation.

## Outputs

* **Strategy model** – an integrated plan summarising avatar psychology, offer positioning, conscious frequency, desired outcomes and an SEO keyword cluster.
* **Blog titles** – seven headline options aligned with the strategy model.
* **Long‑form blog post** – a comprehensive article that educates, persuades or inspires the target avatar, optimised for the chosen SEO intent.
* **Social signal** – a multi‑platform content set (threads, carousels, captions, scripts) derived from the blog and tailored to each platform’s norms.
* **Conversion assets** – ad copy sets and a landing page draft reflecting the offer and tone, with CTA layering and persuasive flow.
* **Optimised revisions** – updated assets if the optimisation context is run.
* **Delivery package** – an indexed bundle of all outputs ready for clients or stakeholders.

## Phases & Contexts

The engine is divided into seven contexts, each corresponding to a phase:

1. **Input Intake** – capture and validate the run brief.
2. **Strategy Modelling** – build the avatar map, offer architecture, tone guidelines and SEO intent map.
3. **Blog Generation** – produce title candidates and a full blog post.
4. **Signal Expansion** – transform the blog into platform‑specific social content.
5. **Conversion Assets** – write ad copy sets and a landing page draft.
6. **Optimisation & Recursion** – refine outputs based on performance feedback.
7. **Packaging Output** – assemble finished assets and a delivery index.

Each context has its own instructions (in `03_contexts/[context]/`) and a corresponding workspace (in `04_workspaces/[context]/`).  The AI must work within the current context’s workspace before moving to the next phase.

## Design Principles

* **Structured inputs** – The run brief standardises the information needed to generate consistent outputs.
* **Context isolation** – Each stage focuses on a single category of work, reducing cognitive load and preventing cross‑contamination.
* **Predictable naming** – File names follow a strict pattern so the AI can locate and update them automatically.
* **Iteration when needed** – Performance feedback can be fed back into the engine to generate improved outputs (higher versions).
* **Portability** – The system is template‑driven and domain‑agnostic; by changing the inputs and tone, it can serve any industry or offer.