# Shared component catalog

The CSS contract lives in `sites/en/src/css/jetson-product-wiki-style.css`. Reuse these classes before adding new ones.

| Pattern | Classes |
| --- | --- |
| Page scope | `jetson-product-page` |
| Family tabs | `jetson-product-doc-nav`, rendered by `JetsonProductDocNav` |
| Hero | `jetson-product-hero`, `jetson-product-eyebrow`, `jetson-product-hero-media` |
| Actions | `jetson-product-actions`, `jetson-product-button`, `jetson-product-button--secondary` |
| Fact cards | `jetson-product-fact-grid`, `jetson-product-fact` |
| Feature cards | `jetson-product-feature-grid`, `jetson-product-feature` |
| Variant cards | `jetson-product-variant-grid`, `jetson-product-variant-card`, `jetson-product-variant-badge`, `jetson-product-variant-metrics` |
| Tables | `jetson-product-table-wrap` |
| Hardware gallery | `jetson-product-hardware-gallery` |
| Flash workflow | `jetson-product-step-flow`, `jetson-product-step-item`, `jetson-product-step-number`, `jetson-product-step-content`, `jetson-product-step-label`, `jetson-product-step-image` |
| Applications | `jetson-product-application-grid`, `jetson-product-application-card`, `jetson-product-application-cover`, `jetson-product-application-body`, `jetson-product-application-labels` |
| Resources | `jetson-product-resource-grid`, `jetson-product-resource-card`, `jetson-product-resource-icon`, `jetson-product-resource-copy`, `jetson-product-resource-arrow` |

## Design invariants

- Use Seeed green tokens already defined in the stylesheet. Do not introduce a competing blue/cyan theme for another reComputer family.
- Preserve light/dark theme behavior and existing responsive breakpoints.
- Buttons require comfortable vertical spacing; use the actions wrapper instead of placing consecutive anchors inline.
- Resource cards use the raised gradient arrow treatment. Do not substitute a plain text arrow floating at the card edge.
- Product and recovery images use `object-fit: contain`; application covers use 16:9 `object-fit: cover`.
- Do not set fixed image height in prose. Use the shared class or a bounded width with automatic height.
- Extend CSS with a generic `jetson-product-*` class only when at least two product families can use it.

## Navigation object

Use a family-specific exported object with generic labels:

```js
const PRODUCT_GETTING_STARTED = '/jetson/recomputer_product/getting_started/';

export const productDocNav = {
  ariaLabel: 'reComputer Product documentation',
  items: [
    {to: PRODUCT_GETTING_STARTED, label: 'Quick Start', hint: 'Overview & flash'},
    {
      to: '/jetson/recomputer_product/hardware_and_interface_usage/',
      label: 'Hardware & I/O',
      hint: 'Interfaces & expansion',
    },
  ],
  application: {
    to: `${PRODUCT_GETTING_STARTED}#applications`,
    label: 'Application',
    hint: 'Use cases & benchmarks',
    activePaths: ['/jetson/recomputer_product/example_application/'],
  },
};
```

Hints may be product-specific, but labels and ordering stay consistent across reComputer families.
