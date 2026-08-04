# Platform Differences (iOS vs Android)

iOS and Android share React Native, but the OS conventions differ. Design for each platform’s expectations instead of forcing a single behavior everywhere.

## When to load

- You are implementing a feature that behaves differently across iOS/Android.
- You are debugging platform-only bugs.
- You need rules for permissions, back behavior, and UI components.

## When NOT to load

- You are tuning performance (`performance.md`).
- You are working on Expo build/release plumbing (use `../expo/SKILL.md`).

## Core rules

- Android has a hardware/software back button; design back behavior intentionally.
- iOS gestures (swipe back) are common; don’t break them.
- Permissions are different: request late, explain why, and handle denial.
- Keep platform conditionals localized (file suffixes or adapter functions).
- Test on real devices for keyboard, safe areas, and gesture conflicts.

## Minimal examples

Prefer platform files over scattered conditionals:

```text
Header.ios.tsx
Header.android.tsx
```

Back handling (conceptual):

```text
Android: intercept back for modals/flows only
iOS: allow gesture back unless it breaks data integrity
```

Android back handler (only when you must):

```ts
import { BackHandler } from "react-native";
import { useEffect } from "react";

export function useAndroidBackGuard(enabled: boolean, onBack: () => boolean) {
  useEffect(() => {
    if (!enabled) return;
    const sub = BackHandler.addEventListener("hardwareBackPress", () => onBack());
    return () => sub.remove();
  }, [enabled, onBack]);
}
```

Android ripple vs iOS opacity feedback:

```tsx
import { Platform, Pressable } from "react-native";

<Pressable
  android_ripple={Platform.OS === "android" ? { color: "rgba(255,255,255,0.12)" } : undefined}
  style={({ pressed }) => [{ opacity: pressed && Platform.OS === "ios" ? 0.7 : 1 }]}
>
  {/* ... */}
</Pressable>;
```

## Anti-patterns

- Disabling iOS back gesture globally.
- Treating permission denial as an error instead of a state.
- Copying web UX (hover, tiny tap targets).

## Checklist

- Back behavior defined for Android.
- Gesture navigation works on iOS.
- Permission flows handle deny/blocked states.
- Platform branching is contained.
