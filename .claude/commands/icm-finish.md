---
description: Completes feature development, performs cleanup, and archives context
argument-hint: 
---
## Context
This command finalizes the feature development process by performing final validation, cleaning up temporary context, merging changes, and archiving the feature context for future reference.

## Task
Use the Task tool to launch multiple agents for feature completion:

**Primary Agent**: feature-context-manager
**Supporting Agents**: git-manager, local-context-manager

**Agent Task**: Complete feature development and perform cleanup
**Instructions**:

**Git Manager Tasks**:
1. Validate that feature has passed review process
2. Ensure all changes are committed and pushed to remote
3. Check that feature branch is up to date with main/master
4. Perform final merge operations:
   - Merge feature branch to main/master (or create final PR)
   - Create release tag if applicable
   - Delete feature branch locally and remotely (if merge completed)
5. Update main branch context with any learned patterns or conventions

**Local Context Manager Tasks**:
1. Validate that all TODOs have been completed
2. Create final session summary with development statistics:
   - Total development time
   - Number of TODOs completed
   - Number of iterations and redos
   - Key challenges and solutions
3. Archive local development session:
   - Move session logs to feature archive
   - Clear active development context
   - Reset local context for next feature
4. Clean up temporary development files and caches

**Feature Context Manager Tasks**:
1. **Final Context Validation**:
   - Verify all feature requirements have been implemented
   - Confirm architectural decisions are documented
   - Validate that context accurately reflects final implementation

2. **Context Archiving**:
   - Create archive of feature context in `.claude/features/completed/[branch-name]/`
   - Include final implementation summary and lessons learned
   - Preserve context for future reference and similar features
   - Update feature metadata with completion timestamp and outcomes

3. **Knowledge Extraction**:
   - Extract reusable patterns and add to project context
   - Update architectural context with new patterns discovered
   - Document any new conventions or standards established
   - Update project functional context if business understanding improved

4. **Context Cleanup**:
   - Remove active feature context from `.claude/features/[branch-name]/`
   - Clean up temporary files and intermediate states
   - Update project context index with completed feature reference

**Project Context Updates**:
- Update project architecture context with new patterns learned
- Enhance functional context with improved business understanding
- Add feature to completed features list for future reference
- Update development standards based on experience

**Final Validation**:
- Confirm feature branch has been properly merged or PR created
- Verify all context has been properly archived
- Validate that development environment is clean for next feature
- Ensure no temporary or intermediate files remain

**Completion Report**:
- Generate feature completion summary with key metrics
- Document lessons learned and improvements for future features
- Provide recommendations for similar feature development
- Update project documentation with new capabilities

**Error Handling**:
- If merge conflicts exist, provide guidance for resolution
- If context is incomplete, flag missing information before cleanup
- If tests are failing, prevent cleanup and require fixes
- Offer rollback options if completion process encounters issues

The goal is to cleanly complete the feature development cycle, preserve valuable context and learnings, and prepare the development environment for the next feature.