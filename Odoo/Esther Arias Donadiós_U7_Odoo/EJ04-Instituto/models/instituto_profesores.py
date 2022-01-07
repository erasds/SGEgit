# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutoProfesores(models.Model):

    #nombre y descripcion del modelo
    _name = 'instituto.profesores'

    _description = 'Profesores del instituto'

    #Parametros de ordenacion por defecto
    _order = 'nombre_profesor, modulos_profesor'

    #ATRIBUTOS
    _rec_name = 'nombre_profesor'
    # campos para indicar nombre y apellidos del profesor
    nombre_profesor = fields.Char("Nombre")
    apellidos_profesor = fields.Char("Apellidos")
    # campo Many2many donde podremos elegir varios módulos en caso de que el profesor imparta más de una asignatura
    modulos_profesor = fields.Many2many('instituto.modulos', string='Módulos que imparte')