# Profiling and Measurement

Performance work must be measurement-led. Guessing is expensive and usually wrong.

## When to load

- You need a baseline and a repeatable investigation loop.
- You are choosing what to measure (timers, spans, flamegraphs).
- You are validating that a change actually improved things.

## When NOT to load

- You already know you need caching (`caching-strategies.md`).
- You are focused on DB schema/index changes (`../database/SKILL.md`).

## Core rules

- Start with a reproducible benchmark (prod traces or a load test).
- Measure p95/p99, not just averages.
- Attribute time to a layer (DB, external API, CPU, queue).
- Change one thing at a time.
- Verify improvement and guard against regression.

## Minimal examples

Loop:

```text
baseline -> locate bottleneck -> implement smallest fix -> re-measure -> regressions test
```

## Anti-patterns

- Optimizing without a baseline.
- Micro-optimizing cold paths.
- Shipping a performance change with no verification.

## Checklist

- Baseline captured.
- Bottleneck identified.
- Fix validated with p95/p99.
- Regression guard exists.
