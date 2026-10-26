# Error Handling Philosophies & Categories

Based on best practices for building resilient applications.

## 1. Philosophies
- **Exceptions**: Use for truly unexpected errors or exceptional conditions that disrupt normal flow.
- **Result Types**: Use for expected failures (e.g., validation, business logic errors) to force the caller to handle them.
- **Fail Fast**: Validate all inputs and state transitions at the earliest possible boundary.
- **Preserve Context**: When catching and re-throwing, use the `from` keyword (Python) or wrap the inner error to maintain the stack trace.

## 2. Error Categories
### Recoverable Errors
*Goal: Catch, log, and potentially retry or degrade gracefully.*
- Network timeouts / API Rate limits.
- Temporary database unavailability.
- Invalid user input (return 400).
- Missing optional configuration.

### Unrecoverable Errors
*Goal: Crash safely, log everything, and notify engineers.*
- Programming bugs (Null pointer, index out of bounds).
- Out of Memory / Stack Overflow.
- Corrupt local data or configuration.
- Illegal state transitions.

## 3. The "Fail Fast" Template
Always prefer early exit over nested logic:
```python
def process(data):
    if not data:
        raise ValueError("Data cannot be empty") # Fail Fast
    
    # ... rest of logic
```
