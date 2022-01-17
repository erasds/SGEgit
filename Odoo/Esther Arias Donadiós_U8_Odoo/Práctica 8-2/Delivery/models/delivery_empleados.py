# -*- coding: utf-8 -*-
from odoo import models, fields


#Definimos modelo Delivery Empleados, que almacenará información de los empleados
class DeliveryEmpleados(models.Model):

    #Nombre y descripción del modelo
    _name = 'delivery.empleados'

    _description = 'Empleados de la empresa'

    #Parámetros de ordenación por defecto
    _order = 'nombre', 'apellidos'

    #ATRIBUTOS

    # el atributo del que cogerá el nombre
    _rec_name = 'nombre'

    # nombre del empleado
    nombre = fields.Char("Nombre")
    # apellidos del empleado
    apellidos = fields.Char("Apellidos")
    # dni del empleado, que debe ser único
    dni = fields.Char("DNI")
    # teléfono del empleado
    telf = fields.Integer("Teléfono")
    # carnet del empleado donde podemos seleccionar entre varias opciones
    carnet = fields.Selection(selection=[
        ('moto', 'Carnet de moto'),
        ('furgoneta', 'Carnet de furgoneta'),
        ('ambos', 'Carnet de moto y furgoneta'),
        ('ninguno', 'No tiene carnet')
    ], string="Tipo de carnet", default='ninguno')
    #Dato binario, para guardar un binario (en la vista indicaremos que es una imagen) con la foto del empleado
    foto = fields.Image('Avatar', max_width=200,max_height=200)

    # Almacenamos los repartos pendientes, realizados, y en proceso de cada empleado
    pendientes = fields.One2many('delivery.repartos', 'pendientes', string="Repartos pendientes", 
    domain=[('pendientes', '=', True),
            ('repartidor', '=', 'nombre')])
    realizados = fields.One2many('delivery.repartos', 'realizados', string="Repartos realizados", 
    domain=[('realizados', '=', True),
            ('repartidor', '=', 'nombre')])
    en_proceso = fields.Many2one('delivery.repartos', string="Repartos en proceso",
    domain=[('en_proceso', '=', True),
            ('repartidor', '=', 'nombre')])

    #Constraints de SQL del modelo, para controlar que el dni sea único
    _sql_constraints = [
        ('dni_uniq', 'UNIQUE (dni)', 'El dni del empleado debe ser único')
    ]
