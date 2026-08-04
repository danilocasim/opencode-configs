# UI Components and Patterns

Ionic UI is strong when you follow its layout primitives (`IonPage`, `IonHeader`, `IonContent`) and avoid fighting scroll/keyboard behaviors.

## When to load

- You are building page layouts, headers/toolbars, lists, sheets/modals.
- You want consistent UI patterns across pages.
- You need iOS vs Android style guidance (mode, components).

## When NOT to load

- You are building the design system layer (`design-system.md`).
- You are debugging native issues (`../capacitor/SKILL.md`).

## Core rules

- Every page uses `IonPage` -> `IonHeader` -> `IonContent`.
- Put scrollable content inside `IonContent`, not nested scroll containers.
- Use `IonList` for lists; keep list rows simple.
- Use modals for create/edit flows; keep dismissal predictable.
- Prefer platform-adaptive patterns, but keep brand tokens consistent.

## Minimal examples

Canonical page skeleton (Ionic React style):

```tsx
import { IonButton, IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from "@ionic/react";

export function ProjectsPage() {
  return (
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>Projects</IonTitle>
        </IonToolbar>
      </IonHeader>

      <IonContent fullscreen>
        <IonButton expand="block">New project</IonButton>
      </IonContent>
    </IonPage>
  );
}
```

## Anti-patterns

- Custom wrappers that break `IonPage`/`IonContent` scroll behavior.
- Multiple nested scroll views.
- Inconsistent header patterns per page.

## Checklist

- Page skeleton correct.
- Scroll behavior predictable.
- Modal/list patterns consistent.
- Works with keyboard.
