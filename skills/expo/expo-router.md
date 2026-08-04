# Expo Router

Expo Router gives you file-based routing for React Native. Keep route groups intentional and avoid mixing app wiring with feature UI.

## When to load

- You are adding routes/screens with Expo Router.
- You need patterns for route groups, layouts, and deep links.
- You are standardizing navigation in an Expo app.

## When NOT to load

- You are using React Navigation directly (`../react-native/navigation.md`).
- You are doing UI tokens (`../react-native/ui-ux-and-design-system.md`).

## Core rules

- Keep routes feature-owned; avoid massive `app/` complexity.
- Use route groups for auth boundaries and “areas” of the app.
- Validate params at the boundary.
- Prefer layout-level wiring (headers, providers) and keep screens focused.

## Minimal examples

Route group posture:

```text
app/
  (auth)/
    login.tsx
  (app)/
    _layout.tsx
    home.tsx
    projects/
      [id].tsx
```

Auth gate in a route-group layout (fail closed):

```tsx
// app/(app)/_layout.tsx
import { Redirect, Stack } from "expo-router";

import { useAuth } from "../../src/features/auth/use-auth";

export default function AppLayout() {
  const { status } = useAuth();

  if (status === "loading") return null;
  if (status === "signed_out") return <Redirect href="/(auth)/login" />;

  return <Stack />;
}
```

Validate dynamic params at the boundary:

```tsx
// app/(app)/projects/[id].tsx
import { useLocalSearchParams } from "expo-router";

export default function ProjectScreen() {
  const { id } = useLocalSearchParams<{ id?: string | string[] }>();
  const projectId = typeof id === "string" ? id : null;

  if (!projectId) return null;
  return null;
}
```

## Anti-patterns

- Business logic in layouts.
- Unvalidated dynamic route params.
- Multiple competing navigation systems.

## Checklist

- Route groups map to auth/areas.
- Params validated.
- Layout wiring minimal.
- Screens stay thin.
