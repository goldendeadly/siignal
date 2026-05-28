# Quality Assurance & Tuning Context

## Purpose

The **qa‑tuning** context ensures that the Realtor Concierge Engine performs reliably and within defined limits before going live.  It runs a standard test suite of twelve call scenarios covering buyer and seller paths, hot and warm leads, disqualifications, call drops, vendor spam and booking failures.  The context records pass/fail results, identifies root causes of any failures and suggests tuning adjustments.  It then determines whether the system meets the Go/No‑Go criteria for deployment.

## Read First

- `06_templates/qa-test-template.md` – contains the twelve test scenarios and expected outcomes.
- `06_templates/fallback-rules-template.md` – for fallback behaviours used in the tests.
- `06_templates/call-script-template.md` – to ensure the script matches expected behaviour.
- The current logging sheet and daily digest template – to verify logging and digest generation.

## Use This Context For

- Performing simulated or real test calls representing each scenario in the QA template.
- Validating that the AI asks the correct mandatory questions (no more than six) and uses the proper script.
- Checking that classification is correct (HOT/WARM/NURTURE/DISQUALIFY) based on input data.
- Confirming that booking behaviour is appropriate (offered and confirmed where expected, fallback used when booking fails or caller declines).
- Ensuring escalation and transfer behaviour works for hot leads (alerts triggered and live transfers attempted when enabled).
- Verifying that each call outcome results in a log row with the correct completeness status and that the daily digest compiles correctly.
- Recording test results and suggesting tuning adjustments.
- Determining Go/No‑Go status based on pass rates and critical failures.

## Ignore

- Ongoing optimisation or improvements (handled after deployment).
- Meeting intake and reporting tasks.

## Expected Outputs

- **QA report** (`qa-report-[date]-[client].md`) summarising:
  - Each scenario, input conditions, expected outcome and observed outcome.
  - Pass/fail status for mandatory questions, classification, booking behaviour, escalation, logging and digest.
  - Root causes of any failures and proposed tuning changes (e.g. adjust hot triggers, reorder questions, modify fallback rules).
  - Go/No‑Go decision: GO if at least 10/12 scenarios pass and critical functions (hot alerts, booking) are working; otherwise NO‑GO.
  - List of tuning requests (max 2 per day for Week 1) with owner and due date.

The QA report is saved to `08_outputs/qa-reports/`.  If tuning changes are required, update the relevant templates or scripts and document the changes.