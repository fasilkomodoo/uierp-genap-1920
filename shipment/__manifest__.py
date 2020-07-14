# -*- coding: utf-8 -*-
{
    'name': "Shipment",

    'summary': """Shipping Plan""",

    'description': """This module helps company to track shipping plan after payment receipt""",

    'author': "Brian Estadimas",
    'website': "http://www.medium.com/@sandyuierp1",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Purchases',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'purchase'],

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