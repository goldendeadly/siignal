# Market Analysis Prompts

These prompts help structure the analysis of the market environment, audience persona and competitive landscape.

## Thinking Task Prompt

> **Task:** Analyse the audience and competitive environment.
>
> **Read:**
> - `offer-details.md` from the offer-intake workspace.
> - Any competitor ads or industry reports available.
>
> **Steps:**
> - Describe the demographics and psychographics of the target audience.
> - Identify their pain points, desires and objections.
> - Model the **5 highest-leverage avatars** in the niche using the schema below:
>   - Avatar Name/Title (archetype label, e.g., "The Status Seeker")
>   - Demographic Profile (age, income, gender, region)
>   - Psychographic Profile (values, fears, aspirations, cognitive biases)
>   - Dominant Emotion Triggers (status, belonging, novelty, safety, control, freedom)
>   - Buying Behavior Type (impulsive, analytical, experiential, social-proof-driven)
>   - Communication Style (visual, logical, narrative, testimonial-driven, meme-driven)
>   - Key Fears and Trust Blockers
>   - Language of Belief (how they justify purchasing decisions)
> - Mine psychographic data from Reddit subcommunities, reviews, and forums where applicable.
> - List key competitors and summarise their positioning, messaging, offers and price points.
> - Note any industry regulations or platform policies that affect how you can advertise the offer.
> - Define the brand voice and resonance mode appropriate for this campaign.
> - Identify the benefits and differentiators that set the offer apart.
> - Apply the Hormozi Value Equation to the offer: Dream Outcome x Perceived Likelihood / Time Delay x Effort Required.
> - Generate 3-5 irresistible hook statements and pair each to the most resonant avatar.
>
> **Output:** A bulleted or sectioned outline capturing 5 avatar profiles, audience insights, competitor analysis, regulatory notes, voice guidelines, benefit ranking, and hook statements.

## File Editing Task Prompt

> **Task:** Produce the market analysis document.
>
> **Read:**
> - The outline produced in the thinking task.
>
> **Steps:**
> - Write `market-analysis-v1.md` with sections for Avatar Profiles, Audience Insights, Competitor Highlights, Regulatory Considerations, Brand Voice Guidelines, Benefits & Differentiators, and Hook Statements.
> - Use short paragraphs and bullet points; avoid long sentences in tables.
> - Save the file to `04_workspaces/market-analysis/[run-folder]/`.
>
> **Output:** A structured analysis document ready for the creative generation phase.

## Folder Processing Task Prompt

> **Task:** Consolidate multiple analysis documents.
>
> **Read:**
> - All `market-analysis-v*.md` files if multiple analysts contributed.
>
> **Steps:**
> - Compare the findings from each analysis and merge them into a single document.
> - Remove duplicate insights and note any conflicting information for resolution.
> - Save the consolidated analysis as `market-analysis-v2.md`.

> **Output:** A unified analysis document that incorporates all perspectives.
