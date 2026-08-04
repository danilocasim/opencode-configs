# Recipe: Release Checklist

Use this before shipping to TestFlight/Play or production.

## When to load

- You are preparing a release.
- You want a minimal checklist that catches common store failures.

## When NOT to load

- You are only doing a web deploy.
- You are adding a plugin and not shipping yet.

## Core rules

- No dev URLs/config in release builds.
- Versions bumped.
- Native projects synced.
- Device smoke test done.
- Monitoring ready.

## Minimal examples

Checklist:

```text
1) verify capacitor.config (no server.url)
2) bump iOS build number + Android versionCode
3) npx cap sync
4) build release artifacts
5) smoke test (login, critical flow)
6) submit + monitor
```

## Anti-patterns

- Shipping without device testing.
- Shipping after adding native deps with no soak.
- No rollback plan.

## Checklist

- Config verified.
- Versions bumped.
- Sync clean.
- Smoke test passed.
- Monitoring/alerts ready.
