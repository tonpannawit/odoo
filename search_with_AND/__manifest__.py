
{
    'name': 'Search with AND logic',
    'version': '19.0.0',
    'summary': """ This app allows us to search using AND operator.""",
    'description': """ Search products more effectively. """,
    'author': 'Veera eCom Solutions',
    'website': 'https://www.linkedin.com/in/ton-pannawit-veerareungrat-603980120/',
    'depends': ['web'],
    'assets': {
        'web.assets_backend': [
            'search_with_AND/static/src/search/search_model.js',
        ]
    },
    'images': ['static/description/banner.jpg'],
    'license': 'OPL-1',
    'price': 70.00,
    'currency': 'USD',
    'installable': True,
    'auto_install': False,
    'application': False,
}
