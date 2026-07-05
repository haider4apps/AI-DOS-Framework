# AI-DOS Option 3 — Example Instances and End-to-End Walkthrough

This companion document provides concrete example instances for the artifact schemas used by the AI-DOS control plane, plus one end-to-end task walkthrough showing how the artifacts evolve across a real execution. The examples are intentionally realistic rather than minimal so they can be used as test fixtures, validator samples, and onboarding references.

## Assumed artifact set

The examples below cover eleven core artifact types commonly used in the AI-DOS orchestration flow:

1. `task_intake`
2. `task_brief`
3. `execution_plan`
4. `agent_assignment`
5. `work_order`
6. `artifact_manifest`
7. `tool_invocation_record`
8. `checkpoint_review`
9. `issue_report`
10. `handoff_packet`
11. `completion_report`

If your canonical schema names differ slightly, these instances can be renamed mechanically while preserving the structure and semantics.

---

## 1) Example instance: `task_intake`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "task_intake",
  "task_id": "TASK-2026-07-04-001",
  "received_at": "2026-07-04T14:03:11Z",
  "requestor": {
    "id": "user-42",
    "role": "product_owner",
    "channel": "chat"
  },
  "priority": "high",
  "title": "Create AI-DOS executable spec",
  "goal": "Turn the markdown constitution into a machine-enforced orchestration system.",
  "request_text": "Create a formal state machine and schema pack for AI-DOS. Then provide concrete examples and a walkthrough.",
  "constraints": [
    "State transitions must be machine-verifiable",
    "Artifacts must validate via JSON Schema",
    "Outputs should be suitable for control-plane enforcement"
  ],
  "acceptance_criteria": [
    "State machine defines canonical transitions",
    "Schema pack covers core orchestration artifacts",
    "Examples exist for every schema",
    "One end-to-end walkthrough demonstrates execution"
  ],
  "attachments": [],
  "tags": ["orchestration", "schema", "state-machine", "governance"]
}
```

## 2) Example instance: `task_brief`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "task_brief",
  "task_id": "TASK-2026-07-04-001",
  "brief_id": "BRIEF-001",
  "prepared_at": "2026-07-04T14:05:02Z",
  "prepared_by": "coordinator",
  "problem_statement": "AI-DOS currently exists as a prose constitution and needs executable control-plane semantics.",
  "objectives": [
    "Define lifecycle states and guarded transitions",
    "Formalize artifact contracts for validation",
    "Provide testable examples and an operational walkthrough"
  ],
  "scope_in": [
    "Task lifecycle state machine",
    "Artifact schema pack",
    "Examples and walkthrough"
  ],
  "scope_out": [
    "Implementation code for the control plane",
    "Persistent storage design",
    "UI design"
  ],
  "assumptions": [
    "A central orchestrator validates artifacts",
    "Agents emit structured JSON outputs",
    "Failure handling is explicit and stateful"
  ],
  "risks": [
    {
      "risk": "Schema drift between agents and validator",
      "impact": "high",
      "mitigation": "Version artifacts and validate on every transition"
    },
    {
      "risk": "Ambiguous ownership across handoffs",
      "impact": "medium",
      "mitigation": "Require explicit assignee and handoff packet"
    }
  ],
  "definition_of_done": [
    "All required artifacts have schemas",
    "Examples validate structurally",
    "Walkthrough covers success and failure touchpoints"
  ]
}
```

## 3) Example instance: `execution_plan`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "execution_plan",
  "task_id": "TASK-2026-07-04-001",
  "plan_id": "PLAN-001",
  "created_at": "2026-07-04T14:07:15Z",
  "created_by": "planner",
  "strategy": "Produce specification artifacts in dependency order, then validate with examples.",
  "steps": [
    {
      "step_id": "STEP-1",
      "name": "Draft lifecycle states",
      "owner_role": "architect",
      "depends_on": [],
      "deliverables": ["state_machine.yaml"]
    },
    {
      "step_id": "STEP-2",
      "name": "Define artifact schemas",
      "owner_role": "architect",
      "depends_on": ["STEP-1"],
      "deliverables": ["schema_pack.json"]
    },
    {
      "step_id": "STEP-3",
      "name": "Create example instances",
      "owner_role": "technical_writer",
      "depends_on": ["STEP-2"],
      "deliverables": ["examples.md"]
    },
    {
      "step_id": "STEP-4",
      "name": "Run end-to-end walkthrough",
      "owner_role": "operator",
      "depends_on": ["STEP-2", "STEP-3"],
      "deliverables": ["walkthrough.md"]
    }
  ],
  "checkpoints": [
    {
      "checkpoint_id": "CP-1",
      "name": "Specification completeness",
      "required_artifacts": ["task_brief", "execution_plan", "artifact_manifest"]
    },
    {
      "checkpoint_id": "CP-2",
      "name": "Validation readiness",
      "required_artifacts": ["schema_pack", "example_set", "completion_report"]
    }
  ],
  "success_metrics": [
    "No undefined lifecycle states",
    "All examples map cleanly to one schema",
    "Walkthrough is traceable from intake to completion"
  ]
}
```

## 4) Example instance: `agent_assignment`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "agent_assignment",
  "task_id": "TASK-2026-07-04-001",
  "assignment_id": "ASG-001",
  "assigned_at": "2026-07-04T14:08:03Z",
  "assigned_by": "coordinator",
  "agent": {
    "agent_id": "agent-architect-01",
    "role": "architect",
    "capabilities": ["state-modeling", "json-schema", "workflow-design"]
  },
  "responsibilities": [
    "Define canonical states",
    "Specify transitions and guards",
    "Produce schema pack compatible with control-plane validation"
  ],
  "inputs": ["task_brief", "requirements_context"],
  "outputs_required": ["execution_plan", "artifact_manifest"],
  "sla": {
    "start_by": "2026-07-04T14:10:00Z",
    "complete_by": "2026-07-04T16:00:00Z"
  },
  "escalation_path": ["coordinator", "operator"]
}
```

## 5) Example instance: `work_order`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "work_order",
  "task_id": "TASK-2026-07-04-001",
  "work_order_id": "WO-001",
  "issued_at": "2026-07-04T14:09:21Z",
  "issued_by": "coordinator",
  "target_agent_id": "agent-architect-01",
  "objective": "Produce the first-draft state machine YAML and schema pack outline.",
  "instructions": [
    "Use canonical state names only",
    "Attach guards and required artifacts to each transition",
    "Mark failure paths explicitly"
  ],
  "required_inputs": [
    {
      "name": "task_brief",
      "ref": "BRIEF-001"
    }
  ],
  "required_outputs": [
    "state_machine",
    "schema_pack_outline"
  ],
  "quality_bar": {
    "validation_required": true,
    "review_level": "peer",
    "must_include_examples": false
  }
}
```

## 6) Example instance: `artifact_manifest`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "artifact_manifest",
  "task_id": "TASK-2026-07-04-001",
  "manifest_id": "MANIFEST-001",
  "generated_at": "2026-07-04T15:10:44Z",
  "generated_by": "architect",
  "artifacts": [
    {
      "artifact_id": "ART-001",
      "name": "ai-dos-state-machine.yaml",
      "type": "state_machine",
      "version": "1.0.0",
      "status": "draft",
      "checksum": "sha256:1d2f6bb0abc123example",
      "produced_by": "agent-architect-01"
    },
    {
      "artifact_id": "ART-002",
      "name": "ai-dos-schema-pack.json",
      "type": "schema_pack",
      "version": "1.0.0",
      "status": "draft",
      "checksum": "sha256:9a73ee19def456example",
      "produced_by": "agent-architect-01"
    }
  ],
  "required_missing": ["example_set", "walkthrough"],
  "ready_for_review": true
}
```

## 7) Example instance: `tool_invocation_record`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "tool_invocation_record",
  "task_id": "TASK-2026-07-04-001",
  "invocation_id": "TOOL-001",
  "timestamp": "2026-07-04T15:12:05Z",
  "agent_id": "agent-architect-01",
  "tool_name": "schema_validator",
  "operation": "validate_pack",
  "inputs": {
    "schema_pack_ref": "ART-002",
    "mode": "strict"
  },
  "outputs": {
    "valid": true,
    "validated_schema_count": 11,
    "warnings": []
  },
  "duration_ms": 842,
  "status": "success"
}
```

## 8) Example instance: `checkpoint_review`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "checkpoint_review",
  "task_id": "TASK-2026-07-04-001",
  "review_id": "REVIEW-001",
  "checkpoint_id": "CP-1",
  "reviewed_at": "2026-07-04T15:30:17Z",
  "reviewed_by": "reviewer",
  "criteria": [
    "Lifecycle states are canonical and closed",
    "Transitions have guards",
    "Required artifacts are named explicitly"
  ],
  "findings": [
    {
      "criterion": "Transitions have guards",
      "result": "pass",
      "notes": "All forward transitions include guard conditions."
    },
    {
      "criterion": "Required artifacts are named explicitly",
      "result": "pass",
      "notes": "Artifact dependencies are machine-readable."
    }
  ],
  "decision": "approved",
  "follow_up_actions": []
}
```

## 9) Example instance: `issue_report`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "issue_report",
  "task_id": "TASK-2026-07-04-001",
  "issue_id": "ISSUE-001",
  "reported_at": "2026-07-04T15:42:11Z",
  "reported_by": "validator",
  "severity": "medium",
  "category": "schema_consistency",
  "summary": "Example set references an artifact name not present in the schema pack.",
  "details": "The example walkthrough uses 'review_packet' while the canonical schema name is 'checkpoint_review'.",
  "affected_artifacts": ["examples.md", "schema_pack.json"],
  "recommended_action": "Rename the example artifact to the canonical schema name and revalidate.",
  "status": "open"
}
```

## 10) Example instance: `handoff_packet`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "handoff_packet",
  "task_id": "TASK-2026-07-04-001",
  "handoff_id": "HANDOFF-001",
  "created_at": "2026-07-04T15:45:33Z",
  "from_agent": "agent-architect-01",
  "to_agent": "agent-technical-writer-01",
  "purpose": "Transfer validated schema context so examples and walkthrough can be authored consistently.",
  "context_summary": "State machine and schema pack are approved at CP-1; remaining work is example generation and narrative walkthrough.",
  "artifacts_included": ["ART-001", "ART-002", "REVIEW-001"],
  "open_issues": ["ISSUE-001"],
  "recipient_expectations": [
    "Produce one example per schema",
    "Use only canonical artifact names",
    "Resolve the naming issue before final completion"
  ]
}
```

## 11) Example instance: `completion_report`

```json
{
  "schema_version": "1.0.0",
  "artifact_type": "completion_report",
  "task_id": "TASK-2026-07-04-001",
  "report_id": "COMPLETE-001",
  "completed_at": "2026-07-04T16:20:49Z",
  "completed_by": "operator",
  "outcome": "success",
  "delivered_artifacts": [
    "ai-dos-state-machine.yaml",
    "ai-dos-schema-pack.json",
    "ai-dos-option-3-examples.md"
  ],
  "acceptance_results": [
    {
      "criterion": "State machine defines canonical transitions",
      "result": "met"
    },
    {
      "criterion": "Schema pack covers core orchestration artifacts",
      "result": "met"
    },
    {
      "criterion": "Examples exist for every schema",
      "result": "met"
    },
    {
      "criterion": "One end-to-end walkthrough demonstrates execution",
      "result": "met"
    }
  ],
  "known_limitations": [
    "Examples are illustrative and may need field-name alignment if canonical schemas use different naming",
    "Checksums are sample values"
  ],
  "next_recommended_actions": [
    "Validate all examples against the canonical schema pack",
    "Convert the walkthrough into automated fixture tests"
  ]
}
```

---

## End-to-end walkthrough: one task from intake to completion

This walkthrough traces a single task through the AI-DOS lifecycle and shows which artifact is produced at each point, which state transition it enables, and what failure handling looks like.

### Scenario

A product owner asks the system to formalize AI-DOS into an executable spec. The control plane must intake the request, plan the work, assign the right agent, validate intermediate outputs, handle one schema naming issue, and complete the task with accepted deliverables.

### Phase 1: Intake and normalization

The request first enters the system as a `task_intake` artifact. At this point, the control plane is in an initial state such as `RECEIVED` or `INTAKE_PENDING`. Validation checks confirm that the request has a title, goal, constraints, and acceptance criteria.

If the intake artifact is incomplete, the task cannot advance and instead transitions to an exception or clarification-needed state. In the happy path shown here, the artifact validates successfully and the control plane transitions into a clarified or scoped state.

**Artifact produced:** `task_intake`

**Transition enabled:** `RECEIVED -> SCOPED`

**Guard:** Required intake fields present and syntactically valid.

### Phase 2: Problem framing

A coordinator or planner converts the intake into a `task_brief`. This artifact sharpens the problem statement, defines what is in and out of scope, captures assumptions, and names risks and mitigations.

The control plane uses the brief as the canonical framing document. Once it validates, the task can move from scope definition into formal planning.

**Artifact produced:** `task_brief`

**Transition enabled:** `SCOPED -> PLANNED`

**Guard:** Brief references a valid `task_id`, objective set is non-empty, and definition-of-done exists.

### Phase 3: Plan creation

The planner emits an `execution_plan` that sequences the work into state machine drafting, schema definition, example creation, and walkthrough validation. Dependencies are explicit, and checkpoints identify where human or machine review is required.

The control plane now has enough structure to route work. The task enters a ready-for-assignment state.

**Artifact produced:** `execution_plan`

**Transition enabled:** `PLANNED -> READY_FOR_ASSIGNMENT`

**Guard:** Steps are well-formed, dependencies are acyclic, and checkpoints reference required artifacts.

### Phase 4: Assignment and dispatch

A coordinator creates an `agent_assignment` naming the architect agent and its responsibilities. A `work_order` is then issued with concrete instructions, required inputs, and expected outputs.

These two artifacts convert abstract planning into operational execution. Once both validate, the task transitions to active execution.

**Artifacts produced:** `agent_assignment`, `work_order`

**Transition enabled:** `READY_FOR_ASSIGNMENT -> IN_PROGRESS`

**Guard:** Assigned agent has matching capabilities, deadlines are valid, and work-order outputs align with the plan.

### Phase 5: Draft outputs and manifesting

The architect produces the state machine and schema pack, then emits an `artifact_manifest` listing the generated files, versions, checksums, and missing items. The manifest is important because it gives the control plane a machine-readable inventory of work products.

At this point, the task may stay in an execution state but becomes eligible for validation and checkpoint review.

**Artifact produced:** `artifact_manifest`

**Transition enabled:** `IN_PROGRESS -> UNDER_REVIEW`

**Guard:** Manifest references at least one produced artifact and marks review readiness truthfully.

### Phase 6: Tool-backed validation

A validator records a `tool_invocation_record` showing that the schema pack was checked in strict mode and all eleven schemas validated. This is the audit trail for automated enforcement and proves that a machine gate was actually executed rather than assumed.

The control plane can treat successful validator records as evidence that objective checks passed. Failed validator records would instead route the task back into remediation.

**Artifact produced:** `tool_invocation_record`

**Transition enabled:** `UNDER_REVIEW -> CHECKPOINT_PENDING`

**Guard:** Validation status is success and required schema counts match expectations.

### Phase 7: Checkpoint approval

A reviewer creates a `checkpoint_review` at CP-1 and approves the state machine and schema pack. This is the governance moment where the system decides whether the task can proceed to example generation and packaging.

Because the review decision is `approved`, downstream work can continue. If it were `changes_required`, the task would return to execution with specific corrective actions.

**Artifact produced:** `checkpoint_review`

**Transition enabled:** `CHECKPOINT_PENDING -> IN_PROGRESS`

**Guard:** Decision is `approved` or `approved_with_conditions`; criteria and findings are present.

### Phase 8: Exception discovery and containment

While authoring examples, the validator notices that one draft references `review_packet` instead of the canonical `checkpoint_review`. The system captures this as an `issue_report` rather than silently tolerating drift.

This is where the machine-enforced model matters. The issue prevents clean promotion to completion and forces a controlled remediation loop.

**Artifact produced:** `issue_report`

**Transition enabled:** `IN_PROGRESS -> BLOCKED`

**Guard:** Severity warrants intervention and the issue affects canonical schema consistency.

### Phase 9: Handoff and correction

To fix the inconsistency cleanly, the architect hands context to the technical writer via a `handoff_packet`. The packet includes approved artifacts, the open issue, and explicit expectations for resolution.

The technical writer updates the example set to use the canonical name, and the validator reruns its checks. Once the issue is resolved, the task leaves the blocked state and returns to active execution or final review.

**Artifact produced:** `handoff_packet`

**Transition enabled:** `BLOCKED -> IN_PROGRESS`

**Guard:** Open issue is assigned, required context is included, and the recipient role is valid for the corrective action.

### Phase 10: Final completion

After examples and walkthrough validate successfully, the operator emits a `completion_report`. This report lists delivered artifacts, evaluates each acceptance criterion, notes known limitations, and recommends next steps.

At this point, the control plane has a full audit trail from request through delivery. The task can transition into a terminal successful state.

**Artifact produced:** `completion_report`

**Transition enabled:** `IN_PROGRESS -> COMPLETED`

**Guard:** All mandatory artifacts exist, unresolved blocking issues are zero, and acceptance criteria are satisfied.

---

## Compact lifecycle trace

The same walkthrough can be summarized as a linear trace:

```text
RECEIVED
  -> task_intake validated
SCOPED
  -> task_brief validated
PLANNED
  -> execution_plan validated
READY_FOR_ASSIGNMENT
  -> agent_assignment + work_order validated
IN_PROGRESS
  -> artifact_manifest created
UNDER_REVIEW
  -> tool_invocation_record shows schema validation success
CHECKPOINT_PENDING
  -> checkpoint_review approved
IN_PROGRESS
  -> issue_report created for naming mismatch
BLOCKED
  -> handoff_packet transfers corrective context
IN_PROGRESS
  -> corrected examples validated
COMPLETED
  -> completion_report accepted
```

---

## How to use these examples operationally

These examples are useful in three different ways. First, they are good human-readable references for anyone authoring artifacts manually. Second, they can become machine fixtures in a validator test suite, where each example is run against the corresponding JSON Schema. Third, the walkthrough can be turned into a scenario-based integration test for the control plane, asserting that each artifact unlocks exactly the intended transition and that invalid artifacts route into explicit failure states.

The most important implementation step after this is alignment. If your canonical schema pack uses different property names, enum values, or artifact identifiers, update these examples so they become exact validation fixtures rather than illustrative references.

## Recommended next step

The strongest next move is to add a fixture directory with one JSON file per artifact type, then run them automatically through the schema validator in CI. That turns Option 3 from documentation into an executable regression harness.
