---
description: Lint ~/.config/opencode/skills for consistency
---

Run the global skills linter and fix any issues.

Run:

```bash
python3 -B "$HOME/.config/opencode/scripts/skills_lint.py"
python3 -B "$HOME/.config/opencode/scripts/skills_lint.py" --skills-dir "$HOME/.config/opencode/.agents/skills"
```

If there are errors:

- Identify the failing file(s)
- Apply minimal fixes to satisfy required headings / frontmatter
- Re-run the linter until it passes
