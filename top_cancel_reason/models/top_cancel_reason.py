from odoo import api, fields, models, _

class TopCancelReason(models.Model):
    _name = "top.cancel.reason"
    _order = 'quantity desc'

    reason = fields.Many2one('sale.order.quota_cancel_reason_id', string ='Reason')
    quantity = fields.Float(string ='Quantity')

