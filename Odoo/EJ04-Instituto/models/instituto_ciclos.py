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


#Definimos modelo Ciclos
class InstitutoCiclos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'instituto.ciclos'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    _inherit = ['base.archive']

    _description = 'Ciclos formativos del instituto'

    #Parametros de ordenacion por defecto
    _order = 'ciclo'

    #ATRIBUTOS
    _rec_name = 'ciclo'
    #Atributo nombre
    ciclo = fields.Char('Ciclo formativo')
    #Atributo para seleccionar entre varios
    modulos_ciclo = fields.Many2many('instituto.modulos', string='Módulos')

