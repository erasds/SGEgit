# -*- coding: utf-8 -*-
from odoo import models, fields


#Definimos modelo Delivery Clientes, que almacenará información de los clientes
class DeliveryClientes(models.Model):

    #Nombre y descripción del modelo
    _name = 'delivery.clientes'

    _description = 'Clientes de la empresa'

    #Parámetros de ordenación por defecto
    _order = 'nombre', 'apellidos'

    #ATRIBUTOS

    # el atributo del que cogerá el nombre
    _rec_name = 'nombre'

    # nombre del cliente
    nombre = fields.Char("Nombre")
    # apellidos del cliente
    apellidos = fields.Char("Apellidos")
    # dni del cliente, que debe ser único
    dni = fields.Char("DNI")
    # teléfono del cliente
    telf = fields.Integer("Teléfono")
    

    #Constraints de SQL del modelo, para controlar que el dni sea único
    _sql_constraints = [
        ('dni_uniq', 'UNIQUE (dni)', 'El dni del cliente debe ser único')
    ]
