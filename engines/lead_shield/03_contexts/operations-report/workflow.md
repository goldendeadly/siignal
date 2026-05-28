# Workflow: Operations Report

## Trigger
End of reporting period (default: Sunday 8:00 PM) or manual trigger by operator.

## Steps

1. **Collect** — Pull all daily digests from the reporting period.
2. **Aggregate** — Sum volume metrics, average response times, count escalations.
3. **Trend** — Compare against previous week's report (if available).
4. **Rank** — Identify top properties by activity and issue frequency.
5. **Backlog** — Query open maintenance tickets older than 48 hours.
6. **Analyze** — Identify patterns and generate recommendations.
7. **Compile** — Generate the formatted Weekly Operations Report.
8. **Deliver** — Send to portfolio manager and any designated stakeholders.

## Output Artifact
Weekly Operations Report (Markdown format) saved to `workspace/operations-report/week-[ISO-week]-report.md`
