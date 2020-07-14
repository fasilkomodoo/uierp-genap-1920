from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    date_cancelled = fields.Datetime(string='Date Cancelled')