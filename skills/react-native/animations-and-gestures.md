# Animations and Gestures

Animations communicate state changes; gestures make mobile UI feel native. Favor a small set of consistent motion patterns over random micro-animations.

## When to load

- You are adding transitions, shared element motion, or gesture-driven UI.
- You need rules for animation performance and reduced motion.

## When NOT to load

- You only need general UI tokens (`ui-ux-and-design-system.md`).
- You are debugging list jank (`performance.md`).

## Core rules

- Prefer native-driven animations (e.g. Reanimated) for gesture-linked motion.
- Keep motion meaningful: navigation transitions, feedback, state changes.
- Respect reduced motion settings.
- Avoid animating layout in ways that trigger expensive re-layout repeatedly.
- Keep gesture handlers scoped; avoid global gesture conflicts.

## Minimal examples

Motion “budget”:

```text
page transition
staggered reveal (small)
gesture-driven sheet
```

Reduced motion posture:

```text
if reduceMotion: disable non-essential animations
```

## Anti-patterns

- Animations that block interaction.
- Gesture conflicts (horizontal swipe inside horizontal lists).
- Motion used as decoration with no UX purpose.

## Checklist

- Motion has a purpose.
- Animations are performant.
- Reduced motion path exists.
- Gestures do not conflict.
