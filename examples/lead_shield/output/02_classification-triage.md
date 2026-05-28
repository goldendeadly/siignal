# Lead Shield — Classification & Triage Output

## Classification Cards

### Call 1 — Maria Gonzalez
```
CLASSIFICATION CARD
─────────────────────────────
Caller:         Maria Gonzalez
Property:       Pinecrest Apartments, Unit 204
Intent:         TENANT
Urgency:        EMERGENCY
Route To:       On-Call Maintenance
Response SLA:   Immediate (< 5 min)
Action:         Dispatch emergency plumber. Water intrusion from ceiling indicates
                possible burst pipe in unit above (304). Contact unit 304 tenant
                to verify. Alert property manager.
Escalation:     YES — Active water damage, keyword "water coming through ceiling"
─────────────────────────────
```

### Call 2 — Dave (Rocky Mountain Plumbing)
```
CLASSIFICATION CARD
─────────────────────────────
Caller:         Dave, Rocky Mountain Plumbing
Property:       Oakwood Commons (vendor, not tenant)
Intent:         VENDOR
Urgency:        ROUTINE
Route To:       Accounts Payable
Response SLA:   24h
Action:         Pull invoice #4521 for water heater install. Verify completion
                and process payment if approved. Call Dave back with status.
Escalation:     NO
─────────────────────────────
```

### Call 3 — Robert Chen (Owner)
```
CLASSIFICATION CARD
─────────────────────────────
Caller:         Robert Chen
Property:       Lakewood Terrace (owner)
Intent:         OWNER-STAFF
Urgency:        ROUTINE (priority flagged)
Route To:       Portfolio Manager
Response SLA:   4h
Action:         Schedule property walkthrough for next week. Prepare and send
                latest occupancy report for Lakewood Terrace. Confirm date/time
                with owner.
Escalation:     NO
─────────────────────────────
```

### Call 4 — SolarMax Energy Solutions
```
CLASSIFICATION CARD
─────────────────────────────
Caller:         SolarMax Energy Solutions (800 number)
Property:       N/A
Intent:         DISQUALIFIED
Urgency:        DISQUALIFIED
Route To:       None (log and discard)
Response SLA:   N/A
Action:         Log as spam/solicitation. No follow-up required.
Escalation:     NO
─────────────────────────────
```

### Call 5 — James, Unit 108
```
CLASSIFICATION CARD
─────────────────────────────
Caller:         James
Property:       Oakwood Commons, Unit 108
Intent:         TENANT
Urgency:        ROUTINE
Route To:       Maintenance Coordinator
Response SLA:   48h
Action:         Create maintenance ticket for dishwasher inspection/repair.
                Appliance category. Schedule technician within 48h window.
Escalation:     NO
─────────────────────────────
```

### Call 6 — Prospective Tenant
```
CLASSIFICATION CARD
─────────────────────────────
Caller:         Unknown (prospective tenant)
Property:       Pinecrest Apartments (2BR listing inquiry)
Intent:         UNKNOWN (prospective tenant — not current tenant/vendor/owner)
Urgency:        INFORMATIONAL
Route To:       Leasing Office / Front Desk
Response SLA:   24h
Action:         Forward to leasing team. Confirm unit availability and schedule
                showing. Add to prospective tenant pipeline.
Escalation:     NO
─────────────────────────────
```

## Summary

| Call | Caller | Intent | Urgency | Route |
|------|--------|--------|---------|-------|
| 1 | Maria Gonzalez | TENANT | EMERGENCY | On-Call Maintenance |
| 2 | Dave (RMP) | VENDOR | ROUTINE | Accounts Payable |
| 3 | Robert Chen | OWNER-STAFF | ROUTINE (priority) | Portfolio Manager |
| 4 | SolarMax | DISQUALIFIED | DISQUALIFIED | Discarded |
| 5 | James | TENANT | ROUTINE | Maintenance Coordinator |
| 6 | Unknown | INFORMATIONAL | INFORMATIONAL | Leasing Office |
