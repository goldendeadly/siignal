# Meeting Report Context

## Purpose

The **meeting‑report** context generates weekly performance reports based on logged call data and weekly settings.  It produces both a client‑facing report (designed for the realtor team) and an operator‑facing report (internal use).  Reports summarise lead throughput, booking and attendance metrics, buyer vs. seller split, priority leads, at‑risk leads, no‑shows, bottlenecks and next‑week focus.  The context also creates replacement queues and execution plans when caps and replacements are in effect.

## Read First

- `06_templates/weekly-report-template-client.md` – for the structure and sections of the client report.
- `06_templates/weekly-report-template-operator.md` – for the structure and sections of the operator report.
- `06_templates/replacement-queue-template.md` – for the format of the replacement queue (used only if caps and replacement rules are enforced).
- `06_templates/execution-plan-template.md` – for the daily execution plan structure.
- Weekly intake settings file (`weekly-intake-[week]-[client].md`).
- Logging sheet covering the reporting period (CSV or spreadsheet).

## Use This Context For

- Calculating weekly totals: number of leads processed, booked consults, attended consults, qualified consults, disqualified calls, no‑shows and unknown attendance.
- Computing buyer vs. seller split for booked, attended and qualified consults.
- Identifying priority leads (top 10) and at‑risk leads (no next action, missing info, unknown attendance or failed booking).
- Summarising no‑shows and unknown attendance, including top drivers and recommended recovery actions.
- Highlighting bottlenecks: recurring objections and missing information patterns.
- Recommending next week focus (1–3 changes) based on observed data.
- For the operator report: grouping leads into HOT, Warm, No‑Show and Missing‑Info queues; listing missing info requests; summarising cap usage and replacement count; producing a week plan with top actions.
- Creating a replacement queue when meeting caps are enforced: track eligible replacements, ineligible leads and pending attendance confirmations; summarise cap usage.
- Generating a daily execution plan for the upcoming week (blocks for HOT response, confirmations, warm follow‑ups, no‑show recovery and close loops).  Populate counts using planned weekly numbers.

## Ignore

- Call classification and booking (handled in earlier contexts).
- Logging and daily digests (handled in `logging-digest`).
- QA and tuning (handled in `qa-tuning`).
- Optimisation recommendations (handled in `optimisation-expansion`).

## Expected Outputs

- **Client‑facing weekly report** (`[client]-weekly-report-client-[week]-v[number].md`) containing sections:
  - Team name, reporting week, time zone, service area, primary focus and report owner.
  - Definitions and rule citations (qualified and disqualify rules used this week).
  - Weekly totals.
  - Buyer vs. seller split.
  - Priority leads (top 10) – leads that should be worked first.
  - At‑risk leads – leads requiring immediate attention due to missing info, unknown attendance, or failed booking.
  - No‑show and attendance notes.
  - Bottlenecks observed (top 3 objections and missing‑info patterns).
  - Next week focus (1–3 changes).
- **Operator‑facing weekly report** (`[client]-weekly-report-operator-[week]-v[number].md`) containing:
  - Same totals and split as the client report.
  - HOT, Warm, No‑Show and Missing‑Info queues.
  - Missing info requests that need resolution within 24 hours.
  - Replacement summary: cap, replacement used, replacement remaining, pending attendance confirmation (if cap model is used).
  - Week plan (top 5 actions).
- **Replacement queue** file (if cap/replacement is enabled): lists replacement‑eligible leads, ineligible leads, pending confirmations and cap tracker counts.
- **Execution plan** file: a week plan broken into daily blocks for HOT response, confirmations, warm follow‑ups, no‑show recovery and close loops.

These outputs are stored in `08_outputs/weekly-reports/` and `08_outputs/`.  They inform the team’s actions for the next week and feed into the optimisation context.