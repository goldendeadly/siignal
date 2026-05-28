# Desktop Prompts – Realtor Concierge Engine

Use the desktop environment when you need to plan and orchestrate tasks across contexts.  Desktop prompts are high‑level thinking prompts that determine which context to enter next and what information to gather before starting detailed work.

## Determine Next Task

> **You are the operator of the Realtor Concierge Engine.  Review the current run folder (`04_workspaces/`) and the `07_inputs/` directory.  Identify which context should be executed next based on available files and outstanding tasks.  For example: if raw call files are present in `call-intake` and not processed, route to `classification-booking`; if classified calls are present but not logged, route to `logging-digest`; if it is Monday morning, route to `meeting-intake`; if the week just ended, route to `meeting-report`.  Produce a concise execution plan with the context to enter and the specific files to process.**

## Analyse Run Brief

> **Open the run brief in `07_inputs/run-briefs/`.  Summarise the reporting period, service area, vertical/niche and primary offer.  Note any special instructions (e.g. custom qualification rules, service area exclusions).  Decide which templates need to be customised before starting the week (e.g. call script modifications, meeting settings).**

## Assess Weekly Intake Form

> **Check `07_inputs/weekly-intake-forms/` for a completed weekly intake file.  If none exists and today is the start of the reporting period, prompt to create one using the meeting intake context.  If a form exists, load its settings and summarise meeting types, durations, availability, qualification rules, disqualify rules, fit rating criteria, target filters and qualifying questions.**

These prompts ensure that the AI stays organised and routes tasks efficiently across contexts before diving into detailed work in VS Code or Terminal.