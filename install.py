#!/usr/bin/env python3
"""Install selected skills for Claude Code, Codex, or both."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
SKILLS_ROOT = REPO_ROOT / "skills"


@dataclass(frozen=True)
class Skill:
    name: str
    category: str
    path: Path


def discover_skills(root: Path = SKILLS_ROOT) -> list[Skill]:
    skills: list[Skill] = []
    if not root.is_dir():
        return skills

    for skill_file in root.rglob("SKILL.md"):
        directory = skill_file.parent
        relative = directory.relative_to(root)
        category = "/".join(relative.parts[:-1]) or "uncategorized"
        skills.append(Skill(directory.name, category, directory))

    return sorted(skills, key=lambda skill: (skill.category, skill.name))


def parse_selection(value: str, skills: list[Skill]) -> list[Skill]:
    value = value.strip().lower()
    if value in {"all", "a", "*"}:
        return skills

    selected: list[Skill] = []
    seen: set[str] = set()
    by_name = {skill.name: skill for skill in skills}

    for item in (part.strip() for part in value.split(",")):
        if not item:
            continue
        if item.isdigit():
            index = int(item) - 1
            if index < 0 or index >= len(skills):
                raise ValueError(f"skill number out of range: {item}")
            skill = skills[index]
        elif item in by_name:
            skill = by_name[item]
        else:
            raise ValueError(f"unknown skill: {item}")
        if skill.name not in seen:
            selected.append(skill)
            seen.add(skill.name)

    if not selected:
        raise ValueError("no skills selected")
    return selected


def prompt_choice(prompt: str, choices: dict[str, str]) -> str:
    while True:
        answer = input(prompt).strip().lower()
        if answer in choices:
            return choices[answer]
        print(f"Choose one of: {', '.join(choices)}", file=sys.stderr)


def prompt_for_configuration(skills: list[Skill]) -> tuple[list[str], str, list[Skill]]:
    print("Available skills:\n")
    current_category = None
    for index, skill in enumerate(skills, start=1):
        if skill.category != current_category:
            current_category = skill.category
            print(f"  {current_category}")
        print(f"    {index}. {skill.name}")

    print()
    agents_value = prompt_choice(
        "Install for [1] Claude, [2] Codex, or [3] both? ",
        {"1": "claude", "2": "codex", "3": "both", "claude": "claude", "codex": "codex", "both": "both"},
    )
    agents = ["claude", "codex"] if agents_value == "both" else [agents_value]
    scope = prompt_choice(
        "Install for [1] this user or [2] this project? ",
        {"1": "user", "2": "project", "user": "user", "project": "project"},
    )

    while True:
        answer = input("Select skills by number/name (comma-separated), or 'all': ")
        try:
            selected = parse_selection(answer, skills)
            return agents, scope, selected
        except ValueError as error:
            print(error, file=sys.stderr)


def destination_root(agent: str, scope: str, project_root: Path) -> Path:
    if scope == "project":
        return project_root / (".claude/skills" if agent == "claude" else ".agents/skills")

    home = Path(os.environ.get("HOME", str(Path.home()))).expanduser()
    return home / (".claude/skills" if agent == "claude" else ".agents/skills")


def install_skill(skill: Skill, destination: Path, *, force: bool, dry_run: bool) -> str:
    target = destination / skill.name
    if target.exists() and not force:
        return f"SKIP {target} (already exists; use --force to replace)"
    if dry_run:
        action = "REPLACE" if target.exists() else "INSTALL"
        return f"{action} {skill.name} -> {target}"

    destination.mkdir(parents=True, exist_ok=True)
    temporary = Path(tempfile.mkdtemp(prefix=f".{skill.name}-", dir=destination))
    staged = temporary / skill.name
    try:
        shutil.copytree(skill.path, staged)
        if target.is_symlink():
            target.unlink()
        elif target.is_dir():
            shutil.rmtree(target)
        elif target.exists():
            target.unlink()
        staged.replace(target)
    finally:
        shutil.rmtree(temporary, ignore_errors=True)
    return f"INSTALLED {skill.name} -> {target}"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Install selected repository skills for Claude Code and/or Codex."
    )
    parser.add_argument(
        "--agent",
        action="append",
        choices=("claude", "codex"),
        help="target agent; repeat to install for both",
    )
    parser.add_argument(
        "--scope",
        choices=("user", "project"),
        default="user",
        help="install globally for the current user or into a project (default: user)",
    )
    parser.add_argument(
        "--project-root",
        type=Path,
        default=Path.cwd(),
        help="project directory for --scope project (default: current directory)",
    )
    parser.add_argument(
        "--skill",
        action="append",
        help="skill name to install; repeat to select multiple",
    )
    parser.add_argument("--all", action="store_true", help="install every discovered skill")
    parser.add_argument("--list", action="store_true", help="list available skills and exit")
    parser.add_argument("--force", action="store_true", help="replace existing selected skills")
    parser.add_argument("--dry-run", action="store_true", help="show changes without copying files")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    skills = discover_skills()
    if not skills:
        parser.error(f"no skills found under {SKILLS_ROOT}")

    if args.list:
        for skill in skills:
            print(f"{skill.name}\t{skill.category}")
        return 0
    if args.all and args.skill:
        parser.error("use either --all or --skill, not both")

    explicit = bool(args.agent or args.skill or args.all)
    if not explicit and sys.stdin.isatty():
        agents, scope, selected = prompt_for_configuration(skills)
    else:
        agents = list(dict.fromkeys(args.agent or []))
        scope = args.scope
        if not agents:
            parser.error("--agent is required in non-interactive mode")
        if args.all:
            selected = skills
        elif args.skill:
            try:
                selected = parse_selection(",".join(args.skill), skills)
            except ValueError as error:
                parser.error(str(error))
        else:
            parser.error("select at least one --skill or use --all")

    project_root = args.project_root.expanduser().resolve()
    skipped = False
    for agent in agents:
        destination = destination_root(agent, scope, project_root)
        for skill in selected:
            result = install_skill(skill, destination, force=args.force, dry_run=args.dry_run)
            print(f"[{agent}] {result}")
            skipped = skipped or result.startswith("SKIP")
    return 1 if skipped else 0


if __name__ == "__main__":
    raise SystemExit(main())
