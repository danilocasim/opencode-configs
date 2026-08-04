# Performance and WebView

Hybrid performance is mostly web performance + startup cost + WebView quirks. Optimize the web app first, then validate on-device.

## When to load

- Startup is slow or app feels laggy on device.
- Scrolling/animations stutter in WebView.
- You need rules for images, caching, and bundle size.

## When NOT to load

- You are doing store release (`builds-and-release.md`).
- You are debugging native build failures (`native-platforms-ios-android.md`).

## Core rules

- Keep bundle size small; defer non-critical code.
- Avoid heavy JS work on first paint.
- Use efficient list rendering and image sizing.
- Measure on real devices (mid/low-tier Android especially).
- Prefer native-driven UI only when web cannot meet performance requirements.

## Minimal examples

Performance investigation loop:

```text
baseline on device -> identify bottleneck -> small change -> re-measure
```

## Anti-patterns

- Optimizing only on desktop.
- Shipping huge images and fonts.
- Overusing blur/shadows and complex compositing.

## Checklist

- Measured on device.
- Bundle size controlled.
- Images sized appropriately.
- Improvements verified.
