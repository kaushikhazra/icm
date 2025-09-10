---
description: Creates user stories from functional documents using User Story Manager agent
argument-hint: [story-template-path] [functional-doc-path]
---
## Context
This command creates a comprehensive set of user stories from provided functional documents using the specialized User Story Manager agent. The agent processes both a story template and functional requirements to generate structured, numbered user stories.

## Task
Use the Task tool to launch the user-story-manager agent with the following instructions:

**Agent Task**: Create user stories from functional documents
**Template Path**: $1
**Functional Document Path**: $2
**Instructions**:
1. Process both the story template and functional requirements document from the provided paths
2. Copy the user-provided template to `.claude/user-stories/template.md` for reference
3. Check if user stories already exist in `.claude/user-stories/` directory
4. If stories exist, ask user if they want to overwrite or merge with existing stories
5. Parse the functional document to extract key features and requirements
6. Use the user-provided template format exactly to generate user stories with:
   - Numerical IDs (1, 2, 3, ..., n)
   - Template structure preserved exactly as provided
   - Template placeholders replaced with actual story content
   - All custom sections and formatting maintained
7. Create `.claude/user-stories/` directory if needed
8. Save each story as individual markdown files: `{id}-{story-title}.md`
9. Create an index file `index.md` with overview of all stories
10. Generate summary report showing:
   - Total number of stories created
   - Story categories or themes identified
   - Any functional requirements not covered by stories
11. Provide recommendations for story refinement or missing elements

The agent should ensure all functional requirements are translated into actionable user stories that can guide feature development and testing.