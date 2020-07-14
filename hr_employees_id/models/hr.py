# -*- coding: utf-8 -*-
# Part of Odoo. See COPYRIGHT & LICENSE files for full copyright and licensing details.

from odoo import models, fields, api, _


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    company_employee_id = fields.Char('Employee ID')
