# -*- coding: utf-8 -*-
from odoo import http

# class Shipment(http.Controller):
#     @http.route('/shipment_list/shipment_list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shipment_list/shipment_list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shipment_list.listing', {
#             'root': '/shipment_list/shipment_list',
#             'objects': http.request.env['shipment_list.shipment_list'].search([]),
#         })

#     @http.route('/shipment_list/shipment_list/objects/<model("shipment_list.shipment_list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shipment_list.object', {
#             'object': obj
#         })