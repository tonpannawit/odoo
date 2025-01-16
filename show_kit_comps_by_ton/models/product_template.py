from odoo import fields, models, api
from datetime import datetime, timedelta

import re

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    kit_components = fields.Html(
    string='Kit Components',
    compute='_compute_kit_components',
    store=True,
    help='Components and their quantities based on the BOM, stored as an HTML table.'
    )

    @api.depends('bom_ids', 'bom_ids.bom_line_ids')
    def _compute_kit_components(self):
        for product in self:
            # Start the HTML table
            components_html = """
                <table style="width: 100%; border-collapse: separate; border-spacing: 0; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                    <thead>
                        <tr style="background-color: #EA6100; color: white;">
                        <th style="padding: 12px; text-align: center;">Image</th>
                        <th style="padding: 12px; text-align: left;">Product</th>
                        <th style="padding: 12px; text-align: center;">Quantity</th>
                        </tr>
                    </thead>
                    <tbody>
            """
            # Add rows for each component
            for line in product.bom_ids.mapped('bom_line_ids'):
                if line.product_id.website_published:
                    product_name_html = f'<a href="{line.product_id.website_url}" target="_blank">{line.product_id.name}</a>'
                else:
                    product_name_html = line.product_id.name
                image_url = f"/web/image/product.product/{line.product_id.id}/image_128"
                components_html += f"""
                    <tr>
                        <td style="padding: 12px; text-align: center;">
                            <img src="{image_url}" style="border-radius: 6px; overflow: hidden; max-width: 60px; max-height: 100%; display: inline-block;"/>
                            <span>{line.product_id.default_code}</span>
                        </td>
                        <td style="padding: 12px;">{product_name_html} </td>
                        <td style="padding: 12px; text-align: center;">{line.product_qty}</td>
                    </tr>
                """
            # Close the table
            components_html += "</tbody></table>"
            # Store the HTML in the field
            product.kit_components = components_html




