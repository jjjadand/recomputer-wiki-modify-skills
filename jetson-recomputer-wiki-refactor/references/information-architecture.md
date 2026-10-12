# Information architecture

## Family-level structure

Treat a reComputer product family as a small documentation set rather than unrelated pages:

| Page | Owns | Links onward to |
| --- | --- | --- |
| Getting Started | Product positioning, variants, common specifications, hardware overview, end-to-end flashing, application and resource indexes | Hardware details and applications |
| Hardware & I/O | Connector maps, pinouts, device-tree or Linux mappings, interface enablement, commands, validation, electrical cautions | Getting Started, relevant accessory guides |
| Application detail | A complete deployable workflow, measured results, limitations, safety, troubleshooting | Getting Started application collection |
| Accessory/maintenance | One bounded installation or service operation | Relevant family page |

Do not duplicate a full specification table, flash guide, or resource list in every page. Put shared facts in Getting Started and link to them.

## Getting Started section order

Use this order unless product needs make a section irrelevant:

1. Frontmatter and shared family navigation
2. Hero with positioning, product image, purchase action, and start action
3. Four concise facts
4. Product/module variants
5. `Why <product family>` feature grid
6. Specifications
7. Hardware Overview and status indicators
8. Flash JetPack
9. Applications
10. Resources
11. Tech Support & Product Discussion

For a single fixed configuration, replace the variant grid with a short configuration card rather than inventing choices.

## Flash JetPack workflow

Use numbered steps and keep each step's explanation, warning, image, and command together:

1. Choose the exact BSP for product, carrier board, Jetson module, storage target, and JetPack version.
2. Prepare a supported physical Ubuntu host, data cable, power, display, and input devices.
3. Enter Force Recovery Mode and verify the expected `lsusb` ID for each supported module.
4. Extract and run the actual flash command shipped with the package.
5. Add post-flash verification only when the product requires it.

Do not guess archive names, board configs, host versions, SHA-256 values, or commands. If required source data is missing, retain the correct existing instruction and report the missing fact.

## Application collection

The Getting Started page is the application landing page. Each available application uses a cover, capability labels, linked title, and one-sentence outcome. The cover and title link to the same canonical route. Add detail pages to navigation `activePaths` so the `Application` tab remains active.

Do not add dead cards for planned applications. A short “more examples are coming” sentence is acceptable, but the grid contains only usable links.

## Resource collection

Use shared resource cards for applicable artifacts:

- Product datasheet
- Carrier-board schematic
- Additional board schematic, when applicable
- 3D mechanical file
- Linux_for_Tegra/BSP source
- Jetson device comparison
- Certification, mechanical drawing, or accessory guide when useful

Each card needs a short type token, precise title, useful description, canonical link, and clear external-link behavior.
