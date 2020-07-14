from odoo import api, fields, models, _

class SaleOrder(models.Model):
    _inherit = "sale.order.line"

    top_order_id = fields.Many2one('name')

