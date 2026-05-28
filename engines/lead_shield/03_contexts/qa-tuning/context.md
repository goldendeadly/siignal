# Context: QA Tuning

## Role
Quality assurance layer that tests the classification and routing logic against a standardized 12-scenario test suite. Ensures the system maintains accuracy over time and detects "drift" in classification behavior.

## Scope
- Runs 12 predefined test scenarios through the classification engine
- Compares actual outputs against expected outputs
- Identifies any drift or degradation in accuracy
- Produces a Pass/Fail scorecard with recommendations

## Test Scenarios (12 Total)

| # | Scenario | Expected Intent | Expected Urgency |
|---|----------|----------------|-----------------|
| 1 | Tenant reports burst pipe flooding kitchen | TENANT | EMERGENCY |
| 2 | Tenant reports no heat in January | TENANT | EMERGENCY |
| 3 | Tenant asks about lease renewal timeline | TENANT | INFORMATIONAL |
| 4 | Tenant reports broken dishwasher | TENANT | ROUTINE |
| 5 | Vendor calls about unpaid invoice | VENDOR | ROUTINE |
| 6 | Vendor confirms scheduling for next week | VENDOR | ROUTINE |
| 7 | Vendor solicits new business (cold call) | DISQUALIFIED | DISQUALIFIED |
| 8 | Owner asks for monthly financial update | OWNER-STAFF | ROUTINE |
| 9 | Owner reports concern about property condition | OWNER-STAFF | ROUTINE |
| 10 | Unknown caller, garbled message | UNKNOWN | INFORMATIONAL |
| 11 | Robocall / automated marketing | DISQUALIFIED | DISQUALIFIED |
| 12 | Tenant reports smoke detector beeping | TENANT | ROUTINE |

## Inputs
- 12 test scenario transcripts (standardized)
- Current classification rules and prompts
- Previous QA scorecard (for drift comparison)

## Outputs
- QA Scorecard: Pass/Fail for each scenario with notes
- Drift Detection: Any scenarios that changed result from last run
- Recommendations: Specific prompt or rule adjustments needed

## Success Criteria
- Must achieve ≥ 10/12 pass rate to remain operational
- Any EMERGENCY scenario that fails = immediate system pause
- Drift in 3+ scenarios = mandatory tuning session
