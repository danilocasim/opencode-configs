# Config and Environments

Capacitor configuration controls runtime behavior (navigation, server URLs, app IDs). Treat it like production config: explicit per environment, no secrets.

## When to load

- You are creating `capacitor.config.ts`.
- You need dev/staging/prod environment behavior.
- You need to set `server.url`, `allowNavigation`, or platform IDs.

## When NOT to load

- You need build/signing guidance (`builds-and-release.md`).
- You need auth/cookies behavior (`networking-and-auth.md`).

## Core rules

- Do not ship secrets in the app bundle.
- Prefer `capacitor.config.ts` and compute config from environment.
- Keep `appId` and `appName` stable; changing identifiers is a migration.
- Be conservative with `allowNavigation` and `cleartext`.

## Minimal examples

`capacitor.config.ts` with environment selection:

```ts
import type { CapacitorConfig } from "@capacitor/cli";

type AppEnv = "development" | "staging" | "production";

function requireEnv(name: string): string {
  const v = process.env[name];
  if (!v) throw new Error(`missing env: ${name}`);
  return v;
}

const appEnv = (process.env.APP_ENV as AppEnv | undefined) ?? "development";

const serverUrl = process.env.CAP_SERVER_URL;

const config: CapacitorConfig = {
  appId: appEnv === "production" ? "com.example.myapp" : `com.example.myapp.${appEnv}`,
  appName: appEnv === "production" ? "MyApp" : `MyApp (${appEnv})`,
  webDir: "dist",
  bundledWebRuntime: false,
  server: serverUrl
    ? {
        url: serverUrl,
        cleartext: appEnv !== "production",
      }
    : undefined,
  android: {
    allowMixedContent: appEnv !== "production",
  },
};

export default config;
```

Rule of thumb:

```text
server.url is great for dev/hot reload
store builds should usually use bundled assets (no server.url)
```

## Anti-patterns

- Shipping API keys in config.
- Leaving `server.url` set for production builds.
- Broad `allowNavigation` patterns.

## Checklist

- Identifiers stable and intentional.
- No secrets in config.
- Production build does not depend on `server.url`.
- Navigation rules are least-privilege.
