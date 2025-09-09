---
description: Updates the project functional context using Project Context Manager agent
argument-hint: [link-to-function-doc]
---
## Context
This command updates the existing project functional context using the specialized Project Context Manager agent. The agent will compare the new document with existing context and update accordingly.

## Task
Use the Task tool to launch the project-context-manager agent with the following instructions:

**Agent Task**: Update project functional context
**Document Source**: $ARGUMENTS (optional - if not provided, agent should refresh from last known source)
**Instructions**:
1. Check if functional context exists in `.claude/project/functional.md`
2. If not exists, inform user they should use `/icm-init-proj-function` first
3. If exists and $ARGUMENTS provided:
   - Process the new functional requirements document from the provided source
   - Compare with existing context in `.claude/project/functional.md`
   - Identify differences and changes in requirements
   - Update the functional context with new information
   - Preserve relevant historical context where appropriate
4. If exists and no $ARGUMENTS provided:
   - Check metadata for last known source
   - Attempt to refresh from original source if possible
   - Update context if source document has changed
5. Update `.claude/project/metadata.json` with new timestamp and version information
6. Create backup of previous context before updating
7. Provide detailed summary of what was changed/updated
8. Flag any breaking changes or significant requirement shifts

The agent should ensure context continuity while incorporating new functional requirements accurately.