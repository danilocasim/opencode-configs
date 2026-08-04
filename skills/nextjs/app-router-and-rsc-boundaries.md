# App Router and RSC Boundaries

Correct Server/Client boundaries are the main lever for performance, security, and maintainability in Next.js App Router.

## When to load

- Deciding if a component should be server or client.
- Designing route segments, layouts, and route groups.
- Fixing hydration or bundle-size issues caused by boundary mistakes.

## When NOT to load

- Task is only folder taxonomy (`component-folder-structure.md`).
- Task is only cache/revalidation policy (`data-fetching-cache-and-revalidation.md`).

## Core rules

- Server Component by default.
- Add `'use client'` only for browser APIs or interactive hooks.
- Keep client islands small; push fetches up to server boundaries.
- Pass serializable props across server/client boundary.
- Never import server-only modules into Client Components.

## Common patterns

- `layout.tsx`: persistent shell and shared reads.
- `page.tsx`: route content and composition.
- `loading.tsx`: route fallback.
- `error.tsx`: route-scoped recovery.
- Route groups `(group)` for organization without URL changes.

## Minimal examples

Server page fetches and composes, client component handles interaction:

```tsx
// app/projects/page.tsx
import { ProjectsList } from "@/features/projects/components/projects-list";
import { getProjects } from "@/features/projects/data/get-projects";

export default async function ProjectsPage() {
  const projects = await getProjects();

  return <ProjectsList projects={projects} />;
}
```

```tsx
// features/projects/components/projects-list.tsx
"use client";

import { useState } from "react";

export function ProjectsList({ projects }: { projects: { id: string; name: string }[] }) {
  const [q, setQ] = useState("");

  const filtered = projects.filter((p) => p.name.toLowerCase().includes(q.toLowerCase()));

  return (
    <div>
      <input value={q} onChange={(e) => setQ(e.target.value)} />
      <ul>
        {filtered.map((p) => (
          <li key={p.id}>{p.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

## Anti-patterns

- Broad `'use client'` at high tree levels.
- Business/data logic hidden inside interactive leaf components.
- Leaking server dependencies into client bundles.

## Checklist

- Does client code only exist where interactivity is required?
- Are secure reads/writes on server boundaries?
- Are serialization boundaries explicit and safe?

## References

- Server and Client Components: https://nextjs.org/docs/app/building-your-application/rendering/server-components
- App Router file conventions: https://nextjs.org/docs/app/api-reference/file-conventions
