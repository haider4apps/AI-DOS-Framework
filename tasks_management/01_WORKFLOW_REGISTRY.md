# Workflow Registry (Task Types & Pipelines)
> **ATTENTION TASK CLASSIFIER & ORCHESTRATOR:** You must strictly follow these pipelines. Do not skip agents unless explicitly allowed here.
> **UNIVERSAL RULE:** Git Sandboxing is MANDATORY for ALL task types (including Tiny). The Orchestrator must create a sandbox branch before the Coder starts.
> **UNIVERSAL RULE:** Conflict Detector must run AFTER sandbox creation and BEFORE the Coder starts on ALL task types.

---

## Phase 0: Discovery & Onboarding (Runs ONCE per project)

### Mode A: New Project (From Scratch)
- **Pipeline:** `Discovery Agent` ➔ `Business Q&A with User` ➔ `Market Analysis` ➔ `Feature Brainstorming with User` ➔ `Auto-Fill PROJECT_BIBLE.md` ➔ `Auto-Fill ARCHITECTURE.md` ➔ `Create Feature Docs` ➔ **[USER REVIEW & APPROVAL]** ➔ `Phase 0 Complete` ➔ `Hand to Project Manager`

### Mode B: Existing Project (Half-Built)
- **Pipeline:** `Codebase Scanner (Full Scan)` ➔ `Tech Stack Detection` ➔ `Module Completion Analysis` ➔ `Gap Report` ➔ `Discovery Agent (User Q&A for gaps)` ➔ `Auto-Fill PROJECT_BIBLE.md` ➔ `Auto-Fill ARCHITECTURE.md` ➔ `Create Feature Docs` ➔ **[USER REVIEW & APPROVAL]** ➔ `Phase 0 Complete` ➔ `Hand to Project Manager`

---

## Phase 1: Development (Runs for every task)

### 🟢 Type 1: Tiny Task (Color, Text, Icon change)
- **Required Docs:** `01_GLOBAL_RULES.md`, `[Relevant Feature Doc].md`
- **Pipeline:** `Task Classifier` ➔ `Librarian` ➔ `Orchestrator (Create Sandbox)` ➔ `Conflict Detector` ➔ `Coder` ➔ `Reviewer` ➔ `Orchestrator (Merge + Metrics Update + User Status)` ➔ `Done`
- **Note:** Memory Card generation is optional. Security Auditor is skipped unless touching auth/payment code.

### 🔵 Type 2: Small Task (New field, API param, Export button)
- **Required Docs:** `01_GLOBAL_RULES.md`, `[Relevant Feature Doc].md`
- **Pipeline:** `Task Classifier` ➔ `Librarian` ➔ `Architect` ➔ `Orchestrator (Create Sandbox)` ➔ `Conflict Detector` ➔ `Coder` ➔ `Reviewer` ➔ `Documentation` ➔ `Memory Agent` ➔ `Orchestrator (Merge + Metrics + Status)` ➔ `Done`
- **Note:** Security Auditor is skipped unless touching auth/payment code.

### 🟡 Type 3: Medium Feature (OTP Login, Theme Support)
- **Required Docs:** `02_PROJECT_BIBLE.md`, `03_ARCHITECTURE.md`, `[Relevant Feature Doc].md`
- **Pipeline:** `Task Classifier` ➔ `Librarian` ➔ `Architect` ➔ **[HUMAN APPROVAL]** ➔ `Orchestrator (Create Sandbox)` ➔ `Conflict Detector` ➔ `Coder` + `Context Guardian (Parallel Monitor)` ➔ `Reviewer` ➔ `Security Auditor` ➔ `Tester` ➔ `Documentation` ➔ `Memory Agent` ➔ `Quality Controller` ➔ `Orchestrator (Merge + Metrics + Status)` ➔ `Done`

### 🔴 Type 4: Large Feature (Payment Gateway, Chat System)
- **Required Docs:** All Core Docs (`00_MASTER`, `01_GLOBAL_RULES`, `02_PROJECT_BIBLE`, `03_ARCHITECTURE`) + All relevant Feature Docs.
- **Pipeline:** `Task Classifier` ➔ `Librarian` ➔ `Architect (Full Impact Analysis)` ➔ **[HUMAN APPROVAL]** ➔ `Orchestrator (Create Sandbox)` ➔ `Conflict Detector` ➔ `Coder` + `Context Guardian (Parallel Monitor)` ➔ `Reviewer` ➔ `Security Auditor` ➔ `Tester (Full Test Suite)` ➔ `Documentation` ➔ `Memory Agent` ➔ `Quality Controller` ➔ `Release Manager` ➔ `Orchestrator (Merge + Metrics + Status)` ➔ `Done`

### 🟣 Type 5: Architecture Change (Description: [Old Tech] ➔ [New Tech])
- **Required Docs:** `03_ARCHITECTURE.md`, `02_PROJECT_BIBLE.md`, `01_GLOBAL_RULES.md`, All related Feature Docs & Memory Cards.
- **Pipeline:** `Task Classifier` ➔ `Librarian (Load ALL context)` ➔ `Architect (Full Impact + Rollback Strategy)` ➔ **[HUMAN APPROVAL - MANDATORY]** ➔ `Orchestrator (Create Sandbox)` ➔ `Conflict Detector` ➔ `Coder` + `Context Guardian (Parallel Monitor)` ➔ `Reviewer` ➔ `Security Auditor` ➔ `Tester (Full Regression Suite)` ➔ `Documentation (Update Architecture.md)` ➔ `Memory Agent` ➔ `Quality Controller` ➔ `Release Manager` ➔ **[HUMAN FINAL REVIEW]** ➔ `Orchestrator (Merge + Metrics + Status)` ➔ `Done`
- **Special Rule:** Architecture changes require TWO human approvals: one before coding and one before final merge.

### ⚫ Type 6: Emergency Bug (Production Crash, Security)
- **Required Docs:** Current Task Context, Active Diff, Error Logs.
- **Pipeline:** `Task Classifier` ➔ `Librarian` ➔ `Orchestrator (Create Sandbox)` ➔ `Conflict Detector` ➔ `Coder` ➔ `Reviewer` ➔ `Security Auditor` ➔ `Memory Agent (Record the Emergency Fix)` ➔ `Documentation (Update Changelog)` ➔ `Orchestrator (Merge + Metrics + Status)` ➔ `Done`
- **Special Rule:** Skips Roadmap and full QC. But Memory Card, Documentation, and Security Audit are MANDATORY.

### ⚪ Type 7: Refactor (Clean-up, Performance)
- **Required Docs:** `01_GLOBAL_RULES.md`, Related Source Files.
- **Pipeline:** `Task Classifier` ➔ `Librarian` ➔ `Orchestrator (Create Sandbox)` ➔ `Conflict Detector` ➔ `Coder` ➔ `Reviewer` ➔ `Tester (Regression Only)` ➔ `Memory Agent` ➔ `Orchestrator (Merge + Metrics + Status)` ➔ `Done`
- **Strict Rule:** Absolutely NO functional changes allowed. Tests must prove zero behavior difference.
