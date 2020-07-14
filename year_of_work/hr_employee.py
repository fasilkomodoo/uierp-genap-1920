from odoo import models, fields, api, _
from datetime import date, datetime


class hr_employee(models.Model):
    _inherit = 'hr.employee'
    date_of_join = fields.Date('Joining Date')
    date_of_leave = fields.Date('Leaving Date')

    employee_low = fields.Char(string="Year of Work")
    
    @api.onchange('date_of_join')
    def onchange_employee_low(self):
        if self.date_of_join:
            today = date.today()
            low = today.year - self.date_of_join.year - ((today.month, today.day) < (self.date_of_join.month, self.date_of_join.day))
            self.employee_low = str(low)
            