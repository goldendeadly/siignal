# Context: Logging Digest

## Role
End-of-day compilation of all processed communications into a structured daily operational digest. This provides the property manager with a single-page view of everything that happened.

## Scope
- Compiles all caller profiles, classification cards, and maintenance tickets from the day
- Calculates key operational metrics
- Highlights items requiring attention
- Provides a "Tomorrow's Priorities" section

## Inputs
- All call-intake profiles from the current day
- All classification cards from the current day
- All maintenance tickets generated
- Any unresolved items from previous days

## Outputs
- Daily Digest containing:
  - Total call volume (with breakdown by intent)
  - Average response time
  - Emergency escalations (count + details)
  - Open maintenance tickets
  - Resolved items
  - Disqualified/spam count
  - Hot items requiring immediate attention
  - Tomorrow's priorities

## Success Criteria
- Must be delivered by 6:00 PM local time
- Must include accurate call counts (verified against intake log)
- Must surface any unresolved EMERGENCY items prominently
- Must provide actionable "Tomorrow's Priorities" list
