# Meeting Report Workflow

Execute this workflow at the end of each reporting period (e.g. Sunday evening) to create the weekly client and operator reports, replacement queue and execution plan.

1. **Collect Inputs** – Retrieve the weekly intake settings file (`weekly-intake-[week]-[client].md`) to understand the chosen meeting types, availability requirements and rules.  Load the logging sheet for the reporting period and filter rows for dates within the reporting week.

2. **Compute Totals** – Calculate:
   - **Leads processed** – number of rows in the logging sheet for the week.
   - **Booked consults** – number of rows where `Booked=Yes`.
   - **Attended consults** – number of rows where `Outcome=Attended` or `Attended=Yes` (if tracked separately).
   - **Qualified consults** – number of rows where `Qualified=Yes` (use `Qualified_Minimum_Data` and rule citations if provided).
   - **Disqualified** – number of rows with `Temperature=DISQUALIFY`.
   - **No‑shows** – number of booked consults that were not attended and have `Outcome=No-show`.
   - **Unknown attendance** – number of bookings without attendance confirmation.
   - Additional counts if needed (e.g. callbacks, nurture follow‑ups).

3. **Buyer vs. Seller Split** – For booked, attended and qualified consults, compute the number of Buyer vs. Seller consults.

4. **Identify Priority Leads** – Select the top 10 leads to prioritise next week based on temperature (HOT first), upcoming consults, urgency or notes.  Include caller name, phone, intent, area, timeline bucket, temperature, booking status, next action and notes.

5. **Identify At‑Risk Leads** – List leads that need immediate action because they have no next action scheduled, missing key information, unknown attendance or a failed booking.  Include details and required actions.

6. **No‑Show & Attendance Notes** – Summarise no‑show count and unknown attendance.  Identify top drivers (e.g. schedule conflicts, communication gaps).  Recommend a recovery plan (reschedule within 7 days, send reminder to confirm attendance, etc.).

7. **Identify Bottlenecks** – Analyse notes to find recurring objections (e.g. price concerns, timeline hesitation) and missing info patterns (e.g. area not specified, budget not captured).  List the top three of each.

8. **Next Week Focus** – Suggest up to three changes to improve performance next week, drawing from bottlenecks and at‑risk analysis.  Examples: adjust hot triggers, change question order, refine disqualify thresholds, update booking script, allocate more slots, change follow‑up cadence.

9. **Create Client Report** – Populate the client report template with the team name, dates, time zone, service area, primary focus, definitions/rule citations, totals, split, priority leads, at‑risk leads, no‑shows, bottlenecks and next week focus.  Save as `[client]-weekly-report-client-[week]-v1.md` in `08_outputs/weekly-reports/`.

10. **Create Operator Report** – Populate the operator report template with totals and split.  Build queues:
    - **HOT Queue** – leads requiring same‑day contact.
    - **Warm Queue** – leads requiring contact within 24–72 hours.
    - **No‑Show Recovery Queue** – leads that missed consults requiring rescheduling within 7 days.
    - **Missing Info Requests** – leads missing critical data to be captured within 24 hours.
  Summarise cap usage and replacement status (if cap model).  Write a week plan with top five actions.  Save as `[client]-weekly-report-operator-[week]-v1.md` in `08_outputs/weekly-reports/`.

11. **Create Replacement Queue** – If cap and replacement rules are active, filter leads that are replacement‑eligible (booked but not attended, unknown attendance, or disqualified due to client reasons), ineligible (client‑caused or excluded) and pending attendance confirmations.  Fill the replacement queue template.  Save as `replacement-queue-[week]-[client].md`.

12. **Create Execution Plan** – Populate the execution plan template with counts for each daily block (HOT response, confirmations, warm follow‑ups, no‑show recovery, close loops) based on totals and cap settings.  Save as `execution-plan-[week]-[client].md`.

13. **Finalise** – Review reports for accuracy.  Deliver the client report to the realtor team and the operator report internally.  Archive previous week’s reports to `09_archive/` if needed.  Notify the `optimisation-expansion` context that reports are ready for analysis.