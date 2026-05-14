#!/usr/bin/env python3
"""Create and configure a GitHub repository for the current project."""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


LABELS = [
    ("Feature", "0e8a16"),
    ("Bug", "d85c56"),
    ("DevOps", "5319e7"),
    ("Documentation", "1d76db"),
    ("Refactor", "fbca04"),
    ("Testing", "d93f0b"),
    ("Update", "006b75"),
]


PROJECT_FIELDS = [
    ("Status", ["Todo", "In Progress", "Done"]),
    ("Priority", ["Low", "Medium", "High", "Urgent"]),
]

PROJECT_TEMPLATE_OWNER = "joegoggin"
PROJECT_TEMPLATE_NUMBER = "32"
REQUIRED_PROJECT_VIEW_FIELDS = {
    "Title",
    "Labels",
    "Status",
    "Priority",
    "Parent issue",
    "Sub-issues progress",
    "Linked pull requests",
    "Repository",
}


class CreateRepoError(RuntimeError):
    """Raised when the workflow cannot safely continue."""


def run(
    args: list[str],
    *,
    dry_run: bool = False,
    capture: bool = False,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    print("+ " + " ".join(shell_quote(part) for part in args))
    if dry_run and is_mutating_command(args):
        return subprocess.CompletedProcess(args, 0, "", "")

    return subprocess.run(
        args,
        check=check,
        text=True,
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
    )


def run_json(args: list[str], *, dry_run: bool = False) -> Any:
    completed = run(args, dry_run=dry_run, capture=True)
    if dry_run and is_mutating_command(args):
        return {}
    try:
        return json.loads(completed.stdout or "{}")
    except json.JSONDecodeError as exc:
        raise CreateRepoError(
            f"Expected JSON output from command but could not parse it: {' '.join(args)}"
        ) from exc


def shell_quote(value: str) -> str:
    if not value:
        return "''"
    if all(char.isalnum() or char in "._-/=:@" for char in value):
        return value
    return "'" + value.replace("'", "'\"'\"'") + "'"


def is_mutating_command(args: list[str]) -> bool:
    if not args:
        return False
    if args[:2] == ["git", "init"]:
        return True
    if args[:3] == ["git", "branch", "-m"]:
        return True
    if args[:3] == ["git", "remote", "add"]:
        return True
    if args[:2] == ["git", "add"]:
        return True
    if args[:2] == ["git", "commit"]:
        return True
    if args[:2] == ["git", "push"]:
        return True
    if args[:3] == ["gh", "repo", "create"]:
        return True
    if args[:3] == ["gh", "label", "delete"]:
        return True
    if args[:3] == ["gh", "label", "create"]:
        return True
    if args[:3] == ["gh", "project", "create"]:
        return True
    if args[:3] == ["gh", "project", "copy"]:
        return True
    if args[:3] == ["gh", "project", "edit"]:
        return True
    if args[:3] == ["gh", "project", "field-create"]:
        return True
    if args[:3] == ["gh", "project", "link"]:
        return True
    return False


def require_command(name: str) -> None:
    try:
        subprocess.run(
            [name, "--version"],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise CreateRepoError(f"Required command is missing or unavailable: {name}") from exc


def ensure_gh_auth() -> None:
    completed = run(["gh", "auth", "status"], capture=True, check=False)
    output = (completed.stdout or "") + (completed.stderr or "")
    if completed.returncode != 0:
        raise CreateRepoError("GitHub CLI is not authenticated. Run `gh auth login` first.")
    missing = [scope for scope in ("repo", "project") if scope not in output]
    if missing:
        joined = ", ".join(missing)
        raise CreateRepoError(
            "GitHub CLI token is missing required scope(s): "
            f"{joined}. Run `gh auth refresh -s repo -s project`."
        )


def current_github_login() -> str:
    completed = run(["gh", "api", "user", "--jq", ".login"], capture=True)
    login = completed.stdout.strip()
    if not login:
        raise CreateRepoError("Could not determine authenticated GitHub user.")
    return login


def git_root() -> Path | None:
    completed = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if completed.returncode != 0:
        return None
    return Path(completed.stdout.strip()).resolve()


def git_has_commits() -> bool:
    completed = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return completed.returncode == 0


def existing_origin() -> str | None:
    completed = subprocess.run(
        ["git", "remote", "get-url", "origin"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )
    if completed.returncode != 0:
        return None
    return completed.stdout.strip()


def ensure_git_ready(project_dir: Path, full_name: str, *, dry_run: bool) -> tuple[str, bool]:
    root = git_root()
    if root is None:
        run(["git", "init", "-b", "main"], dry_run=dry_run)
        return "main", False

    if root != project_dir:
        raise CreateRepoError(
            "Run this script from the git repository root. "
            f"Current directory is {project_dir}, but git root is {root}."
        )

    origin = existing_origin()
    if origin and not remote_matches_full_name(origin, full_name):
        raise CreateRepoError(
            f"Refusing to replace existing origin remote: {origin}. "
            "Ask the user before changing remotes."
        )
    if origin:
        print(f"Using existing origin remote: {origin}")

    has_commits = git_has_commits()
    branch = current_branch()
    if branch == "master" and not has_commits:
        run(["git", "branch", "-m", "main"], dry_run=dry_run)
        return "main", has_commits
    if not branch:
        raise CreateRepoError("Cannot push from a detached HEAD. Check out a branch first.")
    return branch, has_commits


def current_branch() -> str:
    return subprocess.run(
        ["git", "branch", "--show-current"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    ).stdout.strip()


def ensure_git_commit_identity() -> None:
    completed = subprocess.run(
        ["git", "var", "GIT_AUTHOR_IDENT"],
        check=False,
        text=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise CreateRepoError(
            "Git commit identity is not configured. Set git user.name and user.email, "
            "then rerun this script."
        )


def remote_matches_full_name(remote_url: str, full_name: str) -> bool:
    return normalize_remote(remote_url) == f"github.com/{full_name}".lower()


def normalize_remote(remote_url: str) -> str:
    normalized = remote_url.strip().lower()
    if normalized.startswith("git@github.com:"):
        normalized = "github.com/" + normalized.removeprefix("git@github.com:")
    for prefix in ("https://", "http://", "ssh://git@"):
        normalized = normalized.removeprefix(prefix)
    return normalized.removesuffix(".git")


def repo_exists(full_name: str) -> bool:
    completed = run(
        ["gh", "repo", "view", full_name, "--json", "nameWithOwner"],
        capture=True,
        check=False,
    )
    return completed.returncode == 0


def create_repository(
    full_name: str,
    visibility: str,
    *,
    dry_run: bool,
    resume_existing: bool,
) -> None:
    origin = existing_origin()
    exists = False if dry_run else repo_exists(full_name)

    if exists:
        if origin or resume_existing:
            print(f"Using existing GitHub repository: {full_name}")
        else:
            raise CreateRepoError(
                f"GitHub repository already exists: {full_name}. "
                "Rerun with --resume-existing only if it was created by a previous failed run."
            )
    else:
        run(["gh", "repo", "create", full_name, f"--{visibility}"], dry_run=dry_run)

    if not origin:
        run(
            ["git", "remote", "add", "origin", f"https://github.com/{full_name}.git"],
            dry_run=dry_run,
        )


def reset_labels(full_name: str, *, dry_run: bool) -> None:
    if dry_run:
        print("Would delete all existing issue labels.")
        existing_labels: list[dict[str, Any]] = []
    else:
        label_data = run_json(
            ["gh", "label", "list", "-R", full_name, "--limit", "1000", "--json", "name"],
            dry_run=False,
        )
        existing_labels = label_data if isinstance(label_data, list) else []

    for label in existing_labels:
        name = label.get("name")
        if name:
            run(["gh", "label", "delete", name, "-R", full_name, "--yes"], dry_run=dry_run)

    for name, color in LABELS:
        run(
            ["gh", "label", "create", name, "-R", full_name, "--color", color],
            dry_run=dry_run,
        )


def create_project(
    owner: str,
    repo_name: str,
    *,
    dry_run: bool,
    reuse_existing: bool,
) -> tuple[str, str]:
    existing_project = find_project(owner, repo_name) if reuse_existing and not dry_run else None
    if existing_project:
        project_id = str(existing_project["id"])
        validate_project_view_fields(project_id)
        number = str(existing_project["number"])
        url = str(existing_project["url"])
        print(f"Using existing GitHub Project: {url}")
    else:
        data = run_json(
            [
                "gh",
                "project",
                "copy",
                PROJECT_TEMPLATE_NUMBER,
                "--source-owner",
                PROJECT_TEMPLATE_OWNER,
                "--target-owner",
                owner,
                "--title",
                repo_name,
                "--format",
                "json",
            ],
            dry_run=dry_run,
        )
        project_id = str(data.get("id") or "")
        number = str(data.get("number") or "DRY_RUN_PROJECT_NUMBER")
        url = str(data.get("url") or "")

        if not url and not dry_run:
            view_data = run_json(
                ["gh", "project", "view", number, "--owner", owner, "--format", "json"],
                dry_run=False,
            )
            project_id = str(view_data.get("id") or project_id)
            url = str(view_data.get("url") or "")

        if not url:
            url = fallback_project_url(owner, number, dry_run=dry_run)

    run(
        ["gh", "project", "edit", number, "--owner", owner, "--visibility", "PRIVATE"],
        dry_run=dry_run,
    )

    if dry_run:
        print("Would verify copied project fields and visible default view fields.")
    else:
        if not project_id:
            raise CreateRepoError("Could not determine GitHub Project ID for view validation.")
        ensure_project_fields(owner, number, dry_run=False)
        validate_project_view_fields(project_id)

    run(
        ["gh", "project", "link", number, "--owner", owner, "--repo", repo_name],
        dry_run=dry_run,
    )
    return number, url


def find_project(owner: str, title: str) -> dict[str, Any] | None:
    data = run_json(
        [
            "gh",
            "project",
            "list",
            "--owner",
            owner,
            "--format",
            "json",
            "--limit",
            "100",
        ],
        dry_run=False,
    )
    projects = data.get("projects", []) if isinstance(data, dict) else []
    matches = [project for project in projects if project.get("title") == title]
    if len(matches) > 1:
        raise CreateRepoError(
            f"Found multiple GitHub Projects named {title!r}. "
            "Resolve the duplicate projects before rerunning."
        )
    return matches[0] if matches else None


def validate_project_view_fields(project_id: str) -> None:
    data = run_json(
        [
            "gh",
            "api",
            "graphql",
            "-f",
            "query="
            + (
                "query($id: ID!) { "
                "node(id: $id) { "
                "... on ProjectV2 { "
                "views(first: 1) { "
                "nodes { fields(first: 30) { nodes { "
                "... on ProjectV2Field { name } "
                "... on ProjectV2SingleSelectField { name } "
                "... on ProjectV2IterationField { name } "
                "} } } } } } }"
            ),
            "-F",
            f"id={project_id}",
        ],
        dry_run=False,
    )
    node = data.get("data", {}).get("node", {}) if isinstance(data, dict) else {}
    views = node.get("views", {}).get("nodes", [])
    if not views:
        raise CreateRepoError("GitHub Project has no default view to validate.")

    fields = views[0].get("fields", {}).get("nodes", [])
    actual = {field.get("name") for field in fields if field.get("name")}
    missing = sorted(REQUIRED_PROJECT_VIEW_FIELDS - actual)
    unexpected = sorted(actual - REQUIRED_PROJECT_VIEW_FIELDS)
    if missing or unexpected:
        message = "GitHub Project default view does not match expected fields."
        if missing:
            message += f" Missing: {missing}."
        if unexpected:
            message += f" Unexpected: {unexpected}."
        raise CreateRepoError(message)


def ensure_project_fields(owner: str, number: str, *, dry_run: bool) -> None:
    fields = existing_project_fields(owner, number, dry_run=dry_run)
    for field_name, options in PROJECT_FIELDS:
        existing = fields.get(field_name)
        if existing:
            validate_single_select_field(existing, options)
            print(f"Using existing project field: {field_name}")
            continue

        run(
            [
                "gh",
                "project",
                "field-create",
                number,
                "--owner",
                owner,
                "--name",
                field_name,
                "--data-type",
                "SINGLE_SELECT",
                "--single-select-options",
                ",".join(options),
            ],
            dry_run=dry_run,
        )


def existing_project_fields(owner: str, number: str, *, dry_run: bool) -> dict[str, dict[str, Any]]:
    if dry_run:
        return {}
    data = run_json(
        ["gh", "project", "field-list", number, "--owner", owner, "--format", "json"],
        dry_run=False,
    )
    fields = data.get("fields", []) if isinstance(data, dict) else []
    return {field["name"]: field for field in fields if "name" in field}


def validate_single_select_field(field: dict[str, Any], expected_options: list[str]) -> None:
    field_type = field.get("type")
    if field_type != "ProjectV2SingleSelectField":
        raise CreateRepoError(
            f"Project field {field.get('name')!r} exists but is {field_type}, "
            "not a single-select field."
        )
    actual_options = [option.get("name") for option in field.get("options", [])]
    if actual_options != expected_options:
        raise CreateRepoError(
            f"Project field {field.get('name')!r} has options {actual_options}; "
            f"expected {expected_options}."
        )


def fallback_project_url(owner: str, number: str, *, dry_run: bool) -> str:
    if dry_run:
        return f"https://github.com/users/{owner}/projects/{number}"

    completed = run(
        ["gh", "api", f"users/{owner}", "--jq", ".type"],
        capture=True,
        check=False,
    )
    if completed.stdout.strip() == "Organization":
        return f"https://github.com/orgs/{owner}/projects/{number}"
    return f"https://github.com/users/{owner}/projects/{number}"


def update_agents_md(project_dir: Path, repo_name: str, project_url: str, *, dry_run: bool) -> bool:
    path = project_dir / "AGENTS.md"
    section = (
        "## GitHub Project\n\n"
        f"The GitHub Project associated with this project is [{repo_name}]({project_url})\n"
    )

    if path.exists():
        original = path.read_text()
        updated = replace_or_append_project_section(original, section)
    else:
        original = ""
        updated = f"# AI Agent Guidelines\n\n{section}"

    if updated == original:
        print("AGENTS.md already contains the expected GitHub Project section.")
        return False

    if dry_run:
        print(f"Would update {path}:")
        print(updated)
        return True

    path.write_text(updated)
    print(f"Updated {path}")
    return True


def commit_and_push(branch: str, has_commits: bool, agents_changed: bool, *, dry_run: bool) -> None:
    if not has_commits:
        run(["git", "add", "-A"], dry_run=dry_run)
        if not dry_run and not has_staged_changes():
            raise CreateRepoError("No files are staged for the initial commit.")
        run(["git", "commit", "-m", "Initial commit"], dry_run=dry_run)
        run(["git", "push", "-u", "origin", branch], dry_run=dry_run)
        return

    if agents_changed:
        run(["git", "add", "AGENTS.md"], dry_run=dry_run)
        if dry_run or has_staged_changes():
            run(["git", "commit", "-m", "Add GitHub project link"], dry_run=dry_run)

    run(["git", "push", "-u", "origin", branch], dry_run=dry_run)


def ensure_clean_worktree_for_existing_history() -> None:
    completed = subprocess.run(
        ["git", "status", "--porcelain"],
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise CreateRepoError(completed.stderr.strip() or "Could not inspect git status.")
    if completed.stdout.strip():
        raise CreateRepoError(
            "Existing-history repositories must have a clean worktree before this script "
            "can commit the AGENTS.md project link. Commit, stash, or remove local changes, "
            "then rerun."
        )


def has_staged_changes() -> bool:
    completed = subprocess.run(
        ["git", "diff", "--cached", "--quiet"],
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return completed.returncode == 1


def replace_or_append_project_section(original: str, section: str) -> str:
    lines = original.splitlines(keepends=True)
    heading_index = None
    for index, line in enumerate(lines):
        if line.strip().lower() == "## github project":
            heading_index = index
            break

    if heading_index is None:
        if not original or original.endswith("\n\n"):
            separator = ""
        elif original.endswith("\n"):
            separator = "\n"
        else:
            separator = "\n\n"
        return f"{original}{separator}{section}"

    end_index = len(lines)
    for index in range(heading_index + 1, len(lines)):
        stripped = lines[index].strip()
        if stripped.startswith("## ") and not stripped.startswith("### "):
            end_index = index
            break

    replacement = section
    if end_index < len(lines) and not replacement.endswith("\n\n"):
        replacement += "\n"
    return "".join(lines[:heading_index]) + replacement + "".join(lines[end_index:])


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create a GitHub repo, labels, project, and AGENTS.md project link."
    )
    visibility = parser.add_mutually_exclusive_group()
    visibility.add_argument("--public", action="store_true", help="Create a public repository.")
    visibility.add_argument("--private", action="store_true", help="Create a private repository.")
    parser.add_argument(
        "--owner",
        help="GitHub user or organization to own the repository and project. Defaults to the authenticated user.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned commands and file changes without mutating GitHub or local files.",
    )
    parser.add_argument(
        "--resume-existing",
        action="store_true",
        help="Continue when the target GitHub repository already exists but origin is not configured.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.public and not args.private:
        raise CreateRepoError("Specify --public or --private. Ask the user if visibility is unclear.")

    project_dir = Path.cwd().resolve()
    repo_name = project_dir.name
    visibility = "public" if args.public else "private"

    require_command("git")
    require_command("gh")
    ensure_gh_auth()

    owner = args.owner or current_github_login()
    full_name = f"{owner}/{repo_name}"

    print(f"Project directory: {project_dir}")
    print(f"GitHub repository: {full_name}")
    print(f"Visibility: {visibility}")

    branch, has_commits = ensure_git_ready(project_dir, full_name, dry_run=args.dry_run)
    reuse_existing_project = bool(existing_origin()) or args.resume_existing
    if not args.dry_run:
        ensure_git_commit_identity()
    if has_commits:
        ensure_clean_worktree_for_existing_history()
    create_repository(
        full_name,
        visibility,
        dry_run=args.dry_run,
        resume_existing=args.resume_existing,
    )
    reset_labels(full_name, dry_run=args.dry_run)
    _project_number, project_url = create_project(
        owner,
        repo_name,
        dry_run=args.dry_run,
        reuse_existing=reuse_existing_project,
    )
    agents_changed = update_agents_md(project_dir, repo_name, project_url, dry_run=args.dry_run)
    commit_and_push(branch, has_commits, agents_changed, dry_run=args.dry_run)

    print("Repository setup complete.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except subprocess.CalledProcessError as exc:
        message = f"Command failed with exit code {exc.returncode}: {' '.join(exc.cmd)}"
        if exc.stderr:
            message += f"\n{exc.stderr.strip()}"
        print(message, file=sys.stderr)
        raise SystemExit(exc.returncode)
    except CreateRepoError as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1)
