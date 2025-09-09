---
description: Performs automated code review and prepares changes for manual review
argument-hint: 
---
## Context
This command triggers the automated review process using the Reviewer agent to analyze all implemented changes, validate against requirements, and prepare the feature for manual review.

## Task
Use the Task tool to launch the reviewer agent with coordination with git-manager:

**Primary Agent**: reviewer
**Supporting Agent**: git-manager

**Agent Task**: Perform comprehensive automated code review
**Instructions**:

**Git Manager Tasks**:
1. Ensure all changes are committed and working directory is clean
2. Create a review branch or tag for tracking review state
3. Generate comprehensive change summary since feature branch creation
4. Identify all modified, added, and deleted files
5. Prepare Git history for review process

**Reviewer Agent Tasks**:
1. **Context Validation**:
   - Read project context from `.claude/project/`
   - Read feature context from `.claude/features/[branch-name]/`
   - Verify implementation matches feature requirements
   - Check architectural compliance with project standards

2. **Code Quality Analysis**:
   - Run project linting tools and style checkers
   - Validate code follows project conventions and patterns
   - Check for proper error handling and edge cases
   - Analyze code complexity and maintainability
   - Verify proper testing coverage

3. **Security and Performance Review**:
   - Scan for common security vulnerabilities
   - Identify potential performance bottlenecks
   - Check for proper input validation and sanitization
   - Review resource usage and memory management

4. **Requirement Verification**:
   - Validate all TODO items have been implemented
   - Check that acceptance criteria are met
   - Verify business logic matches functional requirements
   - Confirm integration points work as specified

5. **Test Validation**:
   - Run all existing tests to ensure no regressions
   - Validate new tests provide adequate coverage
   - Check test quality and maintainability
   - Ensure tests follow project testing patterns

6. **Review Report Generation**:
   - Create comprehensive review report with findings
   - Categorize issues by severity (blocking, major, minor, suggestions)
   - Generate pull request description with change summary
   - Provide recommendations for improvements
   - Flag any breaking changes or architectural decisions

**Review Categories**:
- **Blocking Issues**: Must be fixed before merge (security, broken functionality)
- **Major Issues**: Should be addressed (significant style violations, missing tests)
- **Minor Issues**: Nice to have fixes (minor style issues, optimization opportunities)
- **Suggestions**: Future improvement opportunities

**Output Preparation**:
- Generate detailed review report for development team
- Create pull request template with change summary and context
- Prepare list of validation steps for manual reviewers
- Highlight areas requiring special attention

**Manual Review Preparation**:
- If no blocking issues found, mark feature as ready for manual review
- If blocking issues found, provide clear guidance for fixes
- Update feature context with review status and findings
- Create checklist for manual reviewer focus areas

The goal is to ensure high code quality and provide comprehensive preparation for efficient manual code review.