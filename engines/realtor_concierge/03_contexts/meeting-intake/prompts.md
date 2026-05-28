# Meeting Intake Prompts

## Thinking Prompt

> **You are configuring the meeting settings for the upcoming week.  Use the weekly intake template to collect all required information from the client or internal team.  Record the reporting period, time zone, niche and service area, primary offer, meeting types and durations, availability requirements, booking method, hot lead handling preferences, qualification and disqualify rules, fit rating criteria, target filters, qualifying questions and optional cap/replacement rules.  Ensure selections are within the allowed limits (no more than two meeting types and six qualifying questions).  Create a well‑structured weekly intake file for the system to use.**

## File Editing Prompt

> **Create a new file `weekly-intake-[week]-[client].md` in the current run workspace.  Use the following structure:**
> 
> ```
> # Weekly Meeting Settings – [Week Start] to [Week End]
> 
> ## Week Context
> - Reporting Start Date: 
> - Reporting End Date: 
> - Time Zone: 
> - Vertical/Niche: 
> - Service Area: 
> 
> ## Primary Offer & CTA
> - Offer Name: 
> - Primary CTA: 
> 
> ## Meeting Types & Availability
> - Meeting Type 1: [Name] ([Duration] minutes)
> - Meeting Type 2: [Name] ([Duration] minutes) (optional)
> - Minimum Open Slots per Week: 
> - Booking Method: [Booking link / Calendar integration / Business hours]
> - Business Hours (if applicable): 
> - Weekend Hours (optional): 
> 
> ## Hot Lead Handling
> - Handling Method: [Live transfer / Alert only]
> - Transfer Numbers: (if applicable)
> - Transfer Hours: (if applicable)
> 
> ## Qualification Rules
> - Rules Selected: [List up to 8]
> - Custom Rule: 
> 
> ## Disqualify Rules
> - Rules Selected: [List all that apply]
> - Custom Rule: 
> 
> ## Fit Rating Criteria
> - Use Fit Rating (Yes/No): 
> - A-fit Definition: 
> - B-fit Definition: 
> - C-fit Definition: 
> 
> ## Target Filters
> - Industry Filters: 
> - Company Size Filters: 
> - Decision-Maker Titles: 
> - Minimum Budget: 
> - Minimum Timeline Urgency: 
> 
> ## Qualifying Questions
> - Questions Selected: [List up to 6]
> - Custom Question: 
> 
> ## Cap & Replacement Rules (Optional)
> - Cap per Week/Month: 
> - Replacement Logic & Exclusions: 
> ```
> 
> **Populate each section with the information collected.  Save the file.**

## Folder Processing Prompt

> **At the start of each reporting period, create a new weekly intake file using the above structure and store it in `04_workspaces/meeting-intake/`.  Copy it to `07_inputs/weekly-intake-forms/` for reference.  Ensure that only one weekly intake file exists per week.  Notify the scheduling system and the `meeting-report` context that new settings are available.**