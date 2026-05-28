# Workflow: Call Intake

## Trigger
Inbound communication received (call, voicemail, text, or web form).

## Steps

1. **Receive** — Accept raw communication data from the forwarding system.
2. **Parse** — Extract caller ID, timestamp, and message content.
3. **Identify** — Match phone number against known tenant/vendor/owner database.
4. **Classify Intent** — Apply intent detection rules to determine caller category.
5. **Structure** — Produce the formatted Caller Profile artifact.
6. **Log** — Write the profile to the daily intake log (Google Sheets row).
7. **Pass** — Send structured profile to Context 2 (Classification & Triage).

## Decision Points

| Condition | Action |
|-----------|--------|
| Phone number matches known tenant | Auto-fill property and unit fields |
| Phone number matches known vendor | Auto-fill vendor name and category |
| Phone number is unknown | Flag for manual identification |
| Message contains emergency keywords | Fast-track to Classification with EMERGENCY flag |

## Emergency Keywords
"flood", "fire", "no heat", "no hot water", "no AC", "gas leak", "broken pipe", "ceiling collapse", "electrical fire", "smoke", "carbon monoxide"

## Output Artifact
Structured Caller Profile (Markdown format) saved to `workspace/call-intake/[timestamp]-profile.md`
