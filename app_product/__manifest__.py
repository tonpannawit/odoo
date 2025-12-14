{
    'name': "Products",
    'version': '19.0.0',
    'depends': ['product', 'stock'],
    'category': 'web',
    'author': "Veera eCom Solutions",
    'website': 'https://www.linkedin.com/in/ton-pannawit-veerareungrat-603980120/',
    'summary': 'Access Product Menu directly from the Odoo App Page',
    'description': """Access Product Menu directly from the Odoo App Page""",
    'data': [
        'views/product_template_view.xml',
    ],
    'images': ['static/description/banner.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'price': '15.00',
    'currency': 'USD'
}
