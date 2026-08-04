---
name: react-native
description: React Native app architecture, platform UX, performance, and native integration (iOS/Android)
---

# React Native Skill Router

Use this for React Native (bare or Expo) when the task involves native platforms, performance constraints, mobile UX, or OS capabilities.

## When to load

- You are building or refactoring a React Native app.
- You need iOS vs Android guidance (navigation, permissions, UI conventions).
- You need performance rules for lists, images, and rendering.
- You are integrating with native modules.

## When NOT to load

- You are working on Expo build/runtime specifics (use `../expo/SKILL.md`).
- You are working on web-only React/Next.js (use `../react/SKILL.md` / `../nextjs/SKILL.md`).
- You only need TypeScript strictness (use `../typescript/SKILL.md`).

## Routing table

| If the task is about...                      | Load file                        |
| -------------------------------------------- | -------------------------------- |
| Project structure and feature ownership      | `project-structure.md`           |
| iOS vs Android behavior and platform rules   | `platform-differences.md`        |
| UI/UX patterns and design system foundations | `ui-ux-and-design-system.md`     |
| Accessibility (screen readers, focus)        | `accessibility.md`               |
| Navigation patterns (non-Expo router)        | `navigation.md`                  |
| Performance (lists, renders, images)         | `performance.md`                 |
| Animations and gestures                      | `animations-and-gestures.md`     |
| Native modules and bridging                  | `native-modules-and-bridging.md` |
| Testing (unit/integration/e2e)               | `testing.md`                     |
| Recipe: build a new screen flow              | `recipes-new-screen-flow.md`     |

## Related skills

- Expo specifics: `../expo/SKILL.md`
- TypeScript strictness: `../typescript/SKILL.md`
- Testing router: `../testing/SKILL.md`
- Security checklist: `../security/SKILL.md`
