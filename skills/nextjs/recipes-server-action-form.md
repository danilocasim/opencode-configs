# Recipe: Server Action Form with Validation

Use this when you need a consistent pattern for a form that calls a Server Action, validates inputs, and renders field errors.

## When to load

- You are building a new form backed by a Server Action.
- You need a repeatable ok/error contract and field error rendering.
- You are standardizing mutation UX across features.

## When NOT to load

- You are building an API route handler (`middleware-and-route-handlers.md`).
- You only need cache invalidation strategy (`data-fetching-cache-and-revalidation.md`).

## Core rules

- Server Action validates inputs and returns `{ ok, message, fieldErrors }`.
- Client component renders errors and does not re-implement business rules.
- Keep feature code colocated (e.g. `features/<domain>/actions/*`).
- Revalidate tags/paths inside the action after a successful write.

## Minimal examples

Server Action:

```ts
"use server";

import { revalidateTag } from "next/cache";

type Result =
  | { ok: true; value: { id: string } }
  | { ok: false; message: string; fieldErrors?: Record<string, string> };

export async function createProject(formData: FormData): Promise<Result> {
  const name = String(formData.get("name") ?? "").trim();
  if (!name) return { ok: false, message: "invalid", fieldErrors: { name: "required" } };

  // ... auth + write ...
  revalidateTag("projects");
  return { ok: true, value: { id: "p_123" } };
}
```

Client form:

```tsx
"use client";

import { useState } from "react";
import { createProject } from "../actions/create-project";

export function CreateProjectForm() {
  const [nameError, setNameError] = useState<string | null>(null);

  return (
    <form
      action={async (fd) => {
        const res = await createProject(fd);
        setNameError(res.ok ? null : (res.fieldErrors?.name ?? res.message));
      }}
    >
      <label>
        Name
        <input name="name" aria-invalid={Boolean(nameError)} />
      </label>
      {nameError ? <p role="alert">{nameError}</p> : null}
      <button type="submit">Create</button>
    </form>
  );
}
```

## Anti-patterns

- Duplicating validation in client and server with different rules.
- Throwing exceptions from the action and relying on a global error boundary.
- Forgetting invalidation after a successful mutation.

## Checklist

- Server action validates and returns stable errors.
- Client renders field errors accessibly.
- Invalidation occurs inside the action.
- Feature code is colocated and easy to find.
