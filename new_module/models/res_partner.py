# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    student_id = fields.Many2one('student', 'Student')