# -*- coding: utf-8 -*-
from odoo import http

# class BillInvoiceSummary(http.Controller):
#     @http.route('/bill_invoice_summary/bill_invoice_summary/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/bill_invoice_summary/bill_invoice_summary/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('bill_invoice_summary.listing', {
#             'root': '/bill_invoice_summary/bill_invoice_summary',
#             'objects': http.request.env['bill_invoice_summary.bill_invoice_summary'].search([]),
#         })

#     @http.route('/bill_invoice_summary/bill_invoice_summary/objects/<model("bill_invoice_summary.bill_invoice_summary"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('bill_invoice_summary.object', {
#             'object': obj
#         })