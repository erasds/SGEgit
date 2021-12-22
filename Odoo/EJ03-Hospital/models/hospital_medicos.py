# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Modelo base, creado como modelo abstracto 
class BaseArchive(models.AbstractModel):
    #Nombre y descripcion del modelo
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    #Introduce el atributo "Activo"
    activo = fields.Boolean(default=True)

    #Introducice metodo "archivar" que invierte el estado de "activo"
    def archivar(self):
        #Por cada registro del modelo
        for record in self:
            #Cambiamos el valor de activo a su version negada
            record.activo = not record.activo


#Definimos modelo Médicos
class HospitalMedicos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'hospital.medicos'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    _inherit = ['base.archive']

    _description = 'Medicos del hospital'

    #Parametros de ordenacion por defecto
    _order = 'nColegiado, nombre'

    #ATRIBUTOS
    _rec_name = 'nombre'
    #Atributo nombre
    nombre = fields.Char('Nombre')
    #Atributo para seleccionar entre varios
    apellidos = fields.Char('Apellidos')
    # Atributo que indica el numero de colegiado
    nColegiado = fields.Integer('Número de colegiado')

    #Constraints de SQL del modelo que indica que el número de colegiado debe ser único
    _sql_constraints = [
        ('nColegiado_uniq', 'UNIQUE (nColegiado)', 'El número de colegiado debe ser único.')
    ]


