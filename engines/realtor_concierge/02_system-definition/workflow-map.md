# Workflow Map

This document outlines the end‑to‑end workflow of the Realtor Concierge Engine.  Each phase corresponds to a context and shows the inputs, core steps and outputs produced.

## Phase 1 – Call Intake (`call-intake`)

**Inputs:**
- Call script template (from `06_templates/call-script-template.md`)
- Business information (service area, hours, booking links, alert recipients)
- Logging sheet template (columns definition)

**Steps:**
1. Greet the caller and disclose that you are the automated scheduling concierge.
2. Ask the six mandatory questions: intent (buyer/seller/other), area, timeline bucket, pre‑approval/listing status (depending on intent), best phone number and booking preference.  Use compliance scripts if the caller requests legal/financing advice, price predictions or emergencies.
3. Optionally ask up to four additional questions if the caller is engaged and time permits (property type, budget band, reason for selling, email).
4. Record the captured data and notes in the working log file.
5. Offer a 15‑minute Buyer Consult or Seller Consult when appropriate.  If the caller declines or booking fails, follow deterministic fallback rules.

**Outputs:**
- A raw call record in the run workspace with the captured fields and any missing info.
- A booking request (if accepted) or a callback task (if booking fails or is declined).

## Phase 2 – Classification & Booking (`classification-booking`)

**Inputs:**
- Raw call records from the call‑intake workspace
- Hard classification rules (HOT/WARM/NURTURE/DISQUALIFY)
- Fallback matrix

**Steps:**
1. Read each call record and evaluate the captured data against the classification rules.
2. Assign a temperature (HOT, WARM, NURTURE, DISQUALIFY).  If required fields are missing, default to WARM and note missing info.
3. Determine the next action: book a consult (if HOT or WARM and caller accepted), schedule a nurture callback, or politely disqualify.  If the call outcome already includes booking, verify the booking details.
4. Update the call record with the classification, next action, appointment details and completeness status.
5. Trigger hot lead alerts and live transfers where configured.

**Outputs:**
- An updated call record with classification, booking status, next action and completeness status.
- Hot lead alerts and booking confirmations.

## Phase 3 – Logging & Daily Digest (`logging-digest`)

**Inputs:**
- Updated call records with classification and booking details
- Logging sheet template (column names)
- Daily digest template (format and sections)

**Steps:**
1. Append each updated call record as a row in the logging sheet.  Ensure mandatory columns are populated and missing info is flagged.
2. At the end of the day, compute totals: total calls, buyer vs. seller calls, booked appointments, hot leads, warm/nurture leads, disqualified calls, incomplete records and lead leaks (missed calls).  Generate lists for each category.
3. Populate the daily digest template: section totals, booked appointments (next 48 hours), hot leads needing immediate follow‑up, callbacks needed, at‑risk/incomplete records, disqualifications and notes snapshot.
4. Save the daily digest to the outputs folder and send via the chosen channel (email, Slack, etc.).

**Outputs:**
- Updated logging sheet (CSV or spreadsheet).
- Daily digest file summarising the day’s activity.

## Phase 4 – Meeting Intake (`meeting-intake`)

**Inputs:**
- Weekly intake form template (questions and selections)
- Previous meeting settings (optional)

**Steps:**
1. During weekly planning (usually Monday), fill out the weekly intake form: reporting period start/end dates, time zone, niche, service area, primary offer, meeting types and durations, availability requirements, booking method, hot lead handling (transfer or alert), qualification rules, disqualify rules, fit rating criteria, target filters, qualifying questions and optional cap/replacement rules.
2. Store the completed form in the run workspace and propagate the settings to subsequent contexts.

**Outputs:**
- Weekly meeting settings file detailing meeting types, availability, rules and filters.

## Phase 5 – Meeting Report (`meeting-report`)

**Inputs:**
- Logging sheet covering the reporting period
- Meeting settings from the weekly intake
- Weekly report templates (client and operator)
- Replacement queue template (if cap/replacement is used)
- Execution plan template

**Steps:**
1. Compute weekly totals: leads processed, booked consults, attended consults, qualified consults, disqualified calls, no‑shows and unknown attendance.  Break down by buyer vs. seller.
2. Identify priority leads (top 10) and at‑risk leads (missing next action, missing info, unknown attendance or booking failed).
3. Summarise no‑shows and unknown attendance with notes on drivers and recommended recovery actions.
4. Identify bottlenecks (recurring objections or missing info patterns) and summarise them.
5. Write next week focus recommendations (1–3 changes max).
6. For operator report: create HOT, Warm and No‑Show queues; list missing info requests; summarise cap and replacement usage; provide a week plan (top 5 actions).
7. Create a replacement queue if the client uses a cap + replacement model: track replacement eligibility, ineligible leads and pending attendance confirmations.
8. Generate a daily execution plan template for the week (blocks for HOT response, confirmations, warm follow‑ups, no‑show recovery and close loops).
9. Save the client‑facing and operator‑facing reports, replacement queue and execution plan to outputs.

**Outputs:**
- Client‑facing weekly report summarising totals, splits, priority leads, at‑risk leads, no‑shows, bottlenecks and next week focus.
- Operator‑facing weekly report with queues, missing info, replacement summary and week plan.
- Replacement queue file (if applicable).
- Execution plan file.

## Phase 6 – Quality Assurance & Tuning (`qa-tuning`)

**Inputs:**
- QA test template (12 scenarios with expected outcomes)
- Current scripts, classification rules and fallback matrix
- Logging sheet and digests

**Steps:**
1. Perform 12 simulated or real test calls, each representing a QA scenario (e.g. Buyer HOT with booking, Buyer urgent requiring transfer, Buyer warm, Buyer nurture, Seller HOT, Seller warm, outside service area, vendor solicitation, angry caller, caller refuses phone, booking fails, after‑hours call).  Record the AI’s behaviour.
2. Compare the observed behaviour against the expected outcomes: correct classification, correct number of mandatory questions, correct booking behaviour, correct escalation, correct logging and correct digest generation.
3. Mark each scenario as pass or fail.  Document any deviations and missing steps.
4. If more than two scenarios fail, the system is “NO‑GO” and cannot go live.  Identify root causes and propose tuning changes (e.g. adjust hot triggers, reorder questions, modify fallback rules).  If at least 10 of 12 scenarios pass and hot alerts and bookings function correctly, the system is “GO.”
5. Limit tuning to two changes per day during Week 1.  Track tuning requests and outcomes in a tuning log.

**Outputs:**
- QA report with pass/fail results, root causes and recommended tuning changes.
- Updated scripts, classification rules or fallback matrix if tuning is applied.

## Phase 7 – Optimisation & Expansion (`optimisation-expansion`)

**Inputs:**
- Logging sheets, digests and weekly reports covering recent periods
- Performance metrics (booking rates, lead mix, conversion from HOT/WARM to consult, no‑shows, classification distribution)
- Feedback from the team (top objections, missing info patterns, questions asked by leads)

**Steps:**
1. Review performance metrics to identify trends: Are booking rates dropping?  Are there too many NURTURE or DISQUALIFY decisions?  Are no‑shows increasing?  Which objections recur most?  Are missing data fields common?  Analyse the buyer vs. seller mix and fit ratings (A/B/C).  Evaluate the distribution across HOT/WARM/NURTURE.
2. Identify areas for improvement: adjust hot triggers, update classification thresholds, modify fallback rules, refine questions, adjust meeting durations or types, fine‑tune booking windows and cut‑off times, or update target filters.
3. Suggest enhancements: add automation (e.g. automatically sending reminders after X hours), integrate with CRM or scheduling tools, expand to handle after‑hours calls or additional appointment types (if in scope for v2), or create follow‑up campaigns for nurture leads.
4. Document all recommendations in a suggestions report with rationale and potential impact.

**Outputs:**
- Recommendations report describing proposed improvements and next steps.

This workflow map ensures the AI follows a repeatable sequence of phases while allowing for periodic tuning and optimisation.  Each context operates independently but draws on shared definitions, rules and templates to maintain consistency.