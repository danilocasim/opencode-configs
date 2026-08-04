# Assets, Fonts, and Splash/Icon

Assets affect perceived quality and startup. Keep pipelines deterministic and avoid platform-specific surprises.

## When to load

- You are adding custom fonts.
- You are updating splash screens or app icons.
- You need asset loading patterns.

## When NOT to load

- You are doing UI system design (use `../react-native/ui-ux-and-design-system.md`).
- You are doing build setup (`eas-build-and-dev-client.md`).

## Core rules

- Define font loading early and avoid FOUC-like flashes.
- Use platform-appropriate icon/splash sizes.
- Keep asset naming consistent and predictable.
- Avoid huge images in the initial bundle.

## Minimal examples

Asset posture:

```text
assets/fonts
assets/images
```

## Anti-patterns

- Loading fonts late inside random screens.
- Shipping multi-megabyte images as defaults.
- Inconsistent icons across platforms.

## Checklist

- Font loading is deterministic.
- Icons/splash tested on iOS and Android.
- Bundle size considered.
