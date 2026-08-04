# Native Platforms (iOS and Android)

Capacitor creates native projects for you, but production quality depends on keeping iOS/Android projects clean, reproducible, and aligned with store requirements.

## When to load

- You are adding iOS/Android platforms.
- You are changing bundle IDs, permissions, or app icons.
- Native builds fail in CI or on a teammate's machine.

## When NOT to load

- You are writing plugin wrappers (`plugins-and-bridging.md`).
- You are doing release process (`builds-and-release.md`).

## Core rules

- Treat `ios/` and `android/` as source-controlled build artifacts: commit them, but avoid hand-editing without documentation.
- Prefer config/plugins over editing native project files directly.
- Keep native dependencies minimal; every native dep increases upgrade risk.
- Test on real devices for permissions, push, deep links, and keyboard.

## Minimal examples

Add platforms (typical):

```bash
npx cap add ios
npx cap add android
npx cap sync
```

Native edits rule:

```text
If you edit ios/ or android/, document why + how to reproduce.
Prefer a plugin/config change when possible.
```

## Anti-patterns

- Editing Xcode/Gradle project files manually for app logic.
- Adding native dependencies with no upgrade plan.
- Platform parity drift (feature works on iOS only).

## Checklist

- Platforms added and `cap sync` runs clean.
- Native changes are documented.
- Both platforms tested.
- CI build is reproducible.
