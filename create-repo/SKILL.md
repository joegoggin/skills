---
name: create-repo
description: Create and bootstrap a GitHub repository from the current project directory. Use when Codex is asked to create a new GitHub repo for the current folder, add it as git origin, replace repo labels, create and link a GitHub Project, configure Status/Priority project fields, write the linked GitHub Project to AGENTS.md for the issues skill, create an initial commit, or push the new repo.
---

# Create Repo

## Overview

Create a GitHub repository named after the current directory and configure the repo so it is ready for issue planning with the `issues` skill.

Use the bundled script for the full workflow. It is designed to fail before replacing an existing `origin` remote.

## Workflow

1. Confirm repository visibility before creating anything.
   - If the user specifies public or private, pass `--public` or `--private`.
   - If the user does not specify visibility, ask whether the repo should be public or private.
2. Run the bundled script from the project root, resolving the script path from
   this skill directory:

```bash
python3 <create-repo-skill-dir>/scripts/create_repo.py --private
```

Use `--public` instead when requested. Use `--owner OWNER` only when the user explicitly asks to create the repo under a specific user or organization.

If a previous run partially completed, rerun only after confirming the existing GitHub repository and any same-named GitHub Project are the intended targets. Use `--resume-existing` when the GitHub repository exists but `origin` is not configured yet.

## What the Script Does

- Derive the repository name from the current directory basename.
- Verify `gh` is installed and authenticated with GitHub.
- Initialize git with `main` when the directory is not already a git repo.
- Stop if the current git repo already has an `origin` remote.
  - Continue when `origin` already points at the intended GitHub repository, so failed runs can be resumed.
- Create the GitHub repository and add it as `origin`.
- Delete all existing issue labels, then create:
  - `Feature` `#0e8a16`
  - `Bug` `#d85c56`
  - `DevOps` `#5319e7`
  - `Documentation` `#1d76db`
  - `Refactor` `#fbca04`
  - `Testing` `#d93f0b`
  - `Update` `#006b75`
- Create a GitHub Project with the same name as the repo by copying the configured template project `joegoggin/32`.
  - During resume paths, reuse one same-named existing GitHub Project instead of creating a duplicate.
- Set the GitHub Project visibility to private, even when the repository is public.
- Verify the default project view has these visible fields:
  - `Title`
  - `Labels`
  - `Status`
  - `Priority`
  - `Parent issue`
  - `Sub-issues progress`
  - `Linked pull requests`
  - `Repository`
- Ensure project fields:
  - `Status`: `Todo`, `In Progress`, `Done`
  - `Priority`: `Low`, `Medium`, `High`, `Urgent`
  - Reuse existing matching project fields, including GitHub's default `Status` field, and create only missing fields.
- Link the project to the repository.
- Create or update `AGENTS.md` with the linked GitHub Project URL so the `issues` skill can locate it.
- Create and push commits:
  - If the repo has no commits, stage all files, commit `Initial commit`, and push the active branch to `origin`.
  - If the repo already has commits, require a clean worktree, commit the generated `AGENTS.md` project-link change when needed, then push the active branch to `origin`.

Project view field order and additional visible fields are intentionally
ignored. Validation should only fail when required fields are missing.

## Validation and Safety

Use dry-run mode before live creation when the target directory or owner is uncertain:

```bash
python3 <create-repo-skill-dir>/scripts/create_repo.py --dry-run --private
```

If the script fails, report the failed step and do not retry destructive steps manually. Never replace an existing `origin` remote unless the user explicitly asks for that separate operation.
