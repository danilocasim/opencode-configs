# Composition

## When to load

- A page or screen needs hierarchy, layout rhythm, density, or focal-point decisions.
- The design risks becoming a stack of equal-weight cards or sections.

## When NOT to load

- The work is limited to a single isolated component.
- A supplied design already defines layout at all required viewports.

## Core rules

- Build around the reading and action order, not a preferred grid.
- Give one element clear first-read priority and subordinate the rest through scale, position, contrast, and whitespace.
- Use alignment and repetition to establish rhythm; break the rhythm only to signal importance.
- Group by user decision, not by data source or implementation boundary.
- Let content determine container width and density.
- Define structural behavior at narrow, middle, and wide viewports instead of merely shrinking dimensions.

## Composition decisions

- Entry point and first five seconds of reading.
- Primary action and its relationship to supporting information.
- Grid, measure, gutters, vertical rhythm, and deliberate asymmetry.
- Persistent versus contextual regions.
- Scroll sequence, sticky behavior, and overflow ownership.
- Empty, sparse, normal, dense, and error content shapes.

## Minimal examples

```md
First read: Case title → urgency reason → recommended action.
Wide: 7/5 split; evidence remains in the reading column and action history is sticky within the viewport.
Middle: Single reading column with the action summary placed before evidence.
Narrow: No sticky sidebar; primary action becomes a bottom-safe action region after the summary.
Rhythm: Large chapter gaps, compact metadata rows, rules instead of nested cards.
Stress cases: Long customer name wraps without displacing urgency; empty history preserves the evidence width.
```

## Anti-patterns

- Repeating a three-column card grid regardless of content.
- Equal visual weight for primary, secondary, and metadata content.
- Desktop sidebars moved below content without reconsidering task order.
- Nested containers, borders, and shadows used as the only grouping method.
- Centering long-form or operational content by default.

## Checklist

- The first read and primary action are unmistakable.
- Grouping reflects user decisions.
- Layout behavior is defined for three structural viewport ranges.
- Long, short, empty, loading, and error content were considered.
- Overflow and sticky ownership are explicit.
