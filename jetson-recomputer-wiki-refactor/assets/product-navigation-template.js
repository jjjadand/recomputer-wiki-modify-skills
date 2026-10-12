const PRODUCT_GETTING_STARTED = '/jetson/{{ROUTE_FAMILY}}/getting_started/';

export const productFamilyDocNav = {
  ariaLabel: '{{PRODUCT_FAMILY}} documentation',
  items: [
    {
      to: PRODUCT_GETTING_STARTED,
      label: 'Quick Start',
      hint: 'Overview & flash',
    },
    {
      to: '/jetson/{{ROUTE_FAMILY}}/hardware_and_interface_usage/',
      label: 'Hardware & I/O',
      hint: 'Interfaces & expansion',
    },
  ],
  application: {
    to: `${PRODUCT_GETTING_STARTED}#applications`,
    label: 'Application',
    hint: 'Use cases & benchmarks',
    activePaths: [
      '/jetson/{{ROUTE_FAMILY}}/{{APPLICATION_ROUTE}}/',
    ],
  },
};
