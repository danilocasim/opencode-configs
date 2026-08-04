# Forms and Validation

Forms are where UX breaks: keyboard overlap, unclear errors, and inconsistent validation. Keep validation consistent and errors accessible.

## When to load

- You are building a form page.
- You need a consistent field error pattern.
- You are standardizing input components.

## When NOT to load

- You are only doing navigation.
- You are building native permission flows.

## Core rules

- Validate on the client for UX, but treat server validation as source of truth.
- Show field errors near fields; show global errors at the top.
- Disable submit while loading.
- Ensure keyboard does not hide primary actions.

## Minimal examples

Ionic input with error text (sketch):

```tsx
import { IonInput, IonItem, IonLabel, IonNote } from "@ionic/react";

export function Field({
  label,
  value,
  onChange,
  error,
}: {
  label: string;
  value: string;
  onChange: (v: string) => void;
  error?: string;
}) {
  return (
    <IonItem>
      <IonLabel position="stacked">{label}</IonLabel>
      <IonInput value={value} onIonInput={(e) => onChange(String(e.detail.value ?? ""))} />
      {error ? <IonNote color="danger">{error}</IonNote> : null}
    </IonItem>
  );
}
```

## Anti-patterns

- Submit remains enabled during request.
- Only showing errors via toast.
- Throwing raw exceptions into the UI.

## Checklist

- Field errors shown near fields.
- Submit disabled while loading.
- Keyboard behavior tested.
- Server validation handled.
