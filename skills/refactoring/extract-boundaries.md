# Extract Boundaries

Extraction reduces risk by creating seams: small modules with explicit inputs/outputs that are easy to test.

## When to load

- A controller/handler is doing too much.
- You need to extract a service, query, or adapter.
- You are untangling dependencies.

## When NOT to load

- You only need naming guidance (`naming-and-ownership.md`).
- You are optimizing hot paths (use performance skill).

## Core rules

- Extract the smallest boundary that makes behavior testable.
- Make dependencies explicit (pass clients/DB handles).
- Keep boundary APIs small (keyword args / named params).
- Avoid global state and implicit singletons.
- Add a test at the boundary.

## Minimal examples

Extraction sequence:

```text
1) identify side effects
2) wrap in a function/class with explicit deps
3) update caller
4) add tests
```

## Anti-patterns

- Extracting “utils” without a clear domain.
- Passing half the world into the new function.
- Leaving the old code path in place (duplicate behavior).

## Checklist

- Boundary has explicit inputs/outputs.
- Dependencies injected.
- Tests exist at the new seam.
- Callers simplified.
