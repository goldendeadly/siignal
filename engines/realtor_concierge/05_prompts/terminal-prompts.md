# Terminal Prompts – Realtor Concierge Engine

Terminal prompts are used for batch operations, such as processing multiple files or generating summary tables.  They often involve reading all files in a folder and producing aggregated outputs.

## Batch Logging

> **Context:** logging‑digest
>
> **Task:** Iterate through all classified call files in `04_workspaces/classification-booking/` and append rows to the logging sheet.  Compute daily statistics and generate the daily digest.  Summarise the operation with a count of processed files and any errors.

## Batch Digest Compilation

> **Context:** logging‑digest
>
> **Task:** For each day in the reporting week, read all classified call files with that date, generate a digest using the template and save it to `08_outputs/daily-digests/`.  Create a log summarising how many digests were generated and where they were saved.

## Batch Report Generation

> **Context:** meeting‑report
>
> **Task:** At the end of the week, read the logging sheet and weekly intake file.  Generate the client and operator reports, replacement queue (if applicable) and execution plan.  Summarise the counts (leads processed, booked, attended, qualified, disqualified, no‑shows).  List the file names of the generated reports.  

## Batch QA Testing

> **Context:** qa‑tuning
>
> **Task:** Execute all QA test scenarios in sequence.  Log the results for each scenario, including pass/fail status for questions, classification, booking, escalation, logging and digest.  At the end, count passes and fails and generate a QA report.

## Batch Recommendations

> **Context:** optimisation‑expansion
>
> **Task:** Aggregate metrics across multiple weeks (if applicable), compute average booking rates, attendance rates and no‑show rates.  Identify trends over time and output a summary table.  Then generate a recommendations report summarising multi‑week trends and improvement suggestions.