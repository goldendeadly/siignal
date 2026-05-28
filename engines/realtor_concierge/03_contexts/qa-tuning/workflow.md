# Quality Assurance & Tuning Workflow

Follow this workflow to run the QA test suite, analyse results and decide whether the system is ready to go live.

1. **Prepare Test Environment** – Ensure the call script, classification rules, logging sheet and daily digest template are up to date.  Set the system in a test mode so that calls are not routed to real clients.  Have access to a separate test phone number or simulator if needed.

2. **Run Test Scenarios** – Execute each of the twelve scenarios defined in the QA template:
   - **QA‑01 Buyer HOT + Books:** buyer, service area, 0–30 days, pre‑approved yes.
   - **QA‑02 Buyer HOT Wants to Talk Now:** buyer, urgent, wants to talk today.
   - **QA‑03 Buyer WARM + Books:** buyer, service area, 31–90 days, pre‑approved not yet.
   - **QA‑04 Buyer NURTURE:** buyer, service area, 90+ days, just browsing.
   - **QA‑05 Seller HOT Listed & Unhappy:** seller, listed yes, wants to switch.
   - **QA‑06 Seller HOT Deadline Trigger:** seller, urgent relocation/deadline within 2 weeks.
   - **QA‑07 Seller WARM:** seller, service area, 2–3 months.
   - **QA‑08 Outside Service Area:** outside service area, disqualify enforced.
   - **QA‑09 Vendor Solicitation:** vendor/spam call.
   - **QA‑10 Angry Caller:** caller complains loudly.
   - **QA‑11 Caller Refuses Phone:** caller refuses to provide phone and booking.
   - **QA‑12 Booking Fails:** calendar full or booking link fails.
   For each scenario, follow the script, ask the mandatory questions, handle the situation deterministically and record the AI’s behaviour.

3. **Record Observations** – For each test call, document:
   - Whether the mandatory questions were asked and not exceeded.
   - Classification outcome (HOT/WARM/NURTURE/DISQUALIFY) and whether it matched the expected result.
   - Booking behaviour (offered and confirmed appropriately or fallback used correctly).
   - Escalation/Transfer behaviour (triggered for hot leads and executed correctly).
   - Logging behaviour (row created with correct completeness status and fields populated).
   - Digest behaviour (if daily digest compiled correctly after multiple tests).

4. **Compare to Expected Outcomes** – Use the QA template to check whether each scenario matches the expected classification, booking and escalation outcomes.  Mark each criteria (questions asked, classification, booking, escalation, logging, digest) as pass or fail.

5. **Determine Pass Rate** – Count the number of scenarios that pass all critical criteria.  If at least 10 out of 12 scenarios pass and critical functions (hot lead alerts and booking) are working, mark the system as **GO**.  Otherwise mark as **NO‑GO**.

6. **Identify Root Causes** – For each failure, identify the root cause.  Example causes: mis‑phrased question, incorrect classification thresholds, missing fallback responses, failure to trigger an alert, logging bug.

7. **Propose Tuning Changes** – Suggest modifications to scripts, classification rules or fallback logic.  Limit changes to two per day during Week 1.  Document the changes and assign an owner and due date.  Update relevant templates (call script, classification rules, fallback matrix) accordingly.

8. **Produce QA Report** – Compile all observations, pass/fail status, root causes, tuning suggestions and the Go/No‑Go decision into a report.  Save the report as `qa-report-[date]-[client].md` in `08_outputs/qa-reports/`.

9. **Implement Approved Changes** – If tuning changes are approved, update the corresponding templates or scripts.  Note these changes in the tuning log and ensure they are tested in the next QA run.

10. **Exit** – If the system is **GO**, proceed to go live.  If **NO‑GO**, repeat the QA process after implementing fixes until the pass rate meets the threshold.