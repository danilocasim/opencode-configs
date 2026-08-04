# Dockerfiles and Images

Images are production artifacts. Keep them small, reproducible, and free of secrets.

## When to load

- You are writing or optimizing a Dockerfile.
- You need guidance for multi-stage builds.
- You are tightening container security posture.

## When NOT to load

- You are working on CI pipeline logic (`ci-pipelines.md`).
- You are designing deployment rollouts (`deploy-strategies.md`).

## Core rules

- Use multi-stage builds.
- Prefer small base images when feasible.
- Run as non-root.
- Pin OS/package versions when it matters.
- Never bake secrets into images.

## Minimal examples

Multi-stage sketch:

```text
builder: install deps -> build
runtime: copy build output only
```

## Anti-patterns

- `ADD . /app` without `.dockerignore`.
- Installing build tools into the runtime image.
- Putting secrets in ENV at build time.

## Checklist

- Multi-stage used.
- Runtime image contains only what it needs.
- Non-root user.
- Secrets not embedded.
