from odoo import models, fields, api
from datetime import date, datetime

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'
    date_cancelled=fields.Datetime('Date Cancelled')