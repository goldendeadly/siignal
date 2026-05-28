# Lead Shield — Routing Table

## Execution Order

| Step | Context | Input | Output | Gate |
|------|---------|-------|--------|------|
| 1 | `call-intake` | Raw call transcript or lead data | Structured caller profile with intent classification | Must identify at least one intent (Tenant/Vendor/Owner-Staff) |
| 2 | `classification-triage` | Structured caller profile | Urgency classification (EMERGENCY/ROUTINE/INFORMATIONAL/DISQUALIFIED) + routing decision | Must assign exactly one urgency level |
| 3 | `maintenance-intake` | Classified request (if maintenance-related) | Structured maintenance ticket with property ID, unit, issue type, photos needed | Must contain actionable repair/maintenance data |
| 4 | `logging-digest` | All processed calls from period | Daily operational digest with metrics and highlights | Must include call count, response time avg, and open items |
| 5 | `operations-report` | Accumulated daily digests | Weekly portfolio health report with trends and recommendations | Must cover all managed properties |
| 6 | `qa-tuning` | 12-scenario test inputs | Pass/Fail scorecard with drift detection | Must achieve ≥10/12 pass rate |
| 7 | `optimisation-expansion` | QA results + operational data | Updated routing rules, new script recommendations, expansion opportunities | Must produce at least 3 actionable recommendations |

## Routing Rules

- If caller intent = TENANT and urgency = EMERGENCY → Immediate escalation to on-call maintenance
- If caller intent = TENANT and urgency = ROUTINE → Log ticket, schedule within 48h
- If caller intent = VENDOR → Route to accounts payable or project manager
- If caller intent = OWNER-STAFF → Route to portfolio manager with priority flag
- If caller intent = UNKNOWN or SPAM → Log and disqualify

## Context Dependencies

```
call-intake → classification-triage → maintenance-intake (conditional)
                                    → logging-digest → operations-report
                                    → qa-tuning → optimisation-expansion
```
