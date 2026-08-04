# Recipe: Protected Routes

Use this when you need a repeatable pattern for protecting a route group (e.g. `/app/*`) with a consistent redirect/401 behavior.

## When to load

- You are adding a protected route group.
- You want a minimal, consistent auth gate.
- You need both middleware gating and server-side enforcement.

## When NOT to load

- You only need in-component identity (`auth-and-sessions.md`).
- You are implementing authorization rules (roles/policies) rather than authentication.

## Core rules

- Use middleware for coarse routing decisions (redirect to `/login`).
- Enforce again on the server in page/actions (defense in depth).
- Keep the protected surface minimal: match only what needs auth.
- Use one helper (`requireUser`) so behavior is uniform.

## Minimal examples

1. Gate the route group in `middleware.ts`:

```ts
export const config = { matcher: ["/app/:path*"] };
```

2. Enforce on the server in the layout:

```tsx
// app/app/layout.tsx
import { requireUser } from "@/lib/auth/require-user";

export default async function AppLayout({ children }: { children: React.ReactNode }) {
  await requireUser();
  return <>{children}</>;
}
```

## Anti-patterns

- Relying only on middleware for security.
- Sprinkling ad-hoc redirects across pages.
- Protecting more routes than necessary (breaks public pages and caching).

## Checklist

- Middleware matcher targets only protected routes.
- Server-side enforcement exists in layout/page/action.
- Redirect/401 behavior is consistent.
