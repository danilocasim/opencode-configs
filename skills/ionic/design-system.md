# Design System (Ionic)

Ionic is designed to be themed. A production design system is mostly: tokens (CSS variables) + a few component wrappers + usage rules.

## When to load

- You are defining brand colors, type scale, spacing, and component defaults.
- You want consistent UI across multiple small apps.
- You need guidance for theming Ionic via CSS variables.

## When NOT to load

- You are building one-off page UI.
- You are doing native build workflows (use `../capacitor/SKILL.md`).

## Core rules

- Use CSS variables as the single source of truth for colors and typography.
- Keep tokens in one file and override Ionic variables intentionally.
- Wrap high-leverage components (Button, Field, Sheet) to enforce usage patterns.
- Avoid ad-hoc inline styles for colors/spacing.
- Test in both iOS and MD modes (if you support both).

## Minimal examples

Token file posture:

```css
/* src/theme/tokens.css */
:root {
  --ds-space-1: 4px;
  --ds-space-2: 8px;
  --ds-space-3: 12px;
  --ds-space-4: 16px;

  --ds-radius-sm: 10px;
  --ds-radius-md: 14px;

  --ds-font-body: 16px;
  --ds-font-title: 24px;

  --ds-color-bg: #0b0d12;
  --ds-color-card: #121622;
  --ds-color-text: #f2f5ff;
  --ds-color-muted: #a8b0c2;
  --ds-color-primary: #4b7bff;
  --ds-color-danger: #ff4d4d;
}
```

Map tokens into Ionic theme variables:

```css
/* src/theme/ionic-overrides.css */
:root {
  --ion-background-color: var(--ds-color-bg);
  --ion-text-color: var(--ds-color-text);

  --ion-color-primary: var(--ds-color-primary);
  --ion-color-primary-contrast: #ffffff;
  --ion-color-danger: var(--ds-color-danger);
}
```

Small wrapper component to enforce intent:

```tsx
import { IonButton } from "@ionic/react";

export function PrimaryButton({
  children,
  loading,
  ...props
}: React.ComponentProps<typeof IonButton> & { loading?: boolean }) {
  return (
    <IonButton expand="block" disabled={loading || props.disabled} {...props}>
      {children}
    </IonButton>
  );
}
```

## Anti-patterns

- Multiple token sources (design tokens in JS + CSS with drift).
- Hardcoded colors in components.
- Wrapping every Ionic component (too heavy).

## Checklist

- Tokens centralized.
- Ionic variables mapped intentionally.
- A few wrappers enforce consistent patterns.
- Visual QA in iOS/MD modes.
