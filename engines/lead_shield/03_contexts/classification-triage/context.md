# Context: Classification & Triage

## Role
The decision engine that takes structured caller profiles and assigns urgency levels, routing decisions, and recommended actions. This is the "brain" of Lead Shield's operational logic.

## Scope
- Urgency classification (EMERGENCY / ROUTINE / INFORMATIONAL / DISQUALIFIED)
- Intent validation (confirming or correcting the intake classification)
- Routing decisions (who handles this, and how fast)
- Escalation triggers (when to alert humans immediately)

## Inputs
- Structured Caller Profile from call-intake context
- Property management company rules (business hours, on-call schedule, SLAs)
- Historical data (has this tenant called before about the same issue?)

## Outputs
- Classification Card containing:
  - Confirmed Intent (TENANT / VENDOR / OWNER-STAFF)
  - Urgency Level (EMERGENCY / ROUTINE / INFORMATIONAL / DISQUALIFIED)
  - Routing Decision (who handles + timeline)
  - Recommended Action (specific next step)
  - Escalation Flag (YES/NO + reason if YES)

## Classification Rules

| Intent | Keywords/Signals | Urgency | Response SLA |
|--------|-----------------|---------|--------------|
| Tenant | Emergency keywords (flood, fire, no heat) | EMERGENCY | Immediate (< 5 min) |
| Tenant | Repair/replace/broken (non-emergency) | ROUTINE | Within 48 hours |
| Tenant | Question/update/general inquiry | INFORMATIONAL | Within 24 hours |
| Vendor | Invoice/payment/scheduling | ROUTINE | Within 24 hours |
| Owner | Any request | ROUTINE (priority flagged) | Within 4 hours |
| Unknown | Cannot determine intent | INFORMATIONAL | Human review within 2 hours |
| Spam | Solicitation/irrelevant | DISQUALIFIED | Log and close |

## Success Criteria
- Must assign exactly one urgency level per caller profile
- Zero missed EMERGENCY classifications (hard requirement)
- Classification accuracy ≥ 90% as measured by QA suite
