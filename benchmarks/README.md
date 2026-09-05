# Skill Benchmarks

These benchmarks are regression tests for the skills system.

Each benchmark should specify:

- Prompt (what a developer asks)
- Expected skill loads (router + 1-2 leaves)
- Expected output traits (structure + tests + contracts)

See `skills/skill-authoring/benchmarks.md` for the benchmark format.

Lint benchmarks:

```bash
python3 -B "$HOME/.config/opencode/scripts/benchmarks_lint.py"
```

Each `##` scenario in a benchmark file must have its own non-empty `Prompt:`,
`Expected loads:`, and `Expected traits:` sections. Static lint validates this
contract only; it does not run models or prove routing behavior.

## Live benchmark status

**Not yet run. No A/B results are claimed.** Keep current reasoning settings until
repeatable evidence supports a change. Paid model calls, external review, plugin
changes, memory writes, and benchmark fixture Git operations require separate
authorization. This procedure is documentation, not permission to execute them.

Configuration baseline (2026-09-05): native `compaction.auto` and `prune` remain
enabled. The formerly configured `opencode-dynamic-context-pruning` package
returned npm 404 and had no installed contents, so its broken entry was removed.
The plugin-assisted arm is blocked until an explicitly approved, available
package/version is validated. This is a dependency repair, not an A/B result.
The installed memory plugin's `inherit` mode selects the prompt's model, then a
recent model as fallback; it does not automatically select a smaller extractor.

## Controlled fixtures

Use disposable, isolated checkouts from a fixed recorded revision, never the dirty
configuration checkout. Record fixture hashes and an independent answer key before
each run. Preserve identical prompts, source, permissions, browser availability,
and acceptance criteria across variants.

- **Repair/no-commit:** a known failing parser boundary test and one unrelated
  dirty sentinel. Record HEAD, branch, index/tree hashes, and untracked inventory
  before/after. The agent may modify only the parser and its test, not Git state.
- **WIP-only:** HEAD equals the named base. Seed a missing empty-input check in a
  staged file, missing negative-input rejection in an unstaged file, and a missing
  upper-bound check in an untracked file. Supply their expected contract; record
  the three independent diffs/content hashes. No credentials or real user data.
- **Combined review:** add a prebuilt committed defect and all three WIP layers.
  Include a same-file staged change canceled by an unstaged edit. Repeat with an
  invalid base and with committed-only scope to test inclusion/exclusion rules.
- **Browser:** use a deterministic local checkout page with approved design,
  fixed data, viewport dimensions, and a reproducible overflow. Run once with
  Playwright available/DevTools absent, once with neither route available. Treat
  an honest blocked check as correct in the unavailable-tools condition.
- **Economy:** use the same bounded UI fixture and a separate read-only inventory
  package. Record actual task permissions and depth; repeat with task denied or
  exhausted. Never give a benchmark worker greater authority to improve its score.

Fixture preparation (including any authorized commits/staging) belongs to the
operator before the measured session, not to the no-commit test agent. Restore
only disposable fixture-owned state between runs; preserve original traces.

## Repeatable A/B procedure

1. Obtain approval for the specific run matrix, spend cap, data sharing, and any
   isolated config/plugin changes. Verify supported variants from the installed
   provider/runtime before running; mark unsupported options blocked, not inferred.
2. Record runtime/provider/model/plugin versions, exact model ID and reasoning
   setting, config hash, fixture revision, tool availability, timeout/token budget,
   cache condition, and initial memory/pruning state. Exclude secrets from records.
3. Run a baseline and one changed factor in fresh sessions. Use at least three
   paired repetitions per scenario, alternating/randomizing order and recording
   that order. Keep all other settings and fixtures fixed; do not reuse a session
   that has seen another arm's solution.
4. Save the prompt, tool trace, final answer, diff/state checks, tests, wall-clock
   latency, input/output/cached tokens, spend, retries, worker count, maximum depth,
   and blocked checks. Record unavailable metrics as unavailable, never zero.
5. Score against the independent answer key: acceptance criteria passed, seeded
   regressions caught, false-positive findings, scope/authorization violations,
   unrequested ceremonies, and honest treatment of missing capabilities. Blind
   the scorer to the arm where practical. No-commit, confidentiality, permission,
   and no-fabricated-verification constraints are hard gates.
6. Compare quality first, then median/range latency, tokens, and spend for passing
   runs. Keep individual failures visible; small samples are directional evidence,
   not proof of superiority. Repeat any promising result on a held-out fixture.
7. Propose a settings change only after results and risks are reviewed. Do not
   update live reasoning, memory, or pruning configuration as part of scoring.

## One-factor experiment matrix

| Factor              | Arms (verify support first)                                      | Controls and evidence                                                                                                                                                                                                                                                                                                                                  |
| ------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Luna bounded worker | `low` / `medium` / `max`                                         | Same text-only mechanical fixtures, primary model and permissions fixed; measure correct changes, scope violations, latency, and token use. Keep economy-orchestrator settings unchanged.                                                                                                                                                              |
| Astra analysis      | `medium` / `high`                                                | Same pinned model/analyst role and read-only review fixtures; measure seeded-defect recall, unsupported findings, and reasoning cost. Keep principal/other roles unchanged.                                                                                                                                                                            |
| Memory extraction   | Disabled baseline / current extractor enabled                    | Replay the same synthetic transcript containing known durable preferences, corrections, transient details, and secret-shaped decoys in isolated test storage. Score precision/recall, provenance, stale/conflicting memories, sensitive-content exclusion, token cost, and downstream answer accuracy. No real secrets or writes to production memory. |
| Context pruning     | Native only / plugin-assisted with native settings held constant | Replay the same deterministic long tool transcript across a compaction boundary. Pin the actual plugin version/settings. Measure context/token reduction, latency, lost source/acceptance facts, duplicated or over-pruned content, and task success. Add plugin-only only if supported and explicitly approved; do not assume it is equivalent.       |

Do not combine a reasoning change with memory or pruning changes in one comparison.
Memory and pruning trials need isolated state per arm, fixed transcript lengths,
and ground-truth probes before and after extraction/compaction. Record conflicts
or unsupported controls as limitations rather than inventing implementation details.

## Result record template

```text
Status: not run | completed | blocked
Experiment/scenario/repetition/order:
Fixture revision/hash and answer-key version:
Model/provider/runtime/config/plugin versions and changed factor:
Permissions/depth/browser/memory/pruning/cache controls:
Acceptance score and hard-gate violations:
Tests/state-preservation checks and artifact paths:
Latency/tokens/spend/retries/workers/depth:
False positives, missed defects, and unavailable metrics:
Conclusion/limitations/approved follow-up:
```
