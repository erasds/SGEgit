# -*- coding: utf-8 -*-
from queue import Empty
from odoo import models, fields, api
from odoo.exceptions import ValidationError



#Definimos modelo Delivery Vehículos, que almacenará información de los vehículos
class DeliveryVehiculos(models.Model):

    #Nombre y descripción del modelo
    _name = 'delivery.vehiculos'

    _description = 'Vehículos de la empresa'

    #Parámetros de ordenación por defecto
    _order = 'tipo, modelo'

    #ATRIBUTOS

    # el atributo del que cogerá el nombre
    _rec_name = 'modelo'

    # tipo de vehículo
    tipo = fields.Selection(selection=[
        ('bicicleta', 'Bicicleta'),
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

    # Almacenamos los repartos pendientes, realizados, y en proceso de cada vehículo
    pendientes = fields.One2many('delivery.repartos', 'pendientes', string="Repartos pendientes", 
    domain=[('pendientes', '=', True),
            ('vehiculo', '=', 'modelo')])
    realizados = fields.One2many('delivery.repartos', 'realizados', string="Repartos realizados", 
    domain=[('realizados', '=', True),
            ('vehiculo', '=', 'modelo')])
    en_proceso = fields.Many2one('delivery.repartos', string="Repartos en proceso",
    domain=[('en_proceso', '=', True),
            ('vehiculo', '=', 'modelo')])
    


    # RESTRICCIONES

    #Constraints de SQL del modelo, para controlar que la matrícula sea única
    _sql_constraints = [
        ('matricula_uniq', 'UNIQUE (matricula)', 'La matrícula de los vehículos debe ser única')
    ]

    # Definimos una función para controlar que las bicicletas no tengan matrícula
    @api.constrains('tipo', 'matricula')
    def _check_tipo_vehiculo(self):
        # Recorremos el modelo
        for record in self:
            # si los km son menores que 1 y el vehículo es una furgoneta lanzamos un error
            if record.tipo == 'bicicleta' and record.matricula != False:
                raise models.ValidationError('Las bicicletas no tienen matrícula')