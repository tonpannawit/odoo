from odoo import fields, models, api


class AccountMove(models.Model):
    _inherit = "account.move"

    def view_report_preview(self):
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')

        filename = f"{self.name}.pdf"
        
        url = (
        f"{base_url}/report/pdf/account.report_invoice/{self.id}"
        f"?filename={filename}"
        )

        values = {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url,
        }
        return values

    def view_report_preview_with_payments(self):
        base_url = self.env['ir.config_parameter'].sudo(
        ).get_param('web.base.url')

        filename = f"{self.name}.pdf"
        
        url = (
        f"{base_url}/report/pdf/account.report_invoice_with_payments/{self.id}"
        f"?filename={filename}"
        )

        values = {
            'type': 'ir.actions.act_url',
            'target': 'new',
            'url': url,
        }
        return values
