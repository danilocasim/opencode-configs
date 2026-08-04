---
name: nextjs
description: Next.js App Router + RSC skill tree (architecture, boundaries, data, mutations)
---

# Next.js Skill Tree Index

Use this index to load only the file(s) needed for the current task.

## When to load

- Building or refactoring a Next.js App Router codebase.
- Deciding Server vs Client Component boundaries.
- Designing data fetching, cache, and revalidation behavior.
- Implementing mutations with Server Actions.

## When NOT to load

- Project is not Next.js App Router.
- Task is framework-agnostic frontend architecture only.
- Task is backend-only with no Next.js runtime concerns.

## Routing table

| If the task is about...                                 | Load file                                 |
| ------------------------------------------------------- | ----------------------------------------- |
| Overall system shape and rendering strategy             | `architecture.md`                         |
| Auth, sessions, and request identity                    | `auth-and-sessions.md`                    |
| Middleware and route handlers                           | `middleware-and-route-handlers.md`        |
| Input validation and form patterns                      | `validation-and-forms.md`                 |
| Error, loading, and not-found boundaries                | `error-and-loading-boundaries.md`         |
| Atomic design with shared primitives + feature-local UI | `atomic-components.md`                    |
| Folder layout for feature ownership and reusable UI     | `component-folder-structure.md`           |
| Route segments, layouts, RSC/client boundaries          | `app-router-and-rsc-boundaries.md`        |
| Server fetching, caching, and revalidation strategy     | `data-fetching-cache-and-revalidation.md` |
| Forms, writes, optimistic UI, Server Actions            | `server-actions-and-mutations.md`         |
| Recipe: protect a route group                           | `recipes-protected-routes.md`             |
| Recipe: server action form with validation              | `recipes-server-action-form.md`           |
| Commenting/documentation standards                      | `documentation-and-comments.md`           |
| Testing strategy for Node/Next.js                       | `../testing/node-nextjs.md`               |

## Typical load combos

- New feature end-to-end:
  - `architecture.md`
  - `auth-and-sessions.md`
  - `component-folder-structure.md`
  - `app-router-and-rsc-boundaries.md`
  - `data-fetching-cache-and-revalidation.md`
  - `server-actions-and-mutations.md`
- UI system cleanup:
  - `atomic-components.md`
  - `component-folder-structure.md`
  - `documentation-and-comments.md`

## Related skills

- React conventions: `../react/SKILL.md`
- TypeScript strictness: `../typescript/SKILL.md`
- API contracts: `../api/SKILL.md`
- Documentation routing: `../documentation/SKILL.md`
