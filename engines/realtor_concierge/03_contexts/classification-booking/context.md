# Classification & Booking Context

## Purpose

The **classification‑booking** context processes raw call records captured in `call-intake` to determine the lead’s temperature (HOT, WARM, NURTURE or DISQUALIFY) using deterministic rules and decides the appropriate next action (book consult, callback, nurture follow‑up or disqualify politely).  It ensures that bookings are confirmed, fallback tasks are created when bookings fail and hot lead alerts are executed.

## Read First

- `06_templates/logging-sheet-template.md` – to understand the required fields and completeness statuses.
- `06_templates/call-script-template.md` – for reference on captured fields and mandatory questions.
- `06_templates/qa-test-template.md` – to see the scenarios used to validate classification logic.
- `06_templates/fallback-rules-template.md` – for deterministic fallback responses.

## Use This Context For

- Reading each raw call record produced by `call-intake`.
- Applying hard classification rules based on timeline, pre‑approval/listing status, urgency, service area and other captured data.
- Assigning a temperature (HOT/WARM/NURTURE/DISQUALIFY).  If conflicting or missing data exists, default to WARM and tag missing info.
- Deciding the next action: book a consult (with date/time), schedule a nurture callback, or disqualify politely.
- Updating the call record with classification, next action, booked status, appointment details and completeness status.
- Triggering hot lead alerts and live transfers when hot criteria are met.
- Handling fallback scenarios (e.g. calendar full, booking link failure, caller refuses to book or provide phone) using deterministic rules.

## Ignore

- Asking additional questions (handled in `call-intake`).
- Logging the final row into the log sheet (handled in `logging-digest`).
- Generating digests or reports (handled in later contexts).
- Tuning or optimisation decisions.

## Expected Outputs

After processing each raw call record, produce:

- **Updated call record** with added fields:
  - Temperature (HOT/WARM/NURTURE/DISQUALIFY)
  - Appointment_DateTime (if booked)
  - Next_Action (book consult / callback / nurture follow‑up / polite exit)
  - Next_Action_Due (date/time for callback or nurture follow‑up)
  - Hot_Alert_Triggered (Yes/No)
  - Transfer_Attempted (Yes/No)
  - Transfer_Result (Connected/NoAnswer/Failed/N/A)
  - Updated Completeness_Status and Missing_Info (if fields were missing in the raw record)
- **Booking confirmations** or **callback tasks** where applicable.
- **Hot lead alerts** (e.g. SMS/email) and **live transfer logs** if hot criteria are met.

Store updated call records in the run workspace.  The `logging-digest` context will convert them into log rows and digests.