# Incremental Context Method

## Document Information
- **Version:** 1.0
- **Date:** 2025-09-05
- **Author(s):** Kaushik Hazra
- **Status:** Draft
- **Last Updated:** 2025-09-05

## Executive Summary
**One-sentence description:** A method to maintain context for AI Coding Assistants

**Problem Statement:** Current method of context creation and management for AI Coding Assistants are mainly focused on initial context. However, a project is build in increments. Current methods do not have a way to extend the contexts as the feature and architecture of the project evolves. There is a need of a context management framework which can extend as the project evolve and get reach in the functionality.

**Proposed Solution:** The proposed solution maintains 3 different types of contexts
- **Project Context:** The overall context of the project, including project structure, function, architecture, slash command for Claude, sub-agents for Claude or any other system that supports sub-agents.
- **Feature Context:** Feature specific context, including any design consideration, functionality, any specific architecture consideration for a feature. This is aligned with the User Stories, Git Pulls, and Branches.
- **Local Context:** Currently development context that includes current state, workspace preferences, etc.

**Key Benefits:** Primary value propositions
- Context for AI coding assistant can be extended as features are getting developed
- Can also maintain a global project specific context
- Can have a context as atomic as individual development workspace level
- Creates a development memory across coding session

## Concept Overview

### Purpose and Goals
**Primary Goal:** The main object is to create an extendable context system for AI coding assistants that can glow as the project grows with functionality and evolves its design.

**Secondary Goals:**
- Context can be traced to a feature.
- Aligned Agile method of development, and also support overall project context.
- Faster context building by automatic context extending.

**Success Metrics:** How will success be measured?
- Metric 1: Contexts can be extended without altering any existing context files. Successfully implemented in 5 project.
- Metric 2: AI Coding Assistant can identify the change or addition and properly implement the new feature or change. The assistant should be able to do it with an accuracy of 0.9. Measurement is
    ```math        
    m/n
    ```
    Where 
    - m = number of time coding assistant successfully identified the change and implemented
    - n = number of time the context has been change
    
### Target Audience
**Primary Users:** Employees of Mountain Leverage
- **Architects** : Architects do not have to rebuild the context every time they are using.
- **Developers** : Developers always go through incremental development. This will be useful for them because they will not have to re-write any of the context, as it builds up automatically.
- **Testers**: Testers will get the context for free, and need to only change the test context.

**Stakeholders:** Mountain Leverage
- CEO: Time saving from progressive context and avoidance of 
- Product Managers: Consistency of the documentation, and time saving
- Project Managers: Standardized development, and time saving

## Detailed Description

### Core Concept
This is a context management system for incremental development. Important feature of this concept is 
- State Persistence
- Modular Context
- Sub-agent Handoffs
- Git Integration

### Key Features
1. **State Persistence:** Persists states at a different scope - project level, feature level, local level.
2. **Modular Context:** The context is broken into project level context, feature level context and progress information, and current development progress and todos.
3. **Sub-agent Handoffs:** Specialized agents for incremental task. Resumption Agent, Progress Tracker Agent, Context Optimizer Agent.
4. **Git Integration:** Automatic safety net by creating check point in git.

### User Journey/Experience
**Initializing The Project**
- Clone the ICM repository.
   ```bash
   git clone icm
   cd icm
   ```
- Run the setup command and provide the project folder name.
   ```bash
   python icm-setup.py <project folder to setup icm>
   ```
- ICM setup initializes the project with required commands, sub-agents, supporting documents and folder structure.

**Create Project Architecture Context**
- `/icm-init-proj-arch [link to the document]`. The link to the document could be Google Drive link, Gitlab Wiki link, or simple path to another folder.

**Update Project Architecture Context**
- `/icm-update-proj-arch`
   - It will download the new project architecture
   - Replace the context with new architecture context

**Create Project Functional Context**
- `/icm-init-proj-function [link to the document]`. The link to the document could be Google Drive link, Gitlab Wiki link, or simple path to another folder

**Update Project Function Context**
- `/icm-update-proj-function`
   - It will download the new project functional document
   - Replace the context with new functional context 

**Create A Feature Context**
- Creates a PR for the story/issue
- `/icm-pull [branch name]`. 

**Create the Code**
- `/icm-create-code`
   - The system creates a TODO list
   - Executes 1 TODO at a time
   - User reviews the code
   - If everything is ok then use `/icm-continue`
   - If anything needed to change `/icm-redo [what to change]`

**Continue Coding**
- `/icm-continue`
   - ICM continues to the next TODO

**Redo Coding**
- `/icm-redo [what to change]`
   - If it is a coding style change ICM will update the coding style context
   - If it is a wrong implementation ICM will update the feature context


**Save intermediate state**
- The intermediate state is saved automatically
   - After every TODO is finished for a feature ICM saves the current state

**Create PR**
- `/icm-review`
   - This will trigger the automated review
   - Fix any review comments
   - If everything is ok it will push the code for manual review

**Finish a Feature**
- `/icm-finish`. It will finish the feature, and will cleans up any context file.


### Technical Approach
**Architecture Overview:** 
The Incremental Context Method is primarily intended for Claude Code. The system has a set of "slash" commands and "sub-agents" to guide CC through managing functional, architectural, feature, and local context.

**Sub-Agents**
- **Context Managers**
   - **Project Context Manager**
   - **Feature Context Manager**
   - **Local Context Manager**
- **Git Manager**
- **Code Manager**
   - **Coder**
   - **Reviewer**

**Slash Commands**
- `/icm-init-proj-arch [link to the document]`
- `/icm-update-proj-arch`
- `/icm-init-proj-function [link to the document]`
- `/icm-update-proj-function`
- `/icm-pull [branch name]`
- `/icm-create-code`
- `/icm-continue`
- `/icm-redo [what to change]`
- `/icm-review`
- `/icm-finish`

**Flow Diagram**

**Project Context Management**
```
+--------------------------------------------+    +-----------------------+
| /icm-init-proj-arch [link to the document] |    | /icm-update-proj-arch |
+--------------------------------------------+    +-----------------------+
                   |                                        |
                   v                                        |
      +-----------------------------+                       |
      |        SUB-AGENT            |                       |
      +-----------------------------+ <---------------------+
      |   Project Context Manager   | <---------------------+
      +-----------------------------+                       |
                  ^                                         |
                  |                                         |
+------------------------------------------------+   +---------------------------+
| /icm-init-proj-function [link to the document] |   | /icm-update-proj-function |
+------------------------------------------------+   +---------------------------+      

```

**Key Technologies:**

**Integration Points:** Directly into the project using `.claude/`

## Requirements and Constraints

### Functional Requirements
- Must have: 
   - Must have a way to initialize and update a project context using slash command 
   - Must have a way to initialize and update a feature or a PR context with slash 
   command
   - Must have a way to create and update 
   - Must have a way to initialize and update a local context using slash command
   - Must have sub-agents for Resumption, Progress Tracking, Context Optimization
- Should have:
   - *TBD*
- Could have: 
   - *TBD*

### Non-Functional Requirements
- **Performance:** [Speed, capacity, efficiency requirements]
   - *TBD*
- **Security:** [Security and privacy requirements]
   - Should be used only with local development environment
- **Usability:** [User experience requirements]
   - All operations are properly supported using slash commands
- **Scalability:** [Growth and scaling requirements]
   - The type of context should be extended
   - Should be able to extend to other coding agents

### Constraints
- **Technical Constraints:** [Technology limitations]
   - Applicable to only AI Coding Agents
- **Business Constraints:** [Budget, timeline, resource limits]
   - No budget is required
   - Should be implemented by October-2025
   - 1 person should be good to implement this
- **Regulatory Constraints:** [Legal or compliance requirements]
   - Used inside ML so there should not be any legal or compliance issue

## Implementation Considerations

### Timeline
- **Phase 1:** Manual state files and basic checkpointing - 2025-09-13
- **Phase 2:** Add custom Claude Code commands for state management - 2025-09-20
- **Phase 3:** Implement sub-agent handoffs - 2025-09-27
- **Phase 4:** Optimize context compression - 2025-10-04

### Resource Requirements
- **Team:** 1 person
- **Technology:** Claude Code
- **Budget:** No money required

### Risks and Mitigation
1. **Risk:** Risk of not getting adopted across teams
   - **Impact:** High
   - **Probability:** Medium
   - **Mitigation:** Make it easy with slash commands

2. **Risk:** LLM confusion with all the contexts
   - **Impact:** High
   - **Probability:** Medium
   - **Mitigation:** Use Sub-agents to limit context bleeding

3. **Risk:** Context not captured correctly
   - **Impact:** Medium
   - **Probability:** High
   - **Mitigation:** Proper slash command instruction to re-check context and flag

## Alternatives Considered
**Option 1:** PRP
- **Pros**: Structured, simple, single document, can reference multiple document
- **Cons**: Not incremental, requires re-creating some of the context or copying when using in incremental development. Also, not much slash command support.
- **Why not chosen**: Not supportive of Agile development. This method requires repeating of some of the contexts when used with incremental feature development.

**Option 2:** BMAD
- **Pros**: Very extensive, had lots of slash command and agent support
- **Cons**: Too complex to use.
- **Why not chosen**: Complexity is too high. Also, good for initializing a project, but no clear way out of the box to maintain feature specific context.

**Option 3:** Claude Flow
- **Pros**: Parallel development capability using Hive and swarm technique
- **Cons**: Method of development not clear, and requires method development
- **Why not chosen**: No proper guide to manage a project, it is more of a tool rather than a context management framework

**Option 4:** AgentOS
- **Pros**: Has hierarchical context, and very similar to this proposed concept
- **Cons**: Only support linux setup. This requires some modification to the existing system.
- **Why not chosen**: Maintainability of a windows version will be challenging.


## Success Criteria and Validation

### Definition of Done
- Successfully implemented in 5 project
- Coding agent is not missing the increment more than 10% of the time

### Testing Strategy
- **User testing approach:** Use it with 5 different teams and validate its usability
- **Technical validation:** Can it capture the incremental concept correctly?
- **Performance testing:** Capture context without exhausting more than 25% of token budget.

### Acceptance Criteria
- [ ] Satisfies 5 project team, and they can use it in their every day work
- [ ] Not missing implementation of an increment more than 10%
- [ ] Accurately capturing the context which is verifiable by creating human readable document.

---

**Document Review History:**
- [2025-09-06] - [Version: 1.0] - [Initial Draft] - [Chris Stremple] 