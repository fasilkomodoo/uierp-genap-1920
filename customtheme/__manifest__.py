# -*- coding: utf-8 -*-
{
    'name': "Custom Theme",

    'summary': """
        Custom Theme
        """,

    'author': "Steffi Alexandra",
    'category': 'Themes',
    'version': '1.0',
    'license': 'LGPL-3',
    'support': 'zamalabdulhalim@gmail.com',
    'images': ['static/description/banner1.png'],

    'depends': ['web'],

    # always loaded
    'data': [
        'view/customtheme.xml',
    ],

    'installable' : True,
    'application' : True,

}