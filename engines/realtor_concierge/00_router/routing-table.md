# Routing Table

This table maps common tasks to the corresponding context.  Use it as a quick reference when deciding where to route work.

| Task Category | Description | Context |
|--------------|-------------|---------|
| **New Call** | An inbound call arrives.  Use the script to capture the mandatory questions, optional questions and compliance statements. | `call-intake` |
| **Lead Classification** | A lead record has been captured.  Apply deterministic rules to classify as HOT, WARM, NURTURE or DISQUALIFY, decide next action and schedule consult if appropriate. | `classification-booking` |
| **Logging & Daily Digest** | Append call outcomes to the log sheet and generate the daily digest summarising totals, booked appointments, hot leads, nurture queue, disqualified calls and incomplete records. | `logging-digest` |
| **Weekly Intake** | Collect the weekly meeting configuration via a form: reporting period, niche, service area, meeting types, availability, qualification/disqualify rules, fit ratings, targeting filters and qualifying questions. | `meeting-intake` |
| **Weekly Report** | Compute weekly totals, buyer/seller split, priority and at‑risk leads, no‑shows, bottlenecks and next week focus.  Produce both client‑facing and operator‑facing reports. | `meeting-report` |
| **Quality Assurance** | Run the 12‑scenario QA test suite to verify classification, booking, escalation and logging behaviours.  Record pass/fail results and tune scripts as needed. | `qa-tuning` |
| **Performance Optimisation** | Review logs and reports to analyse performance metrics and propose improvements to scripts, rules, meeting types, fallback matrices and automation flows. | `optimisation-expansion` |

When a task doesn’t fit neatly into a category, consult the `context.md` files for guidance.  All tasks should be routed to exactly one context to avoid overlapping responsibilities.