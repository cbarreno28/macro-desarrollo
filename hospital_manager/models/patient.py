# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class Patient(models.Model):
    _name = 'patient'
    _description = 'Model Patient'

    number = fields.Char('Number')
    name = fields.Char('Name')
    address = fields.Char('Address')
    country_id = fields.Many2one('res.country', 'Country')
    city_id = fields.Many2one('res.city', 'City')
    email = fields.Char('Email')
    phone = fields.Char('Phone')
    type = fields.Selection([('iess', 'IEES'),
                             ('private', 'Private'),
                             ('no_suscription', 'Suscription')], 'Suscription', default='no_suscription')
    active = fields.Boolean('Active', default=True)
    date_birth = fields.Date('Date Birth')