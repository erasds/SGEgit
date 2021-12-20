# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InstitutoProfesores(models.Model):

    #nombre y descripcion del modelo
    _name = 'instituto.profesores'

    _description = 'Profesores del instituto'

    #Parametros de ordenacion por defecto
    _order = 'nombre_profesor, modulos'

    #ATRIBUTOS
    _rec_name = 'combinacion_profesor'

    nombre_profesor = fields.Char("Nombre del profesor")
    apellidos_profesor = fields.Char("Apellidos del profesor")
    modulos_profesor = fields.One2many('instituto.modulos', 'modulo', string='Módulos que imparte')
    combinacion_profesor = fields.Char(string='Combinacion', compute='_compute_fields_combinacion')

    @api.depends('nombre_profesor', 'apellidos_profesor')
    def _compute_fields_combinacion(self):
        for record in self:
            record.combinacion_profesor = record.nombre_profesor + ' ' + record.apellidos_profesor