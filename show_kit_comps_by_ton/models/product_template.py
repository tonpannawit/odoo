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

    kit_bom_type = fields.Selection(
        related='product_variant_id.bom_ids.type',
        string='BOM Type',
        help='The type of BOM associated with the product variant.',
    )

    @api.depends('bom_ids', 'bom_ids.bom_line_ids')
    def _compute_kit_components(self):
        for product in self:
            # Start the HTML table
            components_html = """
                <table style="width: 100%; border-collapse: separate; border-spacing: 0;">
                    <thead>
                        <tr style="background-color:rgb(102, 102, 102); color: white;">
                        <th style="padding: 12px; text-align: center;">Image</th>
                        <th style="padding: 12px; text-align: center;">Product</th>
                        <th style="padding: 12px; text-align: center;">Quantity</th>
                        </tr>
                    </thead>
                    <tbody>
            """
            # Add rows for each component
            for line in product.bom_ids.mapped('bom_line_ids'):
                image_url = f"/web/image/product.product/{line.product_id.id}/image_128"
                if line.product_id.website_published:
                    product_name_html = f'<a href="{line.product_id.website_url}" target="_blank">{line.product_id.display_name}</a>'
                    image = f'<a href="{line.product_id.website_url}" target="_blank"><img src="{image_url}" style="border-radius: 6px; overflow: hidden; max-width: 100px; max-height: 100%; display: inline-block;"/></a>'
                else:
                    product_name_html = line.product_id.display_name
                    image = f'<img src="{image_url}" style="border-radius: 6px; overflow: hidden; max-width: 100px; max-height: 100%; display: inline-block;"/>'
                components_html += f"""
                    <tr>
                        <td style="padding: 12px; text-align: center;">
                            {image}
                        </td>
                        <td style="padding: 12px; text-align: center;">{product_name_html} </td>
                        <td style="padding: 12px; text-align: center;">{'{:.0f}'.format(line.product_qty)}</td>
                    </tr>
                """
            # Close the table
            components_html += "</tbody></table>"
            # Store the HTML in the field
            product.kit_components = components_html




