# Input Intake Workflow

1. **Locate the run brief**
   * Navigate to `07_inputs/run-briefs/` and identify the most recent run brief or the file specified by the operator.
   * If a run brief does not exist, create one using the run brief template in `06_templates/run-brief-template.md`.  Fill in all required fields and save it using the naming conventions (`[run-slug]-runbrief-intake-v1.md`).

2. **Validate required fields**
   * Ensure the brief contains entries for niche, offer, avatar, tone (conscious frequency), primary outcome and SEO intent.
   * If any fields are missing, prompt the operator to supply the information or flag the brief as incomplete.

3. **Assign run slug and folder**
   * Derive a `run-slug` by combining the niche and a short offer descriptor (e.g. `roofing-leadgen`).  Convert to lowercase and replace spaces with hyphens.
   * Generate a run folder name using the pattern `run-[yyyy-mm-dd]-[niche]-[offer-slug]` and create this directory under `04_workspaces/input-intake/`.

4. **Copy the run brief into the workspace**
   * Save a validated copy of the run brief in the new run folder.  Ensure the file name follows the naming conventions.
   * Document any assumptions or clarifications in a notes file within the run folder (optional).

5. **Mark the context complete**
   * Once the brief is validated and the run folder exists, proceed to the next context (`strategy-modeling`).  Do not create any content here.