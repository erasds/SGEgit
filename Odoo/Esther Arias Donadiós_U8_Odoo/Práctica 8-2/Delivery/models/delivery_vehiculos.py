# -*- coding: utf-8 -*-
from odoo import models, fields


#Definimos modelo Delivery Vehículos, que almacenará información de los vehículos
class DeliveryVehiculos(models.Model):

    #Nombre y descripción del modelo
    _name = 'delivery.vehiculos'

    _description = 'Vehículos de la empresa'

    #Parámetros de ordenación por defecto
    _order = 'tipo', 'modelo'

    #ATRIBUTOS

    # el atributo del que cogerá el nombre
    _rec_name = 'modelo'

    # tipo de vehículo
    tipo = fields.Selection(selection=[
        ('moto', 'Moto'),
        ('furgoneta', 'Furgoneta')
    ], string="Tipo de vehículo", default='furgoneta')
    # modelo del vehículo
    modelo = fields.Char("Modelo")
    # matrícula del vehículo
    matricula = fields.Char("Matrícula")
    # foto del vehículo
    foto = fields.Image('Avatar', max_width=200,max_height=200)
    # descripción del vehículo
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
    

    #Constraints de SQL del modelo, para controlar que la matrícula sea única
    _sql_constraints = [
        ('matricula_uniq', 'UNIQUE (matricula)', 'La matrícula de los vehículos debe ser única')
    ]
