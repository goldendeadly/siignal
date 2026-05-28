# Realtor Concierge Engine Router

## System Description

The **Realtor Concierge Engine** is a deterministic workflow designed to handle inbound real‑estate leads, qualify callers, schedule consults, log interactions, generate daily digests, collect weekly meeting settings and produce weekly reports.  Rather than spinning up separate “agents,” a single AI operates within this system by routing tasks through clearly defined contexts.  Each context focuses on a specific stage of the workflow and contains its own instructions, workflows and prompts.

## Folder Map

This router defines the high‑level directory structure and where each component lives:

- `00_router/` – system map, routing rules and naming rules (this file).
- `02_system-definition/` – high‑level overview of the engine and a detailed workflow map.
- `03_contexts/` – a folder per context (e.g. `call-intake`, `classification-booking`, `logging-digest`, `meeting-intake`, `meeting-report`, `qa-tuning`, `optimisation-expansion`) with three files each: `context.md`, `workflow.md`, and `prompts.md`.
- `04_workspaces/` – run‑specific working directories matching each context; files created during a run live here until moved to outputs.
- `05_prompts/` – general prompt guides for desktop/IDE/terminal environments.
- `06_templates/` – reusable templates for scripts, logging sheets, digests, weekly forms, reports, QA tests and fallback rules.
- `07_inputs/` – user‑provided inputs such as run briefs, business information and weekly intake forms.
- `08_outputs/` – final outputs: call logs, daily digests, weekly reports, QA reports and recommendations.
- `09_archive/` – archived runs, retired logs and superseded outputs.

## Context Definitions

Each context is responsible for a discrete stage of the workflow.  The router routes tasks to these contexts based on the nature of the work.

- **call‑intake** – Handles live inbound calls.  Uses the call script to capture the six mandatory questions, optional questions where appropriate, and compliance scripts.  Records the caller’s intent (buyer/seller/other), area, timeline, pre‑approval/listing status and contact info, then offers booking or determines fallback.
- **classification‑booking** – Processes captured call data to classify the lead as HOT, WARM, NURTURE or DISQUALIFY using deterministic rules.  Decides the appropriate next action (book consult, callback, nurture or disqualify), schedules the consult if required and updates the log with classification and next steps.
- **logging‑digest** – Writes call outcomes to the logging sheet and compiles the daily digest email summarising totals, booked appointments, hot leads, nurture queue, disqualified calls and incomplete records.  Generates the digest at the end of each day and stores it in outputs.
- **meeting‑intake** – Collects weekly intake information via a form (reporting period, niche, service area, meeting types, availability, qualification/disqualify rules, fit rating criteria, target filters and qualifying questions).  Produces a meeting settings file used by subsequent contexts.
- **meeting‑report** – Produces weekly reports for the client and operator.  Combines call logs and meeting records to compute totals, buyer/seller split, priority leads, at‑risk leads, no‑shows and lessons learned.  Also creates the replacement queue and weekly execution plan if caps/replacement are in play.
- **qa‑tuning** – Executes the QA test suite (12 scenarios) to validate classification, booking, escalation and logging behaviours.  Records pass/fail results, identifies any failures and suggests tuning changes.  Determines Go/No‑Go status before going live.
- **optimisation‑expansion** – Reviews performance metrics (lead throughput, booking rates, no‑shows, classification mix), analyses weekly reports and digests, and proposes improvements to scripts, hot triggers, fallback rules, meeting types and automation opportunities.

## Routing Instructions

Use these rules to determine which context a task should be routed to:

- **“Answer a new inbound call”** → `call-intake`.
- **“Classify a captured lead and decide next action”** → `classification-booking`.
- **“Log call outcomes and produce the daily digest”** → `logging-digest`.
- **“Collect weekly meeting settings”** → `meeting-intake`.
- **“Generate the weekly report”** → `meeting-report`.
- **“Run quality assurance tests and tune scripts”** → `qa-tuning`.
- **“Analyse performance and suggest improvements”** → `optimisation-expansion`.

When in doubt, read the relevant `context.md` file for guidance.  Each context file lists the purpose, inputs to read, files to ignore, workflow steps and expected outputs.

## Naming Rules

See `00_router/naming-conventions.md` for detailed naming conventions.  In brief:

- Run folders follow the pattern `run-[YYYY-MM-DD]-[client]`.
- Files generated during a run use the pattern `[client]-[asset]-[status]-v[number].md`.  For example: `smithteam-call-log-draft-v1.md`, `smithteam-daily-digest-final-v1.md`, `smithteam-weekly-report-client-v2.md`.
- Trackers and forms have explicit names, such as `logging-sheet-[client]-[YYYY-MM].csv` and `weekly-intake-[week]-[client].md`.

The naming rules ensure the AI can reliably locate the correct files within the system.