# ©  2024 Viacore
# Alexandre Sousa
# Netsuite Migration only

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class ViacoreCustCateg(models.Model):
    _name = 'viacore.category'
    _description = 'Customer Category'
    _check_company_auto = True
    _inherit = ['mail.thread']

    name = fields.Char(string="Customer Category")
    belterra_category = fields.Char(string="Belterra Category")
    asb_category = fields.Char(string="ASB Category")
    asb_code = fields.Char(string="ASB Industry Code")
    asb_type = fields.Char(string="ASB Customer Type")
