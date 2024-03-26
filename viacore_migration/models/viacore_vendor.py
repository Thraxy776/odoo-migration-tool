# Riley Kilb
# Netsuite Migration only

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError


class ViacoreVendor(models.Model):
    _name = 'viacore.vendor'
    _description = 'Vendor'
    _check_company_auto = True
    _inherit = ['mail.thread']

    legacy_vendor_category = fields.Char(string='Legacy Category')
    legacy_vendor_ASB_ID = fields.Char(string='ASB Vendor ID')
    legacy_vendor_Sage_ID = fields.Char(string='Belterra Vendor ID')
    legacy_vendor_terms = fields.Char(string='Legacy Terms')
    legacy_vendor_email = fields.Char(string='Legacy Email')
    legacy_vendor_payment_email = fields.Char(string="Legacy Email for Payment")
    legacy_vendor_phone = fields.Char(string='Legacy Phone')
    legacy_vendor_altphone = fields.Char(string='Legacy Alt. Phone')
    legacy_vendor_tax_code = fields.Char(string='Legacy Tax Code')
    legacy_vendor_default_Exps_account = fields.Char(string='Legacy Expense Account')
    legacy_vendor_default_Pay_account = fields.Char(string='Legacy Payable Account')
    legacy_vendor_name = fields.Char(string='Legacy Company Name', track_visibility='onchange')
    legacy_vendor_web_address = fields.Char(string='Legacy Web Address')
    legacy_vendor_tax_ID = fields.Char(string='Legacy Tax ID', track_visibility='onchange')
    legacy_vendor_primary_currency = fields.Char(string='Legacy Primary Currency', track_visibility='onchange')
    legacy_vendor_pay_method = fields.Char(string='Legacy Payment Method')
    legacy_vendor_eft_pay = fields.Boolean(string='Legacy EFT Bill Payment')
    legacy_vendor_1099_type = fields.Char(string='Legacy 1099 Form Type', track_visibility='onchange')
    legacy_vendor_entity_type = fields.Char(string='Legacy Entity Type', track_visibility='onchange')
    legacy_vendor_legalname = fields.Char(string='Legacy Legal Name', track_visibility='onchange')
    legacy_vendor_CustID = fields.Char(string='Legacy Vendor Customer ID')
    legacy_vendor_credlimit = fields.Char(string='Legacy Credit Limit')

    name = fields.Char(string="Name", track_visibility='onchange', size=80)
    vendor_type = fields.Char(string='Type', default='Company')
    vendor_id = fields.Char(string='Vendor ID', track_visibility='onchange')
    external_id = fields.Char(string='External ID', track_visibility='onchange')
    legal_name = fields.Char(string="Legal Name", track_visibility='onchange', size=80)
    terms = fields.Many2one("viacore.term", string="Payment Terms", track_visibility='onchange')
    category = fields.Many2one("viacore.vendor.category", string="Category", track_visibility='onchange')
    tax = fields.Many2one("viacore.tax", string="Tax Group", track_visibility='onchange')
    payables = fields.Many2one("viacore.accounts", string="Payables Account", track_visibility='onchange')
    expenses = fields.Many2one("viacore.accounts", string="Expenses Account", track_visibility='onchange')
    email = fields.Char(string="Email", track_visibility='onchange')
    payment_email = fields.Char(string="Email for Payment", track_visibility='onchange')
    phone = fields.Char(string="Phone", track_visibility='onchange')
    altphone = fields.Char(string="Alt Phone", track_visibility='onchange')
    webaddress = fields.Char(string="Web Address", track_visibility='onchange')
    paymethod = fields.Char(string="Payment Method", track_visibility='onchange')
    taxID = fields.Char(string='Tax ID', track_visibility='onchange')
    eftpay = fields.Boolean(string='EFT Bill Payment', track_visibility='onchange')
    vendor_1099type = fields.Char(string='1099 Type', track_visibility='onchange')
    entitytype = fields.Char(string='Entity Type', track_visibility='onchange')
    vendorcustid = fields.Char(string='Vendor Customer ID', track_visibility='onchange')
    credlimit = fields.Char(string='Credit Limit', track_visibility='onchange')
    vouchercomments = fields.Char(string='Voucher Comments', track_visibility='onchange')
    status = fields.Selection([('to_review', 'To Review'), ('revised', 'Revised'), ('ignore', 'Ignore')],
                              string='Status', default='to_review', required=True)

    addresses_ids = fields.One2many("viacore.vendor.address", "address_id", string="Addresses",
                                    track_visibility='onchange')
    bank_ids = fields.One2many("viacore.vendor.banks", "bank_id", string="Banks", track_visibility='onchange')

    vendor_subsidiary = fields.Selection([('belterra', 'Viacore Holding Inc. : Viacore Solutions Inc.'),
                                          ('asb', 'Viacore Holding Inc. : Viacore Solutions LLC')], 'Subsidiary',
                                         required=True, track_visibility='onchange')

    primary_currency = fields.Selection([('belterra', 'Canadian Dollar'),
                                        ('asb', 'US Dollar')], 'Primary Currency',
                                        required=True, track_visibility='onchange')

    _sql_constraints = [
        ('new_name', 'unique(new_name)', 'The field name must be unique!!!')
    ]

    @ api.onchange('new_name')
    def onchange_new_name(self):
        self.status = 'revised'

    class ViacoreVendAddress(models.Model):
        _name = "viacore.vendor.address"
        _description = "Addresses"

        address_id = fields.Many2one("viacore.vendor", string="Vendor", required=True)
        name = fields.Char(string="Address Name")
        shipping = fields.Boolean(string="Default PO Address")
        billing = fields.Boolean(string="Default RMT Address")
        poline1 = fields.Char(string=" PO Address Line 1")
        poline2 = fields.Char(string=" PO Address Line 2")
        pocity = fields.Char(string="PO City")
        postate = fields.Char(string="PO State/Province")
        pozip = fields.Char(string="PO Zip Code")
        pocountry = fields.Char(string="PO Country")
        rmtline1 = fields.Char(string=" RMT Address Line 1")
        rmtline2 = fields.Char(string=" RMT Address Line 2")
        rmtcity = fields.Char(string="RMT City")
        rmtstate = fields.Char(string="RMT State/Province")
        rmtzip = fields.Char(string="RMT Zip Code")
        rmtcountry = fields.Char(string="RMT Country")

    class ViacoreBankDetails(models.Model):
        _name = "viacore.vendor.banks"
        _description = "Bank Details"

        bank_id = fields.Many2one("viacore.vendor", string="Vendor", required=True)
        name = fields.Char(string="Bank Name")
        bank_acc_number = fields.Char(string="Bank Account Number")
        paymethod = fields.Char(string="Payment Method")
        bank_number = fields.Char(string="Bank Routing")
        acctype = fields.Char(string='Account Type')
        bank_currency = fields.Selection([('CA', 'Canadian Dollar'),
                                        ('US', 'US Dollar')], 'Primary Currency',
                                        required=True, track_visibility='onchange')
