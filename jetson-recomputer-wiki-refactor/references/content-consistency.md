# Content consistency

## Canonical field matrix

Build a small source matrix before editing. Resolve disagreements instead of silently choosing one value.

| Field | Preferred repository source |
| --- | --- |
| SKU and store URL | Existing product page/frontmatter or user-provided release data |
| Jetson module, memory, TOPS | Product specification table and `JetsonProductSelector.jsx` |
| I/O counts and connector types | Datasheet, schematic, maintained Hardware & I/O page |
| Power and environmental limits | Datasheet; retain operating conditions such as required airflow |
| JetPack/BSP versions | Current flashing resource page and user-provided release data |
| Archive URL and SHA-256 | User-provided release manifest or existing maintained flash page |
| Recovery USB ID | Existing verified guide for the same module/carrier configuration |
| Canonical route | Frontmatter `slug`, sidebar, internal links, and aliases |
| Application benchmark | Application page with hardware, power mode, software version, and test conditions |

If sources conflict, state the conflict and prefer the most specific, current primary source. Do not “average” or merge incompatible specifications.

## Frontmatter

Maintain at least:

- `description`
- `title`
- `keywords` or existing `tags` convention
- `image`
- `slug`
- `aliases` for published prior routes
- `sku` when the page maps to products
- `last_update.date` and `last_update.author`
- `createdAt` without rewriting the original creation date
- `updatedAt`
- `url`

Update dates only for pages materially changed in the task. Keep YAML valid and include a comma-separated `sku` value only when that matches the repository convention.

## Terminology

- Use `JetPack` for the SDK/platform and `BSP image` or `mass-flash package` for downloadable flashing artifacts.
- Use exact product casing: `reComputer`, NVIDIA `Jetson`, `Orin Nano`, `Orin NX`, `AGX Orin`.
- Distinguish a carrier board from a complete reComputer system.
- Distinguish included hardware from optional expansion modules.
- State conditions for claims: airflow, power mode, MAXN/SUPER mode, model precision, camera count, and software version.

## Links and routes

- Canonical internal links use the final slug with a trailing slash.
- Old public routes belong in `aliases`; do not keep old slugs as the canonical route merely to avoid updating links.
- Update sidebar IDs only when files move; slug-only changes generally do not change document IDs.
- Search the repository for every old route before replacing it.
- Application cards, navigation `activePaths`, sidebar entries, related-page links, and `src/utils/wiki.js` must agree where applicable.

## Scope safeguards

- Do not update all locales when only English is requested.
- Do not replace a valid product-specific procedure with a generic Rugged command.
- Do not remove detailed troubleshooting merely to shorten a page; move it to the responsible page if necessary.
- Do not publish a download without the matching product/module label and checksum when a checksum is available.
