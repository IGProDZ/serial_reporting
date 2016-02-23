# -*- coding: utf-8 -*-

from openerp import models, fields, api
class SoulcoReportCompany(models.Model):
    _inherit = 'res.company'

    capital_social = fields.Char("Capital social")

class soulco(models.Model):
    _inherit = 'report.paperformat'

    def _update_top_margin(self):
        euro_format = self.env['report.paperformat'].search([('name','=','European A4')])
        return euro_format.write({'margin_top':37})

    def _update_bottom_margin(self):
        euro_format = self.env['report.paperformat'].search([('name','=','European A4')])
        return euro_format.inverse({'margin_bottom':45})

    def _update_header_line(self):
        euro_format = self.env['report.paperformat'].search([('name','=','European A4')])
        return euro_format.write({'header_line':False})

    margin_top = fields.Integer(string="Top margin", default=_update_top_margin)
    margin_bottom = fields.Integer(string="Bottom margin", default=_update_bottom_margin)
    header_line = fields.Boolean(string="Display a header line", default=_update_header_line)
