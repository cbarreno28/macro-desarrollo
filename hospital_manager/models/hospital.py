# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Hospital(models.Model):
    _name = 'hospital'
    _description = 'Model Hospital'

    # code = fields.Char(string='Code')
    code = fields.Char('Code')
    name = fields.Char('Name')

    doctor_ids = fields.One2many('doctor', 'hospital_id', 'Doctors')

    def action_admission(self):
        action = self.env['ir.actions.actions']._for_xml_id('hospital_manager.admission_action')
        action['domain'] = [('hospital_id', '=', self.id)]
        action['context'] = {'default_hospital_id': self.id}
        return action

    def initializate_doctors(self):
        speciality_id = self.env['doctor.speciality'].search([('code', '=', '001')])
        if speciality_id:
            # hospital= self.env['hospital'].create({
            #     'name': 'Hospital',
            #     'code': '001',
            #     'doctor_ids': [(0, 0, {'number': '0003', 'name': 'Cristina 1', 'speciality_id': speciality_id.id}),
            #                    (0, 0, {'number': '0004', 'name': 'Cristina 2', 'speciality_id': speciality_id.id}),
            #                    (0, 0, {'number': '0005', 'name': 'Cristina 3', 'speciality_id': speciality_id.id})]})

            hospital = self.env['hospital'].create({'name': 'Hospital #2', 'code': '001',
                                                    'doctor_ids': [(4, 1)]})
            print(hospital)

