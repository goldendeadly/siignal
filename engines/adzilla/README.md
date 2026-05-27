# AdZilla Advertising Engine

## System Overview

**AdZilla** is a structured AI workspace system that transforms a product, service or offer into a multi‑channel advertising campaign.  It uses a layer‑based architecture to analyse your offer, generate compelling value propositions, craft platform‑specific ads, plan audience targeting, track performance and continually optimise and expand campaigns.  The system is designed to work across any niche or industry, preserving brand voice while tailoring messaging to each advertising channel.

### Purpose

AdZilla’s purpose is to simplify and systemise the creation of high‑performing ads.  It guides you from initial offer intake through market analysis, creative generation, campaign assembly, targeting planning, performance tracking and expansion.  By following the workflow, you can produce a comprehensive campaign that is consistent, compliant with platform guidelines, and adaptable for A/B testing and retargeting.

### Primary Inputs

- **Offer Details:** product or service description, unique selling points, pricing, features and benefits.
- **Target Audience:** persona demographics, pain points, desires and objections.
- **Brand Voice / Resonance Mode:** authority, emotional, technical, viral, educational or hybrid.
- **Marketing Objective:** awareness, lead generation, sales conversion, retargeting, brand loyalty, etc.
- **Platform Selection:** channels to target (Facebook, Instagram, Google Ads, LinkedIn, YouTube, TikTok, etc.).
- **Budget & Timeframe:** budget constraints, campaign duration, daily or lifetime spend.

### Primary Outputs

- **Value Proposition Assets:** concise value statements, benefit bullets, taglines and hooks.
- **Platform‑Specific Ads:** headline, body copy, creative suggestions and calls to action for each selected channel.
- **Targeting Plans:** recommended audience segments, geographic targeting, scheduling and budget allocations.
- **Tracker Files:** tables summarising ad performance (impressions, clicks, cost per click, conversions, ROI) and run details.
- **Expansion Recommendations:** ideas for retargeting audiences, new offers, cross‑selling, automation and A/B tests.

### Rules & Constraints

- Preserve brand voice and resonance mode across all ads.
- Ensure claims comply with platform advertising policies and industry regulations.
- Avoid making unsupported promises or unrealistic guarantees.
- Include a canonical or brand line where appropriate (e.g. “Discover more at [YourBrand.com]”).
- Track all outputs for measurement and continuous improvement.

### System Structure

AdZilla uses a layered architecture similar to the reusable folder pack:

1. **Router** – Defines the system, folder map, context definitions, naming conventions and routing instructions.
2. **Context Areas** – Distinct phases of the workflow (offer‑intake, market‑analysis, creative‑generation, ad‑assembly, targeting‑plan, performance‑tracking, optimisation‑expansion).
3. **Workspaces** – Active folders where files are created during each run.

### Usage

To run AdZilla:

1. Place your offer details and run brief into `07_inputs/`.
2. Follow the workflow described in `MASTER_SOP.md` or navigate using the router (`00_router/Claude.md`).
3. Move through the context areas in sequence, creating the required files in the corresponding workspace folders.
4. Log all ads and performance data in the trackers.
5. Use the expansion phase to plan retargeting, A/B tests and new campaigns.
6. Archive completed runs for future reference.
