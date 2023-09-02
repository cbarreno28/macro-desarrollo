# -*- coding: utf-8 -*-

from odoo import models, fields, _, api


class Student(models.Model):
    _name = 'student'
    _description = 'List of student'
 # _inherit = ''

    name = fields.Char('Name')
    age = fields.Integer('Age')
    date_birth = fields.Date('Birth Date')
    register_date = fields.Datetime('Register Date')
    value = fields.Float('Value')
    active = fields.Boolean('Active')

    tag_ids = fields.Many2many('student.tags', 'student_tag_rel', 'student_id', 'tag_id', 'Tags') # Parametros Tabla, nombre de la relacion, fk1, fk2, Nombre del string

    class_id = fields.Many2one('class', 'Class #:')  # Parametros:  TABLA , NOMBRE DEL STRING


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