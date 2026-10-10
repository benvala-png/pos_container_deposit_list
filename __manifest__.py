{
    "name": "POS Container Deposit List",
    "version": "16.0.1.0.0",
    "category": "Point of Sale",
    "summary": "Adds is_deposit and deposit_product_id as optional columns"
    " in the product.template list view.",
    "author": "Benjamin Van Laethem",
    "website": "https://github.com/benvala-png/pos_container_deposit_list",
    "license": "AGPL-3",
    "depends": ["pos_container_deposit"],
    "data": [
        "views/product_template_list.xml",
    ],
    "installable": True,
    "auto_install": False,
}
