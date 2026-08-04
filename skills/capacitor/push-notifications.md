# Push Notifications (Capacitor)

Push is a product feature and an ops surface: permissions, token registration, deep links, and release monitoring must work end-to-end.

## When to load

- You are implementing push notifications.
- You need patterns for permission timing and token registration.
- You need tap/deep-link handling.

## When NOT to load

- You only need deep-link routing (`deeplinks-and-app-links.md`).
- You are doing build signing and store submission (`builds-and-release.md`).

## Core rules

- Ask for permission when value is clear.
- Treat tokens as sensitive identifiers; send to server and rotate/update.
- Use stable notification types/codes; keep payloads minimal.
- Handle taps in both cold and warm starts.
- Do not log full payloads with user data.

## Minimal examples

Token flow:

```text
permission -> get token -> send to server -> server targets device/user
```

Tap behavior:

```text
notification payload includes route + safe params
app validates -> navigates
```

## Anti-patterns

- Requesting permission at first launch.
- Storing tokens only on device.
- Unvalidated params from payload.

## Checklist

- Permission UX exists.
- Token registration is reliable.
- Tap routing validated.
- Release health monitored (crashes after push changes).
