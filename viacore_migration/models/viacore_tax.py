# ©  2024 Viacore
# Alexandre Sousa
# Netsuite Migration only

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class ViacoreTax(models.Model):
    _name = 'viacore.tax'
    _description = 'Tax Group'
    _check_company_auto = True
    _inherit = ['mail.thread']

    name = fields.Char(string="Tax Group")
    belterra_tax = fields.Char(string="Belterra Tax")
    belterra_tax2 = fields.Char(string="Belterra Tax 2")
    asb_tax = fields.Char(string="ASB Tax")
