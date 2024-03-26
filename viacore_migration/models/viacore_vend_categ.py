# ©  2024 Viacore
# Alexandre Sousa
# Netsuite Migration only

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class ViacoreVendCateg(models.Model):
    _name = 'viacore.vendor.category'
    _description = 'Vendor Category'
    _check_company_auto = True
    _inherit = ['mail.thread']

    name = fields.Char(string="Vendor Category")
    belterra_vendor_category = fields.Char(string="Belterra Category")
    asb_vendor_category = fields.Char(string="ASB Category")

