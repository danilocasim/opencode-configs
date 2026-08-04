# Accessibility (Ionic)

Ionic components provide a good baseline, but accessibility still requires consistent labeling, focus behavior, and error messaging.

## When to load

- You are building forms, modals, and interactive lists.
- You are adding custom components around Ionic primitives.
- You need an a11y checklist for review.

## When NOT to load

- You are only doing theming (`design-system.md`).
- You are only doing navigation (`routing-and-navigation.md`).

## Core rules

- Ensure every interactive element has an accessible label.
- Make validation errors discoverable (not only color).
- Use semantic headings and consistent page structure.
- Keep focus behavior sane for modals.

## Minimal examples

Checklist posture:

```text
labels present
errors readable
modal focus sane
keyboard navigation works
```

## Anti-patterns

- Icon-only buttons with no label.
- Errors only as red text with no context.
- Custom components that break tab/focus order.

## Checklist

- Labels exist.
- Errors accessible.
- Modal focus tested.
- Keyboard navigation tested.
