# Replacement Queue Template – Realtor Concierge Engine

Use this template when the client uses a cap + replacement model.  Only eligible leads can be replaced; ineligible leads must be excluded.  Replacement is triggered when a booked consult is not attended or otherwise fails to qualify.

```
REPLACEMENT QUEUE — [Week Start] to [Week End]
Team: [TEAM NAME]
Cap per [Week/Month]: [#]
Replacement Used: [#]
Replacement Remaining: [#]

## Tab A — Replacement Eligible
List leads that are eligible for replacement (e.g. no‑show, disqualified due to client‑caused reasons, unknown attendance beyond SLA).  Include: Lead_ID, Name, Phone, Reason for Replacement, Replacement Rule Citation, Assigned Owner.

## Tab B — Not Eligible (Client‑Caused / Exclusions)
List leads that cannot be replaced because the client caused the failure (e.g. improper calendar availability, late confirmations) or because the exclusion criteria apply (e.g. vendor/spam, wrong industry).  Include: Lead_ID, Name, Phone, Reason for Ineligibility, Exclusion Rule Citation.

## Tab C — Pending Attendance Confirmation
List leads whose attendance has not yet been confirmed and cannot be replaced until confirmed.  Include: Lead_ID, Name, Phone, Consult Date/Time, Assigned Owner, Due by.

## Tab D — Cap Tracker
Keep a running count of how many meetings have been used and how many replacements have been issued.  Include: Week Start, Week End, Cap, Used, Remaining, Notes.
```

Populate this template whenever cap/replacement rules apply.  Use citations from the rules to justify replacement decisions.