========================
POS Container Deposit List
========================

This module extends the ``product.template`` list view to expose two optional
columns:

* **Is Deposit** (``is_deposit``) – flag indicating the product is a deposit container.
* **Deposit Product** (``deposit_product_id``) – the linked deposit product.

Both columns are hidden by default and can be toggled via the optional-columns
button (top-right of the list view).

Requirements
------------

* Odoo 16.0
* Module ``pos_container_deposit``

Installation
------------

Add this module to your Odoo addons path and install it from the Apps menu.
