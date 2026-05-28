# Optimisation & Expansion Prompts

## Thinking Prompt

> **You are reviewing the performance of the Realtor Concierge Engine.  Analyse logging sheets, daily digests, weekly reports and QA outcomes.  Calculate key metrics (booking, attendance, qualification, no‑show rates, lead mix, fit rating distribution, response times).  Identify recurring objections, missing information patterns and fallback triggers.  Determine root causes of performance issues.  Propose improvements to scripts, classification thresholds, fallback rules, meeting settings, qualification/disqualify rules, fit rating criteria, target filters and automation workflows.  Suggest expansion ideas (new appointment types, CRM integration, nurture campaigns).  Prioritise recommendations by impact and effort.  Produce a structured recommendations report with rationale and expected benefits.**

## File Editing Prompt

> **Create a recommendations report file named `recommendations-[week]-[client].md`.  Use the following structure:**
> 
> ```
> # Recommendations Report – Week of [Week Start]
> 
> ## Summary
> Brief overview of observed performance and the goal of the recommendations.
> 
> ## Key Metrics
> - Booking Rate: 
> - Attendance Rate: 
> - Qualification Rate: 
> - No-Show Rate: 
> - Lead Mix (Buyer/Seller/HOT/WARM/NURTURE/DISQUALIFY): 
> - Fit Rating Distribution: 
> - Average Response Time: 
> - Additional Metrics (if any): 
> 
> ## Analysis Findings
> Summarise patterns observed in objections, missing info, fallback triggers and other notable trends.
> 
> ## Proposed Improvements
> 1. **Script & Flow:** …
> 2. **Classification Rules:** …
> 3. **Fallback Matrix:** …
> 4. **Meeting Settings:** …
> 5. **Qualification & Disqualify Rules:** …
> 6. **Fit Rating Criteria:** …
> 7. **Target Filters:** …
> 8. **Automations:** …
> 
> ## Expansion Ideas
> Suggest longer-term additions (e.g. new appointment types, multi-language scripts, CRM integrations, nurture campaigns).  Note that these may require phase 2 development.
> 
> ## Prioritised List
> Rank the proposed changes by impact vs. effort (e.g. high/medium/low impact and high/medium/low effort).  Identify which should be implemented next week, next month and in future phases.
> 
> ## Conclusion
> Summarise why these changes will improve performance and the next steps.
> ```
> 
> **Populate each section with your findings and proposals.  Save the report.**

## Folder Processing Prompt

> **After analysing recent data, write a recommendations report using the above structure.  Save the report in `08_outputs/recommendations/`.  Present the report to decision makers for consideration and implementation.**