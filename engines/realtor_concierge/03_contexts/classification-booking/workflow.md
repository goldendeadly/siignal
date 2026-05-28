# Classification & Booking Workflow

Follow this workflow for each raw call record generated in the `call-intake` context.

1. **Load Raw Record** – Read the raw call file from `04_workspaces/call-intake/` and parse the captured fields: intent, area, timeline bucket, pre‑approval/listing status, phone, booking preference, notes and completeness status.

2. **Check Completeness** – If the record is marked INSUFFICIENT (no phone or key data), automatically classify as DISQUALIFY (refuse booking politely) and proceed to step 7.

3. **Evaluate Classification Rules** – Apply the hard classification rules:
   - **Buyer**:
     - **HOT** if any of: timeline = 0–30 days; pre‑approved = Yes; caller requests to speak today; cash buyer (if stated).
     - **WARM** if timeline = 31–90 days and service area matches.
     - **NURTURE** if timeline = 90+ days or “just browsing” and service area matches.
     - **DISQUALIFY** if outside service area, vendor solicitation or caller refuses phone number and refuses booking.
   - **Seller**:
     - **HOT** if wants consult within 7 days; currently listed and unhappy; stated deadline trigger (relocation, divorce, probate, job change).
     - **WARM** if timeline = 31–90 days and service area matches.
     - **NURTURE** if timeline = 90+ days and “not sure yet” and service area matches.
     - **DISQUALIFY** if outside service area, vendor solicitation or caller refuses phone number and booking.
   - **Other**:
     - **DISQUALIFY** if vendor/spam; otherwise classify as WARM or NURTURE based on the need and decide whether a general callback is warranted.
   - **Missing Data**: If any required field (intent, area, timeline, phone) is missing, default to WARM and list missing fields in `Missing_Info`.

4. **Decide Next Action** – Based on the assigned temperature and caller’s booking preference:
   - **HOT**: Offer booking immediately; if booking is accepted, create appointment.  Trigger hot lead alert.  If live transfer is enabled, attempt transfer.
   - **WARM**: Offer booking; if accepted, schedule; if declined, schedule a callback within 24–72 hours.
   - **NURTURE**: Schedule a nurture follow‑up in 90+ days or add to a nurture list.  Send an informational email if applicable.
   - **DISQUALIFY**: Politely exit with compliance script; log as disqualified.

5. **Handle Fallbacks** – If booking fails (calendar full, booking link fails) or the caller refuses booking, follow the fallback matrix:
   - Capture details and promise a callback within specified SLAs (2 hours for HOT, 24 hours for WARM).
   - Update `Booked` as Attempted or `Outcome` as Callback Requested.
   - Assign owner and due time.
   - For refusal to provide phone number: mark as INSUFFICIENT or DISQUALIFY depending on rules.

6. **Update Record** – Add the following fields to the record: Temperature, Appointment_DateTime (if booked), Next_Action, Next_Action_Due, Hot_Alert_Triggered, Transfer_Attempted, Transfer_Result, Completeness_Status (update if fields were missing), Missing_Info (list any missing required fields) and any relevant notes.

7. **Save Updated Record** – Save the updated record back to the run workspace in a new file (e.g. `classified-call-[timestamp].md`) and mark the raw file as processed or move it to a `processed` subfolder.  Trigger any necessary alerts or notifications.

8. **Prepare for Logging** – Signal to the `logging-digest` context that the call record is ready to be appended to the log sheet.