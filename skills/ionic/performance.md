# Performance (Ionic)

Ionic performance is web performance. Optimize rendering and list virtualization, keep bundles small, and verify on low-tier Android devices.

## When to load

- Scrolling is janky.
- Startup is slow.
- A page re-renders too often.

## When NOT to load

- You are doing native build issues (`../capacitor/SKILL.md`).
- You only need UI patterns (`ui-components-and-patterns.md`).

## Core rules

- Avoid rendering huge lists without virtualization.
- Keep bundles small; code split where it matters.
- Avoid heavy work on first paint.
- Measure on device (especially Android).

## Minimal examples

Investigation loop:

```text
baseline -> identify bottleneck -> small change -> re-measure
```

## Anti-patterns

- Only measuring on desktop.
- Giant images/fonts.
- Re-rendering whole pages on minor state changes.

## Checklist

- Measured on device.
- List rendering is efficient.
- Bundle size controlled.
- Improvement verified.
