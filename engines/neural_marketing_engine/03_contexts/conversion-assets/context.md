# Conversion Assets Context

## Purpose

Generate **ad copy sets** and a **landing page draft** that convert the avatar.  This context translates the strategy model and blog post into persuasive, platform‑specific advertisements and a cohesive landing page flow.

## Read First

* The strategy model (`04_workspaces/strategy-modeling/`).
* The blog post (`04_workspaces/blog-generation/`).
* The conversion assets template (`06_templates/conversion-assets-template.md`).

## Use This Context For

* Writing ad copy variations for multiple platforms (e.g. search, social, display).  Each variation should feature a compelling headline, supporting body text and a clear CTA.
* Crafting a landing page draft including headline, sub‑headline, problem story, solution overview, benefits list, social proof, guarantee, CTA stack and form instructions.

## Ignore

* Do not create social media posts here.  That belongs to the signal expansion context.
* Do not optimise outputs based on performance; that is handled in optimisation recursion.

## Expected Outputs

* `[run-slug]-ad-copy-conversion-v1.md` – a file containing all ad copy sets, grouped by platform.
* `[run-slug]-landing-page-conversion-v1.md` – a landing page draft following conversion best practices.
* Save both files in `04_workspaces/conversion-assets/` until ready to move to `08_outputs/conversion-assets/`.