# AI-DOS Negative Fixture Pack

This pack contains one intentionally invalid JSON example for each core artifact type. Each file is designed to fail schema validation for one or more clear reasons such as missing required properties, incorrect scalar types, malformed arrays, invalid timestamps, or mismatched artifact identifiers.

## Included files

- `task_intake.negative.json` — missing `task_id`, invalid timestamp, wrong scalar types
- `task_brief.negative.json` — wrong `artifact_type`, malformed `risks`, missing `definition_of_done`
- `execution_plan.negative.json` — `steps` is an object instead of an array, malformed checkpoint fields
- `agent_assignment.negative.json` — invalid nested `agent` fields, malformed SLA, wrong escalation shape
- `work_order.negative.json` — invalid timestamp type, wrong instruction and output shapes
- `artifact_manifest.negative.json` — malformed artifact entry, wrong scalar types for review state
- `tool_invocation_record.negative.json` — malformed `inputs` and `outputs`, wrong numeric and status types
- `checkpoint_review.negative.json` — malformed criteria and findings, invalid decision type
- `issue_report.negative.json` — invalid timestamp and severity types, broken affected artifact shape
- `handoff_packet.negative.json` — invalid transfer metadata and recipient expectation types
- `completion_report.negative.json` — wrong terminal field types and malformed acceptance results

## Intended use

Use these files as rejection fixtures in your validator test suite. For each schema, run the matching `.negative.json` file and assert that validation fails for the expected reason. If your canonical schemas disallow extra properties, some fixtures may fail for multiple reasons; that is acceptable and often desirable in a negative pack.

## Suggested testing pattern

For each artifact type, pair the positive example with the corresponding negative example. Your CI assertions should verify that the positive fixture passes validation and the negative fixture fails validation. That gives you a simple but high-value regression harness for schema evolution.
