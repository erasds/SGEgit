# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalDiagnosticos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'hospital.diagnosticos'

    _description = 'Diagnósticos del hospital'

    #Parametros de ordenacion por defecto
    _order = 'num_diagnostico, nombreMedico_ids, nombrePaciente_ids'

    #ATRIBUTOS
    _rec_name = 'num_diagnostico'
    # Definimos una especie de identificador para el diagnóstico
    num_diagnostico = fields.Integer('Número de diagnóstico')
    # campo para referenciar el nombre de los médicos que han realizado el diagnóstico
    nombreMedico_ids = fields.Many2many('hospital.medicos', string="Médico")
    # campo para referenciar los pacientes que han recibido ese diagnóstico
    nombrePaciente_ids = fields.Many2many('hospital.pacientes', string="Paciente")
    # campo para escribir el contenido del diagnóstico
    diagnostico = fields.Html('Diagnóstico', sanitize=True, strip_style=False)

    # definimos la condición de que el número de diagnóstico debe ser único
    _sql_constraints = [
    ('num_diagnostico', 'UNIQUE (num_diagnostico)', 'El número de diagnóstico debe ser único.')
    ]