from odoo import api, fields, models,_
from datetime import datetime
from odoo.exceptions import ValidationError

### wizard
class TopSelling(models.TransientModel):
    _name = "topselling.orderline"

    date_from = fields.Date('From Date')
    date_to = fields.Date('To Date')

    @api.onchange('date_to')
    def onchange_date_to(self):
        for record in self:
            if record.date_to < record.date_from:
                raise ValidationError("Please select right date")
            else:
                pass
    
    @api.multi
    def top_cancel_reason_counter(self):
        sale_order_list = []
        sale_order_ids = self.env['sale.order'].search([('confirmation_date','<=',self.date_to),('confirmation_date','>=',self.date_from),('state','=','cancel')])
        if sale_order_ids:
            for oder in sale_order_ids:
                sale_order_list.append(order)
        print(sale_order_list)
