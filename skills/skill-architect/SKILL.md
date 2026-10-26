---
name: skill-architect
description: Architects and generates modular "Agent Skills" for the Antigravity IDE environment. Follows a strict hierarchy of SKILL.md, scripts, examples, and resources to extend agent capabilities.
---
# Skill Architect

## Goal
To generate high-quality, predictable, and fully functional skill directories for the Antigravity environment following a modular architecture.

## Instructions
1.  **Reference the Manual**: Read the full system instructions located at `resources/skill_creator_manual.md` before starting any skill creation task.
2.  **Plan Structure**: Determine the necessary components (scripts, resources, examples) based on the requirement.
3.  **Generate Files**: Use the `write_to_file` tool to create the directory and all auxiliary files.
4.  **Validate**: Ensure the `SKILL.md` frontmatter adheres to name and description standards.

## Constraints
- Never include LLM brand names (gemini, claude, etc.) in the skill name.
- Always provide full, functional code for scripts—no placeholders.
- Use forward slashes for all paths.
