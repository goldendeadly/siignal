# Realtor Concierge Engine — Master SOP

## Purpose

This Standard Operating Procedure governs the end-to-end execution of the Realtor Concierge Engine.  The engine provides a unified AI-driven workflow for managing real-estate leads from first contact through weekly reporting, quality assurance and performance optimisation.

## Operator Role

The Operator (human or automated runner) is responsible for:

1. Providing the **run brief** with service area, vertical, primary offer and call-handling preferences.
2. Supplying **business information** (phone numbers, appointment types, business hours, hot-lead alert recipients).
3. Triggering each context in sequence and reviewing outputs before advancing.
4. Archiving completed runs to `09_archive/`.

## Execution Sequence

Execute the following contexts in order.  Each context reads the outputs of the previous context(s) as its inputs.

| Step | Context | Purpose |
|------|---------|---------|
| 1 | `call-intake` | Capture inbound call data using the structured call script.  Record mandatory questions (intent, area, timeline, pre-approval/listing status, contact info, booking preference) and optional questions.  Follow compliance scripts and fallback rules. |
| 2 | `classification-booking` | Classify the captured lead as HOT, WARM, NURTURE or DISQUALIFY using deterministic rules.  Decide next action (book consult, callback, nurture follow-up or disqualify).  Schedule the consult if criteria are met. |
| 3 | `logging-digest` | Append call outcomes to the logging sheet.  Generate the daily digest summarising totals, booked appointments, hot leads, nurture queue, disqualified calls and incomplete records. |
| 4 | `meeting-intake` | Collect weekly meeting configuration: reporting period, niche, service area, meeting types, availability, qualification/disqualify rules, fit-rating criteria, target filters and qualifying questions. |
| 5 | `meeting-report` | Produce weekly reports (client-facing and operator-facing).  Compute totals, buyer/seller split, priority leads, at-risk leads, no-shows, bottlenecks and next-week focus.  Generate replacement queue and execution plan if applicable. |
| 6 | `qa-tuning` | Execute the 12-scenario QA test suite.  Validate classification, booking, escalation and logging behaviours.  Record pass/fail results and determine Go/No-Go status.  Limit tuning to two changes per day during Week 1. |
| 7 | `optimisation-expansion` | Review performance metrics (booking rates, lead mix, no-shows, classification distribution).  Analyse weekly reports and digests.  Propose improvements to scripts, triggers, fallback rules, meeting types and automation flows. |

## Rules

1. **Deterministic Classification:** Lead classification MUST follow the deterministic rules defined in the classification-booking context.  The AI must not improvise classification logic.
2. **Compliance Boundaries:** The AI must never provide legal advice, financing advice, price predictions or emergency services.  Use the compliance scripts when these topics arise.
3. **Fallback Rules:** If booking fails or the caller declines, follow the fallback matrix (callback within 2 hours for HOT, next-day for WARM, nurture sequence for NURTURE).
4. **QA Gate:** The system cannot go live until at least 10 of 12 QA scenarios pass and hot alerts plus bookings function correctly.
5. **Tuning Limits:** During Week 1, limit tuning changes to two per day to protect system stability.
6. **Naming Conventions:** All files must follow the naming conventions in `00_router/naming-conventions.md`.

## File Locations

| Directory | Contents |
|-----------|----------|
| `00_router/` | System identity, routing table, naming conventions |
| `02_system-definition/` | Overview and workflow map |
| `03_contexts/` | Context definitions, workflows and prompts for each phase |
| `04_workspaces/` | Active run directories (created at runtime) |
| `05_prompts/` | Desktop, terminal and VS Code prompt collections |
| `06_templates/` | Call scripts, logging sheets, digests, reports, QA tests, fallback rules |
| `07_inputs/` | Run briefs, business info, weekly intake forms |
| `08_outputs/` | Final reports, digests and recommendations |
| `09_archive/` | Completed run folders |
