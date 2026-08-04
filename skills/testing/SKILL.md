---
name: testing
description: TDD operating manual with routing, advanced modules, and recipes
---

# Testing (TDD Operating Manual)

Tests are how you _freeze_ intended behavior so you can change code safely.
This skill routes you to the smallest test that proves the behavior, then adds
modules/recipes for fixtures, mocks, E2E, CI reliability, and contracts.

## When to load

- You are changing behavior (feature/refactor) and want fast safety.
- You are fixing a bug and want a regression test first.
- You need to choose a test level/framework for the current stack.
- CI is flaky and you need a reliability playbook.

## When NOT to load

- Pure docs/content changes with no runtime behavior change.
- You only need static checks (format/lint/type) with no execution.

## Router (task -> file)

| Task                                                | Load                                     |
| --------------------------------------------------- | ---------------------------------------- |
| Run the Red -> Green -> Refactor loop               | `tdd-workflow.md`                        |
| Pick the test framework for a stack                 | Stack mapping below                      |
| Write/organize fixtures and deterministic test data | `fixtures-and-test-data.md`              |
| Decide what to mock (and what not to)               | `test-doubles-and-mocking-discipline.md` |
| Add/maintain Playwright end-to-end coverage         | `e2e-playwright.md`                      |
| Stop flakes / make CI runs trustworthy              | `ci-reliability-and-flake-control.md`    |
| Validate API/queue boundaries between services      | `contract-testing.md`                    |
| Explore invariants with generative tests            | `property-based-testing.md`              |
| Bug fix workflow (repro -> regression -> fix)       | `recipes-bug-fix.md`                     |
| Playwright workflow (setup -> seed -> assert)       | `recipes-playwright-e2e.md`              |
| Naming, test docs, and comment discipline           | `documentation-and-comments.md`          |

## Stack mapping (language/framework -> file)

- Next.js (App Router, server actions, route handlers), Node apps: `node-nextjs.md`
- TypeScript/JavaScript libraries and apps (non-Next specifics): `typescript.md`
- Python (pytest): `python.md`
- Ruby/Rails: `ruby-rails.md` (compat: `ruby.md`)
- Go: `go.md`
- Rust: `rust.md`
- Swift: `swift.md`
- Kotlin: `kotlin.md`

## Default policy (TDD-first)

- Red: write the smallest failing test that proves the behavior.
- Green: implement the minimum change to pass.
- Refactor: improve design/duplication while staying green.
- Prefer the lowest test level that proves behavior; escalate only when necessary.
- Determinism is a feature: control time, randomness, IO, and external services.
- Every bug fix gets a regression test that would fail on the old code.

## Test level decision (fast rule)

- Unit: pure logic, fast, isolated; default start.
- Integration: boundary correctness (DB, filesystem, HTTP handlers, queues).
- End-to-end: critical user journeys and cross-system wiring only.

## Stop triggers (when to stop adding tests / change approach)

- You have one failing test that precisely captures the intended behavior.
- Additional cases are duplicates (same code path, same risk) rather than new risk.
- The test is asserting internals because the design is hard to observe.
- You are mocking more than one boundary in a single test (too coupled).
- A test requires real network/time to pass (fix determinism before expanding).
- CI is red due to flakes (pause feature work; load `ci-reliability-and-flake-control.md`).

## Minimal checklist

- State behavior in one sentence (Given/When/Then).
- Pick the smallest test level that can prove it.
- Write the failing test (fails for the right reason).
- Make it pass with minimal code.
- Refactor; keep suite fast and deterministic.
