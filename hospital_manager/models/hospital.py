# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Hospital(models.Model):
    _name = 'hospital'
    _description = 'Model Hospital'

    # code = fields.Char(string='Code')
    code = fields.Char('Code')
    name = fields.Char('Name')

    doctor_ids = fields.One2many('doctor', 'hospital_id', 'Doctors')