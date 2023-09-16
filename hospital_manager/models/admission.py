# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class Admission(models.Model):
    _name = 'admission'
    _description = 'Model Admission'

    sequence = fields.Char('No.')
    date = fields.Date('Date')
    patient_number = fields.Char('Patient Identification')
    patient_id = fields.Many2one('patient', 'Patient')
    area = fields.Selection([('emergency', 'Emergency'), ('internal', 'Internal')], 'Area', default='emergency')
    speciality_id = fields.Many2one('doctor.speciality', 'Speciality')
    symptoms = fields.Text('Symptoms')

    @api.onchange('patient_number')
    def onchange_patient_number(self):
        if self.patient_number:
            patient_id = self.env['patient'].search([('number', '=', self.patient_number)], limit=1)
            print(patient_id)
            if patient_id:
                self.patient_id = patient_id.id
            else:
                self.patient_id = False

    @api.onchange('area')
    def onchange_area(self):
        # Forma 1: Buscarlo por External ID
        # if self.area == 'emergency':
        #     speciality_id = self.env.ref('hospital_manager.speciality_07')
        #     if speciality_id:
        #         self.speciality_id = speciality_id.id

        # Forma 2: Buscarlo por codigo
        if self.area == 'emergency':
            speciality_id = self.env['doctor.speciality'].search([('code', '=', '001')])
            if speciality_id:
                self.speciality_id = speciality_id.id
            else:
                self.speciality_id = False
        else:
            self.speciality_id = False

    @api.model
    def create(self, vals):
        if vals['area'] == 'emergency':
            vals['sequence'] = self.env['ir.sequence'].next_by_code('adm.emergency')
        else:
            vals['sequence'] = self.env['ir.sequence'].next_by_code('adm.internal')
        return super(Admission, self).create(vals)

    # Todos los pacientes
    # patient_id = self.env['patient'].search([])
    # patient_id = self.env['patient'].search([], limit=1)
    # Todos los pacientes que coinciden con el campo patient_number y un limite = 1