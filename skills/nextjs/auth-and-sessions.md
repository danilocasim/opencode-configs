# Auth and Sessions

Auth decisions should happen on the server. Treat session state as an input to authorization, not as “UI state” managed in client components.

## When to load

- You need a pattern for session lookup (server components, route handlers, server actions).
- You are building protected pages / route groups.
- You need guidance for “who is the current user?” plumbing.

## When NOT to load

- You only need caching/revalidation strategy (`data-fetching-cache-and-revalidation.md`).
- You are designing authorization rules (roles/policies) independent of Next.js.

## Core rules

- Prefer server-side identity: read the session in Server Components, Server Actions, or Route Handlers.
- Client components should receive the minimal identity they need (e.g. `userId`, `email`), not raw session objects.
- Fail closed: unauthenticated requests should redirect or return 401/403.
- Make auth checks consistent: one helper for “require user” and one for “optional user”.
- Never trust client-provided user IDs; derive identity from the session.

## Minimal examples

Server-side session guard helper:

```ts
// lib/auth/require-user.ts
import { redirect } from "next/navigation";

export type SessionUser = { id: string; email: string };

export async function requireUser(): Promise<SessionUser> {
  const user = await getUserFromSession();
  if (!user) redirect("/login");
  return user;
}

async function getUserFromSession(): Promise<SessionUser | null> {
  // Implementation depends on the repo (Auth.js/NextAuth, custom cookies, etc.).
  return null;
}
```

Use in a server component:

```tsx
export default async function SettingsPage() {
  const user = await requireUser();
  return <div>Signed in as {user.email}</div>;
}
```

## Anti-patterns

- Fetching “current user” from the browser without server verification.
- Duplicating auth logic in many pages (inconsistent failure modes).
- Passing full session tokens to client components.
- Mixing auth checks with mutation logic (keep helpers small and reusable).

## Checklist

- Identity derived on the server, not from client input.
- Auth failure mode is explicit (redirect or 401/403).
- Shared helpers exist (`requireUser`, `optionalUser`).
- Client gets only minimal identity data.
