---
name: dart
description: Dart 3.x conventions (null safety, async/streams, tooling, testing) for maintainable apps and packages
---

# Dart Skill Router

Use this for Dart language work (Flutter and non-Flutter): null safety, typing discipline, async/streams, error modeling, and a modern toolchain.

## When to load

- You are writing or refactoring Dart code.
- You need guidance for null safety, sealed classes, and API boundaries.
- You need tooling defaults (format/analyze/lints/tests).

## When NOT to load

- You are doing Flutter widget/UI work (use `../flutter/SKILL.md`).
- You only need cross-service API contract design (use `../api/SKILL.md`).

## Routing table

| If the task is about...                        | Load file                  |
| ---------------------------------------------- | -------------------------- |
| Project structure for apps/packages            | `project-structure.md`     |
| Tooling and quality gates                      | `tooling-and-quality.md`   |
| Null safety, typing, and public API boundaries | `null-safety-and-types.md` |
| Async, Futures, Streams                        | `async-and-streams.md`     |
| Error strategy (exceptions vs Result)          | `errors-and-results.md`    |
| Tests (unit, fakes, determinism)               | `testing.md`               |

## Typical load combos

- New module: `null-safety-and-types.md` + `errors-and-results.md` + `testing.md`
- IO integration: `async-and-streams.md` + `errors-and-results.md`
