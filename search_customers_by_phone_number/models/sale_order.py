from odoo import fields, models, api

import re

class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.model
    def _name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None, **kwargs):
        args = list(args or [])
        if name:
            args += ['|', '|', '|', ('name', operator, name), ('phone', operator, name), ('mobile', operator, name), ('email', operator, name)]
        return self._search(args, limit=limit, access_rights_uid=name_get_uid)