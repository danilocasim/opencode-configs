# Push Notifications

Push is a product surface and an ops surface. Treat tokens as sensitive, handle permission denial gracefully, and design a predictable notification taxonomy.

## When to load

- You are implementing push notifications.
- You are handling notification taps/deep links.
- You need patterns for token registration.

## When NOT to load

- You only need permissions UX (`permissions-and-capabilities.md`).
- You are doing server-side job delivery logic (use backend stack skills).

## Core rules

- Request permission only when value is clear.
- Store push tokens server-side; rotate/update as needed.
- Support deep links from notification payloads with safe param parsing.
- Keep notification categories stable (types/codes).
- Do not log full payloads containing user data.

## Minimal examples

Token flow:

```text
permission -> get token -> send to server -> server targets user/device
```

## Anti-patterns

- Requesting push permission on first launch.
- Handling notification taps with unvalidated params.
- Treating push tokens as non-sensitive.

## Checklist

- Permission is value-timed.
- Token registration is reliable.
- Tap/deep link handling is safe.
- Payload logging is controlled.
