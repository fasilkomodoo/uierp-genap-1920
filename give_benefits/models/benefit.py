# -*- coding: utf-8 -*-

from odoo import models, fields

class BenefitBenefit(models.Model):
    _name = 'benefit.benefit'

    type_of_benefit = fields.Selection(
    ['Money', 'Own Product', 'Other Product', 'Discount', 'Other'],
    string='Type of Benefit', required=True)
    reason = fields.Char(string='Reason', required=True)
    date = fields.Date(string="Date Given")
    value = fields.Integer(string="Benefit's Value", required=True)
    nationality = fields.Many2one('res.partner', string='Partner', required=True)
