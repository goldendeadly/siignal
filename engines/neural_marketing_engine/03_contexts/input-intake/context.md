# Input Intake Context

## Purpose

Capture and normalise the initial marketing input for a run.  This context is responsible for validating that all required fields are present and properly formatted, assigning a run slug and creating the initial run folder.

## Read First

* `06_templates/run-brief-template.md` – use this to ensure all required fields are captured.
* The incoming run brief in `07_inputs/run-briefs/`.

## Use This Context For

* Creating a new run brief.
* Normalising and validating existing run briefs.
* Assigning run slugs and run folder names.

## Ignore

* Strategy modelling, blog generation or any downstream contexts.  Do not generate content here.
* Any files in `08_outputs/` or `09_archive/`.

## Expected Outputs

* A validated run brief saved in `04_workspaces/input-intake/`.
* A new run folder created inside `04_workspaces/input-intake/` for storing intermediate files.