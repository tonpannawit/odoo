from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    trade_price = fields.Char(
        'Trade Price', compute='_compute_product_trade_price', tracking=True, index=True)
    vendor_name = fields.Char(string='Supplier', compute='_compute_vendor_name', search='_search_suppliers', store=True)


    def _compute_product_trade_price(self):
        for res in self:
            pricelist = self.env['product.pricelist.item'].search([
                    ('product_tmpl_id', '=', res.id), ('pricelist_id', '=', 11), ('min_quantity', '=', 0)], limit=1)
            if pricelist:
                res.trade_price = pricelist.price
            else:
                res.trade_price = res.list_price

    @api.depends('seller_ids')
    def _compute_vendor_name(self):
            for res in self:
                        vendor_name = ''
                        if res.purchase_ok and res.seller_ids:
                            vendor_name = res.seller_ids[0].partner_id.display_name
                        res.vendor_name = vendor_name

    def _search_suppliers(self, operator, value):
            products = []
            for product in self.env['product.template'].search([]):
                if product.vendor_name == value:
                    products.append(product)
            return [('id', 'in', [pro.id for pro in products])]