# EAS Build and Dev Client

EAS Build/Submit is the production path for Expo apps. Use a dev client when you need native modules beyond Expo Go.

## When to load

- You are setting up EAS build/submit.
- You need a dev client workflow.
- You are troubleshooting iOS/Android build pipeline issues.

## When NOT to load

- You only need UI/perf guidance (use `../react-native/SKILL.md`).
- You only need updates/channels (`updates-and-channels.md`).

## Core rules

- Use EAS profiles for dev/preview/prod.
- Prefer dev client for native deps; Expo Go for pure-JS.
- Keep signing credentials controlled and environment-scoped.
- Automate builds in CI when possible.

## Minimal examples

Profile posture:

```text
development: internal + dev client
preview: internal distribution
production: store
```

`eas.json` profile sketch:

```json
{
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal"
    },
    "production": {
      "distribution": "store"
    }
  }
}
```

Common commands:

```bash
eas build --profile development --platform ios
eas build --profile preview --platform android
eas submit --profile production --platform ios
```

## Anti-patterns

- Relying on Expo Go for features requiring native code.
- Mixing signing credentials across environments.
- Manual build steps with no documentation.

## Checklist

- EAS profiles defined.
- Dev client chosen when needed.
- Signing creds stored safely.
- Build steps documented.
