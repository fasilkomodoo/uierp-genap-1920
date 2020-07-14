# -*- coding: utf-8 -*-
{
    'name': "Point of Sale User List & Status",

    'summary': """Track users and point of sale status""",

    'description': """This module helps users to track the users and status of the available point of sale configurations""",

    'author': "Teuku M. Farhan S.",
    'website': "http://www.medium.com/@scoobydoo.uierp1",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Point of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'views/posul.xml'
    ],
    # only loaded in demonstration mode
    'demo': [],
    'images': ['static/description/clipboard.png'],
}