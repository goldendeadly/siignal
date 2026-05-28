# Call Intake Context

## Purpose

The **call‑intake** context handles live inbound calls.  Its goal is to capture the minimum required information to classify and route leads while respecting compliance boundaries.  This context uses the provided call script and fallback matrix to ask the six mandatory questions, optional questions if time permits and safe scripts for non‑qualifying topics.  It records the caller’s intent, area, timeline, pre‑approval/listing status, contact information and booking preference.  It then offers to schedule a 15‑minute Buyer or Seller Consult or creates a callback task if booking is not possible.

## Read First

- `06_templates/call-script-template.md` – to see the exact script, mandatory questions, optional questions and compliance/boundary statements.
- `06_templates/fallback-rules-template.md` – to understand deterministic fallback responses when booking fails, caller refuses to book or declines to provide required information.
- `06_templates/logging-sheet-template.md` – for the list of fields you must capture and how to record completeness status.

## Use This Context For

- Answering inbound calls and capturing the six mandatory questions (intent, area, timeline, pre‑approval/listing status, contact number and booking preference).
- Asking up to four optional questions when the caller is engaged and time permits.
- Applying compliance and boundary scripts for legal/financing questions, price predictions, emergencies, opt‑outs and angry callers.
- Offering the appropriate consult type (Buyer or Seller) and scheduling via booking link or manual booking.
- Handling deterministic fallbacks (calendar full, caller refuses to book, caller refuses phone number, call drops, after‑hours calls, etc.).
- Recording all captured data and notes in a raw call record inside the run workspace.

## Ignore

- Lead classification (handled by `classification-booking`).
- Log sheet updates (handled by `logging-digest`).
- Weekly meeting settings (handled by `meeting-intake`).
- Tuning or optimisation decisions (handled by `qa-tuning` and `optimisation-expansion`).

## Expected Outputs

After executing the call‑intake workflow for each call you should produce:

- A raw call record file in the run workspace (e.g. `raw-call-[timestamp].md`) containing:
  - Caller name (if provided)
  - Phone number
  - Email (optional)
  - Intent (Buyer/Seller/Other)
  - Area/Neighbourhood
  - Timeline bucket (0–30 / 31–90 / 90+ / Unknown)
  - Pre‑approval status (buyer) or listing status (seller)
  - Booking preference (accepts booking / declines / link requested)
  - Notes (summary of caller statements, triggers, objections)
  - Outcome (booked, callback requested, disqualified, info only, hangup)
  - Completeness status (COMPLETE / PARTIAL / INSUFFICIENT)
  - Missing info (if any)
- A booking action (if the caller accepts), or a callback task with due date/time and assigned owner.
- A log entry for hot lead alerts or live transfers (if triggered by hot criteria).

These raw outputs feed into the `classification-booking` context for further processing.