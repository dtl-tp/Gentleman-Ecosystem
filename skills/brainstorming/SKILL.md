---
name: brainstorming
description: Engages in a Socratic design refinement process to turn ideas into fully formed designs and specs. Use this before any coding or implementation to explore context, ask clarifying questions, and propose architectural approaches.
---
# Brainstorming

## Goal
To turn high-level ideas into fully validated designs and technical specifications through a structured, collaborative dialogue, preventing wasted effort on unexamined assumptions.

## Instructions
1.  **Context Discovery**: Before starting, explore the project's current state (files, documentation, recent commits).
2.  **Socratic Refinement**: Ask clarifying questions one at a time. Focus on understanding purpose, constraints, and success criteria. Prefer multiple-choice options when possible.
3.  **Propose Alternatives**: Present 2-3 different architectural approaches with trade-offs. Recommend one and explain why.
4.  **Incremental Design**: Present the design in logical sections (architecture, components, data flow, etc.). Request user approval after each section.
5.  **Documentation**: Once fully approved, write the design document to `docs/plans/YYYY-MM-DD-<topic>-design.md` and commit it.
6.  **Handoff**: After committing the design doc, explicitly transition to the `planning` skill to create the implementation tasks.

## Constraints
- **HARD GATE**: Do NOT write project code, scaffold projects, or take any implementation action until the design is approved.
- **One Question Rule**: Never ask more than one question per message.
- **Incremental Approval**: Every project, no matter how "simple," must have a design presented and approved.

## Resources
- Detailed process flow and principles are available in `resources/brainstorming_process.md`.
