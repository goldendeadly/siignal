# Workflow: Classification & Triage

## Trigger
Structured Caller Profile received from call-intake context.

## Steps

1. **Receive** — Accept the Caller Profile artifact.
2. **Validate Intent** — Confirm or correct the intent classification using keyword analysis.
3. **Apply Urgency Rules** — Match message content against the urgency matrix.
4. **Check History** — Query if this caller has prior open tickets or repeated calls.
5. **Determine Route** — Assign the correct handler based on intent + urgency combination.
6. **Set SLA** — Apply the appropriate response timeline.
7. **Escalation Check** — Run the escalation override rules.
8. **Produce Card** — Generate the Classification Card artifact.
9. **Dispatch** — If EMERGENCY, trigger immediate alert. Otherwise, pass to next context.

## Routing Matrix

| Intent + Urgency | Route To | Alert Method |
|-----------------|----------|--------------|
| Tenant + Emergency | On-Call Maintenance | SMS + Phone Call |
| Tenant + Routine | Maintenance Coordinator | Daily batch |
| Tenant + Informational | Front Desk / Auto-reply | Email |
| Vendor + Any | Accounts Payable / PM | Email |
| Owner + Any | Portfolio Manager | SMS + Email |
| Disqualified | None | Log only |

## Output Artifact
Classification Card (Markdown format) saved to `workspace/classification-triage/[timestamp]-card.md`
