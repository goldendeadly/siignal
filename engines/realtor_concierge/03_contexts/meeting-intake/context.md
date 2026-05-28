# Meeting Intake Context

## Purpose

The **meeting‑intake** context captures the weekly settings needed for scheduling and reporting.  It gathers information about the reporting period, niche, service area, primary offer, meeting types and durations, availability requirements, booking methods, hot lead handling preferences, qualification and disqualify rules, fit rating criteria, target filters, qualifying questions and optional cap/replacement rules.  The resulting settings file informs the meeting engine (scheduling and reporting) for the week.

## Read First

- `06_templates/weekly-intake-template.md` – for the list of questions and allowed options.
- Previous weekly intake files (if available) – to understand last week’s settings and update only what has changed.

## Use This Context For

- Preparing a new weekly intake form at the start of each reporting period (typically Monday morning).
- Collecting the necessary information from the client or internal team: reporting week dates, time zone, niche, service area, primary offer, primary call‑to‑action, meeting types and durations (maximum two types), availability requirements, booking method and hours, hot lead handling (live transfer vs. alert), qualification rules, disqualify rules, fit rating criteria, target filters and qualifying questions.
- Recording cap and replacement rules if a cap on meetings and replacement logic is enforced.
- Storing the completed weekly intake file in the run workspace and propagating these settings to the meeting report context.

## Ignore

- Call handling and classification (handled earlier).
- Logging and digests (handled in `logging-digest`).
- Weekly report generation (handled in `meeting-report`).

## Expected Outputs

- A completed weekly intake file named `weekly-intake-[week]-[client].md` stored in the current run folder.  This file should include:
  - Reporting week start and end dates
  - Time zone
  - Vertical/niche and service area
  - Primary offer and primary CTA
  - Meeting types (name and duration) – up to two
  - Availability requirements (minimum slots per week and booking method: link, integration or business hours)
  - Hot lead handling (live transfer for hot leads or alert only; if live transfer, include transfer number and hours)
  - Qualification rules (select up to 8 from the list; may include custom rule)
  - Disqualify rules (select all that apply; may include custom rule)
  - Fit rating criteria (definitions for A/B/C, if used)
  - Target filters (industry, company size, decision‑maker titles, budget thresholds, timeline urgency)
  - Qualifying questions (select up to 6 from the list; may include custom question)
  - Cap and replacement rules (cap per week/month, replacement eligibility and exclusions)

These settings will be referenced by the scheduling and reporting contexts for the entire week.