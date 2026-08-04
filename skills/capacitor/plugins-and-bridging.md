# Plugins and Bridging

Plugins are your boundary between the WebView app and native capabilities. Keep the JS surface typed, minimal, and stable.

## When to load

- You are adding a Capacitor plugin.
- You need a typed wrapper and error mapping strategy.
- You are creating a custom plugin.

## When NOT to load

- You only need permission UX (`permissions-and-privacy.md`).
- You only need build/signing (`builds-and-release.md`).

## Core rules

- Prefer official/maintained plugins.
- Wrap plugin calls in `src/native/*` and return explicit ok/error shapes.
- Do not let plugin exceptions leak into UI.
- Keep platform differences inside the wrapper.

## Minimal examples

Typed wrapper with explicit errors:

```ts
import { Capacitor } from "@capacitor/core";
import { Device } from "@capacitor/device";

export type DeviceInfoResult =
  | { ok: true; value: { model: string; platform: string } }
  | { ok: false; code: "unavailable" | "unexpected"; message: string };

export async function getDeviceInfo(): Promise<DeviceInfoResult> {
  if (!Capacitor.isNativePlatform()) {
    return { ok: false, code: "unavailable", message: "native only" };
  }

  try {
    const info = await Device.getInfo();
    return { ok: true, value: { model: info.model ?? "", platform: info.platform } };
  } catch {
    return { ok: false, code: "unexpected", message: "failed to read device info" };
  }
}
```

## Anti-patterns

- Plugin calls scattered across the app.
- Unhandled permission denial paths.
- Throwing raw errors into UI.

## Checklist

- Plugin use is centralized.
- Wrapper returns stable contract.
- Web fallback is explicit.
- Both platforms tested.
