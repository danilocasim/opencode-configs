# Critique

## When to load

- Reviewing an existing interface, screenshot, prototype, or implementation.
- The UI feels generic, inconsistent, cluttered, inaccessible, or visually weak but the cause is unclear.

## When NOT to load

- No artifact or sufficiently detailed description exists to evaluate.
- The user only wants an implementation status report.

## Core rules

- Describe evidence before preference and connect every issue to user impact.
- Prioritize issues by task failure, accessibility, hierarchy, consistency, and polish—in that order.
- Identify the strongest existing decision so the redesign preserves useful character.
- Recommend the smallest coherent change set that fixes the underlying system.
- Judge shadcn/ui usage by behavior, consistency, and adaptation; do not fault the library for unmodified defaults the implementation chose.

## Critique lenses

1. **Purpose** — Is the primary task and next action clear?
2. **Hierarchy** — Does visual weight match importance?
3. **Composition** — Is the reading path intentional and balanced?
4. **Interaction** — Are affordances, states, feedback, and recovery visible?
5. **Responsive** — Does priority survive reflow and content stress?
6. **Accessibility** — Are semantics, focus, contrast, labels, and motion safe?
7. **Distinctiveness** — Which choices feel authored versus default or trend-driven?

## Minimal examples

```md
Confirmed: The screenshot gives four KPI cards, the page title, and the empty table nearly equal contrast and area.
Impact: Users cannot tell whether to investigate a metric or create the first report.
Priority: High hierarchy issue, not a spacing issue.
Preserve: The compact typography supports frequent operational use.
Change: Replace the empty table frame and KPI row with one task-oriented empty state; move secondary metrics into a quiet inline summary.
shadcn note: Keep the existing Button and Table primitives, but revise composition and variants rather than adding new card primitives.
Validate: First-click target in a five-second test; keyboard path; narrow viewport reflow.
```

## Anti-patterns

- Vague feedback such as "make it pop" or "needs more whitespace."
- A long unprioritized list of cosmetic preferences.
- Redesigning every element instead of finding the systemic cause.
- Calling all shadcn/ui output generic without identifying the unadapted decisions.
- Claiming accessibility compliance from a screenshot alone.

## Checklist

- Observations, inferences, and preferences are separated.
- Each issue includes user impact and priority.
- Strengths to preserve are named.
- Recommendations form one coherent direction.
- Unknowns and browser validation needs are explicit.
