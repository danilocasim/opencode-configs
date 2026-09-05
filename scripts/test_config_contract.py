"""Static regression checks for the global configuration's safety contract.

These checks never load runtime credentials or initialize plugins. Validate the
merged configuration separately with OpenCode; these are not sandbox tests.
"""

from __future__ import annotations

import json
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ConfigurationContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.config = json.loads((ROOT / "opencode.json").read_text())

    def agent(self, name: str) -> str:
        return (ROOT / "agents" / f"{name}.md").read_text().split("---", 2)[1]

    def test_astra_default_and_no_nested_delegation(self) -> None:
        self.assertEqual(self.config["model"], "openai/gpt-6-astra")
        self.assertEqual(self.config["default_agent"], "orchestrator")
        self.assertEqual(self.config["subagent_depth"], 1)
        primary = self.agent("orchestrator")
        self.assertIn("variant: high", primary)
        self.assertIn("economy-bounded-worker: allow", primary)

    def test_shell_requires_approval_outside_narrow_read_commands(self) -> None:
        rules = self.config["permission"]["bash"]
        self.assertEqual(rules["*"], "ask")
        for command in ("git commit*", "git push*", "git rebase*", "git reset*"):
            self.assertEqual(rules[command], "ask")
        for command in ("python*", "node*", "bash*", "sh*", "git *"):
            self.assertNotEqual(rules.get(command), "allow")
        for command in ("git status", "git diff", "git log", "git show"):
            self.assertEqual(rules[command], "allow")
            self.assertEqual(rules[f"{command} *"], "allow")
            self.assertNotEqual(rules.get(f"{command}*"), "allow")

    def test_runtime_secret_is_ignored_and_denied_without_reading_it(self) -> None:
        self.assertIn("/service.json", (ROOT / ".gitignore").read_text().splitlines())
        for operation in ("read", "edit"):
            self.assertEqual(
                self.config["permission"][operation]["**/opencode/service.json"],
                "deny",
            )

    def test_integrations_are_pinned_and_updates_are_opt_in(self) -> None:
        self.assertEqual(self.config["autoupdate"], "notify")
        for plugin in self.config["plugin"]:
            self.assertRegex(plugin, r"@\d+\.\d+\.\d+(?:[-+][\w.-]+)?$")
        for name in ("playwright", "zai-mcp-server"):
            command = self.config["mcp"][name]["command"]
            self.assertIn("-y", command)
            self.assertTrue(
                any(re.search(r"@\d+\.\d+\.\d+$", part) for part in command)
            )

    def test_repository_analysts_have_no_browser_or_memory_mutation_tools(self) -> None:
        for name in ("repository-analyst", "economy-repository-analyst"):
            frontmatter = self.agent(name)
            for rule in (
                '"playwright_*": deny',
                '"zai-mcp-server_*": deny',
                "memory: deny",
            ):
                self.assertIn(rule, frontmatter)
            self.assertIn("task: deny", frontmatter)

    def test_browser_access_is_role_scoped_and_unsafe_rce_is_denied(self) -> None:
        permissions = self.config["permission"]
        self.assertEqual(permissions["playwright_*"], "deny")
        self.assertEqual(permissions["playwright_browser_run_code_unsafe"], "deny")
        for name in ("orchestrator", "economy-orchestrator", "visual-engineer"):
            frontmatter = self.agent(name)
            self.assertIn('"playwright_*": allow', frontmatter)
            self.assertIn('"playwright_browser_run_code_unsafe": deny', frontmatter)

    def test_owned_shell_guidance_and_modern_step_fields(self) -> None:
        self.assertIn("instructions/shell.md", self.config["instructions"])
        self.assertNotIn(
            "plugin/shell-strategy/shell_strategy.md", self.config["instructions"]
        )
        for name in ("visual-engineer", "ui-ux-analyst"):
            self.assertNotIn("maxSteps:", self.agent(name))
            self.assertRegex(self.agent(name), r"(?m)^steps: \d+$")


if __name__ == "__main__":
    unittest.main()
