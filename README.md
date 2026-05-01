# Codex Skills

This repository stores personal Codex skills so they can stay consistent across
devices. Clone or sync this repo into the local skills directory, then manage
changes with normal git commands.

A root-level README does not affect skill behavior. Codex discovers and uses
skills from each skill folder's `SKILL.md` frontmatter, then loads the skill
body and any linked files such as `references/`, `scripts/`, `assets/`, and
`agents/openai.yaml` as needed.

## Repository Layout

```text
.
|-- code-review/
|   |-- SKILL.md
|   `-- agents/openai.yaml
|-- docs/
|   |-- SKILL.md
|   |-- agents/openai.yaml
|   `-- references/rust.md
|-- issues/
|   |-- SKILL.md
|   |-- agents/openai.yaml
|   `-- references/
`-- merge-conflict/
    |-- SKILL.md
    `-- agents/openai.yaml
```

Common skill files:

- `SKILL.md`: Required skill instructions and trigger metadata.
- `references/`: Optional documentation loaded only when needed.
- `agents/openai.yaml`: Optional UI metadata for skill lists and prompts.
- `scripts/` and `assets/`: Optional executable helpers and reusable output
  resources when a skill needs them.

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

## Syncing

Pull updates on an existing device:

```bash
cd ~/.agents/skills
git pull
```

Commit local skill changes:

```bash
git status --short
git add -A
git commit -m "Update skills"
```

Push changes for other devices:

```bash
git push
```

Keep repo-level documentation at the repository root. Avoid adding `README.md`
files inside individual skill folders unless there is a specific reason; skill
folders should stay focused on the files Codex needs to use the skill.

## Skill Catalog

| Skill | Purpose | Notable resources |
| --- | --- | --- |
| `$code-review` | Reviews branch, PR, diff, or local changes one issue at a time. | `code-review/agents/openai.yaml` |
| `$docs` | Applies repository documentation conventions. | `docs/references/rust.md`, `docs/agents/openai.yaml` |
| `$issues` | Creates, plans, updates, and implements GitHub issue workflows. | `issues/references/`, `issues/agents/openai.yaml` |
| `$merge-conflict` | Resolves Git merge conflicts interactively one conflict at a time. | `merge-conflict/agents/openai.yaml` |
