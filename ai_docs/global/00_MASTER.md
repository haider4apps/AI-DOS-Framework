# 00_MASTER: AI-DOS 4.0 Enterprise Control Plane

## 1. System Overview
Welcome to AI-DOS 4.0. You are an agent operating within a strict, machine-enforced orchestration system. 
**CRITICAL RULE:** Agents may *propose* actions by outputting JSON Schema-validated artifacts, but ONLY the Orchestrator may transition task state via the `state_machine.yaml`. 
Markdown prose is for human policy; runtime state is driven exclusively by JSON/YAML control data.

## 2. Core Directories
- **`control_plane/`**: Contains the `state_machine.yaml` (the absolute source of truth for task flow) and documentation.
- **`schemas/`**: Contains the JSON schemas every agent must strictly adhere to when generating outputs.
- **`fixtures/`**: Contains example outputs and negative tests.
- **`sub_agents/`**: Contains the Markdown persona and instruction files for all agents.

## 3. System Lifecycle & Phases

### Phase 0: Business Feasibility & Discovery (Initial Gate)
> Tasks begin in the `FEASIBILITY_PENDING` state.
1. The **Business Strategist** conducts market research, competitor mapping, and defines the UVP.
2. The Strategist outputs intermediate schema artifacts (`market_scan`, `competitor_map`, `uvp_canvas`).
3. The Strategist outputs the canonical `business_feasibility_report` artifact containing a Go/No-Go decision.
4. If approved, the Orchestrator moves the state to `DRAFT` (Intake).
5. The **Project Manager** converts the approved feasibility into a formal `task_intake` and `task_brief`.

### Phase 1: Execution Lifecycle
> A task flows through strict FSM states enforced by the Orchestrator. No states may be skipped.
1. **Intake:** `DRAFT` -> `CLASSIFIED` -> `CONTEXT_PENDING` -> `CONTEXT_RESOLVED`
2. **Planning:** `PLAN_READY` -> `APPROVAL_REQUIRED` (if Medium/High Risk)
3. **Execution & Locking:** `LOCK_PENDING` -> `LOCKED` (acquiring ExecutionLease) -> `IMPLEMENTING`
4. **Validation:** `REVIEW_PENDING` -> `SECURITY_PENDING` -> `TEST_PENDING` -> `QC_PENDING`
5. **Completion:** `READY_TO_MERGE` -> `MERGED` -> `DOCS_PENDING` -> `MEMORY_PENDING` -> `RELEASE_PENDING` -> `COMPLETED`

## 4. Agent Output Requirements
Agents no longer output freeform Markdown reports for execution handoffs. 
- The Architect must output a valid `PlanArtifact`.
- The Coder must output a valid `ImplementationReport`.
- Reviewers and Testers must output valid `FindingReport` and `TestExecutionReport` artifacts.

## 5. Lock & Retry Invariants
- **Locks:** No agent may enter `IMPLEMENTING` without an active `ExecutionLease`.
- **Retries:** Retries are strictly budgeted per defect family. Exceeding the budget forces the task into `QUARANTINED` for human review.
