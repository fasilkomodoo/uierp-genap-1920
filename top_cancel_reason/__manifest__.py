# -*- coding: utf-8 -*-
{
    'name': "CANCEL REASON V2",

    'summary': """
      COBA LAGI NIH""",

    'description': """
    """,

    'author': "FADLI",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/menu_sales_view.xml',
        'views/top_cancel_reason_view.xml',
        'wizard/menu_top_selling_product_view.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}