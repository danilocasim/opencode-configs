# Validation and Forms

The fastest way to ship bugs is to accept unvalidated inputs. Validate at the boundary (Server Actions / route handlers), return typed errors, and keep client components focused on rendering.

## When to load

- You are building a form that triggers a Server Action.
- You need a consistent validation + error-return pattern.
- You want a safe default for parsing `FormData`.

## When NOT to load

- You are only tuning cache/revalidation.
- You are only deciding RSC/client boundaries.

## Core rules

- Validate all inputs on the server.
- Prefer explicit result shapes over throwing into UI.
- For `FormData`, coerce values deliberately (`String(...)`) and treat missing as empty.
- Return field errors separately from global errors.
- Keep form UI components dumb: render state, call action, display errors.

## Minimal examples

Result shape with field errors:

```ts
export type FormResult<T> =
  | { ok: true; value: T }
  | { ok: false; message: string; fieldErrors?: Record<string, string> };
```

Server Action boundary validation:

```ts
// features/projects/actions/create-project.ts
"use server";

import type { FormResult } from "@/lib/forms/form-result";

export async function createProject(formData: FormData): Promise<FormResult<{ id: string }>> {
  const name = String(formData.get("name") ?? "").trim();
  if (!name) return { ok: false, message: "invalid", fieldErrors: { name: "required" } };

  // ... auth + write ...
  return { ok: true, value: { id: "p_123" } };
}
```

Client component displays server-returned errors:

```tsx
"use client";

import { useState } from "react";
import { createProject } from "../actions/create-project";

export function CreateProjectForm() {
  const [error, setError] = useState<string | null>(null);

  return (
    <form
      action={async (fd) => {
        const res = await createProject(fd);
        setError(res.ok ? null : (res.fieldErrors?.name ?? res.message));
      }}
    >
      <input name="name" />
      <button type="submit">Create</button>
      {error ? <p role="alert">{error}</p> : null}
    </form>
  );
}
```

## Anti-patterns

- Trusting client-side validation as the source of truth.
- Throwing random exceptions from actions and hoping the UI renders them.
- Returning inconsistent error shapes across actions.
- Parsing `FormData` with implicit `as string` assumptions.

## Checklist

- Server validates every input.
- Action returns a stable ok/error contract.
- Field errors are mapped by field name.
- UI renders errors without knowing implementation details.
