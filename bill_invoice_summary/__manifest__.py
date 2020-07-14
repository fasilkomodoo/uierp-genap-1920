# -*- coding: utf-8 -*-
{
    'name': "Overdue Summary",

    'summary': """
       Modul for summarize your customer invoice and vendor bill that has been overdue""",

    'description': """
        Until now, we dont have any explanation about this module. This module developed by Bintang Ilham Syahputra.
    """,

    'author': "Bintang Ilham Syahputra",
    'website': "https://github.com/BintangIlhamSy",
    'maintainer': 'Bintang Ilham Syahputra',
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account','om_account_accountant'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/summary_invoice_bill.xml',
        'data/initial.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable' : True,
    'application': True,
}