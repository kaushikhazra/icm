---
description: Creates the project architecture context
argument-hint: [path-to-arch-doc]
---
## Context
This command creates an architecture context that can be used in future to understand the architecture used in this project. The architecture context is a living document

## Task
1. Check if `ctx-arch.md` file exists in `.claude/project-context` or not
2. If exists then tell user that the architecture context document already exists. They can use `/icm-update-proj-arch` to update the document
3. If it does not exist then analyse the document provided by $ARGUMENTS 
4. Create an architecture context document. This document will help you in future to understand the design principle of this project. Create the document keeping that in mind.
5. Add the last updated date and time to the document so that you can reference it later and find out if the document is out of date or not.