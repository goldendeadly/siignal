# Automation Suggestions Workflow

This workflow outlines how to take the system improvement idea from the Signal Expansion phase and turn it into a concrete automation plan.  The aim is to reduce manual labour, ensure consistency and free up human attention for higher‑level tasks.

## Steps

1. **Review the recommended improvement**
   - Open `expansion-recommendations-v1.md` (or v2) and read the **System Improvement** section.
   - Understand what process or task needs to be automated and why.

2. **Outline the automation flow**
   - Determine which tools or services will be involved (e.g. Google Sheets/Airtable, Zapier/Make.com, Canva, Buffer/Metricool/Hypefury, ConvertKit/GHL).
   - Define the trigger event (e.g. new row in tracker, completion of a file, weekly schedule) and subsequent actions (e.g. create Canva design, schedule post, send email).
   - Sketch the data flow: what information moves from one app to another and how it’s transformed.

3. **Draft the automation documentation**
   - Write a Markdown file summarising the proposed automation.  Include:
     - **Objective:** what manual task is being automated and the expected benefit (time saved, errors reduced, etc.).
     - **Toolchain:** list of tools/platforms used and their role in the flow.
     - **Trigger:** what starts the automation.
     - **Actions:** step‑by‑step description of each automated action.
     - **Output:** description of the final state (e.g. scheduled post, updated tracker, sent lead magnet).
   - Save this file to `04_workspaces/automation-suggestions/[run-folder]/automation-plan-v1.md`.

4. **Create VA instructions if needed**
   - If certain steps cannot be fully automated (e.g. designing Canva slides), write a short SOP for the VA.
   - Explain how to take over the process at the appropriate step and what deliverables are expected.
   - Save this as `va-instructions-v1.md` in the same workspace.

5. **Recommend tools and resources**
   - Make a list of recommended tools, plug‑ins or scripts that would aid implementation.  For each, include a short description and a link or reference for further reading.
   - Save this as `recommended-tools.md` in the automation-suggestions workspace.

6. **Hand off to the Recursion Engine**
   - Once automation documentation and instructions are complete, move on to the Recursion Engine context to generate mutated or additional content if needed.

## Outputs

- `automation-plan-v1.md` with the automation design.
- `va-instructions-v1.md` if manual tasks remain.
- `recommended-tools.md` listing tools and integrations.
