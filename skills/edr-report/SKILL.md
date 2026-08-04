---
name: edr-report
description: End-of-day report drafting for intern shifts using a project-manager tone
---

# EDR Report Skill Index

Use this skill to draft concise, professional end-of-day reports from actual work evidence.

## When to load

- You need to generate an End of Day Report (EDR/EOD) for a shift.
- You want project-manager style wording for accomplishments and next steps.
- You need to keep a strict template with placeholders for unknown fields.

## When NOT to load

- You are writing code/docs unrelated to shift reporting.
- You need weekly/monthly summaries (use a different reporting format).

## Routing table

| Task                                             | Load                 |
| ------------------------------------------------ | -------------------- |
| Draft a standard daily report from repo evidence | `report-template.md` |
| Fill placeholders and improve clarity/tone       | `report-template.md` |
| Convert rough notes into manager-ready EDR       | `report-template.md` |

## Typical load combos

- EDR from git activity: load `report-template.md` + `git`.
- EDR from docs/task notes: load `report-template.md` + `documentation`.

## Identity defaults

Always use these values — never leave them as placeholders:

- **NAME**: Danilo Casim Jr
- **POSITION**: IT Intern

## Stop triggers

- No reliable evidence for completed work -> keep claims conservative and state what was verified.
- Missing attendance fields (time in/out) -> keep placeholders, do not invent values.

## Drafting rules

- Use same-day commit messages as the primary evidence source for `END OF DAY REPORT` accomplishments.
- Keep accomplishments in normal, non-technical language (manager-friendly, no commit IDs).
- Do not add extra explanatory phrases under section headers; keep headers clean.
- Default required user inputs are: `TIME IN`, `BREAK`, `TIME OUT`, `NEXT STEPS`, and `NEXT SHIFT`.

## Related skills

- `git`
- `documentation`
