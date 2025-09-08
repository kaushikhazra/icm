---
description: Updates the project architecture context
argument-hint: [path-to-arch-doc]
---
## Context
This command updates the architecture context that can be used in future to understand the architecture used in this project. The architecture context is a living document

## Task
1. Check if `ctx-arch.md` file exists in `.claude/project-context` or not
2. If it does not exist then tell user that the architecture context document should be created using `/icm-init-proj-arch` before it can be updated 
3. If exists then analyse the document provided $ARGUMENTS. 
4. Very carefully check any differences between the provided document and `./claude/project-context/ctx-arch.md` context document.
5. Update the context document if you detect any difference.
6. Update the last updated date and time for future reference.