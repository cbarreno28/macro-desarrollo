# -*- coding: utf-8 -*-
{
    'name': "Hospital Manager",
    'summary': "Hospital Manager",
    'author': "Cristina Barreno",
    'depends': ['base', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'data/speciality_data.xml',

        'views/hospital_views.xml',
        'views/doctor_views.xml',
        'views/patient_views.xml',
        'views/admission_views.xml',
        'views/menu_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
   }
