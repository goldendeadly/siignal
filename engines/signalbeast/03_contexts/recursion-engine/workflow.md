# Recursion Engine Workflow

This workflow describes how to generate additional content through the Recursion Engine using the commands defined in the SignalBeast system.  The aim is to extend the lifecycle of the original blog post and its derivatives by creating new mutations, stories, graphics and prompts.

## Steps

1. **Identify candidate assets**
   - Review all platform outputs and highlights to identify pieces suitable for mutation or further transformation (e.g. a strong quote, an outline, a statistic).
   - Note any recommendations from the expansion phase that suggest specific transformations.

2. **Select recursion commands**
   - Choose the appropriate command based on the desired outcome:
     - `/mutate [asset ID]` – convert an existing piece into another format or tone (e.g. blog post → email sequence; tweet → carousel).
     - `/threadcast` – expand a paragraph into a Twitter or LinkedIn thread.
     - `/glyphseed` – create a visual sigil, graphic or infographic from an insight.
     - `/storybind` – turn logic or data into a personal story, parable or narrative.
     - `/promptforge` – convert an output into a meta‑prompt for future generation tasks.
     - `/recur100` – regenerate a full suite of outputs from the same source using a different SEO cluster or resonance mode.
     - `/mapout` – produce a visual or textual map of the content system.

3. **Execute the command**
   - Use the selected command on the chosen asset.  For example:
     - `/mutate adaptive-prompting-thread-x-v1` could generate an Instagram carousel or YouTube script based on the original tweet thread.
     - `/storybind` could take a statistic and craft a narrative reel.
   - Write the resulting content in the appropriate format with a clear CTA and canonical line.

4. **Record the recursion**
   - Update a **Recursion Pathways** table in the run workspace capturing:
     - Original asset ID and platform.
     - Command used.
     - New asset type and platform.
     - Notes on tone or adjustments made.
   - Save the mutated output with a versioned filename (e.g. `[topic]-mutated-carousel-v1.md`).

5. **Update trackers**
   - Log the new outputs into the **Platform Outputs** and **Content Master Tracker** tables, noting that they originated from a recursion command.
   - If the mutation requires scheduling or automation, add it to the automation plan.

6. **Repeat as necessary**
   - Continue to mutate or expand content until the desired number of new pieces or until all viable insights have been transformed.

7. **Reflect and close**
   - Once recursion is complete, review the overall content system for coherence and coverage.
   - Add any lessons learned or interesting results to the analytics feedback for future reference.

## Outputs

- A set of new or mutated content assets with appropriate version names.
- A **Recursion Pathways** table documenting the transformations performed.
- Updated trackers including the new assets.
