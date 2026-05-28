# Meeting Intake Workflow

Use this workflow at the start of each reporting period (typically Monday morning) to collect and store weekly meeting settings.

1. **Prepare Form** – Open `06_templates/weekly-intake-template.md`.  Review all questions and allowed options.  Gather any necessary contextual information (e.g. last week’s settings, service area changes, offer updates).

2. **Collect Information** – Obtain answers for each section:
   - **Week Context:** Reporting period start and end dates; time zone; vertical/niche; service area (cities/regions).
   - **Primary Offer & CTA:** Offer name; choose a primary call‑to‑action (book a call, book a demo, book an audit, request a quote, other).
   - **Meeting Types & Availability:** Up to two meeting types, each with a duration (10, 15, 20 or 30 minutes).  Minimum open slots per week (10, 15, 20 or 30).  Booking method (booking link, calendar integration or explicit business hours with optional weekend hours).
   - **Hot Lead Handling:** Choose between live transfer for hot leads or alert only.  If live transfer, capture transfer number(s) and hours.
   - **Qualification Rules:** Select 3–8 rules that define a “Qualified” consult (decision‑maker attended, meeting was attended, in service area, matches industry, matches company size threshold, active need, timeline within range, budget signal present, agreed to next step, contact info captured).  Optionally add a custom rule.
   - **Disqualify Rules:** Select all that apply (not decision maker, outside service area, wrong industry/use case, too small or large, no need, timeline far outside target, budget below threshold, vendor/spam, no usable contact info).  Optionally add a custom rule.
   - **Fit Rating Criteria:** Decide whether to use A/B/C ratings.  If yes, define what constitutes an A‑fit, B‑fit and C‑fit.
   - **Target Filters:** Select relevant industries, company sizes, decision‑maker titles and minimum budget or timeline urgency.
   - **Qualifying Questions:** Select up to six questions from the list (what prompted you to take this call; what are you trying to improve; what happens if nothing changes; what’s your timeline; who is involved in the decision; what’s your current process; what have you tried before; what would success look like in 30–60 days; are you currently spending money on this problem; best email + phone) and optionally add a custom question.
   - **Cap & Replacement Rules (Optional):** If meeting caps and replacements are used, specify the cap per week/month, replacement logic and exclusions.

3. **Record Settings** – Create a new weekly intake file named `weekly-intake-[week]-[client].md` in the run workspace.  Populate it with the collected answers under clearly labeled sections.  Use the same headings as the template for consistency.

4. **Confirm & Store** – Review the completed file for accuracy.  Confirm with the client or team lead if necessary.  Save the file in `04_workspaces/meeting-intake/` and ensure a copy is placed in `07_inputs/weekly-intake-forms/` for reference.

5. **Propagate Settings** – Notify the scheduling system (calendar or booking integration) and the `meeting-report` context of the new settings.  These settings will influence meeting durations, availability windows, qualification thresholds and reporting metrics for the week.