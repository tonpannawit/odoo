# -*- coding: utf-8 -*-
{
    'name': 'StarShipIt Stop Auto Manifest',
    'version': '19.0.0.0.0',
    'website': '',
    'author': 'Veera eCom Solutions',
    'summary': 'Disabling auto-manifesting on every order shipped through StarShipIT',
    'description': """Manifest should not be shipped individually and this module prevents auto-manifesting.
    """,
    'category': 'Extra Tools',
    'depends': [
        'base', 'sale_stock', 'delivery_starshipit',
                'stock',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
    'price': '30.00',
    'currency': 'USD'
}
