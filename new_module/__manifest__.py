# -*- coding: utf-8 -*-
{
    'name': "Students Manager",
    'summary': "Student Manager",
    'author': "Cristina Barreno",
    'category': 'Stock',
    'depends': ['base', 'contacts', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/student_views.xml',
        'views/class_views.xml',
        'views/res_partner_views.xml',

        'views/menu_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
   }
