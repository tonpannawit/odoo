from odoo import fields, models, api


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def view_report_preview(self):
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')

        filename = f"{self.name}.pdf"
        
        url = (
        f"{base_url}/report/pdf/sale.report_saleorder/{self.id}"
        f"?filename={filename}"
        )
        
        values = {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url,
        }
        return values
    
    def view_report_proforma(self):
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')
        
        filename = f"Pro-Forma-{self.name}.pdf"

        url = (
        f"{base_url}/report/pdf/sale.report_saleorder_pro_forma/{self.id}"
        f"?filename={filename}"
        )
        
        values = {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url,
        }
        return values




