# Error and Loading Boundaries

Next.js App Router gives you file-based boundaries (`loading.tsx`, `error.tsx`, `not-found.tsx`). Use them intentionally so failures degrade predictably and slow paths don’t freeze the UI.

## When to load

- You are adding `loading.tsx`, `error.tsx`, or `not-found.tsx`.
- You need a consistent “failure surface” for a route group.
- You are debugging confusing error propagation in App Router.

## When NOT to load

- You only need mutation patterns (`server-actions-and-mutations.md`).
- You only need caching strategy (`data-fetching-cache-and-revalidation.md`).

## Core rules

- Use `loading.tsx` for slow data fetches in a segment.
- Use `error.tsx` for recoverable segment-level runtime errors; provide a `reset`.
- Use `not-found.tsx` for missing resources; call `notFound()` from server code.
- Keep boundaries small and presentational.
- Don’t swallow errors silently; log on the server where appropriate.

## Minimal examples

Segment loading:

```tsx
// app/projects/loading.tsx
export default function Loading() {
  return <p>Loading projects...</p>;
}
```

Segment error boundary:

```tsx
// app/projects/error.tsx
"use client";

export default function Error({ reset }: { reset: () => void }) {
  return (
    <div>
      <p role="alert">Something went wrong.</p>
      <button onClick={reset}>Try again</button>
    </div>
  );
}
```

Not found:

```ts
import { notFound } from "next/navigation";

export default async function ProjectPage({ params }: { params: { id: string } }) {
  const project = await loadProject(params.id);
  if (!project) notFound();
  return <div>{project.name}</div>;
}
```

## Anti-patterns

- Putting business logic inside boundaries.
- Catching errors in server components just to return empty UI.
- Using `loading.tsx` everywhere instead of fixing slow waterfalls.
- Client-side try/catch around server-side failures.

## Checklist

- Boundary exists at the right segment (not too global).
- `error.tsx` provides a recovery path (`reset`).
- 404s use `notFound()` and `not-found.tsx`.
- Boundaries are presentational and easy to maintain.
