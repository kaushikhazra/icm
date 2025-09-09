---
description: Creates or switches to feature branch and initializes feature context
argument-hint: [branch-name]
---
## Context
This command creates or switches to a feature branch and initializes the feature context using the Feature Context Manager and Git Manager agents. This sets up the development environment for working on a specific feature or story.

## Task
Use the Task tool to launch multiple agents in coordination:

**Primary Agent**: feature-context-manager
**Supporting Agent**: git-manager

**Agent Task**: Initialize feature development environment
**Branch Name**: $ARGUMENTS
**Instructions**:

**Git Manager Tasks**:
1. Validate the provided branch name follows project conventions
2. Check if branch exists locally or remotely
3. If branch doesn't exist, create new feature branch from main/master
4. If branch exists, switch to it safely (stash uncommitted changes if needed)
5. Update local context with current branch information
6. Ensure working directory is clean and ready for development

**Feature Context Manager Tasks**:
1. Create feature directory structure at `.claude/features/[branch-name]/`
2. If GitLab integration is available:
   - Fetch associated issue/story from GitLab using branch name
   - Parse issue description, acceptance criteria, and requirements
   - Extract architectural considerations from issue labels/descriptions
3. If no GitLab integration, prompt user to provide feature requirements
4. Create comprehensive feature context files:
   - `ctx-function.md`: Feature requirements and acceptance criteria
   - `ctx-arch.md`: Feature-specific architectural considerations
   - `ctx-todo.md`: Breakdown of feature into implementable TODO items
   - `metadata.json`: Feature metadata and source information
5. Validate context completeness and flag any missing information
6. Provide summary of created feature context

**Coordination Requirements**:
- Git Manager should complete branch operations before Feature Context Manager starts
- Both agents should update their respective context files
- Provide unified status report to user upon completion

The goal is to have a ready-to-develop feature environment with proper branch setup and comprehensive context for implementation.