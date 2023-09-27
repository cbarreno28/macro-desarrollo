# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class Patient(models.Model):
    _inherit = 'res.partner'

    patient_type = fields.Selection([('iess', 'IEES'),
                                     ('private', 'Private'),
                                     ('no_suscription', 'No Suscription')], 'Suscription', default='no_suscription')
    date_birth = fields.Date('Date Birth')
    is_patient = fields.Boolean('Is Patient?')

