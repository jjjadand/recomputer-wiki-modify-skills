---
name: jetson-recomputer-wiki-audit
description: Perform a read-only consistency audit of English Seeed Jetson reComputer product-family docs against the shared navigation, green UI, page architecture, route, metadata, accessibility, and content rules. Use when reviewing or validating a reComputer refactor; use the refactor skill instead when implementation is requested.
---

# Jetson reComputer Wiki Audit

Audit by default; do not edit files unless the user explicitly asks for fixes.

## Audit workflow

1. Identify the family directory and related navigation/sidebar/data files.
2. Read [references/audit-checklist.md](references/audit-checklist.md).
3. Run the deterministic audit from the `wiki-documents` root:

```bash
python ~/.codex/skills/jetson-recomputer-wiki-audit/scripts/audit_recomputer_wiki.py \
  sites/en/docs/Edge/NVIDIA_Jetson/reComputer_Jetson_Series/<family-directory>
```

Use `--strict` when the target is expected to be release-ready. Use `--json` only when machine-readable findings help another tool.

4. Inspect the shared navigation object, active application routes, sidebar registration, and repository references to old slugs.
5. If a local preview is already available, check desktop/mobile and light/dark rendering. Otherwise use the English production build as the rendering gate.
6. Report findings by severity with clickable file paths and line numbers. Separate target regressions from unrelated pre-existing build failures.

## Interpretation

- An audit warning about a missing page means the target could not be verified, not that the page must exist.
- Missing GA4, store, download, or product data is not permission to invent it.
- A page can compile while remaining inconsistent; check routes, content ownership, navigation, accessibility, and factual agreement in addition to syntax.
- The Rugged Getting Started page is the primary visual baseline. Its older Hardware & I/O markup is not a reason to permit legacy `class=`, generic image alt text, or plain resource lists in new refactors.

If fixes are requested, use `$jetson-recomputer-wiki-refactor` and rerun this audit after implementation.
