# Quality Assurance & Tuning Prompts

## Thinking Prompt

> **You are running the QA test suite to verify the Realtor Concierge Engine.  For each test scenario, follow the call script, classification rules and fallback matrix.  Record whether the system asks the correct number of mandatory questions, classifies correctly, offers booking correctly, escalates hot leads and logs the call with the correct completeness status.  Compare observed behaviour to expected outcomes and mark pass or fail.  If failures occur, identify the root cause and suggest tuning changes.  At the end, decide if the system is GO (at least 10/12 scenarios pass and critical functions work) or NO‑GO.**

## File Editing Prompt

> **Create a QA report file named `qa-report-[date]-[client].md`.  Include sections for:**
> - Summary of pass/fail status for each scenario and each criterion (questions asked, classification, booking, escalation, logging, digest).
> - Root causes of failures.
> - Proposed tuning changes (max 2 per day), including what to change (e.g. update hot triggers, reorder questions) and why.
> - Go/No‑Go decision (GO if at least 10/12 scenarios pass and critical functions are working; otherwise NO‑GO).
> - Tuning request list with owner and due date.
> **Save the report in `08_outputs/qa-reports/`.**

## Folder Processing Prompt

> **Execute all test scenarios defined in the QA template.  Collect data for each scenario and compile the QA report.  Save the report in `08_outputs/qa-reports/`.  If tuning changes are needed, update the relevant template files (call script, classification rules, fallback matrix) and note the changes in a tuning log.**