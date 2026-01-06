{
    'name': 'StarShipIt Send Order as Draft',
    'version': '19.0.0',
    'website': '',
    'author': 'Veera eCom Solutions',
    'summary': 'Sending through shipping order as draft to StarShipIT to provide more flexibility for sender',
    'description': """This module allows sender to make any final modifications on StarShipIT before the shipping order
    and manifest are finalised.
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
    'price': '60.00',
    'currency': 'USD'
}
