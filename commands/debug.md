---
description: Diagnose an unclear failure and repair its root cause
---

Debug the following issue:

$ARGUMENTS

Workflow:

1. Clarify expected versus actual behavior and how to reproduce.
2. Reproduce the bug using existing tests or commands.
3. Trace the code path to find the true root cause.
4. Propose the smallest, safest code change that fixes the bug.
5. Add or update a regression test that captures the behavior.
6. Run the relevant tests and verify the fix.

Prefer minimal, well-documented fixes over broad refactors.
