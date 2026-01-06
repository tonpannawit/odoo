from odoo import models

    
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    
    def create_bill(self):
        if self:
            action = self.action_create_invoice()
            return action




