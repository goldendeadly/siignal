# Lead Shield — Master Standard Operating Procedure

## Operator Role

The operator (AI agent or human) executes the Lead Shield pipeline by processing inbound communications through a 7-context sequential workflow. Each context produces a structured artifact that feeds the next stage.

## Execution Protocol

### Pre-Flight Checks
1. Confirm phone forwarding is active and routing to the intake system.
2. Verify Google Sheets logging template is accessible.
3. Confirm calendar booking links are live and showing correct availability.
4. Review the last daily digest for any unresolved items.

### Sequential Execution

**Context 1: Call Intake**
- Trigger: Inbound call or message received.
- Action: Capture caller ID, timestamp, raw transcript/message content.
- Output: Structured caller profile (name, property, unit, intent signal).
- Gate: Must identify at least one intent before proceeding.

**Context 2: Classification & Triage**
- Trigger: Caller profile from Context 1.
- Action: Apply classification rules to determine intent and urgency.
- Rules:
  - TENANT + "leak/flood/fire/no heat/no AC" → EMERGENCY
  - TENANT + "broken/repair/replace" → ROUTINE
  - VENDOR + "invoice/payment/schedule" → VENDOR-OPS
  - OWNER + any request → PRIORITY
  - Unknown/irrelevant → DISQUALIFIED
- Output: Classification card (intent, urgency, recommended action).
- Gate: Must assign exactly one urgency level.

**Context 3: Maintenance Intake**
- Trigger: Classification = TENANT + EMERGENCY or ROUTINE.
- Action: Capture structured maintenance data.
- Required Fields: Property ID, Unit #, Issue Type, Description, Photos Needed (Y/N), Preferred Access Time.
- Output: Maintenance ticket ready for dispatch.
- Gate: Must contain enough data to dispatch a technician.

**Context 4: Logging Digest**
- Trigger: End of business day (or manual trigger).
- Action: Compile all processed calls into a daily digest.
- Metrics: Total calls, by-intent breakdown, avg response time, open items, escalations.
- Output: Daily digest document.
- Gate: Must include call count and open items.

**Context 5: Operations Report**
- Trigger: End of week (or manual trigger).
- Action: Aggregate daily digests into weekly portfolio health report.
- Sections: Volume trends, response time trends, maintenance backlog, owner communication log, recommendations.
- Output: Weekly operations report.
- Gate: Must cover all managed properties.

**Context 6: QA Tuning**
- Trigger: Weekly or after routing rule changes.
- Action: Run 12-scenario test suite against current classification logic.
- Scenarios: 4 Tenant (2 emergency, 2 routine), 4 Vendor, 2 Owner, 2 Spam/Unknown.
- Output: Pass/Fail scorecard with notes on any drift.
- Gate: Must achieve ≥10/12 pass rate to remain operational.

**Context 7: Optimisation & Expansion**
- Trigger: After QA results + monthly operational review.
- Action: Analyze patterns in misclassifications, identify new intent types, recommend script updates.
- Output: Optimization recommendations document.
- Gate: Must produce at least 3 actionable recommendations.

## Escalation Protocol

- EMERGENCY classifications trigger immediate SMS/call to on-call maintenance.
- Any call where intent cannot be determined after 2 attempts → escalate to human operator.
- QA score below 10/12 → pause automated responses until tuning is complete.

## Quality Standards

- First response within 60 seconds of call receipt.
- Classification accuracy ≥ 90% (measured by QA suite).
- Zero missed EMERGENCY escalations (hard requirement).
- Daily digest delivered by 6:00 PM local time.
- Weekly report delivered by Monday 9:00 AM.
