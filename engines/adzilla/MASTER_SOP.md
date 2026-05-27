# AdZilla Master SOP

This Standard Operating Procedure provides step‑by‑step guidance for using the AdZilla Advertising Engine.  Follow these instructions to transform an offer into a fully executed advertising campaign.

## 1. Preparation

1. **Gather Offer Information**
   - Collect the product or service description, including features, benefits, pricing and any unique selling points.
   - Define your marketing objective (awareness, lead generation, sales, retargeting, etc.).
   - Identify the target audience persona (demographics, pain points, desires, objections).
   - Determine your budget and campaign duration.

2. **Create a Run Brief**
   - Use the template in `06_templates/run-brief-template.md` to document the run details: date, topic (product name), objectives, resonance mode, core intent, selected platforms and constraints.
   - Save the run brief to `07_inputs/run-briefs/`.

## 2. Offer Intake (Context: offer‑intake)

1. Read the run brief and offer details.
2. Confirm the resonance mode and marketing objective.
3. Create a workspace folder for the run under `04_workspaces/offer-intake/run-YYYY-MM-DD-product/`.
4. Record the offer information in a structured file (e.g. `offer-details.md`) for easy reference.

## 3. Market Analysis (Context: market‑analysis)

1. Analyse the target audience: demographic profile, pain points, desires, objections and objections handling.
2. Research competitors, industry benchmarks and regulatory considerations.
3. Identify the brand’s voice and resonance patterns.
4. Map out key benefits and differentiators that will inform the creative stage.
5. Document findings in `market-analysis-v1.md` within the run workspace.

## 4. Creative Generation (Context: creative‑generation)

1. From the market analysis, craft concise **value propositions** summarising what makes the offer compelling.
2. Write **benefit bullets** highlighting specific features and advantages.
3. Develop **hooks** and **taglines** tailored to the resonance mode (e.g. authoritative statement, emotional question, technical fact).
4. Save these assets as `value-propositions.md`, `benefits.md` and `hooks-taglines.md` in the creative-generation workspace.

## 5. Ad Assembly (Context: ad‑assembly)

1. Determine which advertising platforms will be used (Facebook, Instagram, Google Ads, LinkedIn, YouTube, TikTok, etc.).
2. For each platform, compose ad copy according to the channel’s conventions:
   - **Headline** – succinct and impactful, includes a hook.
   - **Body Copy** – explains the benefit or pain relief in one or two sentences.
   - **CTA** – instructs the reader on what to do next (learn more, sign up, buy now, etc.).
   - **Creative Note** – suggest imagery or video concepts if applicable.
3. Ensure each ad respects the resonance mode and includes the brand or canonical line where required.
4. Save each ad in a file named `[product]-[platform]-ad-v1.md` in the ad‑assembly workspace.

## 6. Targeting Plan (Context: targeting‑plan)

1. Define audience segments for each platform (e.g. demographics, interests, behaviours, lookalike audiences).
2. Determine geographic targeting if needed.
3. Set budget allocations and schedules (daily vs. lifetime budgets, start/end dates, time of day).
4. Document recommended targeting settings in `targeting-plan-v1.md`.

## 7. Performance Tracking (Context: performance‑tracking)

1. Use the templates in `06_templates` to create a **Campaign Tracker** and **Ad Performance Tracker** in the run workspace.
2. After each ad runs, collect performance data: impressions, clicks, CTR, conversions, cost per click (CPC), cost per acquisition (CPA), return on ad spend (ROAS).
3. Update the tracker tables regularly.
4. Add notes on what performed well or poorly and hypotheses for improvement.

## 8. Optimisation & Expansion (Context: optimisation‑expansion)

1. Review performance data and identify high‑performing segments, copy variations and creatives.
2. Suggest **A/B tests** (headline variations, creative differences, CTA changes) to validate hypotheses.
3. Propose **retargeting campaigns** (e.g. audiences who engaged but didn’t convert, lookalike audiences).  Include ideas for cross‑selling or upselling.
4. Recommend any automation or tool integration that could streamline future campaigns (e.g. automated bid adjustments, budget pacing, rule‑based optimisation).
5. Document these suggestions in `optimisation-expansion-v1.md`.

## 9. Archiving

1. Once the campaign cycle is complete, move the run workspace to `09_archive/` with a clear versioned name (e.g. `run-2026-03-13-product-final`).
2. Store final trackers and reports in `08_outputs/` for reference.
3. Create a short post‑mortem summarising what worked, what didn’t and lessons for future campaigns.

Following this SOP will ensure that every AdZilla campaign is systematic, traceable and optimized for success.
