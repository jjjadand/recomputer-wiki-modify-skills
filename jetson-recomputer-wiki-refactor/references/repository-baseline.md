# Repository baseline

All paths are relative to the `wiki-documents` repository root.

## Source-of-truth UI files

- Navigation component: `sites/en/src/components/jetson/JetsonProductDocNav.jsx`
- Navigation data: `sites/en/src/data/jetson/productDocNavigation.js`
- Shared UI stylesheet: `sites/en/src/css/jetson-product-wiki-style.css`
- Jetson sidebar: `sites/en/jetson-sidebar.js`

Do not clone these into a product directory. Add a product-family navigation object to the shared data file and import it from every page in that family.

## Rugged reference files

- Primary visual/template reference: `sites/en/docs/Edge/NVIDIA_Jetson/reComputer_Jetson_Series/reComputer_Rugged_J40/reComputer_Rugged_J40_Getting_Started.md`
- Detailed interface content reference: `sites/en/docs/Edge/NVIDIA_Jetson/reComputer_Jetson_Series/reComputer_Rugged_J40/reComputer_Rugged_J401_hardware_and_interface_usage.md`
- Application/benchmark reference: `sites/en/docs/Edge/NVIDIA_Jetson/reComputer_Jetson_Series/reComputer_Rugged_J40/reComputer_Rugged_J401_for_Industrial_Vision.md`

The Getting Started page is the UI baseline. The older long-form Hardware & I/O page remains useful for content depth, but do not copy its legacy `class=`, generic `alt="Image"`, repeated centered `<div>` blocks, or plain resource lists. Normalize new work to the shared components and JSX conventions.

## Standard imports

```mdx
import JetsonProductDocNav from '@site/src/components/jetson/JetsonProductDocNav';
import {productFamilyDocNav} from '@site/src/data/jetson/productDocNavigation';

# Page title

<JetsonProductDocNav {...productFamilyDocNav} />
```

Wrap the styled Getting Started content in:

```mdx
<div className="jetson-product-page">

...

</div>
```

The navigation remains outside the wrapper because it imports the same theme variables itself.

## Route conventions

Prefer a stable family namespace:

```text
/jetson/recomputer_<family>/getting_started/
/jetson/recomputer_<family>/hardware_and_interface_usage/
/jetson/recomputer_<family>/<application>/
```

Preserve every published former slug in frontmatter `aliases`. The frontmatter `url` must equal `https://wiki.seeedstudio.com` plus the canonical slug and trailing slash.
