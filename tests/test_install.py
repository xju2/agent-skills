import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import install


class InstallerTests(unittest.TestCase):
    def make_skill(self, root: Path, category: str, name: str) -> install.Skill:
        path = root / category / name
        path.mkdir(parents=True)
        (path / "SKILL.md").write_text(f"---\nname: {name}\ndescription: Test\n---\n", encoding="utf-8")
        return install.Skill(name, category, path)

    def test_discovers_nested_skills_and_ignores_other_directories(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            self.make_skill(root, "coding-agents", "bootstrap")
            self.make_skill(root, "proposal", "review")
            (root / "not-a-skill").mkdir()
            self.assertEqual(
                [(skill.category, skill.name) for skill in install.discover_skills(root)],
                [("coding-agents", "bootstrap"), ("proposal", "review")],
            )

    def test_selection_accepts_numbers_names_and_all(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skills = [self.make_skill(root, "category", "first"), self.make_skill(root, "category", "last")]
            self.assertEqual(install.parse_selection("all", skills), skills)
            chosen = install.parse_selection("1,last", skills)
            self.assertEqual(chosen, skills)

    def test_installs_for_both_agents_in_project_scope(self):
        with tempfile.TemporaryDirectory() as directory:
            project = Path(directory)
            source = project / "source"
            skill = self.make_skill(source, "proposal", "red-team-review")
            args = [
                "--agent", "claude", "--agent", "codex", "--scope", "project",
                "--project-root", str(project), "--skill", "red-team-review",
            ]
            with mock.patch.object(install, "discover_skills", return_value=[skill]):
                result = install.main(args)
            self.assertEqual(result, 0)
            self.assertTrue((project / ".claude/skills/red-team-review/SKILL.md").is_file())
            self.assertTrue((project / ".agents/skills/red-team-review/SKILL.md").is_file())

    def test_refuses_existing_skill_without_force(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = self.make_skill(root, "source", "example")
            destination = root / "destination"
            target = destination / skill.name
            target.mkdir(parents=True)
            sentinel = target / "keep.txt"
            sentinel.write_text("keep", encoding="utf-8")
            result = install.install_skill(skill, destination, force=False, dry_run=False)
            self.assertTrue(result.startswith("SKIP"))
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")

    def test_force_replaces_existing_skill(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = self.make_skill(root, "source", "example")
            destination = root / "destination"
            target = destination / skill.name
            target.mkdir(parents=True)
            (target / "stale.txt").write_text("stale", encoding="utf-8")
            install.install_skill(skill, destination, force=True, dry_run=False)
            self.assertTrue((target / "SKILL.md").is_file())
            self.assertFalse((target / "stale.txt").exists())

    def test_force_unlinks_directory_symlink_without_removing_its_target(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            skill = self.make_skill(root, "source", "example")
            destination = root / "destination"
            destination.mkdir()
            linked_directory = root / "linked-skill"
            linked_directory.mkdir()
            sentinel = linked_directory / "keep.txt"
            sentinel.write_text("keep", encoding="utf-8")
            (destination / skill.name).symlink_to(linked_directory, target_is_directory=True)

            install.install_skill(skill, destination, force=True, dry_run=False)

            target = destination / skill.name
            self.assertFalse(target.is_symlink())
            self.assertTrue((target / "SKILL.md").is_file())
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "keep")

    def test_user_scope_uses_home(self):
        with tempfile.TemporaryDirectory() as directory:
            previous = os.environ.get("HOME")
            os.environ["HOME"] = directory
            try:
                self.assertEqual(
                    install.destination_root("codex", "user", Path("unused")),
                    Path(directory) / ".agents/skills",
                )
                self.assertEqual(
                    install.destination_root("claude", "user", Path("unused")),
                    Path(directory) / ".claude/skills",
                )
            finally:
                if previous is None:
                    os.environ.pop("HOME", None)
                else:
                    os.environ["HOME"] = previous


if __name__ == "__main__":
    unittest.main()
