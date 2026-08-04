# Dependency Hygiene

Supply-chain issues are real. Keep dependencies pinned, audited, and updated with intent.

## When to load

- You are adding or upgrading dependencies.
- You are responding to a security advisory.
- You need a policy for lockfiles and audits.

## When NOT to load

- You are fixing auth/session issues (use the stack auth docs).
- You are validating runtime input (`input-validation.md`).

## Core rules

- Commit lockfiles.
- Use automated advisories (Dependabot/Renovate) with review.
- Prefer fewer dependencies; avoid unmaintained packages.
- Audit on CI (language-appropriate tooling).
- Roll upgrades in small steps; verify tests.

## Minimal examples

CI gate (conceptual):

```text
install -> audit -> lint/type -> tests
fail build on high severity vulnerabilities
```

## Anti-patterns

- Floating versions without lockfiles.
- Copy-pasting code from unknown packages.
- Upgrading huge dependency graphs without tests.

## Checklist

- Lockfile committed.
- Audit runs in CI.
- Dependency is maintained and justified.
- Upgrade verified with tests.
