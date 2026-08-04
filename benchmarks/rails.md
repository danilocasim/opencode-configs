# Rails Benchmarks

## Refactor fat controller into service

Prompt:

"Refactor a fat controller action into a service object using our Result contract. Keep the controller orchestration-only and add unit + request specs."

Expected loads:

- `skills/rails/SKILL.md`
- `skills/rails/service-and-query-objects.md`
- `skills/testing/ruby-rails.md`

Expected traits:

- Controller does params/auth/render only.
- Service encapsulates transaction boundary.
- Unit spec covers success + expected failure.
- Request spec asserts status + error shape.
