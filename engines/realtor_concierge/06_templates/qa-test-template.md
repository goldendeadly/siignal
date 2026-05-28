# QA Test Template – Realtor Concierge Engine

This template defines the twelve scenarios used to test the concierge system before going live.  Each scenario includes the input conditions and the expected outcomes.  Use this template to simulate calls and record pass/fail status for each criterion (questions asked, classification, booking, escalation, logging and digest).

| Scenario ID | Input Conditions | Expected Outcome |
|-------------|-----------------|-----------------|
| **QA‑01 Buyer HOT + Books** | Buyer; service area; timeline = 0–30 days; pre‑approved = Yes. | Temperature = HOT; booking offered and confirmed; hot lead alert triggered; completeness = COMPLETE; log row created. |
| **QA‑02 Buyer HOT Wants to Talk Now** | Buyer; urgent; caller requests to speak today. | Temperature = HOT; transfer attempted (if enabled); fallback if transfer fails; booking attempted; log row created. |
| **QA‑03 Buyer WARM + Books** | Buyer; service area; timeline = 31–90 days; pre‑approved = Not yet. | Temperature = WARM; booking offered and scheduled; no hot alert; completeness = COMPLETE. |
| **QA‑04 Buyer NURTURE** | Buyer; service area; timeline = 90+ days; browsing. | Temperature = NURTURE; booking offered or nurture callback scheduled; completeness = COMPLETE. |
| **QA‑05 Seller HOT Listed & Unhappy** | Seller; listed = Yes; wants to switch agent. | Temperature = HOT; booking offered; hot lead alert triggered; completeness = COMPLETE. |
| **QA‑06 Seller HOT Deadline Trigger** | Seller; urgent relocation or deadline within 2 weeks. | Temperature = HOT; escalation triggered; booking or transfer attempted; completeness = COMPLETE. |
| **QA‑07 Seller WARM** | Seller; timeline = 31–90 days. | Temperature = WARM; booking offered; completeness = COMPLETE. |
| **QA‑08 Outside Service Area** | Caller outside service area (enforce disqualify). | Temperature = DISQUALIFY; polite exit using compliance script; log row created; completeness = COMPLETE. |
| **QA‑09 Vendor Solicitation** | Caller offers services (vendor/spam). | Temperature = DISQUALIFY; no booking; log row created; completeness = COMPLETE. |
| **QA‑10 Angry Caller** | Caller complains, angry tone. | De‑escalation script used; booking or callback offered; classification depends on answers; log row created. |
| **QA‑11 Caller Refuses Phone** | Caller refuses to provide phone number and booking. | Temperature = DISQUALIFY or INSUFFICIENT (per rule); polite exit; log row created with completeness = INSUFFICIENT. |
| **QA‑12 Booking Fails** | Booking link fails or no slots available. | Fallback behaviour: capture details; outcome = Callback Requested; next action due within SLA; completeness = COMPLETE or PARTIAL depending on captured fields. |

For each scenario, record whether the system:

1. Asked all six mandatory questions (and no more).
2. Assigned the correct temperature.
3. Offered or scheduled a booking appropriately.
4. Triggered escalation or transfer for hot leads.
5. Logged a row with correct completeness status.
6. Compiled the daily digest correctly after running all scenarios.

Pass the scenario only if all applicable criteria succeed.  Use this template to prepare QA tests.