# Data Fetching, Cache, and Revalidation

Most stale-data bugs come from unclear cache ownership. Define fetch intent up front: static, dynamic, or revalidated.

## When to load

- Implementing or debugging server-side data fetching.
- Choosing cache mode and revalidation strategy.
- Designing invalidation after writes.

## When NOT to load

- You only need component hierarchy guidance (`atomic-components.md`).
- You only need mutation implementation details (`server-actions-and-mutations.md`).

## Core rules

- Prefer server-side fetching in Server Components.
- Pick one intent per query: `force-cache`, `no-store`, or `revalidate`.
- Use domain tags for invalidation (`projects`, `project:{id}`).
- Keep read and write paths aligned on same tag/path invalidation keys.

## Common patterns

- `next: { revalidate: 60 }` for freshness windows.
- `revalidateTag` for domain-scoped invalidation.
- `revalidatePath` for route-scoped refresh where coupling is acceptable.

## Minimal examples

Tag-based caching on reads:

```ts
// features/projects/data/get-projects.ts
export async function getProjects() {
  const res = await fetch("https://example.internal/projects", {
    next: { tags: ["projects"], revalidate: 60 },
  });

  if (!res.ok) throw new Error("failed to load projects");

  return (await res.json()) as { id: string; name: string }[];
}
```

Mutation invalidates the same tag:

```ts
// features/projects/actions/create-project.ts
"use server";

import { revalidateTag } from "next/cache";

export async function createProject(name: string) {
  await fetch("https://example.internal/projects", {
    method: "POST",
    body: JSON.stringify({ name }),
  });

  revalidateTag("projects");
}
```

## Anti-patterns

- Blanket `no-store` everywhere.
- Mixed conflicting cache strategies with no intent.
- Broad path revalidation for narrow data changes.

## Checklist

- Is cache intent explicit for each critical fetch?
- Do write paths invalidate the exact read tags/paths?
- Is invalidation colocated with mutation logic?

## References

- Next.js data fetching: https://nextjs.org/docs/app/building-your-application/data-fetching
- Caching and revalidation: https://nextjs.org/docs/app/building-your-application/caching
