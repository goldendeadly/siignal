# Automation Suggestions Prompts

Use these prompts to design and document the automation plan in the **Automation Suggestions** phase.

## Thinking Task Prompt

> **Task:** Develop an automation plan based on the identified system improvement.
>
> **Read:**
> - The **System Improvement** recommendation from `expansion-recommendations-v1.md` (or v2).
> - Any existing workflow maps or automation notes in `02_system-definition/workflow-map.md` or `01_source-material/`.
>
> **Steps:**
> - Clarify the objective and scope of the automation.
> - Identify which tools and platforms will be involved and what data will flow between them.
> - Decide on the trigger event and the sequence of actions that follow.
> - Note any tasks that cannot be fully automated and require human intervention.
>
> **Output:** A clear outline of the automation flow, including objectives, triggers, actions and required tools.

## File Editing Task Prompt

> **Task:** Document the automation plan and VA instructions.
>
> **Read:**
> - The outline from the thinking task.
>
> **Steps:**
> - Draft `automation-plan-v1.md` according to the structure: Objective, Toolchain, Trigger, Actions, Output.
> - If manual steps are needed, create `va-instructions-v1.md` describing tasks, tools and expected outputs for the VA.
> - List the recommended tools with brief descriptions and references in `recommended-tools.md`.
> - Save these files in `04_workspaces/automation-suggestions/[run-folder]/`.
>
> **Output:** Completed documentation ready for implementation and hand‑off.

## Folder Processing Task Prompt

> **Task:** Consolidate multiple automation plans.
>
> **Read:**
> - All automation plan files (`automation-plan-v*.md`) in the current run’s automation-suggestions workspace.
>
> **Steps:**
> - Compare plans and identify duplicate or overlapping automations.
> - Combine compatible steps into a single plan, noting improvements or additional steps.
> - Merge VA instruction files if there are multiple SOPs; ensure they remain concise and non‑conflicting.
> - Combine tool recommendations into one master list, removing duplicates.
>
> **Output:** A unified set of automation documentation for the run.
