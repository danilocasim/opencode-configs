# Recipe: Add Capacitor to an Existing Web App

Use this to add Capacitor without turning your repo into a native-code mess.

## When to load

- You have an existing SPA and want iOS/Android apps.
- You need a safe initial integration plan.

## When NOT to load

- You already have Capacitor and only need a plugin.
- You are shipping a release (use release checklist).

## Core rules

- Start with the smallest native surface: add platforms, sync, and run on device.
- Keep native edits minimal; document any changes.
- Decide environment strategy early (dev server vs bundled assets).
- Add a typed `src/native/` layer before sprinkling plugin calls.

## Minimal examples

Bootstrap steps:

```text
1) install Capacitor
2) init + create capacitor.config
3) add ios/android
4) cap sync
5) run on device
6) add native wrapper layer
```

## Anti-patterns

- Adding many plugins before the first successful device run.
- Leaving dev server URLs in production.
- Direct plugin calls across many features.

## Checklist

- iOS and Android run on device.
- Config supports dev/staging/prod.
- Native wrapper layer exists.
- Minimal native edits documented.
