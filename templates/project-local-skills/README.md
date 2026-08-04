# Project-Local Skills Template

Project-local skills live in `.opencode/skills/` inside a repo and override global skills.

Copy this folder into your project root, then customize the skill name and leaf docs.

Example tree:

```text
.opencode/
  skills/
    example/
      SKILL.md
      routing.md
```

Run the global linter (from your OpenCode config repo) to validate skills:

```bash
python3 ~/.config/opencode/scripts/skills_lint.py --skills-dir .opencode/skills
```
