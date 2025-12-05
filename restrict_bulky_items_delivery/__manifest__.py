# -*- coding: utf-8 -*-

{
    'name': 'Website Limit Delivery Method for Bulky Items',
    'version': '16.0.0',
    'category': 'Website',
    'summary': 'Limit or Restrict Delivery Method per products',
    'description': "Limit delivery method for bulky items that cannot be shipped by courier on the website.",
    'license': 'LGPL-3',
    'author': 'Veera eCom Solutions',
    'website': 'https://www.linkedin.com/in/ton-pannawit-veerareungrat-603980120/',
    'depends': ['website_sale_delivery', 'base', 'stock', 'product'],
    'data': ['views/views.xml',
             'views/product_template.xml',
             'views/website_sale.xml'
             ],
    
    'images': ['static/description/icon.png'],
    'installable': True,
    'auto_install': False,
    'application': False,
    'price': '20.00',
    'currency': 'USD'
}
