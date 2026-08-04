# Builds and Release

Store releases require discipline: signing, versioning, reproducible builds, and a checklist that prevents “works on my phone” releases.

## When to load

- You are preparing a TestFlight / Play Internal / production release.
- You are setting up CI for iOS/Android builds.
- You are debugging signing/versioning issues.

## When NOT to load

- You are only changing web UI with no native impact.
- You are adding a plugin (see plugin recipe + platform docs).

## Core rules

- Versioning is explicit and monotonic (iOS build number, Android versionCode).
- Signing credentials are least-privilege and stored securely.
- Release builds should not depend on `server.url`.
- Test on real devices and at least one low-tier Android.
- Keep a rollback plan (store rollout + server kill switch).

## Minimal examples

Release hygiene:

```text
1) bump versions
2) cap sync
3) build archive/apk/aab
4) smoke test
5) submit
```

## Anti-patterns

- Changing native deps right before a release with no soak time.
- Ad-hoc signing keys on developer laptops.
- Shipping dev URLs/config.

## Checklist

- Versions bumped.
- Release config verified.
- Both platforms smoke tested.
- Credentials handled safely.
- Monitoring ready.
