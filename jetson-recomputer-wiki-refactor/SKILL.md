---
name: jetson-recomputer-wiki-refactor
description: Refactor English Seeed Jetson reComputer product-family documentation to the shared Rugged-derived information architecture, green UI system, navigation, routes, and content conventions. Use for reComputer Getting Started, hardware/I/O, application, accessory, or resource pages in wiki-documents; do not use for unrelated Jetson application tutorials.
---

# Jetson reComputer Wiki Refactor

Use the reComputer Rugged J40 Getting Started page as the visual and structural baseline, while replacing every product-specific fact with verified data for the target family.

## Before editing

1. Work from the `wiki-documents` repository root. Inspect `git status` and preserve unrelated changes.
2. Inventory the target family: Getting Started, hardware/I/O, application, accessory/maintenance pages, sidebar entries, current slugs, aliases, SKUs, BSP links, checksums, and product links.
3. Read [references/repository-baseline.md](references/repository-baseline.md) for the maintained components and Rugged reference files.
4. Read [references/information-architecture.md](references/information-architecture.md) before restructuring pages.
5. Read [references/component-catalog.md](references/component-catalog.md) when composing or extending UI blocks.
6. Read [references/content-consistency.md](references/content-consistency.md) when reconciling specifications, flashing instructions, routes, or metadata.

## Refactor rules

- Apply the shared `JetsonProductDocNav` to the family pages and keep navigation data centralized in `productDocNavigation.js`.
- Use the existing `jetson-product-*` classes and green Seeed theme. Extend the shared stylesheet only for a genuinely reusable pattern; do not add a family-specific copy of the same CSS.
- Give the Getting Started page a product overview, variants, value proposition, specifications, hardware overview, complete flashing workflow, application collection, resources, and support.
- Keep detailed pinouts and interface commands in the Hardware & I/O page. Keep workload deployment and benchmarks in application pages. Avoid duplicating long procedures across pages.
- Preserve valid legacy URLs with `aliases`. Use the `/jetson/recomputer_<family>/...` route namespace for new canonical routes unless the established family namespace already differs.
- Treat product facts as data, not prose decoration. Verify model names, module memory, TOPS, storage, power, I/O counts, environmental ratings, SKUs, download URLs, SHA-256 values, and recovery USB IDs from repository sources or user-provided data.
- Never transfer Rugged-only claims such as IP66, M12, fanless operation, PoE count, temperature range, or vibration resistance to another family without evidence.
- Use English only unless the user requests additional locales. Do not edit translated sites merely to mirror the English change.
- Keep flashing self-contained when the user requires it. A selector link may help choose the exact image, but it must not replace recovery-mode and flash commands.
- Use accessible image alt text, `className` in JSX, responsive image sizing, and `rel="noopener noreferrer"` on external links opened in a new tab.

The reusable starters are [assets/getting-started-template.mdx](assets/getting-started-template.mdx) and [assets/product-navigation-template.js](assets/product-navigation-template.js). Adapt them selectively; remove sections that genuinely do not apply instead of leaving empty cards or placeholders.

## Navigation and applications

- The primary navigation normally contains `Quick Start`, `Hardware & I/O`, and `Application`.
- `Application` links to the `#applications` collection on Getting Started and uses `activePaths` for every application detail page.
- Application covers and titles must both link to the same canonical route.
- Use specific capability labels such as `Detection`, `GMSL`, `Generative AI`, or `Inference Benchmark`. Do not create non-functional placeholder cards; mention future content in prose if needed.

## Validation

After editing:

1. Invoke `$jetson-recomputer-wiki-audit` on the target family, or run its audit script directly if the skill is installed.
2. Check slugs, URLs, aliases, sidebar entries, navigation active states, image dimensions, light/dark themes, mobile layout, and anchor scrolling.
3. Run the narrowest meaningful build first, then the English production build:

```bash
yarn --cwd sites/en build --out-dir ../../build
```

If the build fails in an unrelated pre-existing page, prove the target pages compile separately where possible and report the unrelated blocker precisely. Do not claim a full successful build unless the command exits successfully.

Do not commit, pull, or push unless requested. When publication is requested, inspect the worktree first; synchronize without overwriting user changes, validate again after synchronization, then commit only scoped files.
