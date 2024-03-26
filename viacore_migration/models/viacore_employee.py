# ©  2024 Viacore
# Alexandre Sousa
# Netsuite Migration only

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class ViacoreEmployee(models.Model):
    _name = 'viacore.employee'
    _description = 'Employee'
    _check_company_auto = True
    _inherit = ['mail.thread']

    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    name = fields.Char(string='Name') #fields.Char(string='Name', compute="_compute_employee_name")
    job_title = fields.Char(string='Job Title')
    email = fields.Char(string='email')
    supervisor = fields.Many2one("viacore.employee", string="Supervisor")
    sales_rep = fields.Boolean(string='Sales Rep')
    location = fields.Many2one("viacore.location", string="Location")
    subsidiary = fields.Selection([('belterra', 'Viacore Holding Inc. : Viacore Solutions Inc.'),
                                   ('asb', 'Viacore Holding Inc. : Viacore Solutions LLC')], 'Subsidiary',
                                  required=True)
    labor_cost = fields.Float(string="Labour cost")
    mobile_user = fields.Boolean(string='NextService Mobile User')
    give_access = fields.Boolean(string='NetSuite Access')
    role = fields.Selection([('super', 'OPS/WAREHOUSE[Super User]'),
                                      ('sales', 'Sales'),
                                      ('ap', 'A/P Analyst'),
                                      ('ar', 'A/R Analyst'),
                                      ('tech','Technician'),
                                      ('cont','Controller'),
                                      ('wm'  ,'Warehouse Manager'),
                                      ('sc'  ,'Supply Chain'),
                                      ('acct', 'Accountant')],
                            'Role',)

    # def _compute_employee_name(self):
    #     for record in self:
    #         if record.first_name and record.last_name:
    #             record.name = record.first_name + ' ' + record.last_name
    #         else:
    #             record.name = ''
    @api.onchange('first_name', 'last_name')
    def onchange_name(self):
        if self.first_name and self.last_name:
            self.name = self.first_name + " " + self.last_name


    @api.onchange('location')
    def onchange_location(self):
        #self.subsidiary = dict(self.location._fields['subsidiary'].selection).get(self.location.subsidiary)
        if self.location:
            self.subsidiary = self.location.subsidiary
