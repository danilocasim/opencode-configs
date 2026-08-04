# App Config and Secrets

Expo apps have config at build-time and runtime. Keep config explicit, avoid leaking secrets into the client bundle, and separate environments cleanly.

## When to load

- You are editing `app.json` / `app.config.ts`.
- You need rules for env vars and secrets.
- You are configuring bundle identifiers, schemes, or deep links.

## When NOT to load

- You are doing EAS build setup (`eas-build-and-dev-client.md`).
- You are doing security logging/redaction (`../security/secrets-and-logging.md`).

## Core rules

- Treat the JS bundle as public; do not ship secrets.
- Separate build-time values from runtime values.
- Use explicit environment selection (dev/staging/prod).
- Keep identifiers stable: iOS bundle id, Android applicationId, schemes.

## Minimal examples

`app.config.ts` with environment selection and allowlisted values:

```ts
import "dotenv/config";

type AppEnv = "development" | "staging" | "production";

function requireEnv(name: string): string {
  const v = process.env[name];
  if (!v) throw new Error(`missing env: ${name}`);
  return v;
}

const appEnv = (process.env.APP_ENV as AppEnv | undefined) ?? "development";

export default ({ config }: { config: Record<string, unknown> }) => {
  const apiBaseUrl = requireEnv("EXPO_PUBLIC_API_BASE_URL");

  return {
    ...config,
    name: appEnv === "production" ? "MyApp" : `MyApp (${appEnv})`,
    slug: "myapp",
    scheme: "myapp",
    extra: {
      appEnv,
      apiBaseUrl,
    },
    ios: {
      bundleIdentifier: appEnv === "production" ? "com.example.myapp" : "com.example.myapp.dev",
    },
    android: {
      package: appEnv === "production" ? "com.example.myapp" : "com.example.myapp.dev",
    },
  };
};
```

Rule of thumb:

```text
EXPO_PUBLIC_* is public
anything secret stays server-side
```

## Anti-patterns

- Putting API keys in `extra`.
- One config used for all environments.
- Changing bundle IDs late without migration planning.

## Checklist

- Secrets are server-side only.
- Environments separated.
- IDs and schemes correct per platform.
