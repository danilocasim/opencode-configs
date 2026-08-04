# Debugging and Devtools

Capacitor debugging is split-brain: web logs, native logs, and platform tooling. Make reproduction deterministic and collect evidence before changing things.

## When to load

- A bug happens only on device.
- You need WebView inspection guidance.
- You are debugging plugin/native integration issues.

## When NOT to load

- You are implementing a new plugin (`plugins-and-bridging.md`).
- You are doing release process (`builds-and-release.md`).

## Core rules

- Repro on a real device for permissions, push, and deep links.
- Collect logs from both WebView and native.
- Narrow scope: isolate whether issue is web code, plugin, or native project config.
- Avoid random cache-clearing until you've captured evidence.

## Minimal examples

Debug loop:

```text
repro -> logs -> hypothesis -> minimal change -> verify
```

Common buckets:

```text
works in browser but not device: cookies/CORS/base URL
works on iOS but not Android: permissions/back behavior
works on Android but not iOS: ATS/Universal Links
```

## Anti-patterns

- Debugging only in the desktop browser.
- Making many changes before verifying.
- Logging secrets.

## Checklist

- Repro steps documented.
- Web + native logs captured.
- Root cause category identified.
- Fix verified on both platforms.
