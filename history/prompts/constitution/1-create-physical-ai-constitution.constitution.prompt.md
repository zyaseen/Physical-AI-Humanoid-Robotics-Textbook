---
id: 1
title: Create-Physical-AI-Constitution
stage: constitution
date: 2025-12-10
surface: agent
model: gpt-4
feature: none
branch: main
user: dell
command: /sp.constitution
labels: [constitution,specification,physical-ai]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
 - .specify/memory/constitution.md
tests:
 - none
---

## Prompt

```
$ARGUMENTS
```

You **MUST** consider the user input before proceeding (if not empty).

## Outline

You are updating the project constitution at `.specify/memory/constitution.md`. This file is a TEMPLATE containing placeholder tokens in square brackets (e.g. `[PROJECT_NAME]`, `[PRINCIPLE_1_NAME]`). Your job is to (a) collect/derive concrete values, (b) fill the template precisely, and (c) propagate any amendments across dependent artifacts.

Follow this execution flow:

1. Load the existing constitution template at `.specify/memory/constitution.md`.
   - Identify every placeholder token of the form `[ALL_CAPS_IDENTIFIER]`.
   **IMPORTANT**: The user might require less or more principles than the ones used in the template. If a number is specified, respect that - follow the general template. You will update the doc accordingly.

2. Collect/derive values for placeholders:
   - If user input (conversation) supplies a value, use it.
   - Otherwise infer from existing repo context (README, docs, prior constitution versions if embedded).
   - For governance dates: `RATIFICATION_DATE` is the original adoption date (if unknown ask or mark TODO), `LAST_AMENDED_DATE` is today if changes are made, otherwise keep previous.
   - `CONSTITUTION_VERSION` must increment according to semantic versioning rules:
     - MAJOR: Backward incompatible governance/principle removals or redefinitions.
     - MINOR: New principle/section added or materially expanded guidance.
     - PATCH: Clarifications, wording, typo fixes, non-semantic refinements.
   - If version bump type ambiguous, propose reasoning before finalizing.

3. Draft the updated constitution content:
   - Replace every placeholder with concrete text (no bracketed tokens left except intentionally retained template slots that the project has chosen not to define yet—explicitly justify any left).
   - Preserve heading hierarchy and comments can be removed once replaced unless they still add clarifying guidance.
   - Ensure each Principle section: succinct name line, paragraph (or bullet list) capturing non‑negotiable rules, explicit rationale if not obvious.
   - Ensure Governance section lists amendment procedure, versioning policy, and compliance review expectations.

4. Consistency propagation checklist (convert prior checklist into active validations):
   - Read `.specify/templates/plan-template.md` and ensure any "Constitution Check" or rules align with updated principles.
   - Read `.specify/templates/spec-template.md` for scope/requirements alignment—update if constitution adds/removes mandatory sections or constraints.
   - Read `.specify/templates/tasks-template.md` and ensure task categorization reflects new or removed principle-driven task types (e.g., observability, versioning, testing discipline).
   - Read each command file in `.specify/templates/commands/*.md` (including this one) to verify no outdated references (agent-specific names like CLAUDE only) remain when generic guidance is required.
   - Read any runtime guidance docs (e.g., `README.md`, `docs/quickstart.md`, or agent-specific guidance files if present). Update references to principles changed.

5. Produce a Sync Impact Report (prepend as an HTML comment at top of the constitution file after update):
   - Version change: old → new
   - List of modified principles (old title → new title if renamed)
   - Added sections
   - Removed sections
   - Templates requiring updates (✅ updated / ⚠ pending) with file paths
   - Follow-up TODOs if any placeholders intentionally deferred.

6. Validation before final output:
   - No remaining unexplained bracket tokens.
   - Version line matches report.
   - Dates ISO format YYYY-MM-DD.
   - Principles are declarative, testable, and free of vague language ("should" → replace with MUST/SHOULD rationale where appropriate).

7. Write the completed constitution back to `.specify/memory/constitution.md` (overwrite).

8. Output a final summary to the user with:
   - New version and bump rationale.
   - Any files flagged for manual follow-up.
   - Suggested commit message (e.g., `docs: amend constitution to vX.Y.Z (principle additions + governance update)`).

Formatting & Style Requirements:

- Use Markdown headings exactly as in the template (do not demote/promote levels).
- Wrap long rationale lines to keep readability (<100 chars ideally) but do not hard enforce with awkward breaks.
- Keep a single blank line between sections.
- Avoid trailing whitespace.

If the user supplies partial updates (e.g., only one principle revision), still perform validation and version decision steps.

If critical info missing (e.g., ratification date truly unknown), insert `TODO(<FIELD_NAME>): explanation` and include in the Sync Impact Report under deferred items.

Do not create a new template; always operate on the existing `.specify/memory/constitution.md` file.

---

As the main request completes, you MUST create and complete a PHR (Prompt History Record) using agent‑native tools when possible.

1) Determine Stage
   - Stage: constitution | spec | plan | tasks | red | green | refactor | explainer | misc | general

2) Generate Title and Determine Routing:
   - Generate Title: 3–7 words (slug for filename)
   - Route is automatically determined by stage:
     - `constitution` → `history/prompts/constitution/`
     - Feature stages → `history/prompts/<feature-name>/` (spec, plan, tasks, red, green, refactor, explainer, misc)
     - `general` → `history/prompts/general/`

3) Create and Fill PHR (Shell first; fallback agent‑native)
   - Run: `.specify/scripts/bash/create-phr.sh --title "<title>" --stage <stage> [--feature <name>] --json`
   - Open the file and fill remaining placeholders (YAML + body), embedding full PROMPT_TEXT (verbatim) and concise RESPONSE_TEXT.
   - If the script fails:
     - Read `.specify/templates/phr-template.prompt.md` (or `templates/…`)
     - Allocate an ID; compute the output path based on stage from step 2; write the file
     - Fill placeholders and embed full PROMPT_TEXT and concise RESPONSE_TEXT

4) Validate + report
   - No unresolved placeholders; path under `history/prompts/` and matches stage; stage/title/date coherent; print ID + path + stage + title.
   - On failure: warn, don't block. Skip only for `/sp.phr`.


/sp.constitution /sp.constitution

Project Name: Physical AI & Humanoid Robotics — Essentials

Purpose:
Create a short, clean, professional AI-Native textbook based on the Physical AI & Humanoid Robotics course. 
The book must serve as a fast, simple, high-quality learning resource built with a modern Docusaurus UI 
and a fully integrated free-tier RAG chatbot.

Scope:
- 6 short chapters:
  1. Introduction to Physical AI  
  2. Basics of Humanoid Robotics  
  3. ROS 2 Fundamentals  
  4. Digital Twin Simulation (Gazebo + Isaac)  
  5. Vision-Language-Action Systems  
  6. Capstone: Simple AI-Robot Pipeline  
- Clean UI
- Free-tier friendly
- Lightweight embeddings

Core Principles:
- Simplicity  
- Accuracy  
- Minimalism  
- Fast builds  
- Free-tier architecture
- RAG answers ONLY from book text

Key Features:
- Docusaurus textbook  
- RAG chatbot (Qdrant + Neon + FastAPI)  
- Select-text → Ask AI  
- Optional Urdu / Personalize features

Constraints:
- No heavy GPU usage  
- Minimal embeddings  

Success Criteria:
- Build success  
- Accurate chatbot  
- Clean UI  
- Smooth GitHub Pages deployment  

Generate full constitution./sp.constitution

Project Name: Physical AI & Humanoid Robotics — Essentials

Purpose:
Create a short, clean, professional AI-Native textbook based on the Physical AI & Humanoid Robotics course. 
The book must serve as a fast, simple, high-quality learning resource built with a modern Docusaurus UI 
and a fully integrated free-tier RAG chatbot.

Scope:
- 6 short chapters:
  1. Introduction to Physical AI  
  2. Basics of Humanoid Robotics  
  3. ROS 2 Fundamentals  
  4. Digital Twin Simulation (Gazebo + Isaac)  
  5. Vision-Language-Action Systems  
  6. Capstone: Simple AI-Robot Pipeline  
- Clean UI
- Free-tier friendly
- Lightweight embeddings

Core Principles:
- Simplicity  
- Accuracy  
- Minimalism  
- Fast builds  
- Free-tier architecture
- RAG answers ONLY from book text

Key Features:
- Docusaurus textbook  
- RAG chatbot (Qdrant + Neon + FastAPI)  
- Select-text → Ask AI  
- Optional Urdu / Personalize features

Constraints:
- No heavy GPU usage  
- Minimal embeddings  

Success Criteria:
- Build success  
- Accurate chatbot  
- Clean UI  
- Smooth GitHub Pages deployment  

Generate full constitution.
```

## Response snapshot

The Physical AI & Humanoid Robotics textbook constitution has been successfully created with the following details:

- **New Version**: 1.0.0
- **Version Bump Rationale**: This is the initial version of the constitution for the Physical AI & Humanoid Robotics textbook project, implementing all six core principles and establishing governance guidelines. Following semantic versioning, this initial release is designated as 1.0.0.

- **Files Flagged for Manual Follow-up**: Several template files will need updates to align with the new constitution:
  - `.specify/templates/plan-template.md`
  - `.specify/templates/spec-template.md` 
  - `.specify/templates/tasks-template.md`
  - Any command files in `.specify/templates/commands/`
  - `README.md` (if created later)

- **Suggested Commit Message**: `docs: add constitution for Physical AI & Humanoid Robotics textbook v1.0.0`

The constitution incorporates all the core principles you specified (Simplicity, Accuracy, Minimalism, Fast builds, Free-tier architecture, and RAG answers only from book text) and establishes constraints and governance for the project.

## Outcome

- ✅ Impact: Created complete project constitution with 6 core principles
- 🧪 Tests: No tests needed for this documentation task
- 📁 Files: .specify/memory/constitution.md created with all required content
- 🔁 Next prompts: None needed - task completed
- 🧠 Reflection: The constitution successfully incorporates all specified project requirements and principles

## Evaluation notes (flywheel)

- Failure modes observed: none
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A