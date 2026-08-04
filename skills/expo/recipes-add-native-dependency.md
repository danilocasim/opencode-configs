# Recipe: Add a Native Dependency

Use this when adding a library that requires native code (not supported by Expo Go).

## When to load

- You need to add a native module.
- You need a safe workflow for dev client + EAS build.

## When NOT to load

- The dependency is pure JS.
- Expo SDK already provides the capability.

## Core rules

- Prefer Expo SDK first.
- Switch to a dev client.
- Confirm iOS and Android parity.
- Document installation and any config plugin usage.
- Verify with a clean build.

## Minimal examples

Workflow:

```text
1) add dependency
2) configure (plugin/permissions)
3) build dev client
4) test on iOS + Android
5) add CI/EAS config if needed
```

## Anti-patterns

- Installing a native lib and expecting Expo Go to work.
- Only testing on one platform.
- Undocumented setup steps.

## Checklist

- Dev client built.
- Both platforms tested.
- Config documented.
- Clean build passes.
