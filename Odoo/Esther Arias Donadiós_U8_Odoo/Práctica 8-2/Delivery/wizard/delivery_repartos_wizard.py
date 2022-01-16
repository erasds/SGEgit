# -*- coding: utf-8 -*-
from odoo import models, fields, api

#Esta clase observamos que hereda de "models.TransientModel" una clase especial
#que crea un modelo, pero es temporal y no hacer permanente sus datos en la base de datos.
#Se utiliza para "mientras dura el Wizard"
class DeliveryRepartosWizard(models.TransientModel):
    _name = 'delivery.repartos.wizard'
    #Campos del modelo que usaremos en el Wizard
    codigo = fields.Char('Código del reparto', default='/')
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

    # MÉTODOS

    # on create method
    @api.model
    def create(self, vals):
        obj = super(DeliveryRepartosWizard, self).create(vals)
        if obj.codigo == '/':
            number = self.env['ir.sequence'].get('delivery.repartos.wizard.codigo') or '/'
            obj.write({'codigo': number})
        return obj
        
    
    # on button click event
    @api.one
    def submit_application(self):
        if self.codigo == '/':
            sequence_id = self.env['ir.sequence'].search([('code', '=', 'delivery.repartos.wizard.codigo')])
            sequence_pool = self.env['ir.sequence']
            codigo = sequence_pool.sudo().get_id(sequence_id.id)
            self.write({'codigo': codigo})
