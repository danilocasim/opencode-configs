# Recipe: Design System Starter (Ionic)

Use this to bootstrap a small, high-signal design system for Ionic: tokens + a few wrappers + usage rules.

## When to load

- You are starting a new Ionic app and want consistent UI.
- You want to share a design system across multiple small apps.

## When NOT to load

- You only need one-off UI.
- You already have an established design system.

## Core rules

- Tokens first (CSS variables).
- Map tokens into Ionic theme variables.
- Wrap only the highest leverage components.
- Add a single demo page to visually QA.

## Minimal examples

Steps:

```text
1) create src/theme/tokens.css
2) create src/theme/ionic-overrides.css
3) import theme files once (global)
4) create 3 wrappers: PrimaryButton, Field, Sheet
5) add "Design System" demo route
```

Demo page checklist:

```text
buttons (primary/secondary/danger)
inputs (error state)
list rows
modal/sheet
dark/light (if supported)
```

## Anti-patterns

- Wrapping every Ionic component.
- Tokens split across multiple files without rules.
- No visual QA surface.

## Checklist

- Tokens centralized.
- Ionic variables mapped.
- Wrapper components exist.
- Demo page exists and is used for QA.
