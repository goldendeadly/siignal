# Optimisation & Expansion Workflow

Use this workflow after completing one or more reporting periods to analyse performance and propose improvements.

1. **Gather Data** – Collect all relevant data: logging sheets, daily digests, weekly reports (client and operator), QA reports and tuning logs from the time period you are analysing.  Ensure data is cleaned and accurate.

2. **Calculate Key Metrics** – Compute performance metrics, such as:
   - **Booking Rate:** (Number of leads booked) ÷ (Number of HOT + WARM leads).
   - **Attendance Rate:** (Number of bookings attended) ÷ (Number of bookings).
   - **Qualification Rate:** (Number of qualified consults) ÷ (Number of attended consults).
   - **No‑Show Rate:** (Number of no‑shows) ÷ (Number of bookings).
   - **Lead Mix:** Distribution of Buyer vs. Seller calls and the ratio of HOT/WARM/NURTURE/DISQUALIFY.
   - **Fit Rating Distribution:** Percentage of A, B, C and unknown fit ratings.
   - **Average Response Time:** Time between call and callback for callbacks (from log entries).
   - **Time in Each Context:** Average time spent in call intake, classification, logging and meeting scheduling (if available).

3. **Identify Patterns** – Review notes and digest snapshots to find recurring themes:
   - Common objections (e.g. budget concerns, market timing, fear of commitment).
   - Missing information patterns (e.g. area not captured, timeline not captured, phone missing).
   - Frequent fallback triggers (calendar full, booking link failure, caller refuses booking).
   - Times of day with high call volume or missed calls.

4. **Root Cause Analysis** – For each negative metric or pattern (e.g. low booking rate, high no‑show rate), determine underlying causes.  Consider script phrasing, question order, classification thresholds, meeting availability and follow‑up cadences.

5. **Draft Improvements** – Based on root causes, propose modifications:
   - **Script & Flow:** Rephrase or reorder questions, reduce optional questions, change call‑to‑action phrasing.
   - **Classification:** Adjust hot triggers (timeline thresholds, urgency signals), refine warm/nurture boundaries, or require additional signals.
   - **Fallbacks:** Update response times, change default outcome for refusal to book, adjust escalation criteria.
   - **Meeting Settings:** Change durations or add a triage call, increase availability slots, modify booking method.
   - **Qualification & Disqualify Rules:** Add or remove rules to better match ideal client profile.
   - **Fit Rating Definitions:** Clarify A/B/C definitions to improve prioritisation.
   - **Target Filters:** Update industries, company sizes and decision maker titles.
   - **Automations:** Implement reminders, sync with CRM, schedule nurture emails or texts for NURTURE leads.

6. **Prioritise Recommendations** – Assess each proposed change for effort vs. impact.  Prioritise high‑impact, low‑effort changes first.  Group changes into short‑term (next week), medium‑term (next month) and long‑term (phase 2+).

7. **Write Recommendations Report** – Compile findings and proposals into a report.  Structure the report with a summary, key metrics, analysis findings, improvement proposals, automation suggestions and expansion ideas.  Include rationale for each recommendation and expected impact.

8. **Deliver & Implement** – Save the report in `08_outputs/recommendations/` as `recommendations-[week]-[client].md`.  Present the report to the team or decision maker.  If approved, plan implementation: update scripts, rules and templates; schedule automation work; and incorporate expansions into future planning.

9. **Monitor & Iterate** – After implementing changes, continue monitoring metrics to see if improvements are realised.  Use the optimisation context periodically (e.g. monthly or quarterly) to drive continuous improvement.