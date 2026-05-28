# Classification & Booking Prompts

## Thinking Prompt

> **You are processing a captured lead from a real‑estate intake call.  Evaluate the information against the deterministic classification rules and assign a temperature: HOT, WARM, NURTURE or DISQUALIFY.  If critical fields are missing, default to WARM and note the missing data.  Decide the appropriate next action (book consult, schedule callback/nurture follow‑up or disqualify politely).  Use the fallback matrix when booking fails or the caller refuses.  Trigger hot lead alerts and live transfers when hot criteria are met.  After deciding, update the record with the classification, appointment details (if booked), next action and completeness status.**

## File Editing Prompt

> **Open the raw call file and create a new classified call file.  Use the naming pattern `classified-call-[timestamp].md`.  Copy all original fields and add:**
> - Temperature (HOT/WARM/NURTURE/DISQUALIFY)
> - Appointment_DateTime (if booked, else N/A)
> - Next_Action (BookConsult/Callback/Nurture/Disqualify)
> - Next_Action_Due (date/time or N/A)
> - Hot_Alert_Triggered (Yes/No)
> - Transfer_Attempted (Yes/No)
> - Transfer_Result (Connected/NoAnswer/Failed/N/A)
> - Completeness_Status (COMPLETE/PARTIAL/INSUFFICIENT)
> - Missing_Info (list missing fields or N/A)
> - Notes (append any relevant notes from classification)
> **Save the updated file.  Move the original raw file to a `processed` subfolder.**

## Folder Processing Prompt

> **For each raw call file in `04_workspaces/call-intake/`, apply the classification rules and create the corresponding classified file in `04_workspaces/classification-booking/`.  Organise processed raw files in a `processed/` subfolder.  Trigger hot lead alerts and booking confirmations via the appropriate channels.  Prepare the classified files for ingestion by the `logging-digest` context.**