---
description: Provides current status of ICM project including contexts, active features, and progress
argument-hint: 
---
## Context
This command provides a comprehensive overview of the current ICM project status including project contexts, active features, local development state, and overall progress tracking.

## Task
Use the Task tool to launch the local-context-manager agent with coordination from project-context-manager and feature-context-manager agents:

**Primary Agent**: Local Context Manager
**Supporting Agents**: Project Context Manager, Feature Context Manager

**Agent Task**: Generate comprehensive ICM project status report
**Instructions**:

**Local Context Manager Tasks**:
1. Read current local context from `.claude/local/local-context.md` if exists
2. Identify current active feature and TODO item
3. Check for any active development session state
4. Generate local development status summary

**Project Context Manager Tasks**:
1. Check project architecture context status:
   - Read `.claude/project/ctx-arch.md` if exists
   - Report last updated timestamp and version
   - Indicate if context needs updating
2. Check project functional context status:
   - Read `.claude/project/ctx-function.md` if exists
   - Report last updated timestamp and version
   - Indicate if context needs updating
3. Provide project-level configuration summary

**Feature Context Manager Tasks**:
1. Scan all feature directories in `.claude/features/`
2. For each feature, report:
   - Feature name and branch association
   - Status (active, completed, in-progress)
   - TODO completion percentage
   - Last activity timestamp
3. Identify current active feature(s)
4. Report any stale or abandoned features

**Status Report Structure**:
```
# ICM Project Status Report
Generated: [timestamp]

## Project Context Status
- Architecture Context: [status/last updated/needs update]
- Functional Context: [status/last updated/needs update]

## User Stories Status
- Total User Stories: [count]
- Status breakdown: [created/in-progress/completed]

## Feature Development Status
### Active Features
- [list active features with progress]

### Completed Features
- [list recently completed features]

### All Features Summary
- [tabular view of all features with status]

## Local Development Status
- Current Feature: [feature name or "None"]
- Current TODO: [todo description or "None"]
- Session State: [active/idle/ready for review]
- Last Activity: [timestamp]

## Git Integration Status
- Current Branch: [branch name]
- Uncommitted Changes: [yes/no/count]
- Last Commit: [commit message and timestamp]

## Next Recommended Actions
- [context-aware suggestions based on current state]
```

**Error Handling**:
- If no ICM structure exists, report "ICM not initialized"
- If contexts are missing, suggest initialization commands
- If features exist but no active session, suggest next steps
- Handle corrupted or incomplete context files gracefully

**Performance Considerations**:
- Cache frequently accessed information
- Limit file system traversal to essential directories
- Provide quick vs detailed status options if needed

The goal is to give developers and teams complete visibility into their ICM project state and actionable next steps.