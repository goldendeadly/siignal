# Ad Assembly Prompts

These prompts assist with planning, writing and managing ad copy across multiple platforms.

## Thinking Task Prompt

> **Task:** Plan the ad content for each platform.
>
> **Read:**
> - Messaging assets (`value-propositions.md`, `benefits.md`, `hooks-taglines.md`).
> - The run brief and market analysis for objectives and audience details.
> - Any platform guidelines or best practices.
>
> **Steps:**
> - Decide which platforms to include and how many ad variations each platform should have.
> - For each platform, outline the required elements (headline length, body length, CTA options, creative notes).
> - Map specific hooks and value propositions to each platform based on audience behaviour and resonance mode.
>
> **Output:** A high‑level plan detailing the number and type of ads for each platform and which messaging assets to use.

## File Editing Task Prompt

> **Task:** Write the ad drafts.
>
> **Read:**
> - The ad plan from the thinking task.
> - Messaging assets and any competitor ads for reference.
>
> **Steps:**
> - For each platform, write a complete ad with headline, body copy, CTA and creative notes.
> - Use the resonance mode to guide tone and word choice.
> - Include the canonical brand line at the end of each ad.
> - Save the ad as `[product]-[platform]-ad-draft-v1.md` in `04_workspaces/ad-assembly/[run-folder]/`.
>
> **Output:** Draft ad files ready for review and targeting.

## Folder Processing Task Prompt

> **Task:** Batch‑generate or update multiple ad files.
>
> **Read:**
> - A list of platforms and versions to update.
>
> **Steps:**
> - Loop through each platform and generate or revise the ad copy based on the latest messaging assets and any feedback received.
> - Save new versions with incremented version numbers (e.g. `v2`, `final`).
> - Ensure naming conventions are followed and no files are overwritten.

> **Output:** Updated ad files reflecting new versions and improvements.
