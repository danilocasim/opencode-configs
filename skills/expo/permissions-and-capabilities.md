# Permissions and Capabilities

Mobile permissions are UX-sensitive and failure-prone. Request permissions as late as possible, explain why, and handle denial as a normal state.

## When to load

- You are using camera, photos, location, notifications, contacts, etc.
- You need permission request UX rules.
- You are handling "denied" / "blocked" states.

## When NOT to load

- You only need platform UI differences (`../react-native/platform-differences.md`).
- You are working on updates/build tooling.

## Core rules

- Ask just-in-time, not on app launch.
- Provide a pre-permission explanation screen when appropriate.
- Handle 3 states: granted, denied, blocked (needs Settings).
- Keep permission logic in one adapter module.
- Test on real devices for OS prompts.

## Minimal examples

State model:

```text
unknown -> request -> granted | denied
denied can become blocked depending on OS behavior
```

## Anti-patterns

- Requesting everything at startup.
- Treating denial as an exception.
- No Settings deep link for blocked permissions.

## Checklist

- Request is just-in-time.
- Denied/blocked UX exists.
- Logic centralized.
- Real-device testing done.
