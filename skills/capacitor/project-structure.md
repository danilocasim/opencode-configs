# Project Structure (Capacitor)

Capacitor works best when you keep web code owned by the web app, and treat native folders as build artifacts with minimal custom code.

## When to load

- You are adding Capacitor to an existing repo.
- You need a folder strategy for `ios/` and `android/`.
- You want boundaries between web app, Capacitor config, and native customization.

## When NOT to load

- You are debugging native build failures (`native-platforms-ios-android.md`).
- You only need plugin patterns (`plugins-and-bridging.md`).

## Core rules

- Keep the web app as the source of truth; native projects should not contain app logic.
- Minimize native edits; prefer Capacitor config and plugins.
- Create a typed `src/native/` wrapper layer so your web code doesn't import Capacitor directly everywhere.
- Keep `ios/` and `android/` committed for production apps (reproducibility + CI), but treat them as generated-with-overrides.

## Minimal examples

Suggested structure:

```text
src/
  native/
    index.ts
    push.ts
    deeplinks.ts
    storage.ts
    permissions.ts
  features/
  ui/
capacitor.config.ts
ios/
android/
```

Typed wrapper posture:

```ts
// src/native/index.ts
export * as NativePush from "./push";
export * as NativeLinks from "./deeplinks";
export * as NativeStorage from "./storage";
```

## Anti-patterns

- Native-only logic duplicated from web.
- Direct `import { Plugins } from ...` scattered across many feature files.
- Editing generated native files without documenting why.

## Checklist

- Web app owns business logic.
- Native folders have minimal custom code.
- Capacitor usage is behind a typed wrapper layer.
- Native changes are documented and reproducible.
