# Permissions and Privacy

Permission prompts are UX: users must understand why you need access, and denial must be handled as a normal state.

## When to load

- You are using camera, photos, location, microphone, contacts, etc.
- You need a permission request flow.
- You need to avoid platform-only permission bugs.

## When NOT to load

- You are adding a plugin wrapper (`plugins-and-bridging.md`).
- You are doing store release (`builds-and-release.md`).

## Core rules

- Ask just-in-time (not on app launch).
- Provide a pre-permission explanation when appropriate.
- Handle 3 states: granted, denied, blocked.
- Keep permission logic centralized.
- Avoid surprising background collection.

## Minimal examples

Permission UX posture:

```text
show value -> request -> granted|denied
if blocked -> show "Open Settings" path
```

## Anti-patterns

- Requesting multiple permissions at startup.
- Treating denial as a crash-worthy error.
- Platform-only behavior with no parity testing.

## Checklist

- Request is value-timed.
- Denied/blocked UX exists.
- Logic centralized.
- Real-device QA on iOS + Android.
