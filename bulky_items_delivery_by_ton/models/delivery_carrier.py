from odoo import fields, models, api

import re

class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    for_bulky_products = fields.Boolean(
            string="For Bulky Products",
            help="Indicates if the delivery method is available for Bulky Products"
        )


