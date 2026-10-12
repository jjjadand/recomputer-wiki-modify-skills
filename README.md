# reComputer Wiki Modification Skills

Reusable Codex skills for standardizing Seeed Studio reComputer Jetson wiki pages against the reComputer Rugged documentation pattern.

## Included skills

- `jetson-recomputer-wiki-refactor`: Refactors English reComputer product documentation with a consistent information architecture, reusable UI components, Seeed-green styling, flashing workflow, application cards, resources, and content rules.
- `jetson-recomputer-wiki-audit`: Audits a page or product family for required structure, UI consistency, MDX risks, links, legacy markup, and build readiness.

Each skill directory includes its complete `SKILL.md`, agent metadata, references, templates, and scripts.

## Install

Clone the repository and copy both skill directories into your Codex skills directory:

```bash
git clone git@github.com:jjjadand/recomputer-wiki-modify-skills.git
cd recomputer-wiki-modify-skills
cp -a jetson-recomputer-wiki-refactor ~/.codex/skills/
cp -a jetson-recomputer-wiki-audit ~/.codex/skills/
```

Restart the Codex session after installation so the skills are rediscovered.

## Use

Invoke the refactoring skill when updating a reComputer Jetson product family:

```text
$jetson-recomputer-wiki-refactor refactor the reComputer product documentation in <path>
```

Run the audit skill independently when reviewing existing pages:

```text
$jetson-recomputer-wiki-audit audit the reComputer product documentation in <path>
```

The audit script can also be run directly:

```bash
python3 jetson-recomputer-wiki-audit/scripts/audit_recomputer_wiki.py <file-or-directory>
```

Use `--strict` to make warnings produce a non-zero exit status.

## Repository layout

```text
.
├── jetson-recomputer-wiki-refactor/
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/
│   └── references/
└── jetson-recomputer-wiki-audit/
    ├── SKILL.md
    ├── agents/
    ├── references/
    └── scripts/
```
