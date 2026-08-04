# Animations and Motion

Motion should communicate state changes and hierarchy, not decorate randomly. Keep patterns consistent and respect reduced motion.

## When to load

- You are adding transitions or interactive motion.
- You need guidelines for implicit vs explicit animations.
- You are debugging animation jank.

## When NOT to load

- You are doing list performance (`performance.md`).
- You are building basic layout (`widgets-layout-and-theming.md`).

## Core rules

- Prefer implicit animations for simple state changes.
- Use explicit controllers only when you need fine control.
- Keep durations consistent across the app.
- Avoid blocking interactions during animations.
- Respect accessibility settings when possible.

## Minimal examples

Implicit animation:

```dart
AnimatedContainer(
  duration: const Duration(milliseconds: 180),
  curve: Curves.easeOut,
  padding: EdgeInsets.all(selected ? 16 : 12),
  child: child,
)
```

## Anti-patterns

- Too many different durations/curves.
- Animations that delay user actions.
- Using controllers for simple cases.

## Checklist

- Motion has a purpose.
- Patterns are consistent.
- Performance verified.
