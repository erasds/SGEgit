# -*- coding: utf-8 -*-

from odoo import models, fields, api


class InstitutoAlumnos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'instituto.alumnos'

    _description = 'Alumnos matriculados en el instituto'

    #Parametros de ordenacion por defecto
    _order = 'nombre_alumno, modulos_alumno'

    #ATRIBUTOS
    _rec_name = 'nombre_alumno'
    # campos para definir el nombre y apellidos del alumno
    nombre_alumno = fields.Char("Nombre")
    apellidos_alumno = fields.Char("Apellidos")
    # campo many2many donde podemos elegir todos los módulos en los que esté matriculado el alumno
    modulos_alumno = fields.Many2many('instituto.modulos', string='Módulos en los que se ha matriculado')
