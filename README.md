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
| `$docs` | Applies repository documentation conventions. | `docs/references/rust.md`, `docs/agents/openai.yaml` |
| `$issues` | Creates, plans, updates, and implements GitHub issue workflows. | `issues/references/`, `issues/agents/openai.yaml` |
| `$merge-conflict` | Resolves Git merge conflicts interactively one conflict at a time. | `merge-conflict/agents/openai.yaml` |
| `$plan-project` | Plans new projects as phased GitHub issues without implementing the project. | `plan-project/agents/openai.yaml` |
