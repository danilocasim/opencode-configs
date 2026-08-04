# Middleware and Route Handlers

Middleware is for fast edge decisions (redirects, rewrites, headers). Route handlers are for HTTP boundaries (webhooks, APIs, file uploads) that need explicit request/response contracts.

## When to load

- You are adding `middleware.ts` behavior.
- You are building a `route.ts` HTTP endpoint.
- You need to standardize auth gating, request validation, and response errors.

## When NOT to load

- You are building UI-only pages with no HTTP boundary.
- You should use Server Actions for app mutations (`server-actions-and-mutations.md`).

## Core rules

- Middleware must be fast and deterministic: no heavy IO.
- Use middleware for routing decisions and coarse gating; do fine-grained auth in handlers/actions.
- Route handlers validate inputs and return stable JSON error shapes.
- Prefer server-side redirects (`NextResponse.redirect`) over client hacks.
- Do not leak internal errors to clients; map to a consistent contract.

## Minimal examples

Auth gating in middleware (coarse):

```ts
// middleware.ts
import { NextResponse, type NextRequest } from "next/server";

export function middleware(req: NextRequest) {
  const isAuthed = Boolean(req.cookies.get("session")?.value);

  if (!isAuthed && req.nextUrl.pathname.startsWith("/app")) {
    const url = req.nextUrl.clone();
    url.pathname = "/login";
    return NextResponse.redirect(url);
  }

  return NextResponse.next();
}

export const config = {
  matcher: ["/app/:path*"],
};
```

Route handler with explicit JSON contract:

```ts
// app/api/health/route.ts
import { NextResponse } from "next/server";

export async function GET() {
  return NextResponse.json({ ok: true });
}
```

## Anti-patterns

- Doing DB/network work in middleware.
- Relying on middleware alone for authorization.
- Route handlers that return inconsistent error shapes.
- “Catch all” error responses without status codes.

## Checklist

- Middleware work is bounded and fast.
- Handler validates inputs and maps errors to a stable contract.
- Auth gating uses the right layer (middleware vs handler/action).
- Status codes match the error type (400/401/403/404/500).
