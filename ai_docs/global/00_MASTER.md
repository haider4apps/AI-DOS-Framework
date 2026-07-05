# 00_MASTER: AI-DOS Entry Point & System Core

## 1. System Overview
Welcome to AI-DOS (Agentic Operating System). You are an agent operating within a strictly controlled, multi-agent ecosystem. This file is the global entry point. Your memory is limited by design to maintain focus, reduce latency, and prevent context pollution.

## 2. Document Hierarchy (The 5-Layer Context)
You must load context in this order, depending on the Task Type:
1. **User Preferences (Permanent):** `USER_PREFS.md` (Language & Tone - ALWAYS LOAD FIRST)
2. **Global Rules (Permanent):** `global/01_GLOBAL_RULES.md` (Always applies)
3. **Project Context:** `project_specific/02_PROJECT_BIBLE.md` & `03_ARCHITECTURE.md`
4. **Feature Context:** Individual module docs in `project_specific/features/` (Format: `[module_name].md`)
5. **Task Context:** `tasks_management/04_TASK_CONTEXT.md`

## 3. System Phases
AI-DOS operates in 2 major phases:

### Phase 0: Discovery & Onboarding (Runs ONCE per project)
> This phase sets up the project's brain BEFORE any code is written.

- **For NEW Projects:**
  1. The **Discovery Agent** conducts interactive brainstorming with the user (Business logic, Market analysis, Feature planning).
  2. The Discovery Agent auto-fills `02_PROJECT_BIBLE.md`, `03_ARCHITECTURE.md`, and creates feature docs in `features/`.
  3. User reviews and approves all docs.
  4. Phase 0 complete. Hand control to Phase 1.

- **For EXISTING Projects:**
  1. The **Codebase Scanner** scans the entire project directory (tech stack, modules, completion status).
  2. The Scanner generates a Gap Report of unclear/incomplete areas.
  3. The **Discovery Agent** asks the user targeted questions to fill gaps.
  4. Docs are auto-filled from scan results + user answers.
  5. User reviews and approves all docs.
  6. Phase 0 complete. Hand control to Phase 1.

### Phase 1: Development (Runs for every task)
> This is the standard AI-DOS development workflow.
> Refer to `tasks_management/01_WORKFLOW_REGISTRY.md` for the 7 task type pipelines.

## 4. Agent Roster (Full Team — 16 Agents)
The following agents operate in this system. Refer to `sub_agents/` folder for each agent's detailed prompt.

**Phase 0 Agents (Discovery & Onboarding):**
1. **Discovery Agent (Brainstormer):** Interactive Q&A, market analysis, feature brainstorming, auto-fills project docs.
2. **Codebase Scanner:** Scans existing projects. Detects tech stack, module completion, and gaps. Read-only.

**Phase 1 Agents — Planning & Routing Layer:**
3. **Project Manager & Task Classifier:** Classifies task type, assigns Task ID, routes workflow.
4. **Librarian:** Retrieves ONLY the required context (docs + memory cards + feature docs).
5. **Architect:** Designs the implementation plan and performs impact analysis.
6. **Task Orchestrator:** Manages Git Sandboxing, pipeline routing, Feedback Loops, Hard Rollbacks, Task Queue, Agent Metrics, and User Status Updates.

**Phase 1 Agents — Execution & Quality Layer:**
7. **Coder:** The ONLY agent with code write access. Executes the Architect's plan.
8. **Context Guardian:** Watchdog. Monitors execution for Scope Creep and Hallucination. Can halt the workflow.
9. **Reviewer:** Inspects code quality and generates structured Fix Reports.
10. **Tester:** Designs test cases and validation checklists.
11. **Conflict Detector:** Checks for file conflicts between parallel sandbox branches before coding starts.
12. **Security Auditor:** Dedicated security vulnerability scanner. Runs after Reviewer on Medium+ tasks.

**Phase 1 Agents — Governance & Memory Layer:**
13. **Documentation Agent:** Keeps all `.ai_framework` docs synced.
14. **Context Memory Agent:** Generates Memory Cards after every task.
15. **Release Manager:** Compiles release notes.
16. **Quality Controller:** Final gatekeeper. Issues PASS, Fix Report, or Fatal Reject.

## 5. Task ID Convention
All tasks MUST be assigned a unique, auto-incrementing ID in the format: `TASK_001`, `TASK_002`, `TASK_003`, etc. The Project Manager is responsible for assigning the next available ID at the start of each new task. Memory Cards, Changelogs, and Queue entries must reference this ID.

## 6. Operational Files Reference
- **Task Queue:** `tasks_management/03_TASK_QUEUE.md` — Priority-based task backlog.
- **Agent Metrics:** `tasks_management/02_AGENT_METRICS.md` — Performance tracking per agent.
- **Memory Cards:** `tasks_management/memory_cards/` — Surgical context history per task.

## 7. Standard Workflow Execution Rule (Phase 1)
Before executing ANY task, the system MUST:
1. The **Project Manager** assigns a Task ID and classifies the **Task Type** (Type 1 to Type 7).
2. The **Librarian** loads ONLY the required docs (including relevant Feature Docs from `features/`).
3. The **Task Orchestrator** creates a Git Sandbox branch (Format: `[TASK_ID]_sandbox`).
4. The **Conflict Detector** verifies no file conflicts with other active sandboxes.
5. If a task requires human approval (Medium, Large, Architecture changes), STOP and present the plan to the user. Enter **Discussion Mode** until approval is received.
6. Execute via the Coder. The **Context Guardian** monitors execution in parallel.
7. Pass through Reviewer → Security Auditor (if applicable) → Tester (if applicable) → Quality Controller.
8. On QC PASS, the Orchestrator merges the sandbox branch and updates **Agent Metrics**.
9. The **Context Memory Agent** creates a Memory Card.
10. The Orchestrator sends a **User Status Update** confirming task completion.
