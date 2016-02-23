# -*- coding: utf-8 -*-

from openerp import models, fields, api
import montantEnLettres

class SoulcoReportCompany(models.Model):
    _inherit = 'res.company'

    capital_social = fields.Char("Capital social")


class SoulcoPurchase(models.Model):
    _inherit = 'purchase.order'

    amounTexte = fields.Text(compute="amountToText")
    @api.depends("amount_total")
    def amountToText(self):
        for r in self:
            if r.amount_total != 0:
                montant = montantEnLettres.montant_en_lettres(r.amount_total)
                self.amounTexte = montant[0] + "dinar(s)" + montant[1]
                self.amounTexte = self.amounTexte.capitalize()
            else:
                self.amounTexte = "Zéro dinars"

class SoulcoSaleOrder(models.Model):
    _inherit = 'sale.order'

    amounTexte = fields.Text(compute="amountToText")
    @api.depends("amount_total", "total_timbre", "amount_timbre")
    def amountToText(self):
        for r in self:
            if r.amount_total == 0:
                self.amounTexte = "Zéro dinars"
            else:
                if r.amount_timbre:
                    montant = montantEnLettres.montant_en_lettres(r.total_timbre)
                else:
                    montant = montantEnLettres.montant_en_lettres(r.amount_total)
                self.amounTexte = montant[0] + "dinar(s)" + montant[1]
                self.amounTexte = self.amounTexte.capitalize()

class SoulcoSettings(models.Model):
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
