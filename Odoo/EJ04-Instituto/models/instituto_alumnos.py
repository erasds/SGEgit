# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InstitutoAlumnos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'instituto.alumnos'

    _description = 'Alumnos matriculados en el instituto'

    #Parametros de ordenacion por defecto
    _order = 'nombre_alumno, modulos_alumno'

    #ATRIBUTOS
    _rec_name = 'combinacion'

    nombre_alumno = fields.Char("Nombre del alumno")
    apellidos_alumno = fields.Char("Apellidos del alumno")
    modulos_alumno = fields.Many2many('instituto.modulos', string='Módulos en los que se ha matriculado')
    combinacion = fields.Char(string='Combinacion', compute='_compute_fields_combinacion')

    @api.depends('nombre_alumno', 'apellidos_alumno')
    def _compute_fields_combinacion(self):
        for record in self:
            record.combinacion = record.nombre_alumno + ' ' + record.apellidos_alumno