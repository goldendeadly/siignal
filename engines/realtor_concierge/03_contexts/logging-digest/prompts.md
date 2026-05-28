# Logging & Daily Digest Prompts

## Thinking Prompt

> **You are updating the logging sheet and compiling the daily digest.  For each classified call file, extract the required fields and append them to the log sheet.  Compute daily totals (total calls, buyer vs. seller calls, booked appointments, hot leads, warm/nurture leads, disqualified calls, incomplete records, lead leaks) and build lists (booked appointments, hot leads, callbacks, at‑risk/incomplete, disqualified).  Populate the daily digest template with these values.  Ensure all fields are populated, completeness status is accurate and missing information is flagged.**

## File Editing Prompt

> **Open or create the logging sheet (`logging-sheet-[client]-[YYYY-MM].csv`).  Append a new row for each classified call file with the following columns (matching the template):**
> - Log_ID (generate a unique identifier, e.g. `L-[YYYY-MM-DD]-[increment]`)
> - Date
> - Time
> - Caller_Name
> - Phone
> - Email
> - Intent (Buyer/Seller/Other)
> - Area/Neighbourhood
> - Timeline_Bucket
> - Preapproved (Yes/No/NotYet/Unknown)
> - Listed (Yes/No/Unknown)
> - Temperature
> - Qualified_Minimum_Data (Yes/No) (COMPLETE if mandatory fields captured, otherwise No)
> - Booked (Yes/No/Attempted)
> - Appointment_Type (Buyer Consult / Seller Consult / N/A)
> - Appointment_DateTime
> - Escalation_Triggered (Yes/No)
> - Escalation_Reason (Hot rule / Angry / Transfer requested / Other)
> - Transfer_Attempted (Yes/No)
> - Transfer_Result (Connected/NoAnswer/Failed/N/A)
> - Outcome (Booked / Callback Requested / Disqualified / Info Only / Hangup)
> - Completeness_Status (COMPLETE/PARTIAL/INSUFFICIENT)
> - Missing_Info
> - Notes_Summary (max 25 words)
> - Next_Action (exact)
> - Next_Action_Due (date/time)
> - Owner (agent/team lead)
> - OptOut_SMS (Yes/No/Unknown)
> - OptOut_Email (Yes/No/Unknown)

> **After updating the sheet, create a daily digest file using the template.  Populate the sections with totals and lists.  Save the digest in `08_outputs/daily-digests/`.**

## Folder Processing Prompt

> **Process all unlogged classified call files in `04_workspaces/classification-booking/`.  Append rows to the log sheet.  Move processed files to a `logged/` subfolder.  Calculate totals and lists.  Generate the daily digest file using `06_templates/daily-digest-template.md`.  Save it in `08_outputs/daily-digests/` with the correct name.  If lead leaks exist, create `lead-leaks-[date]-[client].md` with details and recovery suggestions.**