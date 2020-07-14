# -*- coding: utf-8 -*-

from odoo import models, fields, api

class shipment_list(models.Model):
    _name = 'shipment_list.shipment_list'

    date = fields.Date()
    shipment_id = fields.Text()
    purchase_order = fields.Many2one('purchase.order', 'Purchase Order')
    # purchase_order = fields.Text()
    shipping_date = fields.Date()
    status = fields.Text()
    expedition = fields.Text()
    shipping_cost = fields.Text()
    vehicle_number = fields.Text()
    country = fields.Text()
    region = fields.Text()
    city = fields.Text()
    postal_code = fields.Text()
    address = fields.Text()
    phone_number = fields.Text()

    # @api.depends('users')
    # def _value_users(self):
    #     self.number_of_users = int(len(self.users))

    