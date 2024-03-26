# ©  2024 Viacore
# Alexandre Sousa
# Netsuite Migration only

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class ViacoreTerms(models.Model):
    _name = 'viacore.term'
    _description = 'Payment Terms'
    _check_company_auto = True
    _inherit = ['mail.thread']

    name = fields.Char(string="Term")
    belterra_term = fields.Char(string="Belterra Term")
    asb_term = fields.Char(string="ASB Term")
