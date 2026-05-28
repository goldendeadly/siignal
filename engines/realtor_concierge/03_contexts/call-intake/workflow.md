# Call Intake Workflow

This workflow describes how to handle an inbound call from start to finish using the call‑intake context.  Follow these steps for each call:

1. **Greet and Disclose** – Answer with the standard greeting and disclosure: “Hi, you’ve reached [TEAM NAME].  I’m the automated scheduling concierge assisting the team.  Are you calling about buying or selling?”  If the caller asks for legal/financing advice, price predictions or commission details, politely state you cannot provide those and redirect to a consult.

2. **Intent Question** – Determine whether the caller is a buyer, a seller or other.  If “other,” ask the nature of the inquiry and determine if it’s vendor/spam or general question.

3. **Area Question** – Ask: “What area are you looking in / where is the property located?”  Record the city, neighbourhood or region.  If outside the service area and disqualification rules require, prepare to disqualify politely.

4. **Timeline Question** – Ask: “What’s your timeline?” and offer the three buckets: 0–30 days, 31–90 days or 90+ days.  Record the bucket and any relevant notes (e.g. urgent or just browsing).

5. **Status Question** – If the caller is a buyer, ask: “Are you pre‑approved?” (Yes/No/Not yet).  If the caller is a seller, ask: “Is it currently listed?” (Yes/No).  Record the status.  If the intent is “other,” skip this question.

6. **Contact Question** – Ask for the best phone number to reach them.  Record exactly as provided.  If the caller refuses to provide a phone number and also refuses booking, classify as DISQUALIFY or INSUFFICIENT according to the rules and proceed to close the call.

7. **Booking Question** – Ask: “Would you like to book a 15‑minute consult now?”  If yes, proceed to booking.  If no, ask if they would like a callback.  Record their preference.

8. **Optional Questions** – If the caller is engaged and there is time (no more than four optional questions):
   - **Buyer:** Ask property type (condo/townhouse/detached) and budget band.
   - **Seller:** Ask reason for selling or deadline trigger.
   - **Both:** Ask for email if they are willing.

9. **Booking or Callback** – If the caller accepts booking:
   - Choose the consult type (Buyer or Seller Consult) and schedule using the booking link.  Capture appointment date/time.  Confirm with the caller.
   - If booking link fails or there are no slots, follow fallback rules: capture details, promise a callback and log accordingly.
  If the caller declines booking but accepts a callback, capture preferred callback window and assign a task to the owner.
  If the caller refuses both booking and callback, politely close the call and log as information only.

10. **Escalation and Hot Leads** – If the caller meets hot criteria (e.g. buyer timeline ≤30 days, pre‑approved, cash buyer; seller wants consult within 7 days, listed and unhappy, relocation deadline), trigger a hot lead alert via SMS/email and attempt a live transfer if enabled.  Follow fallback rules if the transfer fails.

11. **Logging Raw Call** – Immediately after the call, create a raw call file in the run workspace capturing all fields listed in the `context.md`.  Mark completeness status:
   - **COMPLETE** if intent, area, timeline and phone are captured and booking or outcome recorded.
   - **PARTIAL** if phone is captured but one of intent/area/timeline or booking is missing.
   - **INSUFFICIENT** if phone is missing or call ends before capturing intent/area/timeline.

12. **Prepare for Next Context** – Save the raw call file.  If there is an immediate action (booking or callback), create a note to ensure follow‑through.  The `classification-booking` context will process the raw file next.