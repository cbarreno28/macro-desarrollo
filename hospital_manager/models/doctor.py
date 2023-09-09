# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class Doctor(models.Model):
    _name = 'doctor'
    _description = 'Model Doctor'

    number = fields.Char('Code')
    name = fields.Char('Name')

    speciality_id = fields.Many2one('doctor.speciality', 'Speciality')
    hospital_id = fields.Many2one('hospital', 'Hospital')


class DoctorSpeciality(models.Model):
    _name = 'doctor.speciality'

    name = fields.Char('Name')