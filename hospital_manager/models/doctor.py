# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Model Doctor'

    number = fields.Char('Code')
    name = fields.Char('Name')

    hospital_id = fields.Many2one('hospital', 'Hospital')