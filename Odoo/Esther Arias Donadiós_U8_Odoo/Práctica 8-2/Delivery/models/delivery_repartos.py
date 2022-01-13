# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields


#Definimos modelo Delivery Repartos, que almacenará información de los repartos
class DeliveryRepartos(models.Model):

    #Nombre y descripción del modelo
    _name = 'delivery.repartos'

    _description = 'Repartos de la empresa'

    #Parámetros de ordenación por defecto
    _order = 'codigo', 'estado'

    #ATRIBUTOS

    # el atributo del que cogerá el nombre
    _rec_name = 'codigo'


    # código del reparto, que debe ser único
    codigo = fields.Integer("Código del reparto")

    """ Falta la hora!!! """
    # fecha de inicio del reparto
    f_inicio = fields.Date("Fecha de inicio")
    # fecha de entrega del reparto
    f_entrega = fields.Date("Fecha de entrega")
    # fecha de retorno del vehículo de reparto
    f_retorno = fields.Date("Fecha de retorno")

    km = fields.Integer("Kilómetros del reparto")
    kg = fields.Integer("Peso del paquete")
    volumen = fields.Char("Medidas del paquete")
    observaciones = fields.Html('Observaciones', sanitize=True, strip_style=False)
    estado = fields.Selection(selection=[
        ('procesado', 'Procesado'),
        ('enviado', 'En camino'),
        ('entregado', 'Entregado')
    ], string="Estado del reparto", default='procesado')
    
    # repartidor, a elegir entre los empleados de la empresa con carnet
    repartidor = fields.Many2one('delivery.empleados', string="Repartidor")
    # vehículo, a elegir entre los vehículos de la empresa
    vehiculo = fields.Many2one('delivery.vehiculos', string="Vehículo")

    # cliente que realiza el envío
    emisor = fields.Many2one('delivery.clientes', string="Cliente emisor")
    # cliente que recibe el envío
    receptor = fields.Many2one('delivery.clientes', string="Cliente receptor")
    

    #Constraints de SQL del modelo, para controlar que la matrícula sea única
    _sql_constraints = [
        ('codigo_uniq', 'UNIQUE (codigo)', 'El código de los repartos debe ser único')
    ]

    """ Faltan restricciones de fechas, repartidores y vehículos !!!! """