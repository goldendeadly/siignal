# Optimisation & Expansion Context

## Purpose

The **optimisation‑expansion** context analyses performance data from logs, digests and weekly reports to identify trends, bottlenecks and opportunities for improvement.  It proposes changes to scripts, classification thresholds, fallback rules, meeting types, availability settings and automation.  It also suggests longer‑term expansions, such as adding new appointment types, integrating with CRMs or scheduling tools, or launching nurture campaigns.  The goal is to improve conversion rates, reduce no‑shows and increase operational efficiency over time.

## Read First

- Latest logging sheets and daily digests (covering at least one week).
- Latest weekly reports (client and operator versions).
- Tuning changes and outcomes from the `qa-tuning` context.
- Business goals and constraints (e.g. cap limits, service area boundaries, compliance restrictions).

## Use This Context For

- Reviewing performance metrics: booking rates (HOT/WARM to booked), attendance rates (booked to attended), qualification rates, no‑show rates, buyer vs. seller mix, fit rating distribution (A/B/C), classification distribution (HOT/WARM/NURTURE/DISQUALIFY), call volume per day and per time block, and lead throughput.
- Analysing recurring objections and missing information patterns.
- Identifying root causes of declines (e.g. low booking due to script wording, high no‑show due to lack of reminders, over‑qualification or under‑qualification due to thresholds).
- Proposing improvements to:
  - Script language, ordering of questions or number of optional questions.
  - Hot, warm and nurture thresholds (timeline buckets, urgency signals, pre‑approval status).
  - Fallback matrix (adjust response times, escalation criteria, or default behaviours).
  - Meeting types and durations (e.g. add a 10‑minute triage call or extend consult to 20 minutes for complex cases).
  - Availability requirements (increase minimum slots to match call volume).
  - Qualification/disqualify rules to improve the fit of booked consults.
  - Fit rating definitions (refine A/B/C criteria for better prioritisation).
  - Target filters (industries, company sizes, decision maker titles).
  - Automations (e.g. schedule reminders, integrate with CRM, create nurture workflows for NURTURE leads).
- Suggesting expansions (phase 2 or later) – additional appointment types, multi‑language support, deeper CRM integration, marketing follow‑ups.
- Summarising recommendations in a structured report.

## Ignore

- Immediate call handling and booking (handled earlier contexts).
- QA testing (handled in `qa-tuning`).

## Expected Outputs

- **Recommendations report** (`recommendations-[week]-[client].md`) containing:
  - Key findings from metrics analysis (booking rates, attendance, qualification, no‑shows, classifications, objections, missing info patterns).
  - Proposed changes to scripts, rules, fallback matrix and meeting settings, with rationale and expected impact.
  - Suggested automation or integration upgrades (e.g. CRM integration, SMS reminders, nurture campaigns).
  - Optional expansion ideas for future phases (e.g. new appointment types, multilingual scripts, advanced analytics dashboards).
  - Prioritised list of improvements with estimated effort and expected benefit.

This report guides the product or operations team when making updates to the concierge system.  It is stored in `08_outputs/recommendations/`.