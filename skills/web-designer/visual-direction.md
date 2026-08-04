# Visual Direction

## When to load

- The interface needs a distinct visual thesis, brand expression, or polish direction.
- Typography, color, density, surfaces, imagery, or motion require deliberate choices.

## When NOT to load

- The approved design system fully specifies these choices.
- The task is only interaction behavior or responsive layout.

## Core rules

- Choose one coherent visual stance and explain how it supports the user and task.
- Start with typography and content hierarchy; decoration comes later.
- Define semantic color roles before raw values and verify contrast in every state.
- Make density, corner shape, borders, elevation, and motion part of one system.
- Use shadcn/ui variables and variants as implementation hooks, not as the source of taste.
- Prefer a restrained signature detail repeated intentionally over many unrelated effects.

## Direction framework

1. **Thesis** — a sentence naming the intended feeling and why it fits.
2. **Type** — display/body roles, scale contrast, measure, weight, and numeric treatment.
3. **Color** — canvas, surfaces, text, accent, status, and data roles.
4. **Shape and surface** — radius logic, borders, shadows, texture, and depth.
5. **Imagery** — subject, crop, treatment, illustration, icon, or deliberate absence.
6. **Motion** — what moves, why, duration character, and reduced-motion fallback.
7. **Signature** — one memorable device tied to the product story.

## Minimal examples

```md
Thesis: Technical field notes—precise, tactile, and quiet enough for prolonged analysis.
Type: Compact grotesk UI with a serif display only for section openings; tabular numerals for measurements.
Color: Warm paper canvas, graphite text, oxide accent reserved for decisions, desaturated status fills.
Surface: Mostly flat with hairline rules; small radius on controls, no floating glass cards.
Motion: Fast state transitions and one measured chart reveal; reduced motion removes translation.
Signature: Margin annotations connect evidence to decisions.
shadcn translation: Theme semantic CSS variables and variants; preserve primitive behavior.
```

## Anti-patterns

- A palette without semantic roles or state coverage.
- More than one visual gimmick competing for attention.
- Default shadcn/ui radius, shadows, and colors left unchanged but called branded.
- Display typography used where scanning speed matters.
- Motion that only advertises implementation effort.

## Checklist

- The thesis connects visual choices to audience and task.
- Type, color, density, shape, surfaces, imagery, and motion agree.
- Light/dark and status states are defined when applicable.
- Semantic tokens map cleanly to the project theme.
- Contrast and reduced-motion implications are explicit.
