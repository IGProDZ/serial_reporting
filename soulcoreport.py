# -*- coding: utf-8 -*-

from openerp import models, fields, api
class SoulcoReport(models.Model):
    _inherit = 'res.company'

    capital_social = fields.Char("Capital social")
