---
description: Updates project architecture from document source AND scans code for changes using Project Context Manager and Code Analyzer agents
argument-hint: [link-to-arch-doc]
---
## Context
This command updates the existing project architecture context by processing architecture documents AND scanning the actual codebase for implementation changes. It combines document-based updates with code analysis to ensure architecture context reflects both intended design and actual implementation.

## Task
Use the Task tool to launch the project-context-manager agent with coordination with the code-analyzer agent:

**Primary Agent**: Project Context Manager  
**Supporting Agent**: Code Analyzer

**Agent Task**: Update project architecture from document source and code analysis
**Document Source**: $ARGUMENTS (optional - if not provided, agent should refresh from last known source)
**Instructions**:

**Project Context Manager Tasks (Primary)**:
1. Check if architecture context exists in `.claude/project/architecture.md`
2. If not exists, inform user they should use `/icm-init-proj-arch` first
3. **Document Processing Phase**:
   - If $ARGUMENTS provided: Process the new architecture document from the provided source
   - If no $ARGUMENTS: Check metadata for last known source and attempt to refresh from original source
   - Compare with existing context in `.claude/project/architecture.md`
   - Identify document-based changes and updates
4. **Code Analysis Phase**:
   - Coordinate with Code Analyzer agent to scan current codebase
   - Receive code analysis report of actual implemented architecture
   - Compare code findings with both existing context and new document updates
   - Identify discrepancies between documented design and actual implementation
5. **Context Integration**:
   - Merge document updates with code analysis findings
   - Update `.claude/project/architecture.md` with:
     - New architecture information from document source
     - Actual implementation details from code analysis
     - Reconciled differences between design and implementation
     - Notes on architectural evolution and drift
6. Create backup of previous context before updating
7. Update `.claude/project/metadata.json` with new timestamp and version information
8. Provide detailed summary of:
   - What was updated from document source
   - What was discovered from code analysis
   - Any conflicts or discrepancies found
   - Recommendations for alignment

**Code Analyzer Tasks (Supporting)**:
1. Perform focused codebase analysis to understand current architecture:
   - Scan directory structure and identify main components/modules
   - Analyze dependencies between components
   - Identify architectural patterns actually implemented
   - Map data flow and communication patterns in code
   - Identify key interfaces and contracts
   - Document technology stack and frameworks in use
2. Generate architecture analysis report focusing on:
   - Component hierarchy and relationships as implemented
   - Technology stack actually used
   - Patterns and practices found in code
   - Any implementation that differs from typical architecture documentation
3. Provide findings to Project Context Manager for integration

**Workflow**:
1. Project Context Manager processes architecture document updates
2. Code Analyzer scans and analyzes actual codebase implementation
3. Project Context Manager integrates both sources of information
4. Architecture context is updated with comprehensive view of design + implementation
5. Report highlights any gaps or conflicts between documented design and actual code

The goal is to maintain architecture documentation that accurately reflects both the intended design and the actual implementation.