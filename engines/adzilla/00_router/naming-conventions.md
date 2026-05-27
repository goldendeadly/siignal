# Naming Conventions

Consistent naming makes it easy for both humans and AI to locate files.  Use these rules throughout the AdZilla system.

## Run Folders

- Format: `run-[YYYY-MM-DD]-[product-slug]`
- Example: `run-2026-03-13-electric-scooter`
- Each run folder is created inside the context‑specific workspace (e.g. `04_workspaces/offer-intake/run-2026-03-13-electric-scooter/`).

## Offer & Analysis Files

- **Offer Details:** `offer-details-v[number].md`
- **Market Analysis:** `market-analysis-v[number].md`

## Creative Assets

- **Value Propositions:** `[product]-value-propositions-v[number].md`
- **Benefit Bullets:** `[product]-benefits-v[number].md`
- **Hooks & Taglines:** `[product]-hooks-taglines-v[number].md`

## Ad Files

- Format: `[product]-[platform]-ad-[status]-v[number].md`
- Platform values should be lowercase and hyphenated if multi‑word (e.g. `facebook`, `google-ads`, `linkedin`, `youtube`, `tiktok`).
- Status values include: `draft`, `review`, `final`, `published`.

## Targeting Plan

- Format: `[product]-targeting-plan-v[number].md`

## Tracker Files

- **Campaign Master Tracker:** `tracker-[product]-campaign-v[number].md`
- **Ad Performance Tracker:** `tracker-[product]-ads-v[number].md`

## Expansion & Optimisation

- Format: `[product]-optimisation-expansion-v[number].md`

Increment the version (`v1`, `v2`, etc.) each time you make significant changes.  When copying templates to a new run, start with `v1`.
