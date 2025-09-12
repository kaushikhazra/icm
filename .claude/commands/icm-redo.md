---
description: Redoes current TODO implementation based on user feedback
argument-hint: [what-to-change]
---
## Context
This command handles user feedback to redo the current TODO implementation. It reverts recent changes, updates context if needed, and re-implements the TODO with the requested modifications.

## Task
Use the Task tool to launch the coder agent with coordination with the local-context-manager agent:

**Primary Agent**: Coder  
**Supporting Agent**: Local Context Manager

**Agent Task**: Redo current TODO implementation with user feedback
**User Feedback**: $ARGUMENTS
**Instructions**:

**Coder Agent Tasks (Primary)**:
1. Coordinate with Local Context Manager to get current context and validate active TODO
2. Read updated context and user feedback requirements
3. Understand what needs to be changed from previous implementation
4. Revert to clean state (remove previous implementation)
5. Re-implement the TODO item incorporating user feedback:
   - Apply different coding style if requested
   - Use different implementation approach if needed
   - Address any missed requirements or edge cases
6. Follow updated context guidelines and patterns
7. Run tests to ensure new implementation works correctly
8. Create new atomic commits for the revised implementation
9. Report implementation status back to Local Context Manager

**Local Context Manager Tasks (Supporting)**:
1. Validate that there is an active TODO in progress
2. Log user feedback in session history with timestamp
3. Analyze feedback to determine type of change requested:
   - **Coding style change**: Update project coding style context
   - **Wrong implementation**: Update feature context or TODO details
   - **Requirement clarification**: Update functional context
   - **Architecture change**: Update architectural context
4. Provide current context to Coder agent
5. Update relevant context files based on feedback type:
   - If coding style: Update project style guidelines
   - If implementation approach: Update feature architectural context
   - If requirements: Update feature functional context
6. Update current TODO details if implementation approach needs to change
7. Update TODO status based on Coder agent results

**Context Updates**:
- If feedback indicates systematic issues, update appropriate context files
- Ensure future implementations benefit from learned improvements
- Maintain context evolution history for reference

**Feedback Categories**:
- **Style/Convention Changes**: Update coding standards and apply consistently
- **Implementation Logic**: Revise approach while maintaining requirements
- **Requirement Updates**: Clarify and update functional requirements
- **Architecture Adjustments**: Update architectural patterns or constraints

**User Interaction**:
- Present revised implementation for review
- Explain what was changed based on feedback
- Wait for approval or additional feedback

**Learning Integration**:
- Update project context with style preferences learned
- Enhance feature context with clearer implementation guidance
- Improve TODO descriptions to prevent future confusion

The goal is to handle user feedback constructively, improving both the immediate implementation and the context for future development.