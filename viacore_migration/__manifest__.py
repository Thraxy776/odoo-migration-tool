# Copyright 2015 Camptocamp SA
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Viacore Data",
    "version": "17.0.0.0.0",
    "author": "Viacore Team",
    "license": "AGPL-3",
    "category": "Extra Tools",
    "website": "https://www.viacore.com",
    'depends': [
        'mail',
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "views/viacore_migration_menus.xml",
        "views/viacore_employee.xml",
        "views/viacore_location.xml",
        "views/viacore_customer.xml",
        "views/viacore_terms.xml",
        "views/viacore_category.xml",
        "views/viacore_tax.xml",
        "views/viacore_vendor_category.xml",
        "views/viacore_accounts.xml",
        "views/viacore_vendor.xml",
    ],
    "installable": True,
    "auto_install": False,
}
