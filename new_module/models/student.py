# -*- coding: utf-8 -*-
# _inherit = ['mail.thread', 'mail.activity.mixin']
from odoo import models, fields, _, api
from odoo.exceptions import UserError

class Student(models.Model):
    _name = 'student'
    _description = 'List of student'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Name', tracking=True, placeholder='Name')
    age = fields.Integer('Age', tracking=True, required=True)
    date_birth = fields.Date('Birth Date')
    register_date = fields.Datetime('Register Date')
    value = fields.Float('Value', default=1.0)
    active = fields.Boolean('Active', default=True)
    priority = fields.Selection([('low','Low'), ('medium', 'Medium'), ('high', 'High')], 'Priority', default='medium', tracking=True)
    campo_text = fields.Text('Campo tipo Text')
    photo = fields.Binary('Photo')


    tag_ids = fields.Many2many('student.tags', 'student_tag_rel', 'student_id', 'tag_id', 'Tags') # Parametros Tabla, nombre de la relacion, fk1, fk2, Nombre del string
    class_id = fields.Many2one('class', 'Class #:')  # Parametros:  TABLA , NOMBRE DEL STRING

    score_ids = fields.One2many('score', 'student_id', 'Scores')

    @api.model
    def create(self, vals):
        if vals['age'] and vals['age'] >= 0:
            raise UserError(_('La edad debe ser mayor a 0'))
        return super(Student, self).create(vals)



class Class(models.Model):
    _name = 'class'
    _description = 'Class'

    year = fields.Char('Year')
    capacity = fields.Integer('Capacity')

    student_ids = fields.One2many('student', 'class_id', 'List of Students') # Parametros: Tabla, relacion, Nombre del string


class Tags(models.Model):
    _name = 'student.tags'
    _description = 'Tags'

    name = fields.Char('Name')
    color = fields.Integer('Color', default=1)


    #
    # Many2one
    # One2many
    # Many2many