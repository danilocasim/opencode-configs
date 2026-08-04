---
description: Design and implement UI components or pages through the shared UI workflow
agent: orchestrator
---

Load the `web-designer` skill first and inspect the project's existing design
system and shadcn/ui setup.

Request:

```text
$ARGUMENTS
```

- For clear implementation requirements, route to the Visual Engineer.
- For a new high-impact experience, major redesign, or unresolved product flow,
  route to the UI/UX Analyst first, then hand the approved direction to the
  Visual Engineer.
- Reuse project-owned shadcn/ui primitives when compatible; do not overwrite
  customized components blindly or present default shadcn styling as design.
- Verify responsive behavior and accessibility in the browser when code changes.
