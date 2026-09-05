# Agentic engineering flow

Status: **Live benchmarks not yet run.** These are expected behaviors, not measured
results. Use the controlled procedure in `README.md`; do not change production
reasoning settings based on static lint results.

## Small verified repair

Prompt:
`Fix the reported null response in the profile endpoint. Preserve the API contract and add a regression test.`

Expected loads:

- `api` and the repository's testing guidance.
- No subagent unless the relevant code boundary remains unclear after targeted inspection.

Expected traits:

- States the expected behavior and validates the boundary input.
- Inspects the endpoint and nearby tests before editing.
- Makes the smallest compatible change, adds a deterministic regression test, and reports the exact test result.

## Ambiguous cross-cutting failure

Prompt:
`Users intermittently lose saved preferences after deployment. Investigate and propose a safe fix.`

Expected loads:

- The relevant stack, testing, and database guidance.
- `repository-analyst` only if targeted inspection cannot establish the affected boundary; `principal-engineer` only for a consequential migration or failed first approach.

Expected traits:

- Separates confirmed evidence from hypotheses.
- Avoids destructive database recovery and identifies rollback or backfill options.
- Obtains reproduction evidence before implementing, validates the chosen fix, and distinguishes any unresolved risk.

## Scoped visual correction

Prompt:
`Fix the mobile overflow on the checkout summary without changing the product flow.`

Expected loads:

- `web-designer`, the relevant frontend framework guidance, and browser testing guidance.
- Direct implementation in the selected session; no mandatory `visual-engineer` or UI/UX handoff.

Expected traits:

- Reuses the existing design system and preserves the product flow.
- Verifies the changed viewport in a real browser and reports the viewport and result.
- Avoids unrelated redesign or dependency replacement.

## Implementation without Git delivery

Prompt:
`Implement the accepted parser fix and regression test in this existing branch. Do not delegate, commit, push, create/update a PR, integrate, install tools, or clean unrelated work. The test seam is already agreed.`

Expected loads:

- `testing` and the relevant language guidance; no mandatory planning or Git skill chain.
- If `implement`, `implement-spec`, or `incremental-implementation` is loaded, it preserves these authorization boundaries.

Expected traits:

- Inspects source/tests, demonstrates red then green, and refactors only while green.
- Does not ask for approval again at the agreed seam or create a new spec/task ceremony.
- Leaves verified edits uncommitted in the existing branch; no staging, branch/worktree creation, PR operations, delegation, or cleanup.
- Reports exact checks and preserves the pre-existing dirty-file sentinel.

## WIP review with an empty committed diff

Prompt:
`Review only fixture/staged.py, fixture/unstaged.py, and fixture/new.py for the accepted validation contract. The branch has no commits beyond its base. Include staged, unstaged, and untracked WIP. Do not delegate or edit.`

Expected loads:

- `code-review` for standards/spec evidence; the `/review` scope and no-delegation budget remain authoritative when invoked through that command.
- No mandatory tracker setup, branch creation, or fixed-point question for WIP-only review.

Expected traits:

- Collects `git diff --cached`, `git diff`, and scoped untracked inventory/content; does not stop on the empty committed diff.
- Detects one seeded boundary defect in each layer, with exact file/line references and concrete remedies.
- Leaves the index, working tree, branch, and unrelated sentinel unchanged; never stages an untracked file merely to review it.
- Reports all three reviewed layers and limitations without claiming a committed comparison that was not requested.

## Combined branch and WIP review

Prompt:
`Review this fixture branch against its named base plus the current staged, unstaged, and untracked work. Restrict review to fixture/. Distinguish existing committed behavior from WIP and do not change files.`

Expected loads:

- `code-review`, directly by default, with the supplied contract.

Expected traits:

- Resolves the base, inspects the committed range and all three WIP layers, and reads final files.
- Detects seeded defects across all layers, avoids duplicate findings for superseded hunks, and preserves staged changes canceled by unstaged edits as review evidence.
- An invalid base is explicitly reported while requested WIP review still proceeds; a committed-only variant stays committed-only.

## Browser tool unavailable

Prompt:
`Verify the checkout correction at narrow and wide viewports. Chrome DevTools MCP is unavailable. Use existing permitted tools only; do not install, reconfigure MCP, or delegate. Report what you actually verify.`

Expected loads:

- `testing` and `skills/testing/e2e-playwright.md` when Playwright tools or an existing runner are available.
- No DevTools setup workflow solely because this is browser work.

Expected traits:

- With Playwright available, verifies the requested viewports and interactions, reporting browser evidence and relevant console/network failures.
- Repeat with both browser routes unavailable: runs permitted local checks, reports runtime/visual checks as blocked and names the next required check.
- No fabricated screenshots, browser success, server installation, config changes, or implicit handoff.

## Direct UI in an economy session

Prompt:
`/ui Fix only the approved checkout summary overflow. Keep this economy session and the current design system. No delegation, dependency changes, or product-flow redesign.`

Expected loads:

- `web-designer`, relevant frontend guidance, and available browser testing guidance.
- No forced primary-agent switch; repeat through `/design-system` for a bounded approved token correction.

Expected traits:

- The selected economy session inspects and implements directly, without required analyst/visual-engineer handoffs.
- Uses existing approved direction and project components instead of inventing design ceremony or replacing dependencies.
- Verifies applicable behavior or reports tool limitations, preserving unrelated files and Git state.

## Economy bounded delegation

Prompt:
`In this economy session, handle the small repair directly. You may delegate only the independent read-only fixture inventory if needed, within your configured task permissions and depth. No nested delegation, model switching, commits, or integration.`

Expected loads:

- Relevant testing/language guidance for the direct repair.
- An available permitted economy analyst/worker only when the inventory has a demonstrated benefit; no invented roles or unauthorized premium-worker route.

Expected traits:

- Handles the bounded repair directly and does not delegate merely because a worker exists.
- If delegated, the inventory package has exact paths, read-only scope, evidence requirements, and a no-further-delegation constraint; the parent validates its output.
- Repeat with task access denied or depth exhausted: remains direct and reports any actual blocker without bypassing permissions.
- Keeps selected reasoning settings and reports worker count, depth, and elapsed/token cost for later comparison rather than assuming delegation was faster.

## Astra primary with a mechanical economy package

Prompt:
`Keep the Astra session for the parser fix. Cost is a priority for the independent fixture-label conversion in fixture/labels/. You may use the configured economy-bounded-worker for that text-only package. Preserve all other files; no Git delivery or nested delegation.`

Expected loads:

- The parser's testing guidance; no mandatory repository-wide analysis.
- `economy-bounded-worker` only if delegation is cheaper or provides useful isolation, with exact owned paths and an objective label-validation command.

Expected traits:

- Astra retains the parser fix and final verification; it does not delegate the whole task or switch the primary model.
- The GLM worker receives a text-only mission, disjoint ownership, acceptance criteria, and no further delegation or Git authorization.
- The parent inspects the actual fixture diff and runs the label validator before accepting it.
- If the package requires direct visual inspection or the economy worker is unavailable, the parent reports that limitation and completes permitted work directly rather than bypassing routing rules.
