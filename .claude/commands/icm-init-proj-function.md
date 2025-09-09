---
description: Creates the project functional context using Project Context Manager agent
argument-hint: [link-to-function-doc]
---
## Context
This command initializes the project functional context using the specialized Project Context Manager agent. The agent will process the provided functional document and create structured context files for future reference.

## Task
Use the Task tool to launch the project-context-manager agent with the following instructions:

**Agent Task**: Initialize project functional context
**Document Source**: $ARGUMENTS
**Instructions**:
1. Process the functional requirements document from the provided source (Google Drive link, GitLab Wiki, or local path)
2. Check if functional context already exists in `.claude/project/functional.md`
3. If exists, inform user they should use `/icm-update-proj-function` instead
4. If not exists, create comprehensive functional context including:
   - Business requirements and objectives
   - User stories and use cases
   - Functional specifications and behavior
   - Business rules and constraints
   - Integration requirements
   - Data flow and processing requirements
5. Create `.claude/project/` directory structure if needed
6. Save structured context to `.claude/project/functional.md`
7. Update metadata in `.claude/project/metadata.json` with timestamp and source information
8. Provide summary of created context to user

The agent should ensure the functional context is comprehensive and will help future development understand the project's business requirements and expected behavior.