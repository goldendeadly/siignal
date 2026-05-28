# Workflow: Logging Digest

## Trigger
End of business day (default: 5:30 PM local time) or manual trigger by operator.

## Steps

1. **Collect** — Pull all intake profiles, classification cards, and tickets from today's log.
2. **Count** — Calculate volume metrics (total, by-intent, by-urgency).
3. **Measure** — Compute average response times (intake-to-classification, classification-to-action).
4. **Flag** — Identify any SLA breaches or unresolved emergencies.
5. **Compile** — Generate the formatted Daily Digest.
6. **Deliver** — Send digest to property manager via email or Slack.
7. **Archive** — Save digest to the weekly accumulator for operations-report context.

## Output Artifact
Daily Digest (Markdown format) saved to `workspace/logging-digest/[date]-digest.md`
