# -*- coding: utf-8 -*-
from odoo import http

# class PosUserList(http.Controller):
#     @http.route('/pos_user_list/pos_user_list/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pos_user_list/pos_user_list/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('pos_user_list.listing', {
#             'root': '/pos_user_list/pos_user_list',
#             'objects': http.request.env['pos_user_list.pos_user_list'].search([]),
#         })

#     @http.route('/pos_user_list/pos_user_list/objects/<model("pos_user_list.pos_user_list"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pos_user_list.object', {
#             'object': obj
#         })