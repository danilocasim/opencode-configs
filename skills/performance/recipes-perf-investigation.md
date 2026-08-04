# Recipe: Performance Investigation

Use this when you need a step-by-step approach to making something faster without breaking behavior.

## When to load

- You are assigned “make it faster”.
- You need a reproducible investigation workflow.

## When NOT to load

- You already know the bottleneck and only need implementation guidance.
- You are fixing correctness bugs.

## Core rules

- Start with a measurable baseline.
- Use production traces if available.
- Form a hypothesis and test it.
- Ship the smallest change that moves the metric.
- Add regression protection (dashboards, tests, budgets).

## Minimal examples

Workflow:

```text
baseline -> hypothesis -> implement -> measure -> repeat
```

## Anti-patterns

- Multiple changes per iteration.
- No verification.
- Optimizing non-critical paths.

## Checklist

- Baseline documented.
- One hypothesis tested.
- Metrics improved.
- Regression guard added.
