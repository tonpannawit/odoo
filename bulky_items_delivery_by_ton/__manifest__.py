# -*- coding: utf-8 -*-

{
    'name': 'Website Limit Delivery Method for Bulky Items',
    'version': '1.1',
    'category': 'Website',
    'summary': 'Limit or Restrict Delivery Method per products',
    'description': "Limit delivery method for bulky items that cannot be shipped by courier on the website.",
    'license': 'LGPL-3',
    'author': 'Ton Pannawit',
    'website': '',
    'depends': ['website_sale_delivery', 'base', 'stock', 'product'],
    'data': ['views/views.xml',
             'views/product_template.xml',
             'views/website_sale.xml'
             ],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': '70.00',
    'currency': 'USD'
}
