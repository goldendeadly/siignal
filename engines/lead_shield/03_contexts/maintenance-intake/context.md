# Context: Maintenance Intake

## Role
Structured capture of maintenance and repair requests. This context transforms a classified tenant request into an actionable maintenance ticket that can be dispatched to a technician or vendor.

## Scope
- Only processes calls classified as TENANT + EMERGENCY or TENANT + ROUTINE
- Captures all data needed to dispatch a maintenance technician
- Integrates with Jobber/AppFolio for ticket creation

## Inputs
- Classification Card (from classification-triage context)
- Property database (addresses, unit layouts, access instructions)
- Vendor directory (plumbers, electricians, HVAC, general maintenance)

## Outputs
- Maintenance Ticket containing:
  - Ticket ID (auto-generated)
  - Property address and unit number
  - Issue category (Plumbing / Electrical / HVAC / Structural / Appliance / General)
  - Description of issue (tenant's words + structured summary)
  - Urgency (inherited from classification)
  - Photos needed (YES/NO)
  - Preferred access time (tenant availability)
  - Assigned vendor/technician (if auto-assignable)
  - Estimated response time

## Success Criteria
- Must contain enough information to dispatch a technician without callback
- Must categorize the issue type for correct vendor assignment
- Must capture tenant access preferences to avoid missed appointments
