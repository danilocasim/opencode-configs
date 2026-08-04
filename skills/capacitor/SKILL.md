---
name: capacitor
description: Capacitor conventions for production hybrid apps (iOS/Android), plugins, config, builds, and webview UX
---

# Capacitor Skill Router

Use this when building production hybrid apps with Capacitor: config, native platforms, plugins, permissions, builds/signing, and "web inside native" UX.

## When to load

- You are adding Capacitor to a web app (React/Vue/Svelte/etc.).
- You are working on iOS/Android build pipelines, signing, or native project hygiene.
- You are integrating device capabilities (camera, filesystem, push, deep links).
- You need safe patterns for auth/session, storage, and security in a WebView app.

## When NOT to load

- You are building native UI in React Native/Flutter (use those skills).
- You only need web app architecture (use `../react/SKILL.md` / `../nextjs/SKILL.md`).
- You are doing backend API design (use `../api/SKILL.md`).

## Routing table

| If the task is about...                               | Load file                             |
| ----------------------------------------------------- | ------------------------------------- |
| Project structure and "where code lives"              | `project-structure.md`                |
| `capacitor.config.*`, environments, and runtime flags | `config-and-environments.md`          |
| iOS/Android platform projects and hygiene             | `native-platforms-ios-android.md`     |
| Plugins, bridging, and typed wrappers                 | `plugins-and-bridging.md`             |
| Permissions and privacy UX                            | `permissions-and-privacy.md`          |
| Storage (tokens), secure storage, and secrets         | `storage-and-secrets.md`              |
| Networking, auth, cookies, and CORS in WebView        | `networking-and-auth.md`              |
| Deep links / universal links / app links              | `deeplinks-and-app-links.md`          |
| Push notifications (high level)                       | `push-notifications.md`               |
| Performance (webview, rendering, startup)             | `performance-and-webview.md`          |
| Debugging (device logs, WebView inspection)           | `debugging-and-devtools.md`           |
| Build/release (signing, CI, App Store/Play)           | `builds-and-release.md`               |
| Testing strategy (unit, e2e, device smoke)            | `testing.md`                          |
| Recipe: add Capacitor to an existing web app          | `recipes-add-capacitor-to-web-app.md` |
| Recipe: add a plugin safely                           | `recipes-add-plugin.md`               |
| Recipe: release checklist                             | `recipes-release-checklist.md`        |

## Typical load combos

- New app bootstrap: `project-structure.md` + `config-and-environments.md` + `native-platforms-ios-android.md`
- Add device capability: `plugins-and-bridging.md` + `permissions-and-privacy.md`
- Ship to stores: `builds-and-release.md` + `recipes-release-checklist.md`

## Related skills

- Security: `../security/SKILL.md`
- Auth models: `../auth/SKILL.md`
- DevOps/CI: `../devops/SKILL.md`
