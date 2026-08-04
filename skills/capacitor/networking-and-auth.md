# Networking and Auth (WebView)

WebView networking behaves like a browser with extra footguns: cookies, CORS, and mixed content can break differently on device than on desktop.

## When to load

- Your app's auth works on web but not on device.
- You need rules for cookies vs tokens.
- You are making API calls from the WebView.

## When NOT to load

- You are designing backend auth flows (use `../auth/SKILL.md`).
- You only need plugin wrappers (`plugins-and-bridging.md`).

## Core rules

- Prefer HTTPS everywhere; avoid mixed content.
- If using cookies, ensure `SameSite`/`Secure` are compatible with your embedding and domain strategy.
- Be explicit about your API base URL per environment.
- Handle offline mode and timeouts.
- Treat 401/403 as state transitions (signed out / unauthorized).

## Minimal examples

Boundary contract for API calls:

```text
client: request -> map network errors -> map 401 to sign-out
do not throw raw fetch errors into UI
```

## Anti-patterns

- Relying on localhost URLs on device builds.
- Allowing cleartext in production.
- Silent failures when cookies aren't persisted.

## Checklist

- API base URL correct per environment.
- HTTPS and certs valid.
- Auth persistence strategy documented.
- Offline/timeouts handled.
