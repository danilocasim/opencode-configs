# Server Actions and Mutations

Writes are where consistency breaks. Centralizing mutations in Server Actions keeps auth, validation, and invalidation reliable.

## When to load

- Building forms or mutations in App Router.
- Adding optimistic UI with rollback paths.
- Standardizing mutation contracts and error handling.

## When NOT to load

- Task is read-side cache tuning only (`data-fetching-cache-and-revalidation.md`).
- Task is route boundary design only (`app-router-and-rsc-boundaries.md`).

## Core rules

- Perform writes on the server (Server Actions or route handlers).
- Validate all action inputs at boundary.
- Return explicit success/error shape.
- Revalidate affected tags/paths in the same action.

## Common patterns

- Form -> Server Action -> validate/auth -> mutate -> revalidate -> return typed result.
- Action result shape: `{ ok: true, value }` or `{ ok: false, code, message, fields }`.
- Keep action files scoped by domain/feature.

## Minimal examples

Typed action result shape:

```ts
type ActionResult<T> = { ok: true; value: T } | { ok: false; code: string; message: string };

function requireNonEmpty(input: string, field: string): ActionResult<string> {
  const v = input.trim();

  if (!v) {
    return { ok: false, code: "invalid", message: `${field} is required` };
  }

  return { ok: true, value: v };
}
```

```ts
// features/projects/actions/create-project.ts
"use server";

import { revalidateTag } from "next/cache";

export async function createProject(formData: FormData): Promise<ActionResult<{ id: string }>> {
  const nameRes = requireNonEmpty(String(formData.get("name") ?? ""), "name");

  if (!nameRes.ok) return nameRes;

  const res = await fetch("https://example.internal/projects", {
    method: "POST",
    body: JSON.stringify({ name: nameRes.value }),
  });

  if (!res.ok) {
    return { ok: false, code: "server", message: "failed to create" };
  }

  revalidateTag("projects");

  return { ok: true, value: (await res.json()) as { id: string } };
}
```

## Anti-patterns

- Client-side direct writes to protected resources.
- Mutation without revalidation.
- One action file handling unrelated domains.
- Throwing untyped errors directly into UI.

## Checklist

- Is mutation server-side and authorized?
- Are validation and error contracts explicit?
- Is invalidation mapped to the read model?
- Is optimistic UI rollback-safe?

## References

- Server Actions: https://nextjs.org/docs/app/building-your-application/data-fetching/server-actions-and-mutations
