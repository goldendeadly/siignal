# Workflow: Maintenance Intake

## Trigger
Classification Card received with Intent = TENANT and Urgency = EMERGENCY or ROUTINE.

## Steps

1. **Receive** — Accept Classification Card from triage context.
2. **Enrich** — Cross-reference property database for unit details and access instructions.
3. **Categorize** — Assign issue category based on keywords and description.
4. **Structure** — Generate the Maintenance Ticket with all required fields.
5. **Validate** — Check for missing critical fields (property, unit, description).
6. **Dispatch or Callback** — If complete, route to vendor. If incomplete, generate callback script.
7. **Log** — Write ticket to maintenance log and update daily count.

## Category Detection Keywords

| Category | Keywords |
|----------|----------|
| Plumbing | leak, pipe, drain, toilet, faucet, water heater, flood, clog |
| Electrical | outlet, breaker, light, switch, wiring, spark, power |
| HVAC | heat, AC, thermostat, furnace, air conditioning, vent, filter |
| Structural | wall, ceiling, floor, door, window, roof, foundation, crack |
| Appliance | refrigerator, stove, oven, dishwasher, washer, dryer, disposal |
| General | pest, lock, key, paint, carpet, cleaning, smoke detector |

## Output Artifact
Maintenance Ticket (Markdown format) saved to `workspace/maintenance-intake/[ticket-id].md`
