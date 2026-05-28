# Context: Call Intake

## Role
First point of contact for all inbound communications to the property management company. This context captures raw data and produces a structured caller profile.

## Scope
- Inbound phone calls (via Twilio/VoIP forwarding)
- Voicemail transcriptions
- Text messages from tenants, vendors, or owners
- Web form submissions

## Inputs
- Raw call transcript or message content
- Caller ID / phone number
- Timestamp
- Property management company profile (portfolio size, properties managed)

## Outputs
- Structured Caller Profile containing:
  - Caller name (if identifiable)
  - Phone number
  - Associated property (if identifiable)
  - Unit number (if applicable)
  - Intent signal (Tenant / Vendor / Owner-Staff / Unknown)
  - Raw message summary (2-3 sentences)
  - Confidence score (HIGH / MEDIUM / LOW)

## Success Criteria
- Must identify at least one intent signal before passing to classification
- Must capture caller contact information for follow-up
- Must timestamp all entries for audit trail
