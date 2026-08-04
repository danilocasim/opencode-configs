# Next.js Documentation and Comments

In Next.js, behavior is split across server/client/cache boundaries. Comments should capture intent and boundary decisions, not restate syntax.

## When to load

- Writing docs for Next.js architecture or feature modules.
- Adding comments to clarify RSC boundaries, cache intent, or invalidation logic.
- Standardizing docs for components, actions, and data contracts.

## When NOT to load

- You need implementation mechanics for cache/revalidation.
- You only need route boundary rules.

## Core rules

- Document why component is server vs client.
- Document why fetch is static/dynamic/revalidated.
- Document which tags/paths each mutation invalidates.
- Prefer short decision comments near boundaries.
- Route broader style questions through `../documentation/SKILL.md`.

## Common patterns

- TSDoc for exported utilities/actions/hooks.
- One-line rationale above `'use client'` where non-obvious.
- Feature README section: reads, writes, invalidation map.

## Minimal examples

Rationale on a client island:

```tsx
"use client";

// Why client: this component uses local interactive state and DOM events.
export function SearchBox() {
  // ...
}
```

Cache intent + invalidation note:

```ts
// Why cache: projects list is safe to revalidate every 60s.
// Invalidation: mutations call revalidateTag("projects").
export async function getProjects() {
  // ...
}
```

## Anti-patterns

- Comments that duplicate obvious code behavior.
- Missing rationale for unusual cache strategy.
- Stale comments after boundary changes.

## Checklist

- Are boundary decisions documented where non-obvious?
- Are action contracts and invalidation paths documented?
- Are comments concise and kept in sync with behavior?

## References

- Next.js docs: https://nextjs.org/docs
- Documentation skill index: `../documentation/SKILL.md`
