---
description: Starts incremental code development using Local Context Manager and Coder agents
argument-hint: 
---
## Context
This command starts the incremental code development process by initializing the local development session and beginning implementation of the first TODO item from the current feature context.

## Task
Use the Task tool to launch the local-context-manager agent with coordination with the coder agent:

**Primary Agent**: local-context-manager
**Supporting Agent**: coder

**Agent Task**: Initialize incremental development session
**Instructions**:

**Local Context Manager Tasks**:
1. Identify current feature branch and load feature context from `.claude/features/[branch-name]/`
2. Validate that feature context exists and is complete
3. Load TODO list from `ctx-todo.md` and identify first pending TODO item
4. Initialize local development session:
   - Create/update `.claude/local/local-context.md` with current feature and TODO
   - Create/update `.claude/local/active-todo.md` with detailed TODO information
   - Initialize `.claude/local/session-log.md` for tracking development progress
5. Mark first TODO as "in_progress" in the feature TODO list
6. Coordinate with Coder agent to implement the first TODO

**Coder Agent Tasks**:
1. Read project context from `.claude/project/` for architecture and functional guidance
2. Read feature context for specific requirements and constraints
3. Read current TODO item details and implementation requirements
4. Analyze existing codebase to understand patterns and conventions
5. Implement the TODO item following project architecture and conventions
6. Run tests to ensure implementation doesn't break existing functionality
7. Create clean, atomic commits for the implemented changes
8. Report implementation status back to Local Context Manager

**Development Flow**:
- Present implemented changes to user for review
- Wait for user feedback (`/icm-continue` or `/icm-redo`)
- Update context and progress tracking
- Provide clear status of current development session

**Error Handling**:
- If no feature context exists, guide user to use `/icm-pull [branch-name]` first
- If TODO list is empty, inform user that feature planning may be incomplete
- If implementation fails, provide clear error messages and suggested next steps

The goal is to start a structured, incremental development session with clear progress tracking and user review cycles.