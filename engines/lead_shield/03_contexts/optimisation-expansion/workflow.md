# Workflow: Optimisation & Expansion

## Trigger
Monthly scheduled run (default: last Friday of the month) or after significant QA drift.

## Steps

1. **Collect** — Pull all weekly reports, QA scorecards, and failure logs from the period.
2. **Analyze Patterns** — Identify recurring issues, seasonal trends, and problem properties.
3. **Detect Gaps** — Find caller intents or scenarios not covered by current rules.
4. **Benchmark** — Compare current performance against initial baseline and SLA targets.
5. **Generate Recommendations** — Produce specific, actionable improvements.
6. **Estimate ROI** — Quantify the value delivered and potential value of recommendations.
7. **Compile** — Generate the Optimization Report.
8. **Deliver** — Present to portfolio manager with implementation priority order.

## Recommendation Categories

| Category | Example | Impact Level |
|----------|---------|--------------|
| Routing Rule Change | "Add 'pest control' as ROUTINE instead of INFORMATIONAL" | Medium |
| Script Update | "Change callback script to ask about pet access" | Low |
| New Intent | "Add 'prospective tenant' as a new intent category" | High |
| Integration | "Connect to AppFolio for automatic ticket creation" | High |
| Expansion | "Add after-hours emergency line for Portfolio B" | High |

## Output Artifact
Optimization Report (Markdown format) saved to `workspace/optimisation-expansion/[month]-optimization.md`
