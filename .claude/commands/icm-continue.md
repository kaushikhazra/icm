---
description: Continues to next TODO item after user approval of current implementation
argument-hint: 
---
## Context
This command continues the incremental development process by marking the current TODO as complete and moving to the next TODO item in the feature development cycle.

## Task
Use the Task tool to launch the local-context-manager agent with coordination with the coder agent:

**Primary Agent**: local-context-manager
**Supporting Agent**: coder

**Agent Task**: Continue incremental development to next TODO
**Instructions**:

**Local Context Manager Tasks**:
1. Validate that there is an active development session in progress
2. Mark current TODO as "completed" in both local and feature context:
   - Update `.claude/features/[branch-name]/ctx-todo.md`
   - Update `.claude/local/active-todo.md`
3. Create checkpoint commit with current changes using descriptive commit message
4. Update session log with completion details and timestamp
5. Identify next pending TODO item from the feature TODO list
6. If next TODO exists:
   - Update local context with next TODO information
   - Mark next TODO as "in_progress"
   - Coordinate with Coder agent to implement next TODO
7. If no more TODOs exist:
   - Mark feature as ready for review
   - Suggest user run `/icm-review` to prepare for manual review
   - Update session status to indicate completion

**Coder Agent Tasks** (if next TODO exists):
1. Read updated TODO information and requirements
2. Analyze any changes in context or dependencies from previous TODO
3. Implement the next TODO item following established patterns
4. Run tests to ensure continued functionality
5. Create atomic commits for the new implementation
6. Report implementation status back to Local Context Manager

**Progress Tracking**:
- Update completion percentage in local context
- Log development milestones in session history
- Maintain clear audit trail of implemented changes

**User Interaction**:
- Present next TODO implementation for review (if applicable)
- Provide progress summary and remaining work
- Wait for next user feedback cycle

**Completion Handling**:
- If all TODOs are complete, prepare feature for review phase
- Update feature context with implementation status
- Provide summary of all completed work

The goal is to maintain smooth incremental development flow with proper progress tracking and user visibility.