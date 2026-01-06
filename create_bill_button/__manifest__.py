# -*- coding: utf-8 -*-
{
    'name': 'Create Bill Button in Purchase',
    'version': '19.0.0.0.0',
    'website': '',
    'author': 'Veera eCom Solutions',
    'summary': 'Create Bill manually directly from Purchase',
    'description': """This module allows a users to generate a bill manually from Purchase module.
    Odoo19 has been intentionally modified to replace 'Create Bill' with 'Upload Bill'.
    """,
    'category': 'Extra Tools',
    'depends': [
        'purchase'
    ],
    'data': [
        'views/purchase_order.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
    'price': '25.00',
    'currency': 'USD'
}
