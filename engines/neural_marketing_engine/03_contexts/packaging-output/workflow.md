# Packaging Output Workflow

1. **Gather Final Versions**
   * Identify the latest version of each asset across all workspaces.  Use version numbers to determine the most recent file (e.g. `v2` supersedes `v1`).
   * Assets to gather:
     * Strategy model (`strategy-model-core-v*`)
     * Blog titles (`blog-titles-generation-v*`)
     * Blog post (`blog-post-generation-v*`)
     * Social signal (`social-signal-expansion-v*`)
     * Ad copy set (`ad-copy-conversion-v*`)
     * Landing page (`landing-page-conversion-v*`)
     * Any revised assets (`feedback-recursion-v*`)

2. **Copy to Final Delivery Folder**
   * Create a subfolder inside `08_outputs/final-delivery/` named after the run folder (optional for organisation).
   * Copy each final asset into this folder.  Ensure file names follow the naming conventions and include the correct version number.

3. **Create the Output Index**
   * Use the output index template in `06_templates/output-index-template.md` as a guide.
   * List each deliverable with columns for asset type, file name, version, description and notes.
   * Save this index as `[run-slug]-output-index-final-v1.md` in the final delivery folder.

4. **Verify & Clean Up**
   * Check that no intermediate files remain in the final delivery folder.
   * Ensure all paths and file names are correct.  Fix any naming inconsistencies.
   * Move the run folder from `04_workspaces/` to `09_archive/old-runs/` (if archiving is part of this context).

5. **Mark completion**
   * Once the final delivery bundle and index are prepared, notify the operator or client.  Document any observations or suggestions for future runs.