# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Esta clase observamos que hereda de "models.TransientModel" una clase especial
#que crea un modelo, pero es temporal y no hacer permanente sus datos en la base de datos.
#Se utiliza para "mientras dura el Wizard"
class DeliveryRepartosWizard(models.TransientModel):
    _name = 'delivery.repartos.wizard'
    #Campos del modelo que usaremos en el Wizard
    codigo = fields.Integer(string="Código del reparto", default=lambda self:
    self.env['ir.sequence'].next_by_code('delivery.repartos.wizard'))
    observaciones = fields.Html('Descripción', sanitize=True, strip_style=False)
    repartidor = fields.Many2one('delivery.empleados', string="Repartidor", 
    domain=[('moto', '=', True),
            ('furgoneta', '=', True),
            ('ambos', '=', True)]
    )
    vehiculo = fields.Many2one('delivery.vehiculos', string="Vehículo")
    emisor = fields.Many2one('delivery.clientes', string="Cliente emisor")
    receptor = fields.Many2one('delivery.clientes', string="Cliente receptor")

    #Funcion que se llamará desde el Wizard, para utilizar este modelo temporal
    #y con él crear un nuevo registro en el modelo destino
    def add_delivery_repartos(self):
        # Obtenemos referencia al modelo destino
        DeliveryRepartosModel = self.env['delivery.repartos']
        # Lo recorremos
        for wiz in self:
            # Por cada elemento
            # Creamos un registro en "delivery.repartos"
            DeliveryRepartosModel.create({
                'codigo': wiz.codigo,
                'observaciones': wiz.observaciones,
                'repartidor': wiz.repartidor,
                'vehiculo': wiz.vehiculo,
                'emisor': wiz.emisor,
                'receptor': wiz.receptor
            })
