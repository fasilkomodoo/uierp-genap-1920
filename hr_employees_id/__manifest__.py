# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Employees ID',
	'summary': """ Employees ID """,
    'version': '12.0.1.0.0',
    'category': 'Human Resources',
    'summary': 'Add Employee ID from the company',
    'author': 'Fikri Ahmad',
    'maintainer': 'Fikri Ahmad',
    'description': "",
    'images': [],
    'depends': ['hr'],
    'data': [
        'views/hr_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}