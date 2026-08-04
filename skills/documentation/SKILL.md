---
name: documentation
description: Documentation style index across languages (doc comments, docstrings, and API docs)
---

# Documentation Style Index

This skill is a routing table for choosing the correct documentation format.

## Default rule

- Public APIs must be documented.
- Use the project's established conventions first.
- If there is no project convention, use the language default below.

## Language mapping

- Ruby: YARD (tagged comments)
  - See: `skills/ruby/SKILL.md`
- JavaScript: JSDoc
  - See: `skills/javascript/SKILL.md`
- TypeScript: TSDoc
  - See: `skills/typescript/SKILL.md`
- Python: Google-style docstrings
  - See: `skills/python/SKILL.md`
- Go: GoDoc
  - See: `skills/go/SKILL.md`
- Rust: rustdoc
  - See: `skills/rust/SKILL.md`
- Swift: SwiftDoc
  - See: `skills/swift/SKILL.md`
- Kotlin: KDoc
  - See: `skills/kotlin/SKILL.md`

## Notes for agents

- `docs-writer` should consult this index first when the target language is unclear.
- If the project already uses a doc tool (Typedoc, yardoc, Sphinx, MkDocs), match it.

## API documentation

If documenting APIs (HTTP/GraphQL), prefer:

- OpenAPI / Swagger for REST endpoints
- Request/response examples and error semantics
- Authentication and rate-limit notes
