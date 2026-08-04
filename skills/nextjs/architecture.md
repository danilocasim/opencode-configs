# Next.js Architecture (App Router)

App Router apps fail when boundaries are implicit. This file defines explicit boundaries so data flow, rendering, and mutation behavior stay predictable.

## When to load

- Choosing architecture for a new Next.js app or major refactor.
- Aligning team conventions for RSC-first design.
- Defining where reads and writes live.

## When NOT to load

- You only need folder naming details (`component-folder-structure.md`).
- You only need cache knobs (`data-fetching-cache-and-revalidation.md`).
- You only need mutation mechanics (`server-actions-and-mutations.md`).

## Core rules

- Default to Server Components for reads and composition.
- Use Client Components only for browser-only interactivity.
- Keep reads near server boundaries.
- Keep writes in Server Actions or route handlers.
- Prefer hybrid atomic structure: shared UI primitives + feature-local compositions.

## Common patterns

- Server route/page composes data and passes serializable props.
- Small client islands for interactive controls.
- Feature-level server modules for read models.
- Promote feature-local component to shared only after proven reuse.

## Minimal examples

Hybrid atomic + feature-first layout:

```text
components/
  ui/
    button.tsx
    input.tsx

features/
  projects/
    components/
      project-card.tsx
    actions/
      create-project.ts
    data/
      get-projects.ts
```

Promotion rule in practice:

```text
Start: features/projects/components/project-card.tsx

Promote to components/ui only if:
- used by 2+ features
- domain-neutral naming/API
- no feature-specific data dependencies
```

## Anti-patterns

- Global dumping ground in `components/` with no ownership.
- Marking large trees `'use client'` to make things work.
- Client fetch by default when server fetch is safer/faster.
- Premature shared abstractions before reuse exists.

## Checklist

- Is this component server by default unless client behavior is required?
- Is data fetched server-side where possible?
- Are writes centralized through server boundaries?
- Is ownership clear between `components/ui` and `features/*`?

## References

- Next.js docs: https://nextjs.org/docs
- App Router: https://nextjs.org/docs/app
