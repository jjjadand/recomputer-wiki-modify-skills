# Audit checklist

## Family navigation

- Every primary family page imports `JetsonProductDocNav` and the same family navigation object.
- Labels are ordered `Quick Start`, `Hardware & I/O`, `Application`.
- Application detail routes are present in `activePaths`.
- Sidebar IDs point to existing files.

## Getting Started

- Uses `jetson-product-page` and the shared green UI classes.
- Has product hero, facts, verified variants, differentiators, specifications, hardware overview, end-to-end flashing, application collection, resources, and support.
- Product image is contained and appropriately sized.
- Numbered flash steps keep their related commands and warnings together.
- Application cover and title point to the same route.
- Resource cards use the shared icon/copy/raised-arrow layout.

## Content ownership

- Getting Started provides the overview and complete first-run path.
- Hardware & I/O owns pinouts, mappings, interface commands, and electrical cautions.
- Applications own deployment, performance conditions, limitations, and troubleshooting.
- No long flash/spec/resource blocks are inconsistently duplicated.

## Data and routes

- Model names, modules, memory, TOPS, storage, I/O, power, environmental ratings, SKU, USB ID, BSP URL, and SHA-256 agree with maintained sources.
- Canonical slugs use the family namespace and all prior public routes remain aliases.
- `url` matches `slug`; internal links, sidebar, nav `activePaths`, and discovery data agree.
- `createdAt` is preserved while `updatedAt` and `last_update` reflect material edits.

## UI and accessibility

- Uses `className`, not HTML `class`, in JSX/MDX.
- External `_blank` links use `rel="noopener noreferrer"`.
- Images have descriptive alt text rather than `Image`, `photo`, or an empty value unless intentionally decorative.
- Cards and buttons have adequate spacing in desktop and mobile layouts.
- Light and dark themes retain readable contrast.
- No dead application cards or placeholder tokens remain.

## Validation

- Audit script has no errors; release-ready work has no unexplained warnings.
- English production build exits successfully.
- If a full build is blocked elsewhere, the exact unrelated file/error is reported and target compilation is demonstrated separately where possible.
