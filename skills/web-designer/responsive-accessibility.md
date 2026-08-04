# Responsive Accessibility

## When to load

- Layout or interaction changes across viewport, input mode, zoom, or content size.
- Accessibility acceptance criteria need to be designed rather than checked after implementation.

## When NOT to load

- The task has no user-facing output.
- A tiny visual adjustment cannot affect semantics, interaction, contrast, or reflow.

## Core rules

- Design for reflow and task priority, not device labels.
- Treat 320 CSS-pixel width, 200% zoom, long content, and browser text scaling as layout inputs.
- Preserve semantics and action availability when regions collapse, reorder, scroll, or become modal.
- Prefer native elements and accessible shadcn/ui primitives; custom styling must not remove their behavior.
- Define visible focus, contrast, target size, error association, live feedback, and reduced-motion behavior.
- Do not hide essential content or actions only to make a narrow screenshot cleaner.

## Responsive plan

For narrow, middle, and wide ranges document:

- Content order and primary action location.
- Navigation pattern and disclosure behavior.
- Columns, containers, gutters, and readable measure.
- Table, chart, media, and code overflow strategy.
- Sticky or fixed regions and safe-area handling.
- Pointer, touch, keyboard, and screen-reader implications.

## Minimal examples

```md
Narrow: Filters open in a shadcn Sheet triggered by a labeled button; active filters remain summarized above results.
Middle: Filter groups become an inline collapsible region; results remain one column.
Wide: Persistent filter rail and results grid; source order keeps filters before results.
Keyboard: Trigger announces expanded state; focus enters the Sheet heading and returns to the trigger on close.
Reflow: At 320px and 200% zoom there is no page-level horizontal scrolling; the data table has its own labeled scroll region.
Motion: Sheet and result transitions become opacity-only under reduced motion.
```

## Anti-patterns

- Desktop-first shrinking that leaves controls cramped or order incoherent.
- Breakpoints copied from a framework without content-based validation.
- Placeholder-only labels, low-contrast muted text, or focus rings removed for aesthetics.
- Turning a complex region into a dialog without defining focus and close behavior.
- Horizontal page scrolling caused by tables or fixed-width children.

## Checklist

- Narrow, middle, and wide behavior is explicit.
- Keyboard order follows visual and semantic order.
- Focus, labels, errors, status announcements, and contrast are covered.
- Zoom, long content, reduced motion, and coarse pointers are considered.
- Browser verification viewports and accessibility checks are named.
