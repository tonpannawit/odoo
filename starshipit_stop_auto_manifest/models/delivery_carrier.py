from odoo import _, fields, models
from odoo.exceptions import UserError, ValidationError


class DeliveryCarrier(models.Model):
    _inherit = "delivery.carrier"

    def starshipit_send_shipping(self, pickings, is_return=False):
        """ For a given picking, this method will execute a few API calls in order to get the order to be sent to the carrier.
        The order of actions is:
            - Create the order(s) on starshipit side. This will not send them, just register them and return the id(s)
            - Get the labels for each picking, one at a time. This will return the tracking number(s) and url(s).
                - The labels are attached to the picking as ir.attachment
            - If return_label_on_delivery is set, generate the return label(s) for each picking too.
            - Get the delivery order information from starshipit to fetch the final rate, and whether the order was manifested or not.
            - Finally either manifest (send) the order(s) or archive them in test mode.
              If sent, the manifest report is added to the picking as ir.attachment.
        """
        starshipit = self._get_starshipit()
        unshipped_orders = starshipit._create_orders(self, pickings, is_return)['orders']
        res = []

        for picking in pickings:
            starshipit_order_number = starshipit._get_starshipit_order_number(picking)
            # We cant use the api that prints labels for multiple order at once because this endpoint doesn't return the tracking information.
            order = unshipped_orders.get(starshipit_order_number)
            order_id = order['order_id']
            picking.starshipit_parcel_reference = order_id

            label_data = self._create_label_for_order(order_id)

            tracking_number = ', '.join(tracking_number for tracking_number in label_data['tracking_numbers'] if tracking_number is not None)
            picking.carrier_tracking_ref = tracking_number
            try:
                # generate return if config is set
                if self.return_label_on_delivery:
                    self.get_return_label(picking)
            except UserError:
                # if the return fails need to log that they failed and continue
                picking.message_post(body=_('The return label creation failed.'))

            # Get the exact price for the shipping.
            attachment_data = []
            # Attach the labels we got to the picking
            for label in label_data['labels']:
                attachment_data.append({
                    'name': f'{self._get_delivery_label_prefix()}-{picking.name.replace("/", "_").lower()}.pdf',
                    'datas': label,
                    'type': 'binary',
                    'res_model': picking._name,
                    'res_id': picking.id,
                })
            attachment_ids = self.env['ir.attachment'].create(attachment_data)

            order_data = starshipit._get_order_details(order_id)
            total_shipping_price = order_data['order'].get('total_shipping_price', 0.0)

            if not total_shipping_price:
                picking.message_post(body=_('The exact price could not be retrieved. It will be updated by a scheduled action.'))

            order_result = {
                'exact_price': total_shipping_price,
                'tracking_number': tracking_number,
            }
            res.append(order_result)
            if attachment_ids:
                picking.message_post(body=_('Labels were generated for the order %s', picking.name), attachment_ids=attachment_ids.ids)
            
        return res