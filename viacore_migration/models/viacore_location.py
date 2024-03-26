# ©  2024 Viacore
# Alexandre Sousa
# Netsuite Migration only

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError


class ViacoreLocation(models.Model):
    _name = 'viacore.location'
    _description = 'Location'
    _check_company_auto = True
    _inherit = ['mail.thread']

    name = fields.Char(string='Name', required=True)
    branch_id = fields.Char(string='Branch ID')
    netsuite_id = fields.Char(string='Netsuite ID', required=True)
    belterra_id = fields.Char(string='Belterra ID')
    asb_id = fields.Char(string='ASB ID')
    subsidiary = fields.Selection([('belterra', 'Viacore Holding Inc. : Viacore Solutions Inc.'), ('asb', 'Viacore Holding Inc. : Viacore Solutions LLC')], 'Subsidiary', required=True)

    _sql_constraints = [('name_uniq', 'unique (name)', "Location name already exists!"),
                        ('netsuite_uniq', 'unique (netsuite_id)', "Netsuite id already exists!"),]

