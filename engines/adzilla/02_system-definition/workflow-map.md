# Workflow Map

This map outlines the flow of information and tasks through the AdZilla system.  It identifies the input, output and key actions of each context, and shows how they connect to form a complete advertising workflow.

## Phase 1 – Offer Intake (`offer-intake`)

- **Inputs:** Run brief, offer details, objectives, audience persona, resonance mode, platform selection.
- **Actions:** Document offer details in `offer-details.md`; confirm resonance mode and marketing objective; create run folder.
- **Outputs:** Structured offer file (`offer-details.md`), ready for analysis.
- **Next:** Market Analysis.

## Phase 2 – Market Analysis (`market-analysis`)

- **Inputs:** Offer details; audience persona; competitor research; regulatory considerations.
- **Actions:** Analyse audience demographics and psychographics; identify pain points and desires; research competitors and industry; define brand voice; map benefits and differentiators.
- **Outputs:** Analysis document (`market-analysis-v1.md`) summarising persona insights, competitor benchmarks, brand voice and key benefits.
- **Next:** Creative Generation.

## Phase 3 – Creative Generation (`creative-generation`)

- **Inputs:** Market analysis document; resonance mode; offer details.
- **Actions:** Craft value propositions; write benefit bullets; develop hooks and taglines tailored to the resonance mode; ensure alignment with the marketing objective.
- **Outputs:** `value-propositions.md`, `benefits.md`, `hooks-taglines.md` – a set of core messaging assets.
- **Next:** Ad Assembly.

## Phase 4 – Ad Assembly (`ad-assembly`)

- **Inputs:** Core messaging assets; resonance mode; platform selection.
- **Actions:** For each selected platform, write ads with appropriate headlines, body copy, CTAs and creative notes; adapt language and length to platform conventions; include canonical brand line.
- **Outputs:** A set of ad files (e.g. `product-facebook-ad-draft-v1.md`, `product-google-ads-ad-draft-v1.md`).
- **Next:** Targeting Plan.

## Phase 5 – Targeting Plan (`targeting-plan`)

- **Inputs:** Platform list; audience persona; budget and timing information.
- **Actions:** Define target segments (demographics, interests, behaviours, lookalike audiences); set geographic targeting; allocate budgets; determine start/end dates and daily schedules; choose optimisation goals (e.g. clicks, conversions).
- **Outputs:** `targeting-plan-v1.md` describing target audiences, budgets and schedules for each platform.
- **Next:** Performance Tracking.

## Phase 6 – Performance Tracking (`performance-tracking`)

- **Inputs:** Ads in market; tracking templates; platform analytics data.
- **Actions:** Populate the master campaign tracker and ad performance tracker; verify canonical lines; record impressions, clicks, CTR, conversions, cost per click, ROAS and other metrics; note qualitative feedback and lessons learned.
- **Outputs:** Updated tracker files; reflections on performance.
- **Next:** Optimisation & Expansion.

## Phase 7 – Optimisation & Expansion (`optimisation-expansion`)

- **Inputs:** Performance data; market analysis; core assets; audience insights.
- **Actions:** Identify top‑performing elements; propose A/B tests (headlines, creatives, audiences); design retargeting and lookalike campaigns; suggest cross‑sell or up‑sell offers; recommend automation improvements for bidding, scheduling or reporting.
- **Outputs:** `optimisation-expansion-v1.md` containing tests, retargeting strategies, cross‑selling ideas and automation recommendations.
- **Next:** Iterate or Archive.

## Loop & Archive

After completing the optimisation and expansion phase, you may loop back to Ad Assembly, Targeting Plan or any other phase to implement tests or new campaigns.  When the campaign has run its course, move the run folder into `09_archive/` and store final reports in `08_outputs/`.
