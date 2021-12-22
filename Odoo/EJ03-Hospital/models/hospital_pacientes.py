from odoo import models, fields, api    

class HospitalPacientes(models.Model):
    #Nombre y descripción del modelo
    _name = 'hospital.pacientes'

    _description = 'Pacientes del hospital'

    #Parametros de ordenación por defecto
    _order = 'apellidos, nombre'

    #ATRIBUTOS
    _rec_name = 'nombre'
    # campos para definir nombre y apellidos del paciente
    nombre = fields.Char("Nombre")
    apellidos = fields.Char("Apellidos")
    #Campo con HTML (Sanitizado) donde se guardan los síntomas
    sintomas = fields.Html('Síntomas', sanitize=True, strip_style=False)