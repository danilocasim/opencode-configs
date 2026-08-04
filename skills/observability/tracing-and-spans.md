# Tracing and Spans

Distributed tracing shows you where time goes across services. Spans should align to meaningful boundaries: incoming request, DB calls, external calls, and background jobs.

## When to load

- You need to identify latency bottlenecks across services.
- You are instrumenting an HTTP client or DB client.
- You are connecting job execution to the originating request.

## When NOT to load

- You only need structured logs (`logging-and-correlation-ids.md`).
- You are defining alerts/SLOs (`metrics-and-slos.md`).

## Core rules

- Propagate trace context across HTTP and queues.
- Use consistent span names (service.operation).
- Tag spans with safe identifiers (request_id, user_id) but not secrets.
- Record errors with stable error codes.
- Sample intentionally; keep high-value spans.

## Minimal examples

Span boundaries:

```text
http.server
db.query
http.client
job.perform
```

## Anti-patterns

- Spans for every tiny function (noise).
- Missing context propagation (broken traces).
- Adding secrets as span attributes.

## Checklist

- Context propagation works across services.
- Span naming is consistent.
- Attributes are safe and useful.
- Sampling strategy defined.
