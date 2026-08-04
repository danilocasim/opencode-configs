---
name: expo
description: Expo (managed + dev client) patterns for routing, builds, EAS, updates, and device capabilities
---

# Expo Skill Router

Use this when your React Native app uses Expo: Expo Router, EAS Build/Submit, config plugins, expo-updates, and device capabilities.

## When to load

- You are working in an Expo-managed app or dev client.
- You are configuring builds, updates, permissions, or native modules via Expo.
- You are using Expo Router.

## When NOT to load

- You are doing core React Native UI/performance (use `../react-native/SKILL.md`).
- You are doing native-module work in bare RN without Expo tooling.

## Routing table

| If the task is about...                    | Load file                          |
| ------------------------------------------ | ---------------------------------- |
| Expo Router architecture and route groups  | `expo-router.md`                   |
| App config (`app.json`/`app.config.ts`)    | `app-config-and-secrets.md`        |
| EAS build, submit, and dev client          | `eas-build-and-dev-client.md`      |
| Permissions and device capabilities        | `permissions-and-capabilities.md`  |
| expo-updates, channels, and rollout safety | `updates-and-channels.md`          |
| Assets, fonts, and splash/icon pipelines   | `assets-fonts-and-splash.md`       |
| Notifications (push)                       | `push-notifications.md`            |
| Native modules and prebuild/config plugins | `native-modules-and-prebuild.md`   |
| Debugging (Metro, device logs)             | `debugging-and-devtools.md`        |
| Recipe: add a new route with auth gating   | `recipes-protected-route.md`       |
| Recipe: add a native dependency safely     | `recipes-add-native-dependency.md` |

## Related skills

- React Native core: `../react-native/SKILL.md`
- Security checklist: `../security/SKILL.md`
- DevOps/CI: `../devops/SKILL.md`
