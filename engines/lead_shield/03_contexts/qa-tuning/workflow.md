# Workflow: QA Tuning

## Trigger
Weekly scheduled run (default: Friday 4:00 PM) or after any routing rule change.

## Steps

1. **Load Scenarios** — Pull the 12 standardized test transcripts.
2. **Execute** — Run each scenario through the full intake → classification pipeline.
3. **Compare** — Match actual outputs against expected results.
4. **Score** — Calculate pass rate and mark individual results.
5. **Detect Drift** — Compare against previous QA run for changes.
6. **Recommend** — Generate specific fixes for any failures.
7. **Gate Check** — If pass rate < 10/12 or EMERGENCY scenarios fail, set status to PAUSED.
8. **Report** — Generate QA Scorecard and deliver to operator.

## Operational Gates

| Condition | System Status | Required Action |
|-----------|--------------|-----------------|
| 12/12 pass | OPERATIONAL | No action needed |
| 10–11/12 pass (no EMERGENCY fails) | OPERATIONAL (with warnings) | Review failures within 48h |
| < 10/12 pass | NEEDS TUNING | Pause automated responses, manual review |
| Any EMERGENCY scenario fails | PAUSED | Immediate intervention required |

## Output Artifact
QA Scorecard (Markdown format) saved to `workspace/qa-tuning/[date]-scorecard.md`
