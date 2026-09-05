---
name: web-designer
description: Use when designing, redesigning, critiquing, or polishing web UI/UX for creative direction, visual style, composition, interaction, responsive behavior, accessibility, shadcn/ui composition, and anti-slop review.
---

# Web Designer Skill

Use this skill for web UI/UX design direction. It is a creative reasoning skill, not a page-template library. When implementation is requested and the project supports it, use shadcn/ui as the accessible component foundation without accepting its defaults as the visual direction.

## When to load

- The user asks for web design, UI/UX, visual direction, layout, landing pages, app screens, dashboards, polish, redesign, critique, or styling ideas.
- The task needs taste, hierarchy, composition, brand feel, responsive behavior, accessibility, or interaction design.
- The user wants something more distinctive, less generic, or less like a common AI-generated SaaS page.
- You are about to implement a visually meaningful UI and need a design thesis before code.
- A design must be translated into a concrete shadcn/ui component and state plan.

## When NOT to load

- The task is only framework behavior, routing, data fetching, validation, or state architecture with no design judgment.
- The user wants pixel-perfect implementation from an existing approved design and no visual decisions remain; use the relevant frontend and testing skills.
- The UI work is incidental to a mostly backend task.
- The request is only to install or troubleshoot shadcn/ui or Tailwind; use current official documentation and the relevant framework skill.

## Prime directive

Make a point of view. Do not produce generic "modern clean" UI.

Every creative output should have:

- A design thesis: what the interface should feel like and why.
- A visual stance: type, color, density, shape, surface, imagery, and motion choices.
- A composition plan: hierarchy, rhythm, breakpoints, and focal points.
- A UX plan: affordances, states, feedback, and recovery paths.
- An accessibility plan: semantics, keyboard behavior, focus, contrast, and reduced motion.
- An anti-slop check: which defaults were avoided and what still needs validation.

## shadcn/ui baseline

- Inspect `components.json`, the configured aliases, global CSS, theme variables, `components/ui/`, and existing compositions before proposing new primitives.
- Reuse installed and customized shadcn/ui components before adding equivalents. Treat them as project-owned source code.
- If a compatible project lacks a needed primitive, prefer the official CLI for individual components: `npx shadcn@latest add <component>`. Get approval before initialization or dependency-changing commands.
- Use `npx shadcn@latest info` or a dry run when available to understand the current setup before writing over files.
- Never overwrite a customized component blindly, install every component, or copy an unofficial lookalike when an accessible official primitive fits.
- shadcn/ui is the behavioral and accessibility substrate, not the aesthetic. Express the design thesis through tokens, composition, typography, content, and deliberate variants.
- If the project uses another established design system, preserve it instead of forcing shadcn/ui.

## Routing table

| Need                                                                               | Load                          |
| ---------------------------------------------------------------------------------- | ----------------------------- |
| Define goals, audience, constraints, and success criteria                          | `creative-brief.md`           |
| Establish the visual thesis, type, color, surface, imagery, and motion stance      | `visual-direction.md`         |
| Plan hierarchy, layout rhythm, density, and focal points                           | `composition.md`              |
| Define flows, affordances, states, feedback, and recovery                          | `interaction-ux.md`           |
| Specify breakpoint behavior, keyboard use, semantics, contrast, and reduced motion | `responsive-accessibility.md` |
| Audit an existing interface and remove generic or incoherent choices               | `critique.md`                 |
| Translate approved direction into components, tokens, states, and shadcn/ui work   | `implementation-handoff.md`   |

## Typical load combinations

- New page: `creative-brief.md` + `visual-direction.md` + `composition.md`.
- Product flow: `creative-brief.md` + `interaction-ux.md` + `responsive-accessibility.md`.
- Redesign: `critique.md` + `visual-direction.md` + `composition.md`.
- Implementation-ready spec: the approved design leaves + `implementation-handoff.md`.
- Visual polish: `critique.md` + the one leaf covering the identified weakness.

## Workflow

1. Inspect the current interface, content, assets, design tokens, and component inventory.
2. State confirmed evidence, assumptions, and the one or two decisions that matter most.
3. Form a design thesis before selecting components.
4. Define composition, interaction, responsive, and accessibility behavior.
5. Map the approved direction to existing components and shadcn/ui primitives.
6. Implement only when requested, then verify in a real browser at representative viewports.
7. Run the anti-slop critique and repair the weakest visible decision.

Work directly in the selected session by default, including economy sessions.
Scale the design notes to the task: a bounded correction with approved direction
does not need a new design ceremony or specialist handoff. Optional specialist
help needs parent approval and configured task permissions/depth.

## Hard rules

- No generic SaaS hero, feature-card grid, icon row, or dashboard shell by default.
- No automatic blue-purple gradient, glassmorphism, excessive rounded cards, or decorative blur.
- No arbitrary visual novelty that weakens comprehension, accessibility, or task completion.
- No page template presented as a finished design without content and context.
- No code before the design thesis and state requirements are clear, unless the user supplied an approved design.
- No shadcn/ui default styling presented as custom design; adapt it deliberately.
- No inaccessible custom primitive when a suitable shadcn/ui primitive already handles semantics and keyboard behavior.

## Stop triggers

- Materially ambiguous user flow or information architecture: clarify the blocking decision before implementation; specialist review is optional and permission-gated.
- Clear design with implementation work: implement directly, using `implementation-handoff.md` as a checklist when useful, not a required agent handoff.
- Framework-specific implementation: load the framework, language, testing, and browser-testing skills.
- Authentication, sensitive input, uploads, or external content: load the security skill.
- A library API or CLI detail may have changed: retrieve current official documentation before prescribing it.

## Related skills

- `frontend-ui-engineering` for production frontend implementation.
- `testing` with `skills/testing/e2e-playwright.md` for available Playwright browser checks; `browser-testing-with-devtools` only for available Chrome DevTools-specific diagnostics. If neither browser route is usable, run permitted local tests and report live/visual verification as blocked; do not install a server implicitly.
- `react`, `nextjs`, `typescript`, or another stack skill for framework conventions.
- `testing` for deterministic behavior and accessibility tests.
