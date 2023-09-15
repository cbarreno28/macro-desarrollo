# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class Score(models.Model):
    _name = 'score'
    _description = 'List of score'

    value_1 = fields.Float('Value 1')
    value_2 = fields.Float('Value 2')
    value_3 = fields.Float('Value 3')
    total = fields.Float('Total', compute='calculate_total', store=True)
    total_lbl = fields.Char('TL', compute='calculate_total')

    student_id = fields.Many2one('student', 'Student')

    @api.depends('value_1', 'value_2', 'value_3')
    def calculate_total(self):
        for record in self:
            # record.value_3 = 3
            record.total = (record.value_1 + record.value_2 + record.value_3) / 3
            record.total_lbl = 'new label'



