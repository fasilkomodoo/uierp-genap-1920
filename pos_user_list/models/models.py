# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pos_user_list(models.Model):
    _name = 'pos_user_list.pos_user_list'

    pos_config = fields.Many2one('pos.config', string="PoS Configuration")
    date = fields.Date()
    status = fields.Text()
    users = fields.Many2many('res.users')
    number_of_users = fields.Integer(compute="_value_users", store=True)

    _sql_constraints = [('unique_list', 'UNIQUE(pos_config, date)', 'Entry already exists\nPlease select a different date and configuration')]

    @api.depends('users')
    def _value_users(self):
        self.number_of_users = int(len(self.users))

    