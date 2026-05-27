# VS Code Prompts

VS Code prompts are used when generating or editing files within a specific context. They instruct the model to read context definitions and workflow steps, then create or update files accordingly.

Example prompt:

“You are operating in VS Code mode. Read `03_contexts/repurposing-engine/context.md` and `03_contexts/repurposing-engine/workflow.md`. Then open all files in `04_workspaces/content-decoding/[run-folder]/`. Generate the first‑pass platform assets for the source blog based on the decoded summary, highlights, SEO layer and CTA rules. Save outputs in `04_workspaces/repurposing-engine/[run-folder]/` using the naming conventions.”

Use VS Code prompts when creating or modifying multiple files in a context, ensuring that you follow the specified workflows and naming rules.