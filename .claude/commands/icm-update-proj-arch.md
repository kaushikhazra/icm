---
description: Updates the project architecture context using Project Context Manager agent
argument-hint: [link-to-arch-doc]
---
## Context
This command updates the existing project architecture context using the specialized Project Context Manager agent. The agent will compare the new document with existing context and update accordingly.

## Task
Use the Task tool to launch the project-context-manager agent with the following instructions:

**Agent Task**: Update project architecture context
**Document Source**: $ARGUMENTS (optional - if not provided, agent should refresh from last known source)
**Instructions**:
1. Check if architecture context exists in `.claude/project/architecture.md`
2. If not exists, inform user they should use `/icm-init-proj-arch` first
3. If exists and $ARGUMENTS provided:
   - Process the new architecture document from the provided source
   - Compare with existing context in `.claude/project/architecture.md`
   - Identify differences and changes
   - Update the architecture context with new information
   - Preserve relevant historical context where appropriate
4. If exists and no $ARGUMENTS provided:
   - Check metadata for last known source
   - Attempt to refresh from original source if possible
   - Update context if source document has changed
5. Update `.claude/project/metadata.json` with new timestamp and version information
6. Create backup of previous context before updating
7. Provide detailed summary of what was changed/updated
8. Flag any breaking changes or significant architectural shifts

The agent should ensure context continuity while incorporating new architectural information accurately.