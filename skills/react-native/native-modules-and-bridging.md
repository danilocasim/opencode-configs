# Native Modules and Bridging

Native integration is high-leverage and high-risk: it affects build stability, upgrades, and platform parity. Keep boundaries explicit and the JS surface small.

## When to load

- You are adding a native dependency.
- You need to bridge a native capability to JS.
- You are debugging iOS/Android build issues due to native modules.

## When NOT to load

- You can use an existing cross-platform library.
- You are on Expo Managed and should prefer Expo modules (use `../expo/native-modules-and-prebuild.md`).

## Core rules

- Prefer battle-tested libraries over custom bridges.
- Keep the JS API minimal and typed.
- Ensure parity: implement both iOS and Android or provide a safe fallback.
- Keep native side effects explicit; avoid hidden initialization.
- Document installation steps and platform caveats.

## Minimal examples

Boundary design:

```text
JS: lib/<capability>.ts exports typed functions
Native: platform implementation behind a module
```

Fallback posture:

```text
if capability unavailable -> return explicit error (not crash)
```

## Anti-patterns

- One-off native code with no tests and no docs.
- Android-only implementation.
- Exposing a huge native surface area to JS.

## Checklist

- JS surface typed and minimal.
- iOS and Android parity or explicit fallback.
- Build/install docs written.
- Upgrade impact understood.
