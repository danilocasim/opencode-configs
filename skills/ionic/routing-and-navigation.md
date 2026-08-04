# Routing and Navigation

Ionic navigation is mobile-first: tabs, stacks, and modals. Keep routes stable, validate params, and avoid ad-hoc navigation logic scattered across components.

## When to load

- You are adding new pages and routes.
- You are building tabbed navigation.
- You need deep link and param validation patterns.

## When NOT to load

- You are building UI primitives (`ui-components-and-patterns.md`).
- You are designing theme tokens (`design-system.md`).

## Core rules

- Define routes in one place.
- Validate route params at boundaries.
- Use tabs for primary sections; use stacks for drill-down.
- Prefer modals for transient flows.
- Keep navigation events out of business logic.

## Minimal examples

Param validation posture:

```text
parse -> validate -> render
invalid -> show not-found or redirect
```

Tabs + stack mental model:

```text
Tabs: top-level areas
Stack: within-area drilldown
Modal: temporary tasks
```

## Anti-patterns

- Stringly-typed route params used without validation.
- Multiple competing routers.
- Navigation side effects inside services.

## Checklist

- Routes centralized.
- Params validated.
- Tabs/stacks/modals used consistently.
