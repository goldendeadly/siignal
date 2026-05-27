# Naming Conventions – Neural Marketing Engine v1

Consistent naming makes it easy for the AI to locate, update and package files automatically.  Use the following patterns for all files and folders.

## General File Pattern

```
[run-slug]-[asset-type]-[stage]-v[number].md
```

* **run‑slug** – a short hyphenated identifier for the current run, typically derived from the niche and offer (e.g. `roofing-leadgen`).
* **asset‑type** – describes what the file contains (e.g. `runbrief`, `strategy-model`, `blog-titles`, `blog-post`, `social-signal`, `ad-copy`, `landing-page`, `feedback`).
* **stage** – indicates the context or step of the workflow (`intake`, `core`, `generation`, `expansion`, `conversion`, `recursion`, `final`).
* **v[number]** – version number starting at 1.  Increment this number when revising assets (e.g. after optimisation).

### Examples

```
roofing-leadgen-runbrief-intake-v1.md
roofing-leadgen-strategy-model-core-v1.md
roofing-leadgen-blog-titles-generation-v1.md
roofing-leadgen-blog-post-generation-v1.md
roofing-leadgen-social-signal-expansion-v1.md
roofing-leadgen-ad-copy-conversion-v1.md
roofing-leadgen-landing-page-conversion-v1.md
roofing-leadgen-feedback-recursion-v1.md
roofing-leadgen-output-index-final-v1.md
```

## Run Folder Pattern

Run folders hold all intermediate files for a single execution.  Use the following pattern:

```
run-[yyyy-mm-dd]-[niche]-[offer-slug]
```

### Example

```
run-2026-03-18-roofing-leadgen
```

Create the run folder inside the appropriate workspace and move it to `09_archive/old-runs/` once the run is complete.

## Feedback Files

When collecting performance data or stakeholder feedback, name the files using this pattern:

```
[run-slug]-feedback-[platform]-[yyyy-mm-dd]-v[number].md
```

Use the platform name (e.g. `blog`, `facebook`, `ads`) to distinguish where the feedback comes from.

## Rules

* Always use lowercase letters and hyphens.  Avoid spaces or special characters.
* Increment version numbers when revising an asset; never overwrite a previous version.
* Use the same run slug across all files for a given run.
* For supplementary materials (e.g. templates filled out during a run), append an appropriate descriptor (e.g. `avatar-map` or `offer-architecture`).