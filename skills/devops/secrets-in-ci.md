# Secrets in CI

CI is a common leak path. Treat secrets as ephemeral and minimize their exposure.

## When to load

- You are adding CI secrets (tokens, deploy keys, registry creds).
- You are integrating with cloud providers.
- You need a policy for forks and PRs.

## When NOT to load

- You are doing app-level secrets handling (use `../security/secrets-and-logging.md`).
- You are working on deployment rollout logic (`deploy-strategies.md`).

## Core rules

- Scope secrets to the minimum permissions.
- Separate secrets for staging vs production.
- Do not expose secrets to untrusted PRs/forks.
- Avoid long-lived credentials; prefer OIDC where possible.
- Never print secret values.

## Minimal examples

Policy:

```text
prod deploy credentials only available on protected branches
fork PRs run tests with no secrets
```

## Anti-patterns

- Using production keys in all environments.
- Logging environment variables.
- Sharing one token for many systems.

## Checklist

- Least privilege.
- Env separation.
- Fork safety.
- No secret logging.
