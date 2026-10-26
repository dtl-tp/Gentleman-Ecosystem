# Troubleshooting & Error Handling Checklist

Use this checklist during every debugging session to ensure no steps are skipped.

## Reproduction
- [ ] Have you captured the exact error message and stack trace?
- [ ] Have you created a script/test that reproduces the error in < 5 seconds?
- [ ] Does the reproduction fail for the exact same reasons as the original bug?

## Isolation
- [ ] Are you catching the error at the right level? (Catch where you can handle).
- [ ] Have you added logging/print statements *before* the crash to see the state?
- [ ] If it's a silent bug (no crash), have you added assertions to find where the data goes stale?

## Implementation
- [ ] Does the fix "Preserve Context"? (No empty catch blocks).
- [ ] Does the fix "Fail Fast"? (Validation at the top of the function).
- [ ] Are resources (files, sockets) cleaned up using `try-finally` or `using`?

## Verification
- [ ] Does the reproduction script now pass?
- [ ] Have you checked for side effects in related modules?
- [ ] Have you added a permanent regression test to the suite?
