# -*- coding: utf-8 -*-

from odoo import models, fields

class StudentStudent(models.Model):
	_name = 'student.student'

	name = fields.Char(string='Name', required=True)
	reason = fields.Char(string='Reason', required=True)