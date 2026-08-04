# Recipe: Add a Plugin Safely

Plugins are where production apps break (permissions, native deps, build config). Use a repeatable checklist.

## When to load

- You are adding any Capacitor plugin.
- You need a cross-platform parity plan.

## When NOT to load

- You only need web code changes.
- You are only changing Capacitor config.

## Core rules

- Prefer official/maintained plugins.
- Add one plugin at a time; verify builds.
- Add permission UX and denial paths.
- Wrap plugin calls behind a typed API.
- Test on real devices (both platforms).

## Minimal examples

Checklist:

```text
1) install plugin
2) cap sync
3) configure permissions (iOS Info.plist / Android manifest)
4) typed wrapper in src/native
5) smoke test on iOS + Android
6) document caveats
```

## Anti-patterns

- Installing multiple plugins before building.
- Ignoring permission denial.
- Testing only simulator.

## Checklist

- Builds succeed.
- Permissions correct.
- Wrapper contract stable.
- Device parity verified.
