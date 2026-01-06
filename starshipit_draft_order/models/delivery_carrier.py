from odoo import _, models

class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"
    
    def starshipit_send_shipping(self, pickings, is_return=False):
        starshipit = self._get_starshipit()

        # Create orders in Starshipit ONLY (Draft / New)
        unshipped_orders = starshipit._create_orders(self, pickings, False)['orders']

        res = []
        for picking in pickings:
            starshipit_order_number = starshipit._get_starshipit_order_number(picking)
            order = unshipped_orders.get(starshipit_order_number)

            if not order:
                continue

            order_id = order['order_id']
            picking.starshipit_parcel_reference = order_id

            # Optional chatter message
            picking.message_post(
                body=_(
                    'Order was created in Starshipit as a draft. '
                )
            )

            res.append({
                'exact_price': 0.0,
                'tracking_number': False,
            })

        return res