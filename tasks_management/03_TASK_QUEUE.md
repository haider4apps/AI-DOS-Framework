# Task Queue (Priority System)
> **Purpose:** When multiple tasks are requested, this file acts as the task backlog. The Task Orchestrator picks tasks from this queue based on priority.
> **Maintained By:** Project Manager (adds tasks) & Task Orchestrator (picks and updates status).

## Priority Levels
- 🔴 **CRITICAL:** Emergency Bugs, Production Crashes (Process Immediately)
- 🟠 **HIGH:** Large Features, Architecture Changes (Process Next)
- 🟡 **MEDIUM:** Medium Features, Small Tasks (Process In Order)
- 🟢 **LOW:** Refactors, Tiny Tasks, Nice-to-haves (Process When Free)

## Active Queue

| Queue # | Task ID | Priority | Task Description | Status | Assigned Pipeline |
|---------|---------|----------|-----------------|--------|------------------|
| 1 | TASK_XXX | 🔴 CRITICAL | [Description] | ⏳ Waiting | Type 6: Emergency |
| 2 | TASK_XXX | 🟠 HIGH | [Description] | ⏳ Waiting | Type 4: Large |
| 3 | TASK_XXX | 🟡 MEDIUM | [Description] | ⏳ Waiting | Type 3: Medium |

## Status Legend
- ⏳ Waiting (In Queue)
- 🔄 In Progress (Currently Executing)
- ✅ Completed
- ❌ Rejected / Rolled Back
- ⏸️ Paused (Waiting for Human Approval)
