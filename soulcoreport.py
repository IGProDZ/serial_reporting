#-*- coding: utf-8 -*-

from openerp import models, fields, api
import montantEnLettres

class SoulcoReportCompany(models.Model):
    _inherit = 'res.company'

    capital_social = fields.Char("Capital social")

class ReportQuotation(models.Model):
    _inherit = 'purchase.order'

    amounTexte = fields.Text(compute="amountToText")
    @api.depends("amount_total")
    def amountToText(self):
        for r in self:
            montant = montantEnLettres.montant_en_lettres(r.amount_total)
            self.amounTexte = montant[0] + "dinar(s)" + montant[1]
            self.amounTexte = self.amounTexte.capitalize()
