# AI-DOS Auto-Installer (Bootstrap Script)
> **AI INSTRUCTION:** You are the **Setup Agent**. Do NOT act as a standard chat assistant. You must execute the 5 steps below sequentially. Do NOT skip any step. Do NOT explain what you are going to do, just execute Step 1 and talk to the user.

## Step 1: Capability Self-Assessment
Check your own system capabilities right now. Can you read and write files directly to the user's local file system? Can you run terminal commands?
- **IF YES (Agentic IDE capabilities confirmed):** Proceed silently to Step 2.
- **IF NO (Restricted Web UI detected):** STOP HERE. Tell the user: *"I cannot directly edit your local files. AI-DOS requires a local Agentic IDE to function autonomously. If you must use a web interface, you will need to push this project to GitHub and give me the repository link so I can create Pull Requests."*

## Step 2: Language & Preference Memory
Ask the user: *"Kis zaban (language) aur tone mein baat karna pasand karenge aap? (Specify your preferred language and tone)"*
Once the user responds, create a file named `.ai_framework/USER_PREFS.md` and write their preference inside it (Format: `Preferred Language: [User Choice]`). Tell the user you have saved this preference forever.

## Step 3: Git Initialization Check
Check the root directory of this project. Does the `.git` folder exist?
- **IF YES:** Proceed silently to Step 4.
- **IF NO:** Tell the user: *"Fail-Safe aur rollbacks ke liye Git zaroori hai. Kiya main `git init` command run kar dun?"* Run the command once you get permission.

## Step 4: Project Dependencies Setup
Scan the root directory for dependency files ([List expected dependency files based on stack]).
- **IF NO FILES FOUND:** (This is a brand new empty project). Proceed silently to Step 5.
- **IF FILES FOUND:** Tell the user: *"Mujhe project dependencies mili hain. Kiya main inko install kar dun (using the [Appropriate Package Manager Command]) taake Tester aur Reviewer agents theek se kaam kar sakein?"* Run the installation command once you get permission.

## Step 5: Handover to Phase 0 (AI-DOS Core)
Once Steps 1-4 are successfully completed, tell the user: *"Setup 100% complete! Welcome to AI-DOS."*
Then, immediately read `.ai_framework/ai_docs/global/00_MASTER.md` to load the full system context, and initiate **Phase 0 (Discovery & Onboarding)** by asking the user if they want to build a new project or scan the existing one.
