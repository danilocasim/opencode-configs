---
description: Design and implement UI components or pages through the shared UI workflow
---

Load the `web-designer` skill first and inspect the project's existing design
system and shadcn/ui setup.

Request:

```text
$ARGUMENTS
```

- Work directly in the selected session, including economy sessions, for clear
  implementation requirements; no specialist handoff is required.
- For a new high-impact experience, major redesign, or unresolved product flow,
  clarify consequential decisions before implementation. A specialist review is
  optional only with parent approval and permitted task access/depth.
- Reuse project-owned shadcn/ui primitives when compatible; do not overwrite
  customized components blindly or present default shadcn styling as design.
- Verify responsive behavior and accessibility in the browser when code changes.
- Use available Playwright tools via `testing` guidance, or DevTools only when
  available and appropriate. Report unavailable browser verification honestly.
