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
    num_diagnostico = fields.Integer('Número de diagnóstico')
    nombreMedico_ids = fields.Many2many('hospital.medicos', string="Médico")
    nombrePaciente_ids = fields.Many2many('hospital.pacientes', string="Paciente")
    diagnostico = fields.Html('Diagnóstico', sanitize=True, strip_style=False)

    _sql_constraints = [
    ('num_diagnostico', 'UNIQUE (num_diagnostico)', 'El número de diagnóstico debe ser único.')
    ]