# ©  2024 Viacore
# Alexandre Sousa
# Netsuite Migration only

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError

class ViacoreCustomer(models.Model):
    _name = 'viacore.customer'
    _description = 'Customer'
    _check_company_auto = True
    _inherit = ['mail.thread']

    status = fields.Selection([('to_review', 'To Review'), ('revised', 'Revised'), ('ignore', 'Ignore')], 'Status', default='to_review', required=True)

    legacy_id = fields.Char(string="Customer ID", track_visibility='onchange')
    legacy_parent = fields.Char(string="Parent ID")
    legacy_name = fields.Char(string="Legacy Name")
    legacy_credit_limit = fields.Float(string="Legacy Credit Limit")
    legacy_sales_rep = fields.Char(string="Legacy Sales Rep")
    legacy_category = fields.Char(string="Legacy Category")
    legacy_terms = fields.Char(string="Legacy Payment Terms")
    legacy_email = fields.Char(string="Legacy Email")
    legacy_phone = fields.Char(string="Legacy Phone")
    legacy_fax = fields.Char(string="Legacy Fax")
    legacy_tax = fields.Char(string="Legacy Tax Item")
    legacy_invoice_email = fields.Char(string="Legacy Invoice email")
    legacy_credit_date = fields.Char(string="Legacy Cred. Application Date")
    legacy_first_sale = fields.Char(string="Legacy Fist Sales Date")
    legacy_duns = fields.Char(string="Legacy DUNS #")
    legacy_service_rep = fields.Char(string="Legacy Service Rep")
    legacy_tax_exemption1 = fields.Char(string="Legacy Tax Exemption 1")
    legacy_tax_exemption2 = fields.Char(string="Legacy Tax Exemption 2")

    addresses_ids = fields.One2many("viacore.address", "address_id", string="Addresses", track_visibility='onchange')
    contacts_ids = fields.One2many("viacore.contact", "contact_id", string="Contacts", track_visibility='onchange')

    name = fields.Char(string="Name", track_visibility='onchange', size=80)

    credit_limit = fields.Float(string="Credit Limit",track_visibility='onchange')
    subsidiary = fields.Selection([('belterra', 'Viacore Holding Inc. : Viacore Solutions Inc.'),
                                   ('asb', 'Viacore Holding Inc. : Viacore Solutions LLC')], 'Subsidiary',
                                  required=True, track_visibility='onchange')

    sales_rep = fields.Many2one("viacore.employee", string="Sales Rep", domain="[('sales_rep', '=', True)]",
                                force_create=False, track_visibility='onchange')

    category = fields.Many2one("viacore.category", string="Category", track_visibility='onchange')
    terms = fields.Many2one("viacore.term", string="Payment Terms", track_visibility='onchange')
    email = fields.Char(string="Email", track_visibility='onchange')
    phone = fields.Char(string="Phone", track_visibility='onchange')
    fax = fields.Char(string="Fax", track_visibility='onchange')
    tax = fields.Many2one("viacore.tax", string="Tax Group", track_visibility='onchange')
    invoice_email = fields.Char(string="Invoice email", track_visibility='onchange')
    credit_date = fields.Char(string="Cred. Application Date")
    first_sale = fields.Char(string="Fist Sales Date")
    duns = fields.Char(string="DUNS #", track_visibility='onchange')
    service_rep = fields.Char(string="Service Rep")
    tax_exemption1 = fields.Char(string="Tax Exemption 1")
    tax_exemption2 = fields.Char(string="Tax Exemption 2")

    _sql_constraints = [
        ('new_name', 'unique(new_name)', 'The field name must be unique!!!')
    ]

    @api.onchange('new_name')
    def onchange_new_name(self):
        self.status = 'revised'


class ViacorAddress(models.Model):
    _name = "viacore.address"
    _description = "Addresses"

    address_id = fields.Many2one("viacore.customer", string="Customer", required=True)
    name = fields.Char(string="Address Name")
    shipping = fields.Boolean(string="Default Shipping")
    billing = fields.Boolean(string="Default Billing")
    line1 = fields.Char(string="Address Line 1")
    line2 = fields.Char(string="Address Line 2")
    city = fields.Char(string="City")
    state = fields.Char(string="State/Province")
    zip = fields.Char(string="Zip Code")
    country = fields.Char(string="Country")

#    state = fields.Many2one('res.country.state', 'Fed. State', domain="[('country_id', '=?', country)]")
#    country = fields.Many2one('res.country')


class ViacorContact(models.Model):
    _name = "viacore.contact"
    _description = "Contacts"

    contact_id = fields.Many2one("viacore.customer", string="Customer", required=True)
    first_name = fields.Char(string="First Name")
    last_name = fields.Char(string="Last Name")
    email = fields.Char(string="Email")
    job_title = fields.Char(string="Job Title")
    contact_role = fields.Char(string="Contact Role")
    phone = fields.Char(string="Phone")
    mobile_phone = fields.Char(string="Mobile Phone")
    fax = fields.Char(string="Fax")
    website = fields.Char(string="Website")
    notes = fields.Text(string="Notes")
