# Contract Testing

## When to load

- You own a consumer/provider boundary (HTTP, events, queues) and need safety.
- You want confidence that refactors do not break external clients.
- Multiple services/teams integrate and failures show up late.

## When NOT to load

- You can fully test within one codebase using integration tests.
- You need property-based exploration (use `property-based-testing.md`).

## Core rules

- Contracts are about _interfaces_ (status codes, schemas, headers, events), not internals.
- Prefer schema-first (OpenAPI/JSON Schema/Protobuf) when available.
- Keep contracts small and versioned; deprecate deliberately.
- Test both sides: consumer expectations + provider guarantees.
- Run provider verification in CI before deploy.

## Common patterns

- OpenAPI conformance tests for response/request schema.
- Consumer-driven contracts (e.g., Pact) for multiple consumers.
- Event contract tests: validate message shape + required fields.
- Backward compatibility tests (old client payloads still accepted).

## Minimal examples

Node/TS response-shape contract test (schema via Zod):

```ts
import { expect, it } from "vitest";
import { z } from "zod";

const Project = z.object({ id: z.string(), name: z.string() });

it("GET /api/projects/:id returns contract", async () => {
  const res = await fetch("http://localhost:3000/api/projects/p_123");
  expect(res.status).toBe(200);

  const json = await res.json();
  expect(Project.safeParse(json).success).toBe(true);
});
```

## Anti-patterns

- Snapshotting entire payloads when only a contract subset matters.
- Using contract tests as a substitute for unit tests.
- Contract "tests" that hit production endpoints.

## Checklist

- Is the contract explicit (schema/examples) and versioned?
- Do tests cover both success and error shapes?
- Do provider tests run in CI for changes to the contract?
- Are compatibility expectations documented (what stays stable)?

## References

- Pact: https://docs.pact.io/
- OpenAPI: https://www.openapis.org/
