# -*- coding: utf-8 -*-
{
    'name': "Hospital Manager",
    'summary': "Hospital Manager",
    'author': "Cristina Barreno",
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',

        'views/hospital_views.xml',
        'views/menu_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
   }
