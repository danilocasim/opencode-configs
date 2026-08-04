# OpenAPI and Examples

OpenAPI is part of the contract. Keep specs close to reality and include examples so humans and tools can both understand behavior.

## When to load

- You are adding/updating OpenAPI.
- You need example requests/responses.
- You want rules for keeping specs in sync.

## When NOT to load

- You are deciding error shapes (`errors-and-response-shapes.md`).
- You are planning breaking changes (`versioning-and-deprecation.md`).

## Core rules

- Every endpoint defines success + error responses.
- Include at least one example per response.
- Reuse schemas (components) for shared shapes.
- Version the spec alongside code changes.
- Prefer generated clients only if the contract is stable.

## Minimal examples

Error response schema:

```yaml
components:
  schemas:
    Error:
      type: object
      required: [code, message]
      properties:
        code: { type: string }
        message: { type: string }
        fields:
          type: object
          additionalProperties: { type: string }
```

## Anti-patterns

- Specs that only document 200 responses.
- No examples (hard for humans, hard for tests).
- Specs that drift for months.

## Checklist

- Success and error responses documented.
- Examples included.
- Shared schemas reused.
- Spec changes ship with code changes.
