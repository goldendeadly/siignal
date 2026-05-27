# Performance Tracking Context

## Purpose

The **Performance Tracking** context monitors and records the performance of each ad and campaign.  It uses tracker templates to log metrics like impressions, clicks, conversions and ROI.  This data informs optimisation and expansion decisions.

## Read First

- The ads generated in the Ad Assembly context.
- The targeting plan to understand the intended audience and budget.
- Tracking templates in `06_templates/`.
- Any existing analytics data or dashboards.

## Use This Context For

- Creating a master campaign tracker capturing run details (product, resonance mode, objective, budgets, platforms).
- Logging each ad’s performance metrics: impressions, clicks, CTR, conversions, cost per click, cost per acquisition, ROAS.
- Verifying that each ad contains the canonical brand line and that messaging is consistent.
- Recording qualitative feedback and lessons learned (e.g. comments, sentiment, reasons for high or low performance).
- Summarising metrics into performance scores and identifying top‑performing ads and segments.

## Ignore

- Generating new content or messaging (handled elsewhere).
- Planning tests and retargeting (handled in Optimisation & Expansion).

## Expected Outputs

- Updated master campaign tracker (`tracker-[product]-campaign-v1.md`).
- Updated ad performance tracker (`tracker-[product]-ads-v1.md`).
- A reflection document summarising metrics and insights (`performance-reflections-v1.md`).
