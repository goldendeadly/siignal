# Fallback Rules Template – Realtor Concierge Engine

Use this matrix to handle situations when the standard booking flow cannot be completed.  Do not improvise; follow these deterministic responses.

| Scenario | What to Say | Logging Outcome | Next Action |
|---------|-------------|-----------------|-------------|
| **Calendar full / no slots** | “We’re fully booked at the moment. I’ll capture your details and the team will contact you to schedule.” | Outcome = Callback Requested; Booked = Attempted; Missing_Info if any. | Owner calls within 2 hours (HOT) or 24 hours (WARM). |
| **Booking link failure** | “The booking link isn’t loading. I’ll book you manually or have the team call you to confirm a time.” | Outcome = Callback Requested; Booked = Attempted. | Callback within 1 hour. |
| **Caller refuses to book** | “No problem. Would you like a quick callback instead?” | Outcome = Callback Requested; Booked = No. | Call back within 2 hours (HOT) or next business day (WARM). |
| **Caller refuses phone** | “I can’t schedule without a callback number. If you change your mind, you can call again anytime.” | Completeness = INSUFFICIENT; Outcome = Info Only. | No outbound contact created. |
| **Call drops / hangup** | N/A (call ended prematurely). | Log whatever information was captured; Completeness = PARTIAL or INSUFFICIENT. | If phone captured: callback within 2 hours (HOT) or 24 hours (WARM).  If no phone: mark as lead leak (lost lead). |
| **Live transfer fails** | “They’re unavailable right now. I’ll prioritise you and book the fastest slot.” | Transfer_Result = Failed; Outcome = Booked or Callback Requested. | Send hot alert + transfer fail note; schedule booking or callback. |
| **After-hours call** | Capture details, book next available slot or schedule callback for next business day (per client setting). | Log call as after-hours in Notes_Summary. | Book the next available slot or callback next business day. |
| **Opt-out request** | “Understood. I’ll mark you as do‑not‑contact.” | OptOut_SMS/Email = Yes. | Do not contact further. |

These rules ensure consistent behaviour in edge cases.  Update them only through the tuning process and document any changes.