from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Computed Many2many field for pricelist items
    pricelist_items = fields.Many2many(
        'product.pricelist.item',  # Link to the product.pricelist.item model
        string='Quantity Pricing',
        compute='_compute_pricelist_items',
        help='Quantity pricing for this product.',
        store=True
    )

    @api.depends('product_variant_ids')
    def _compute_pricelist_items(self):
        for product in self:
            # Fetch pricelist items related to this product template
            product.pricelist_items = self.env['product.pricelist.item'].search([
                ('product_tmpl_id', '=', product.id), ('pricelist_id', '=', 1)
            ])