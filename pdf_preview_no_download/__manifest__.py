# -*- coding: utf-8 -*-
{
    'name': 'PDF Preview without Download',
    'version': '16.0.0',
    'website': 'https://www.linkedin.com/in/ton-pannawit-veerareungrat-603980120/',
    'author': 'Veera eCom Solutions',
    'summary': 'Preview PDF on a new tab without downloading',
    'description': """This module allows a users to open a pdf file on a new tab without downloading. Print buttons appear for Sales Order/Quotation,
    Pro-Forma Invoice, Stock Move Operations, RFQ/PO, and Paid/Unpaid Invoice.
    """,
    'category': 'Extra Tools',
    'depends': [
        'base', 'base_setup', 'sale_management',
                'stock', 'purchase', 'account'
    ],
    'data': [
        'views/sale_order.xml',
        'views/stock_picking.xml',
        'views/purchase_order.xml',
        'views/account_move.xml'
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'OPL-1',
    'price': '20.00',
    'currency': 'USD'
}
