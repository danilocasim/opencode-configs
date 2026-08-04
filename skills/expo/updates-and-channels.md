# Updates and Channels (expo-updates)

Over-the-air updates are powerful and risky. Use channels/branches intentionally, stage rollouts, and keep a fast rollback plan.

## When to load

- You are configuring expo-updates.
- You need a rollout/rollback strategy.
- You are deciding channel structure (dev/preview/prod).

## When NOT to load

- You are working on EAS build itself (`eas-build-and-dev-client.md`).
- You are doing app-level error boundaries (use RN/feature guidance).

## Core rules

- Separate channels per environment.
- Treat updates as releases: test before promoting.
- Roll out gradually when possible.
- Keep an emergency rollback plan (revert update / new update).
- Monitor crash rates by release.

## Minimal examples

Channel posture:

```text
development
preview
production
```

Update commands (typical):

```bash
eas update --channel preview --message "fix: login crash"
eas update --channel production --message "feat: new settings screen"
```

Compatibility rule to keep in mind:

```text
If native code changes, you usually need a new build.
OTA updates must remain compatible with the installed native binary.
```

## Anti-patterns

- One channel for everything.
- Shipping risky migrations via OTA without compatibility.
- No monitoring on rollout.

## Checklist

- Channels defined.
- Rollout plan exists.
- Rollback plan exists.
- Monitoring by release.
