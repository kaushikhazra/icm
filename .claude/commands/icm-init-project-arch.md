---
description: Creates the project architecture context using Project Context Manager agent
argument-hint: [link-to-arch-doc]
---
## Context
This command initializes the project architecture context using the specialized Project Context Manager agent. The agent will process the provided document and create structured context files for future reference.

## Task
Use the Task tool to launch the project-context-manager agent with the following instructions:

**Agent Task**: Initialize project architecture context
**Document Source**: $ARGUMENTS
**Instructions**:
1. Process the architecture document from the provided source (Google Drive link, GitLab Wiki, or local path)
2. Check if architecture context already exists in `.claude/project/architecture.md`
3. If exists, inform user they should use `/icm-update-proj-arch` instead
4. If not exists, create comprehensive architecture context including:
   - System architecture overview
   - Key design principles and patterns
   - Technology stack and dependencies
   - Component relationships and interactions
   - Deployment architecture if available
5. Create `.claude/project/` directory structure if needed
6. Save structured context to `.claude/project/architecture.md`
7. Update metadata in `.claude/project/metadata.json` with timestamp and source information
8. Provide summary of created context to user

The agent should ensure the architecture context is comprehensive and will help future development understand the project's design principles and structure.