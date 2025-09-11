# /icm-reverse-engg-proj-arch

## Command Description
Reverse engineers the project architecture from the existing codebase and creates comprehensive architecture documentation.

## Usage
```
/icm-reverse-engg-proj-arch
```

## Purpose
This command analyzes the existing codebase to automatically generate project architecture context that can be used for future development. It's particularly useful when:
- Starting work on an existing project without documentation
- Updating architecture documentation after significant changes
- Onboarding new team members to understand project structure
- Establishing baseline architecture context for ICM workflow

## What It Does
1. **Launches Code Analyzer Agent**: Deploys the specialized code-analyzer agent to perform comprehensive codebase analysis
2. **Analyzes Project Structure**: Examines directory organization, file relationships, and module dependencies
3. **Identifies Architecture Patterns**: Detects architectural styles, design patterns, and technology choices
4. **Generates Documentation**: Creates structured architecture context documentation
5. **Updates Project Context**: Stores results in `.claude/project/ctx-arch.md` via Project Context Manager

## Execution Flow
```
User: /icm-reverse-engg-proj-arch
  ↓
Launch Code Analyzer Agent
  ↓
Analyze codebase structure
  ↓
Identify architecture patterns
  ↓
Generate architecture documentation
  ↓
Update project context files
  ↓
Report results to user
```

## Output
- Creates or updates `.claude/project/ctx-arch.md` with comprehensive architecture documentation
- Provides analysis summary including:
  - Identified architecture patterns
  - Technology stack
  - Key components and their relationships
  - Design patterns in use
  - Recommendations for future development

## Prerequisites
- Must be run from a project root directory
- Project should contain source code files
- `.claude/` directory structure should exist (created by icm-setup.py)

## Example Output Structure
The command generates architecture context in this format:
```markdown
# Project Architecture Context

## Overview
[Generated project description]

## Architecture Style
[Detected architectural pattern]

## Technology Stack
- Languages: [Detected languages]
- Frameworks: [Identified frameworks]
- Build Tools: [Build configuration]

## Project Structure
[Directory organization analysis]

## Key Components
[Main modules and services]

## Design Patterns
[Identified patterns and usage]

## Integration Points
[External dependencies and APIs]

## Recommendations
[Suggestions for development]
```

## Performance Considerations
- Analysis time varies based on codebase size
- Large projects are processed in chunks for better performance
- Progress updates provided for long-running analyses
- Results are cached to avoid redundant processing

## Integration with ICM Workflow
This command integrates with the broader ICM system by:
- Providing baseline architecture context for feature development
- Supporting the Project Context Manager with structured documentation
- Enabling consistent architectural decisions across development cycles
- Facilitating project onboarding and knowledge transfer

## Error Handling
- Validates project structure before analysis
- Handles missing or inaccessible files gracefully
- Provides clear error messages for common issues
- Supports retry mechanisms for partial failures

## Related Commands
- `/icm-init-proj-arch` - Initialize architecture context from external document
- `/icm-update-proj-arch` - Update existing architecture context
- `/icm-status` - Check current project context status