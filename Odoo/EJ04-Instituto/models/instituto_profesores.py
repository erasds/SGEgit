# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InstitutoProfesores(models.Model):

    #nombre y descripcion del modelo
    _name = 'instituto.profesores'

    _description = 'Profesores del instituto'

    #Parametros de ordenacion por defecto
    _order = 'nombre_profesor, modulos_profesor'

    #ATRIBUTOS
    _rec_name = 'nombre_profesor'

    nombre_profesor = fields.Char("Nombre")
    apellidos_profesor = fields.Char("Apellidos")
    modulos_profesor = fields.One2many('instituto.modulos', 'modulo', string='Módulos que imparte')