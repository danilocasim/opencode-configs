# Native Modules and Prebuild

Expo Managed is easiest when you stay inside the Expo SDK. When you need native modules, use a dev client and be deliberate about prebuild/config plugins.

## When to load

- You need a native dependency not supported by Expo Go.
- You are using config plugins.
- You are deciding between managed and bare workflows.

## When NOT to load

- You are doing pure JS app work.
- You are adding general RN native modules without Expo tooling (use `../react-native/native-modules-and-bridging.md`).

## Core rules

- Prefer Expo SDK modules first.
- Use a dev client when native code is required.
- Keep config plugins minimal and well-documented.
- Avoid frequent prebuild churn; treat native folders as generated.
- Test both platforms for parity.

## Minimal examples

Decision posture:

```text
Expo Go: JS-only + supported SDK modules
Dev client: native dependencies
Bare: full control, more maintenance
```

## Anti-patterns

- Adding native dependencies without switching off Expo Go.
- Editing generated native files by hand with no strategy.
- Platform-only dependencies with no fallback.

## Checklist

- Dev client used when required.
- Config plugin documented.
- Parity tested on iOS and Android.
- Upgrade impact considered.
