# Component Folder Structure

Folder structure encodes ownership. Ownership reduces coupling and prevents a monolithic `components` directory.

## When to load

- Setting or enforcing component directory conventions.
- Refactoring a flat `components/` tree into feature ownership.
- Creating onboarding docs for where components should live.

## When NOT to load

- You need route/RSC boundary guidance (`app-router-and-rsc-boundaries.md`).
- You need cache semantics (`data-fetching-cache-and-revalidation.md`).

## Core rules

- `components/ui` is for shared primitives only.
- Feature UI belongs in `features/<feature>/components`.
- Feature reads/writes live with the feature (`data`, `actions`).
- Avoid vague folders like `common`, `shared2`, `misc`.

## Common patterns

```text
app/
  dashboard/page.tsx

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

## Minimal examples

Promote local to shared only after reuse:

```text
features/projects/components/project-empty-state.tsx  (first)
features/tasks/components/task-empty-state.tsx        (second)

Then consider a shared:
components/ui/empty-state.tsx
```

## Anti-patterns

- Domain-specific UI under `components/ui`.
- One giant `lib/` for unrelated reads/writes.
- Route files doing heavy business logic directly.

## Checklist

- Is ownership obvious from file path?
- Are shared primitives truly domain-neutral?
- Are feature actions/data colocated with the feature?

## References

- Next.js project structure: https://nextjs.org/docs/app/getting-started/project-structure
