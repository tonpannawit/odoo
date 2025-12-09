from odoo import fields, models, api


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def view_report_preview(self):
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')

        filename = f"{self.name}.pdf"
        
        url = (
        f"{base_url}/report/pdf/stock.report_picking/{self.id}"
        f"?filename={filename}"
        )

        values = {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url,
        }
        return values

