# ©  2024 Viacore
# Alexandre Sousa
# Netsuite Migration only

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class ViacoreAccounts(models.Model):
    _name = 'viacore.accounts'
    _description = 'Chart of Accounts'
    _check_company_auto = True
    _inherit = ['mail.thread']

    name = fields.Char(string='Account Name')
    number = fields.Char(string='Account Number')
    type = fields.Char(string='Account Type')
    belterra_name = fields.Char(string='Belterra Account Name')
    belterra_number = fields.Char(string='Belterra Account Number')
    asb_name = fields.Char(string='ASB Account Name')
    asb_number = fields.Char(string='ASB Account Number')
