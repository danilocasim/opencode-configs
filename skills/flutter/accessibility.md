# Accessibility (Flutter)

Accessibility is part of UI correctness: semantics labels, focus, text scaling, and contrast must work.

## When to load

- You are building custom widgets or complex screens.
- You need semantics/focus guidance.
- You need rules for text scaling and reduced motion.

## When NOT to load

- You only need theming (`widgets-layout-and-theming.md`).
- You are optimizing performance (`performance.md`).

## Core rules

- Add labels for icon-only controls.
- Prefer built-in Material widgets (they have semantics baked in).
- Respect text scaling; avoid hard-coded heights that clip.
- Ensure focus behavior for dialogs and sheets.

## Minimal examples

Semantics label for an icon button:

```dart
IconButton(
  onPressed: onShare,
  tooltip: 'Share',
  icon: const Icon(Icons.share),
)
```

Large text friendly layout:

```text
avoid fixed-height rows for multi-line text
prefer wrapping + flexible layouts
```

## Anti-patterns

- Icon-only buttons with no tooltip/label.
- Fixed heights that clip at large font sizes.
- Custom gestures without semantics.

## Checklist

- Labels/tooltips exist.
- Text scaling tested.
- Focus behavior sane.
