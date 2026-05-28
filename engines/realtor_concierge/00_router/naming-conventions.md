# Naming Conventions

Consistent naming makes it easy for the AI to locate the right files automatically.  The following conventions apply across the Realtor Concierge Engine:

## Run Folder

Each run (representing a single day or reporting period) lives in its own folder under the `04_workspaces/` root.  Use the pattern:

```
run-[YYYY-MM-DD]-[client]
```

*Example:* `run-2026-03-13-smithteam`

## File Names

Generated files follow this pattern:

```
[client]-[asset]-[status]-v[number].md
```

- **client** – the slug or short name for the realtor team (e.g. `smithteam`).
- **asset** – the type of content, such as `call-log`, `daily-digest`, `weekly-report-client`, `weekly-report-operator`, `qa-report`, `recommendations`.
- **status** – indicates the lifecycle stage: `draft`, `final`, or `archived`.
- **v[number]** – version number starting at `v1`; increment when the file is regenerated or updated.

*Examples:* `smithteam-call-log-draft-v1.md`, `smithteam-daily-digest-final-v1.md`, `smithteam-weekly-report-client-final-v2.md`.

## Trackers and Forms

- **Logging Sheets:** `logging-sheet-[client]-[YYYY-MM].csv` – used for call logs.
- **Weekly Intake Forms:** `weekly-intake-[week]-[client].md` – used to store weekly meeting settings.
- **QA Reports:** `qa-report-[date]-[client].md` – used to store test results.
- **Replacement Queue:** `replacement-queue-[week]-[client].md` – used if cap/replacement is enabled.

## Template Files

Template files in `06_templates/` are named descriptively to indicate their purpose, such as `call-script-template.md`, `logging-sheet-template.md`, `daily-digest-template.md`, `weekly-intake-template.md`, `weekly-report-template-client.md`, `weekly-report-template-operator.md`, `replacement-queue-template.md`, `qa-test-template.md`, `fallback-rules-template.md`, and `execution-plan-template.md`.

By following these naming conventions, the AI can reliably find inputs, produce outputs and avoid conflicts across runs.