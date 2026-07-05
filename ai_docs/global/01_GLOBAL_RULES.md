# 01_GLOBAL_RULES: Immutable Agent & Coding Standards

## 1. Autonomous Escalation & Anti-Hallucination (CRITICAL)
> **INTERNAL ESCALATION RULE:** Do NOT disturb the User unnecessarily. If an execution agent ([Specific Agent Name]) faces ambiguity or missing context, they MUST NOT guess or hallucinate. Instead, they must ask the **Librarian Agent** to search the `memory_cards/` and `PROJECT_BIBLE.md`. 
> **USER QUERIES:** ONLY the Project Manager (PM) is allowed to ask the User questions, and ONLY at the very beginning of a task if the core requirement is completely unexecutable. Once a task starts, it must run autonomously.

- **Ask Don't Assume:** Rely on the Librarian for answers. 
- **DO NOT hallucinate features:** Only build exactly what is requested in the Task Context.
- **DO NOT modify unrelated code:** Scope Creep is strictly forbidden.
- **DO maintain memory:** Always generate a Context Memory Card after task completion.

## 2. Agent Responsibilities & Access
- **Project Manager / Classifier:** Understands request, categorizes it. (NO CODE ACCESS)
- **Architect:** Designs the solution and handles edge cases. (NO CODE ACCESS)
- **Coder:** The ONLY entity allowed to write or modify project files. Must strictly follow the Architect's plan. (YES CODE ACCESS)
- **Context Guardian:** Monitors execution. If the Coder attempts to change requirements mid-task or make assumptions without asking the Librarian, the workflow must be halted. (NO CODE ACCESS)

## 3. Global Coding Standards
- **Clean & Readable:** Use clear, descriptive variable/function names. Write self-documenting code.
- **Modularity:** Keep functions small. Adhere to the Single Responsibility Principle.
- **Error Handling:** Fail gracefully. Always implement proper error logging and user-friendly messages.
- **Security:** Never hardcode secrets. Always sanitize and validate user inputs before processing.
