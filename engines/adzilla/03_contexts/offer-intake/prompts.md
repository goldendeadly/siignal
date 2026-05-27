# Offer Intake Prompts

Use these prompts to guide AI through the thinking, file editing and folder processing tasks in the **Offer Intake** context.

## Thinking Task Prompt

> **Task:** Understand and organise the basic inputs for a new advertising campaign.
>
> **Read:**
> - The run brief in `07_inputs/run-briefs/[run-file].md`.
> - Any product or service descriptions provided in `07_inputs/`.
>
> **Steps:**
> - Identify the product name, resonance mode, marketing objective and selected platforms.
> - Extract key features, benefits and unique selling points from the offer description.
> - Determine the target audience persona (demographics, psychographics, pain points, desires).
> - Note any constraints or guidelines (budget, timeline, regulatory requirements).
>
> **Output:** A concise outline summarising the offer, audience, objectives and constraints.  Highlight any missing information or assumptions.

## File Editing Task Prompt

> **Task:** Create the `offer-details.md` file.
>
> **Read:**
> - The outline from the thinking task.
>
> **Steps:**
> - Write a Markdown document summarising the product or service details, target audience persona, resonance mode, marketing objective, selected platforms and constraints.
> - Use clear headings and bullet points; avoid long sentences in tables.
> - Save the file to `04_workspaces/offer-intake/[run-folder]/offer-details.md`.
>
> **Output:** A structured offer details file ready for analysis.

## Folder Processing Task Prompt

> **Task:** Initialise the run workspace.
>
> **Read:**
> - The run brief file for the current run.
>
> **Steps:**
> - Create a new folder in `04_workspaces/offer-intake/` using the naming convention `run-[YYYY-MM-DD]-[product-slug]`.
> - Copy the run brief into this folder for reference.
> - Ensure the folder contains `offer-details.md` once created.

> **Output:** A prepared workspace ready for the next context.
