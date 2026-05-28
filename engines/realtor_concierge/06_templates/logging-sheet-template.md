# Logging Sheet Template – Realtor Concierge Engine

This template defines the columns and standards for the concierge logging sheet.  Each call record should be appended as a row with the following fields.  Do not rearrange or rename columns; the AI depends on this exact order.

| Column Name | Description |
|-------------|-------------|
| **Log_ID** | Unique identifier generated for each call (e.g. `L-YYYY-MM-DD-XXX`). |
| **Date** | Date of the call (YYYY-MM-DD). |
| **Time** | Time of the call (HH:MM in 24‑hour format). |
| **Caller_Name** | Name of the caller (if provided). |
| **Phone** | Phone number captured during the call. |
| **Email** | Email address (optional). |
| **Intent** | Caller intent: Buyer, Seller or Other. |
| **Area/Neighbourhood** | Service area or neighbourhood provided by caller. |
| **Timeline_Bucket** | 0–30, 31–90, 90+, or Unknown. |
| **Preapproved** | For buyers: Yes, No, NotYet or Unknown. |
| **Listed** | For sellers: Yes, No or Unknown. |
| **Temperature** | Classification: HOT, WARM, NURTURE or DISQUALIFY. |
| **Qualified_Minimum_Data** | Yes if intent, area, timeline and phone captured; otherwise No. |
| **Booked** | Yes if a consult was booked, No if not booked, Attempted if booking was attempted but failed. |
| **Appointment_Type** | Buyer Consult, Seller Consult or N/A. |
| **Appointment_DateTime** | Date and time of the booked consult (YYYY-MM-DD HH:MM) or N/A. |
| **Escalation_Triggered** | Yes if a hot lead alert or live transfer was triggered, otherwise No. |
| **Escalation_Reason** | Reason for escalation: Hot rule, Angry caller, Transfer requested or Other. |
| **Transfer_Attempted** | Yes if a live transfer attempt was made, otherwise No. |
| **Transfer_Result** | Outcome of the transfer attempt: Connected, NoAnswer, Failed or N/A. |
| **Outcome** | Booked, Callback Requested, Disqualified, Info Only or Hangup. |
| **Completeness_Status** | COMPLETE, PARTIAL or INSUFFICIENT. |
| **Missing_Info** | List any missing required fields (e.g. “timeline,” “area,” “phone”). |
| **Notes_Summary** | Brief summary of caller statements and triggers (max 25 words). |
| **Next_Action** | Exact next step: BookConsult, Callback, Nurture, Polite Exit or N/A. |
| **Next_Action_Due** | Due date/time for the next action (YYYY-MM-DD HH:MM) or N/A. |
| **Owner** | The agent or team member responsible for the next action. |
| **OptOut_SMS** | Yes, No or Unknown. |
| **OptOut_Email** | Yes, No or Unknown. |

**Completeness Standards:**

- **COMPLETE** – Intent, area, timeline and phone captured; booking or outcome recorded.
- **PARTIAL** – Phone captured but one of intent/area/timeline missing or booking not offered.
- **INSUFFICIENT** – No phone captured or caller hung up before intent/area/timeline captured.

Use this template to create monthly logging sheets.  Ensure all rows follow the column order.