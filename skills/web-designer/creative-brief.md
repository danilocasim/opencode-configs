# Creative Brief

## When to load

- A new page, feature, or redesign lacks an explicit design rationale.
- Audience, task priority, brand constraints, content, or success criteria are unclear.

## When NOT to load

- An approved brief already answers the questions below.
- The request is a small, isolated implementation fix with no design choice.

## Core rules

- Explain why the experience exists before deciding how it looks.
- Separate confirmed facts from assumptions and open decisions.
- Ask only questions whose answers could change hierarchy, interaction, or visual direction.
- Use real or structurally realistic content; do not design around lorem ipsum.
- Reduce the brief to one primary user, one primary task, and one measurable outcome.

## Brief fields

| Field | Required answer |
| --- | --- |
| Audience | Who is using this, in what context, with what level of knowledge? |
| Primary task | What must the user accomplish first? |
| Outcome | What observable result means the design worked? |
| Content | What real content, data, and actions must appear? |
| Brand | Which traits should be felt, and which should be avoided? |
| Constraints | Stack, design system, shadcn/ui status, accessibility, assets, deadlines |
| Competition | Which familiar patterns help comprehension, and which clichés should be rejected? |

## Minimal examples

```md
Design thesis seed: A calm, editorial workspace for operators making high-stakes decisions—not a dense admin template.
Primary user: Experienced support lead reviewing escalations between calls.
Primary task: Identify the next case requiring intervention.
Success: The correct case and reason are understandable within ten seconds.
Constraints: Existing shadcn/ui primitives, keyboard-first operation, WCAG AA, no new dependencies.
Avoid: Equal-weight cards, vanity metrics, vague icon-only actions, decorative gradients.
Assumptions to validate: Whether urgency or account value determines sort order.
```

## Anti-patterns

- A mood-board adjective list with no task or content implications.
- Asking broad questions after repository evidence already answers them.
- Treating "modern," "clean," or "premium" as a usable direction.
- Choosing a component library before understanding the information hierarchy.

## Checklist

- The primary audience, task, and outcome are explicit.
- Required content and states are known.
- Existing tokens and component systems were inspected.
- Brand traits include both desired and forbidden qualities.
- Assumptions and approval decisions are visible.
