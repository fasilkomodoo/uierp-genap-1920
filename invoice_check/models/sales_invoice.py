from odoo import api, fields, models, _

class SaleOrderUpdate(models.Model):
    _inherit = 'sale.order'

    invoice_check = fields.Character(String = "Invoice", compute = '_computeCek')

    @api.multi
    def _computeCek(self):
        invoice_id = self.env['account.invoice'].search(['&',('origin','=', self.name),'|',('state','=','open'),('state','=','paid')])
        if(invoice_id == null):
            self.invoice_check = "Belum Dibuat"

        else:
            self.invoice_check = "Sudah Dibuat"