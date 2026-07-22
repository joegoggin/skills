# Codex Skills

This repository stores personal Codex skills so they can stay consistent across
devices. Clone or sync this repo into the local skills directory, then manage
changes with normal git commands.

A root-level README does not affect skill behavior. Codex discovers and uses
skills from each skill folder's `SKILL.md` frontmatter, then loads the skill
body and any linked files such as `references/`, `scripts/`, `assets/`, and
`agents/openai.yaml` as needed.


## Setup

The expected local path is:

```bash
~/.agents/skills
```

On a new device, clone the repo into that path:

```bash
mkdir -p ~/.agents
git clone https://github.com/joegoggin/skills.git ~/.agents/skills
```

Confirm the skills are present:

```bash
find ~/.agents/skills -maxdepth 2 -name SKILL.md
```


## Skill Catalog

| Skill | Purpose | Notable resources |
| --- | --- | --- |
| `$code-review` | Reviews branch, PR, diff, or local changes one issue at a time. | `code-review/agents/openai.yaml` |
| `$create-repo` | Creates and bootstraps GitHub repos with labels, a linked private project, `AGENTS.md`, and an initial push. | `create-repo/scripts/create_repo.py`, `create-repo/agents/openai.yaml` |
| `$debug` | Diagnoses bugs from symptoms, diagnostics, logs, or both, then proposes a diff before applying fixes. | `debug/agents/openai.yaml` |
| `$docs` | Applies repository documentation conventions. | `docs/references/rust.md`, `docs/references/lua.md`, `docs/agents/openai.yaml` |
| `$issues` | Routes GitHub issue requests to the focused issue workflow skills below. | `issues/agents/openai.yaml` |
| `$issues-create` | Creates project-linked GitHub issues and ordered sub-issues. | `issues-create/references/create.md`, `issues-create/agents/openai.yaml` |
| `$issues-implement` | Implements all remaining steps for a GitHub issue and records the completed work. | `issues-implement/references/implement.md`, `issues-implement/agents/openai.yaml` |
| `$issues-instructions` | Writes local implementation instructions for GitHub issues without implementing them. | `issues-instructions/references/instructions.md`, `issues-instructions/agents/openai.yaml` |
| `$issues-step` | Implements exactly one numbered step from a local issue instruction file. | `issues-step/references/step.md`, `issues-step/agents/openai.yaml` |
| `$issues-update` | Updates and normalizes existing GitHub issue bodies. | `issues-update/references/update.md`, `issues-update/agents/openai.yaml` |
| `$merge-conflict` | Resolves Git merge conflicts interactively one conflict at a time. | `merge-conflict/agents/openai.yaml` |
| `$plan-project` | Plans new or continuing projects as sequential GitHub phase issues, continuing after existing phase numbers without implementing them. | `plan-project/agents/openai.yaml` |
| `$refactor-review` | Suggests behavior-preserving refactors one at a time with affected files, code examples, and file tree changes when needed. | `refactor-review/agents/openai.yaml` |
| `$skill-review` | Reviews skill changes for trigger quality, structure, resources, validation, and metadata one issue at a time. | `skill-review/agents/openai.yaml` |
