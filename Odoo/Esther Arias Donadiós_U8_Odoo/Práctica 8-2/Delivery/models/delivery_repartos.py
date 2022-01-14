# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


#Definimos modelo Delivery Repartos, que almacenará información de los repartos
class DeliveryRepartos(models.Model):

    #Nombre y descripción del modelo
    _name = 'delivery.repartos'

    _description = 'Repartos de la empresa'

    #Parámetros de ordenación por defecto
    _order = 'f_entrega', 'urgencia'

    #ATRIBUTOS

    # el atributo del que cogerá el nombre
    _rec_name = 'codigo'


    # código del reparto, que será único e irá incrementando automáticamente
    codigo = fields.Char('Código del reparto', default='/')


    """ Falta la hora!!! """
    # fecha de inicio del reparto
    f_inicio = fields.Date("Fecha de inicio")
    # fecha de entrega del reparto
    f_entrega = fields.Date("Fecha de entrega")
    # fecha de retorno del vehículo de reparto
    f_retorno = fields.Date("Fecha de retorno")

    km = fields.Float("Kilómetros del reparto")
    kg = fields.Float("Peso del paquete")
    volumen = fields.Char("Medidas del paquete")
    urgencia = fields.Selection(selection=[
        ('organos', 'Órganos humanos'),
        ('refrigerados', 'Alimentos refrigerados'),
        ('alimentos', 'Alimentos'),
        ('alta_prioridad', 'Alta prioridad'),
        ('baja_prioridad', 'Baja prioridad')
    ], string="Urgencia del reparto", default='baja_prioridad')
    observaciones = fields.Html('Observaciones', sanitize=True, strip_style=False)
    estado = fields.Selection(selection=[
        ('procesado', 'Procesado'),
        ('enviado', 'En camino'),
        ('entregado', 'Entregado')
    ], string="Estado del reparto", default='procesado')
    
    # repartidor, a elegir entre los empleados de la empresa con carnet
    repartidor = fields.Many2one('delivery.empleados', string="Repartidor", 
    domain=[('moto', '=', True),
            ('furgoneta', '=', True),
            ('ambos', '=', True)]
    )
    # vehículo, a elegir entre los vehículos de la empresa
    vehiculo = fields.Many2one('delivery.vehiculos', string="Vehículo")

    # cliente que realiza el envío
    emisor = fields.Many2one('delivery.clientes', string="Cliente emisor")
    # cliente que recibe el envío
    receptor = fields.Many2one('delivery.clientes', string="Cliente receptor")

    # RESTRICCIONES

    """ Faltan restricciones de repartidores y vehículos !!!! """
    # Definimos una función para controlar las condiciones de las fechas
    @api.constrains('f_inicio', 'f_entrega', 'f_retorno')
    def _check_reparto_date(self):
        # Recorremos el modelo
        for record in self:
            """ Dejar solo el 2o if??. REVISAR!!! """
            # comprobamos que la fecha de inicio no sea posterior a la fecha de fin del reparto
            if record.f_inicio > record.f_retorno :
                raise models.ValidationError('La fecha de inicio del reparto no puede ser posterior a la fecha de retorno')
            # y que la fecha de entrega no sea anterior a la de inicio, ni posterior a la de retorno
            if record.f_retorno < record.f_entrega < record.f_inicio:
                raise models.ValidationError('La fecha de entrega no puede ser anterior a la de inicio, ni posterior a la de retorno')
    
    # Definimos una función para controlar que los repartos de pocos km no se hagan en furgoneta
    @api.constrains('km', 'vehiculo')
    def _check_reparto_km(self):
        # Recorremos el modelo
        for record in self:
            # si los km son menores que 1 y el vehículo es una furgoneta lanzamos un error
            if record.km < 1 and record.vehiculo == 'furgoneta':
                raise models.ValidationError('Los repartos de menos de 1 Km no se pueden realizar en furgoneta')

    """ si un repartidor ya está en reparto no puedes volver a seleccionarlo... """
    """ si el vehiculo ya está en reparto no puedes volver a seleccionarlo... """


    # MÉTODOS

    # on create method
    @api.model
    def create(self, vals):
        obj = super(DeliveryRepartos, self).create(vals)
        if obj.codigo == '/':
            number = self.env['ir.sequence'].get('delivery.repartos.codigo') or '/'
            obj.write({'codigo': number})
        return obj
        
    
    # on button click event
    @api.one
    def submit_application(self):
        if self.codigo == '/':
            sequence_id = self.env['ir.sequence'].search([('code', '=', 'delivery.repartos.codigo')])
            sequence_pool = self.env['ir.sequence']
            codigo = sequence_pool.sudo().get_id(sequence_id.id)
            self.write({'codigo': codigo})
