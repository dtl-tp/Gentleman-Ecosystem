# Plan Document Template

## Header Requirement
Every plan MUST start with this header:

```markdown
# [Feature Name] Implementation Plan

> **Note:** Use the executing-plans skill to implement this plan task-by-task.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies/libraries]

---
```

## Task Structure Structure
```markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.ext`
- Modify: `exact/path/to/existing.ext`
- Test: `tests/exact/path/to/test.ext`

**Step 1: Write the failing test**
(Insert exact code snippet)

**Step 2: Run test to verify it fails**
Run: `[Command]`
Expected: FAIL

**Step 3: Write minimal implementation**
(Insert exact code snippet)

**Step 4: Run test to verify it passes**
Run: `[Command]`
Expected: PASS

**Step 5: Commit**
Run: `git add ... && git commit -m "..."`
```
