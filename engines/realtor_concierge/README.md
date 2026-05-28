# Realtor Concierge Engine

## System Overview

The **Realtor Concierge Engine** is a structured AI workspace designed to manage inbound real‑estate leads, qualify callers, schedule consults, log interactions, generate daily digests, capture weekly meeting settings, and produce weekly reports—all within a single reusable framework.  It allows one AI to perform multiple tasks without spawning separate agents by routing work to clearly defined contexts.

### Purpose

This system ensures that realtors never miss an opportunity by:

- Answering inbound calls and capturing the minimum required information to classify and route leads.
- Asking up to six mandatory questions to determine buyer/seller intent, location and timeline, with deterministic rules for HOT, WARM, NURTURE or DISQUALIFY classification.
- Booking appropriate consults (15‑minute buyer or seller) when the caller meets qualification criteria.
- Logging every call outcome into a structured sheet for later analysis.
- Sending daily digests summarising new leads, booked consults, hot leads requiring immediate follow‑up, warm/nurture leads, disqualified callers and missed calls.
- Collecting weekly intake information (e.g. service area, meeting types, availability, qualification rules) to configure the meeting engine.
- Producing weekly reports that show leads processed, consults booked/attended/qualified, buyer/seller splits, at‑risk leads and no‑shows.
- Running quality assurance (QA) tests and tuning scripts to keep the system robust.

### Key Inputs

- **Run Brief** – A document specifying the reporting period, service area, vertical/niche, primary offer and call‑handling preferences.
- **Offer & Business Information** – Phone numbers, appointment types, business hours, hot‑lead alert recipients and tool choices (e.g. calendar integration).
- **Caller Data** – Inbound call details captured via the mandatory questions (intent, area, timeline, pre‑approval/listing status, contact information, booking preference).
- **Weekly Intake Form** – A questionnaire covering meeting types, availability requirements, qualification/disqualify rules, fit‑rating criteria and target filters.

### Key Outputs

- **Call Script & Logging** – A script to guide the AI through the intake call and a logging sheet template capturing fields such as caller name, phone, intent, area, timeline bucket, temperature, outcome, next action and owner.
- **Booked Appointments** – Scheduled buyer/seller consults, with confirmation and reminders sent as configured.
- **Daily Digest** – A concise summary of new leads, booked appointments, hot leads requiring immediate attention, nurture queue, disqualified callers and missed calls.
- **Weekly Meeting Settings** – A record of the week’s meeting types, availability, qualification/disqualify rules and targeting filters.
- **Weekly Report** – A client‑facing report listing totals (leads processed, booked consults, attended consults, qualified consults, disqualifications), buyer vs. seller split, priority leads, at‑risk leads, no‑shows and insights.
- **QA & Tuning Notes** – A checklist of test scenarios and any issues found during quality assurance to ensure the system remains compliant and deterministic.

### System Structure

The engine follows a layered architecture similar to the reusable folder pack:

1. **Router** – Defines the system description, folder map, context definitions, naming conventions and routing instructions.
2. **Context Areas** – Distinct stages of work (call‑intake, classification‑booking, logging‑digest, meeting‑intake, meeting‑report, qa‑tuning, optimisation‑expansion).
3. **Workspaces** – Active directories where files are created during each run.

### How to Use

1. Populate the run brief and business information in `07_inputs/`.
2. Follow the **Master SOP** to move through each context in sequence.
3. Use the prompts provided in `05_prompts/` for thinking, file editing and batch processing tasks.
4. Fill in the templates in `06_templates/` to customise scripts, logging sheets, digests and reports.
5. Save all outputs in the matching workspace folders.  After each run, move final reports to `08_outputs/` and archive the run folder in `09_archive/`.
