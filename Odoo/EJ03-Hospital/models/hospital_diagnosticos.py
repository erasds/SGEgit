# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class HospitalDiagnosticos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'hospital.diagnosticos'

    _description = 'Diagnósticos del hospital'

    #Parametros de ordenacion por defecto
    _order = 'nombreMedico_ids, nombrePaciente_ids'

    #ATRIBUTOS
    _rec_name = 'nombreMedico_ids'

    nombreMedico_ids = fields.Many2many('hospital.medicos', string="Médico")
    nombrePaciente_ids = fields.Many2many('hospital.pacientes', string="Paciente")
    diagnostico = fields.Html('Diagnóstico', sanitize=True, strip_style=False)