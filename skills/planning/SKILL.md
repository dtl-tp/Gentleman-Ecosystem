---
name: planning
description: Generates detailed, bite-sized implementation plans from a technical design or spec. Use this after brainstorming to decompose a feature into discrete, testable tasks with exact file paths and code snippets.
---
# Systematic Planning

## Goal
To decompose a technical design into a series of highly granular, test-driven implementation tasks that a developer (or subagent) can execute with minimal ambiguity.

## Instructions
1.  **Analyze Design**: Read the approved design document (usually from `docs/plans/`).
2.  **Generate Plan**: Create a comprehensive implementation plan documented in `docs/plans/YYYY-MM-DD-<feature-name>.md`.
3.  **Task Granularity**: Each task should represent 2-5 minutes of work (e.g., "Write failing test", "Run test", "Implement minimal code", "Commit").
4.  **Formatting**: Follow the strict task structure defined in `resources/plan_template.md`.
5.  **Handoff**: After saving the plan, offer the user a choice between "Subagent-Driven" execution or "Parallel Session" execution.

## Constraints
- **Exact Paths**: Always specify exact file paths.
- **TDD First**: Every code change must be preceded by a failing test.
- **Frequent Commits**: Every task must end with a git commit step.
- **No Placeholders**: Never use descriptive placeholders like "add validation"; provide the exact code as a snippet.

## Resources
- Plan header and task template: `resources/plan_template.md`.
