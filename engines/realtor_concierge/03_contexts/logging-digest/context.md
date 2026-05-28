# Logging & Daily Digest Context

## Purpose

The **logging‑digest** context converts classified call records into structured log entries and compiles a daily digest summarising the day’s performance.  It writes the required columns to the logging sheet, computes aggregate statistics and lists calls by category (booked appointments, hot leads, callbacks, nurture leads, incomplete records and disqualified calls).  The resulting digest provides the agent or team with an actionable overview of new leads and tasks.

## Read First

- `06_templates/logging-sheet-template.md` – for the required columns and completeness standards.
- `06_templates/daily-digest-template.md` – for the structure and sections of the daily digest email.
- Classified call records in `04_workspaces/classification-booking/`.

## Use This Context For

- Reading each classified call record from the current run and appending its data as a row in the logging sheet.
- Ensuring mandatory columns are populated and marking completeness status (COMPLETE, PARTIAL, INSUFFICIENT).
- Calculating daily totals: total calls, buyer vs. seller calls, booked appointments, hot leads, warm/nurture leads, disqualified calls, incomplete records and lead leaks (missed calls not reached).
- Creating lists of booked appointments (next 48 hours), hot leads requiring immediate follow‑up, callbacks needed, at‑risk/incomplete records and disqualified calls.
- Populating the daily digest template with totals, lists and notes.
- Saving the daily digest to the outputs folder and optionally sending it to the agent/team via email or other channels.

## Ignore

- Lead classification logic (handled in `classification-booking`).
- Weekly reporting (handled in `meeting-report`).
- Meeting intake and weekly settings.
- QA and optimisation tasks.

## Expected Outputs

- **Updated logging sheet** for the current month (e.g. `logging-sheet-smithteam-2026-03.csv`) with a new row for each call.
- **Daily digest file** named using the naming convention (e.g. `smithteam-daily-digest-final-v1.md`) containing:
  - Topline summary of new leads, booked appointments, hot leads, warm/nurture leads, disqualified calls and lead leaks.
  - A list of booked appointments for the next 48 hours with names, contact info, intent, temperature, appointment time, outcome and recommended owner action.
  - A list of hot leads requiring immediate follow‑up with key details and next action due.
  - A list of callbacks needed with reason and recommended next action.
  - A list of at‑risk/incomplete records with missing info and required action.
  - A summary of disqualifications with counts and reasons.
  - A notes snapshot summarising key statements and triggers from the day (top 10 entries).
- **Lead leak list** of missed calls not reached (if available) and recommended next step to recover the lead.
- These outputs feed into the `meeting-report` context and provide daily visibility to the team.