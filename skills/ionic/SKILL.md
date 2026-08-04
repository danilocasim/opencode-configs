---
name: ionic
description: Ionic Framework conventions (React/Angular/Vue) with routing, theming, UI patterns, and Capacitor integration
---

# Ionic Skill Router

Use this when building Ionic apps (React/Angular/Vue): navigation, UI patterns, theming/design system, forms, performance, and device integration via Capacitor.

## When to load

- You are starting or refactoring an Ionic app.
- You need consistent routing/navigation and page layout patterns.
- You need theming and a design-system approach using CSS variables.
- You are integrating native capabilities (via Capacitor).

## When NOT to load

- You are building a purely web (non-Ionic) React app (use `../react/SKILL.md`).
- You are doing native platform build/signing (use `../capacitor/SKILL.md`).
- You only need API design (use `../api/SKILL.md`).

## Router (task -> file)

| If the task is about...                       | Load file                          |
| --------------------------------------------- | ---------------------------------- |
| Picking Ionic React vs Angular vs Vue         | `framework-flavors.md`             |
| Project structure and feature ownership       | `project-structure.md`             |
| Routing and navigation patterns               | `routing-and-navigation.md`        |
| Page layout, headers, tabs, and modals        | `ui-components-and-patterns.md`    |
| Forms and validation                          | `forms-and-validation.md`          |
| State, server data, and caching               | `state-and-data.md`                |
| Theming and design system (tokens/components) | `design-system.md`                 |
| Accessibility                                 | `accessibility.md`                 |
| Performance (lists, rendering, startup)       | `performance.md`                   |
| Capacitor integration surface                 | `capacitor-integration.md`         |
| Testing strategy                              | `testing.md`                       |
| Recipe: add a new screen flow                 | `recipes-new-screen-flow.md`       |
| Recipe: bootstrap a design system             | `recipes-design-system-starter.md` |

## Typical load combos

- New screen: `routing-and-navigation.md` + `ui-components-and-patterns.md` + `recipes-new-screen-flow.md`
- Visual system: `design-system.md` + `recipes-design-system-starter.md`
- Device feature: `capacitor-integration.md` + `../capacitor/plugins-and-bridging.md`

## Related skills

- Capacitor native workflows: `../capacitor/SKILL.md`
- Security checklist: `../security/SKILL.md`
- Testing router: `../testing/SKILL.md`
