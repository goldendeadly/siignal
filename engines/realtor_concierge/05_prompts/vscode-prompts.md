# VS Code Prompts – Realtor Concierge Engine

VS Code prompts are used when editing or generating individual files within a context.  They specify which files to read, what task to perform and where to save the output.  Use them when you need to write or update a document, template or report.

## Call Script Editing

> **Context:** call‑intake
>
> **Read:** `06_templates/call-script-template.md`, `weekly-intake-[week]-[client].md` (for custom qualification/disqualify rules or target filters), any tuning notes from `qa-report`.  
> **Task:** Modify the call script to include client‑specific introductions, adjust question order if specified, update hot trigger language or fallback responses.  Incorporate any custom qualification or disqualify rules from the weekly intake.  
> **Output:** Save the updated script as `call-script-[client]-[week]-v[number].md` in `04_workspaces/call-intake/`.  Do not overwrite the template.  
> **Note:** Ensure the script still asks no more than six mandatory questions and follows compliance boundaries.

## Logging Sheet Generation

> **Context:** logging‑digest
>
> **Read:** `06_templates/logging-sheet-template.md`, any existing logging sheet for the month.
> **Task:** If no logging sheet exists for the current month, create one by copying the template header.  Ensure column names and order match exactly.  
> **Output:** Save as `logging-sheet-[client]-[YYYY-MM].csv` in `08_outputs/logs/`.

## Daily Digest Compilation

> **Context:** logging‑digest
>
> **Read:** all classified call records in the current run, `logging-sheet-[client]-[YYYY-MM].csv`, `06_templates/daily-digest-template.md`.
> **Task:** Compute totals and lists as per the workflow.  Populate the digest template with actual numbers and details.  
> **Output:** Save as `[client]-daily-digest-[date]-v[number].md` in `08_outputs/daily-digests/`.

## Weekly Report Writing

> **Context:** meeting‑report
>
> **Read:** `logging-sheet-[client]-[YYYY-MM].csv`, `weekly-intake-[week]-[client].md`, `06_templates/weekly-report-template-client.md`, `06_templates/weekly-report-template-operator.md`, `06_templates/replacement-queue-template.md`, `06_templates/execution-plan-template.md`.
> **Task:** Compute weekly metrics and populate the client and operator report templates.  Create replacement queue and execution plan if applicable.  
> **Output:** Save reports and related files in `08_outputs/weekly-reports/` with names following the naming conventions.

## QA Report Writing

> **Context:** qa‑tuning
>
> **Read:** `06_templates/qa-test-template.md`, call script, classification rules, fallback matrix.
> **Task:** After running tests, record pass/fail results, root causes, tuning suggestions and Go/No‑Go decision.  
> **Output:** Save as `qa-report-[date]-[client].md` in `08_outputs/qa-reports/`.

## Recommendations Report

> **Context:** optimisation‑expansion
>
> **Read:** logging sheets, digests, weekly reports, QA reports, tuning logs.
> **Task:** Analyse performance and propose improvements.  Populate the recommendations report template.  
> **Output:** Save as `recommendations-[week]-[client].md` in `08_outputs/recommendations/`.