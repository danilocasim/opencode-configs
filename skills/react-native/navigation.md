# Navigation (React Native)

Navigation is UX-critical. Keep navigation state separate from app state and avoid pushing navigation concerns into domain logic.

## When to load

- You are using React Navigation (or a non-Expo router stack).
- You need patterns for stacks, tabs, modals, deep links.
- You are standardizing navigation types.

## When NOT to load

- You are using Expo Router (use `../expo/expo-router.md`).
- You are designing UI tokens (`ui-ux-and-design-system.md`).

## Core rules

- Define a single navigation hierarchy (Stack + Tabs + modal routes).
- Keep route params typed.
- Prefer modal routes for transient flows (pickers, confirmations).
- Deep links map to stable routes with safe param parsing.
- Back behavior must be predictable on Android.

## Minimal examples

Hierarchy sketch:

```text
RootStack
  (AuthStack)
  (AppTabs)
  (Modals)
```

Type posture:

```ts
type RootStackParamList = {
  Home: undefined;
  Project: { id: string };
};
```

## Anti-patterns

- Passing large objects through route params.
- Navigation side effects inside reducers/services.
- Unvalidated deep-link params.

## Checklist

- Route params typed.
- Deep links validated.
- Android back behavior covered.
- Modal vs push patterns consistent.
