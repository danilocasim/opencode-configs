---
description: Apply and verify a focused repair when the issue is understood
---

Apply a focused repair for the following understood issue:

$ARGUMENTS

Approach:

1. Confirm the expected behavior and the affected scope.
2. Inspect the relevant code and nearby tests before editing.
3. Add or update the smallest regression test that proves the repair.
4. Implement the minimal fix.
5. Run the focused verification and report its exact outcome.

If the root cause or scope is unclear, stop and use `/debug` instead of
guessing.
