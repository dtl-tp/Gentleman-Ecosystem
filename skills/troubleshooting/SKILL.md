---
name: troubleshooting
description: Systematically identifies, isolates, and resolves application errors and bugs. Use this when an application crashes, returns incorrect data, or behaves unexpectedly.
---
# Troubleshooting

## Goal
To resolve application issues through a structured, 4-phase root cause analysis and fix process, ensuring the bug is fully understood and verified as fixed.

## Instructions
1.  **Phase 1: Reproduction**:
    *   Explore current logs and error messages.
    *   Create a minimal, automated reproduction script or unit test that triggers the issue.
    *   **Constraint**: Do NOT start fixing until the failure is consistently reproducible.
2.  **Phase 2: Isolation**:
    *   Trace the error using the "Fail Fast" principle (add assertions to catch the state before the crash).
    *   Inspect variables at the moment of failure.
    *   Identify if the error is **Recoverable** (network, input) or **Unrecoverable** (logic bug, OOM).
3.  **Phase 3: Root Cause Analysis**:
    *   Determine *why* the error occurred.
    *   Reference `resources/error_handling_philosophies.md` to determine if the logic should use exceptions, result types, or explicit validation.
4.  **Phase 4: Implementation & Verification**:
    *   Apply the fix ensuring resource cleanup (finally/defer/with).
    *   Run the reproduction test to verify the fix.
    *   Verify "Defense in Depth": Add guards to prevent similar future failures.

## Constraints
- **Preserve Context**: Never swallow errors (`except: pass`). Always log or re-throw with context.
- **Fail Fast**: Fixes should validate state early rather than letting corrupt state propagate.
- **No Placeholders**: Provide the exact code for the fix.

## Resources
- Troubleshooting Checklist: `resources/troubleshooting_checklist.md`
- Error Philosophies: `resources/error_handling_philosophies.md`
