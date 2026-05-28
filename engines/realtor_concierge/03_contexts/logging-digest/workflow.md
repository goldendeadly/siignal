# Logging & Daily Digest Workflow

Follow this workflow to process classified call records into the log sheet and compile the daily digest.

1. **Prepare Logging Sheet** – If a logging sheet for the current month does not exist in `08_outputs/logs/`, create one using `06_templates/logging-sheet-template.md` as a reference for column order.  Name it `logging-sheet-[client]-[YYYY-MM].csv`.  Ensure headers match the template exactly.

2. **Read Classified Records** – Iterate over all classified call files in `04_workspaces/classification-booking/` that have not yet been logged.  For each file:
   - Parse the fields: caller name, phone, email, intent, area, timeline bucket, pre‑approval/listing status, temperature, appointment date/time, next action, next action due, completeness status, missing info, notes, outcome, hot alert, transfer attempted and result.
   - Create a new row in the logging sheet using these values.  Mark completeness (COMPLETE/PARTIAL/INSUFFICIENT).
   - Move the classified file to a `logged/` subfolder to avoid duplicate entries.

3. **Aggregate Statistics** – After all records are logged, compute totals:
   - **Total calls** processed today.
   - **Buyer calls vs. Seller calls**.
   - **Booked appointments** (count of rows with `Booked=Yes` and an appointment time within the next 48 hours).
   - **Hot leads** (rows with Temperature=HOT).
   - **Warm/Nurture leads** (Temperature=WARM or NURTURE).
   - **Disqualified calls** (Temperature=DISQUALIFY).
   - **Incomplete records** (Completeness=PARTIAL or INSUFFICIENT).
   - **Lead leaks**: calls that dropped or hung up where no phone was captured or follow‑up could not be created.

4. **Generate Lists** – Build lists for the digest:
   - **Booked Appointments**: For each booked row, include appointment time, caller name, phone, intent, temperature and a recommended owner action (e.g. confirm details, arrive with specific materials).
   - **Hot Leads**: For each hot row not booked, include caller name, phone, intent, area, timeline bucket, trigger (why it is hot), booking status and recommended immediate action with due time.
   - **Callbacks Needed**: For each row with outcome `Callback Requested`, list caller name, phone, reason for callback and recommended next action and due time.
   - **At‑Risk / Incomplete**: For each row with completeness=PARTIAL or INSUFFICIENT, list caller name, phone, missing fields and required next action.
   - **Disqualified**: Summarise counts by reason (e.g. outside service area, vendor solicitation, refused phone) and optionally list top examples.

5. **Compile Digest** – Populate the daily digest template:
   - Write the subject line: `Daily Concierge Summary — [DATE] — [TEAM NAME]`.
   - In section 1, insert the aggregated totals.
   - In section 2, list booked appointments with key details and recommended actions.
   - In section 3, list hot leads requiring immediate follow‑up.
   - In section 4, list callbacks needed.
   - In section 5, list at‑risk/incomplete records.
   - In section 6, summarise disqualifications.
   - In section 7, provide a notes snapshot (top 10 notes from the day).

6. **Save and Deliver** – Save the digest as a markdown file in `08_outputs/daily-digests/` using the naming convention.  Optionally send the digest via email or messaging system to the specified recipients.  Ensure hot leads have already received immediate alerts via SMS/email.

7. **Update Lead Leak List** – If there are calls where contact information was not captured, record them in a separate `lead-leaks-[date]-[client].md` file with details and suggested recovery actions (e.g. additional research to match phone number, call back from call logs, etc.).

8. **Prepare for Reporting** – Notify the `meeting-report` context that logging and digest tasks are complete and the logging sheet is ready for weekly report calculations.