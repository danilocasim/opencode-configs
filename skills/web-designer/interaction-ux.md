# Interaction UX

## When to load

- A feature includes forms, navigation, dialogs, menus, drag/drop, progressive disclosure, or asynchronous actions.
- The happy path exists but states, feedback, recovery, or keyboard behavior are underspecified.

## When NOT to load

- The request is purely visual with no interaction change.
- Backend workflow semantics must be designed first.

## Core rules

- Define the user goal and state machine before micro-interactions.
- Make the next action discoverable without relying on hover, color, or icon shape alone.
- Keep feedback close to the action and preserve user input on recoverable errors.
- Distinguish pending, success, empty, partial, stale, offline, permission-denied, and failure states when relevant.
- Use established shadcn/ui primitives for complex accessible behavior such as dialogs, menus, popovers, tabs, and forms when compatible.
- Reserve confirmation for consequential or hard-to-reverse actions; offer undo when reversal is cheap.

## State map

For each meaningful action specify:

1. Trigger and preconditions.
2. Immediate feedback.
3. Pending behavior and repeat-click policy.
4. Success result and focus destination.
5. Validation or system failure.
6. Recovery, retry, undo, or escalation.
7. Keyboard and assistive-technology behavior.

## Minimal examples

```md
Action: Archive project
Trigger: Destructive menu item labeled "Archive project".
Precondition: User has archive permission.
Immediate: AlertDialog describes impact and names the project.
Pending: Confirm button shows progress and disables repeat submission; cancel remains available until request starts.
Success: Dialog closes, focus returns to the project row, toast offers Undo.
Failure: Dialog remains open with an inline error; project name and selection are preserved.
Keyboard: Menu and AlertDialog use their shadcn/ui focus management; Escape only closes before submission.
```

## Anti-patterns

- Hover-only controls or icon-only actions without accessible names.
- Toasts as the sole location for validation or critical errors.
- Disabling submit without explaining unmet requirements.
- Closing a dialog and discarding input after a server failure.
- Custom keyboard behavior that conflicts with the chosen accessible primitive.

## Checklist

- Every action has pending, success, failure, and recovery behavior.
- Destructive actions communicate impact and reversibility.
- Focus placement and keyboard operation are defined.
- Loading feedback does not cause layout shift.
- Existing accessible primitives are reused where appropriate.
