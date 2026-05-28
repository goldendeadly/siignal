# Lead Shield — Property Management AI Concierge

**Version:** 0.2.0  
**Type:** Operational Triage Agent  
**Target:** Property Management Portfolio Operators

## Purpose

Lead Shield is an autonomous AI concierge designed to handle inbound tenant, vendor, and owner-staff requests for property management companies. It prevents "silent leakage" — missed maintenance calls, mishandled vendor inquiries, and unlogged owner requests that erode portfolio value.

## Core Capabilities

- **Inbound Call Triage:** Captures every call, classifies by intent (Tenant / Vendor / Owner-Staff), and routes appropriately.
- **Classification Engine:** Applies deterministic rules to categorize urgency (EMERGENCY / ROUTINE / INFORMATIONAL / DISQUALIFIED).
- **Maintenance Intake:** Structured capture of maintenance requests with property ID, unit, issue type, and urgency.
- **Operations Reporting:** Daily/weekly digests showing call volume, response times, and resolution rates.
- **QA Testing:** 12-scenario test suite ensuring correct routing and classification.

## Contexts (7-Phase Pipeline)

| # | Context | Purpose |
|---|---------|---------|
| 1 | `call-intake` | Capture inbound call data and identify caller intent |
| 2 | `classification-triage` | Classify urgency and route to correct handler |
| 3 | `maintenance-intake` | Structured capture of maintenance/repair requests |
| 4 | `logging-digest` | Generate daily operational digests |
| 5 | `operations-report` | Weekly performance and portfolio health reports |
| 6 | `qa-tuning` | Run 12-scenario QA suite and tune responses |
| 7 | `optimisation-expansion` | Identify patterns and optimize routing rules |

## Pricing Model

- **One-Time Install:** $1,500 – $3,000
- **Optional Managed Optimization:** $300 – $750/month
- **Install Timeline:** 72 hours (Day 0 Kickoff → Day 3 Go-Live)

## Integration Points

- Google Sheets (default logging)
- Google Calendar / Outlook (booking)
- Twilio / VoIP (call forwarding)
- Jobber / AppFolio (maintenance ticketing)
