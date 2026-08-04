# Capacitor Integration

Most Ionic mobile apps ship with Capacitor. Keep native access behind wrappers and follow the Capacitor production playbooks.

## When to load

- You are adding device capabilities (camera, filesystem, push).
- You need patterns for safe plugin use in an Ionic app.
- You are debugging differences between web and device.

## When NOT to load

- You need deep native build/release details (use `../capacitor/SKILL.md`).
- You are doing pure UI work.

## Core rules

- Wrap Capacitor in `src/native/*`.
- Treat device-only features as optional: add web fallbacks.
- Validate and handle permission denial.
- Test on real devices.

## Minimal examples

Wrapper posture:

```ts
// src/native/storage.ts
import { Capacitor } from "@capacitor/core";
import { Preferences } from "@capacitor/preferences";

export async function setString(key: string, value: string): Promise<void> {
  if (!Capacitor.isNativePlatform()) {
    localStorage.setItem(key, value);
    return;
  }

  await Preferences.set({ key, value });
}
```

## Anti-patterns

- Plugin calls in random UI components.
- No parity testing on iOS/Android.
- Missing permission UX.

## Checklist

- Wrapper layer exists.
- Fallback behavior defined.
- Permission flows handled.
- Device QA done.
