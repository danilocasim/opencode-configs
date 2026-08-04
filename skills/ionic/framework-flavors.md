# Framework Flavors (React, Angular, Vue)

Ionic shares UI primitives, but routing/state patterns vary significantly by framework. Pick one stack and follow its conventions.

## When to load

- You are deciding which Ionic flavor to use.
- You are reviewing an existing project and need to identify conventions.

## When NOT to load

- You already know the framework and only need routing/theming guidance.

## Core rules

- Match the repo: Ionic React uses React Router + hooks; Ionic Angular uses Angular router + services; Ionic Vue uses Vue Router + composition.
- Avoid mixing patterns (e.g. Angular-style services inside Ionic React without good reason).
- Keep feature code framework-idiomatic.

## Minimal examples

What to look for:

```text
Ionic React: @ionic/react, @ionic/react-router
Ionic Angular: @ionic/angular, Angular modules, router
Ionic Vue: @ionic/vue, vue-router
```

## Anti-patterns

- Copy-pasting examples from a different framework flavor.
- Mixing multiple routing systems.

## Checklist

- Framework flavor identified.
- Routing library identified.
- Patterns stay consistent with the chosen stack.
