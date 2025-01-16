from odoo import fields, models, api

import re

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    bulky_product = fields.Boolean(
        string="Bulky Product",
        help="Indicates if the product is bulky and may require special handling."
    )

