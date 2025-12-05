from odoo import fields, models, api

    
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def view_report_preview(self):
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')

        filename = f"{self.name}.pdf"
        
        url = (
        f"{base_url}/report/pdf/purchase.report_purchaseorder/{self.id}"
        f"?filename={filename}"
        )

        values = {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url,
        }
        return values



