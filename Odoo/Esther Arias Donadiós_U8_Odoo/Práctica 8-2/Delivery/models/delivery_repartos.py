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
    _order = 'f_entrega, urgencia'

    #ATRIBUTOS

    # el atributo del que cogerá el nombre
    _rec_name = 'codigo'


    # código del reparto, que será único e irá incrementando automáticamente
    codigo = fields.Integer(string="Código del reparto", default=lambda self:
    self.env['ir.sequence'].next_by_code('delivery.repartos'))


    # fecha y hora de inicio del reparto
    f_inicio = fields.Datetime(default= lambda s: fields.Datetime.now(), string="Fecha de inicio")
    # fecha de entrega del reparto
    f_entrega = fields.Datetime("Fecha de entrega")
    # fecha de retorno del vehículo de reparto
    f_retorno = fields.Datetime("Fecha de retorno")

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

    # Añadimos unos campos para clasificar los pedidos como pendientes, realizados o en proceso
    pendientes = fields.Boolean(compute="_value_pendientes", store=True)
    realizados = fields.Boolean(compute="_value_realizados", store=True)
    en_proceso = fields.Boolean(compute="_value_en_proceso", store=True)
    
    # repartidor, a elegir entre los empleados de la empresa con carnet
    repartidor = fields.Many2one('delivery.empleados', string="Repartidor")
    # vehículo, a elegir entre los vehículos de la empresa
    vehiculo = fields.Many2one('delivery.vehiculos', string="Vehículo")

    # cliente que realiza el envío
    emisor = fields.Many2one('delivery.clientes', string="Cliente emisor")
    # cliente que recibe el envío
    receptor = fields.Many2one('delivery.clientes', string="Cliente receptor")



    # RESTRICCIONES

    # Definimos una función para controlar las condiciones de las fechas
    @api.constrains('f_inicio', 'f_entrega', 'f_retorno')
    def _check_reparto_date(self):
        # Recorremos el modelo
        for record in self:
            # comprobamos que la fecha de inicio no sea posterior a la fecha de fin del reparto
            if record.f_inicio > record.f_retorno:
                raise models.ValidationError('La fecha de inicio del reparto no puede ser posterior a la fecha de retorno')
            # y que la fecha de entrega no sea anterior a la de inicio, ni posterior a la de retorno
            if record.f_retorno < record.f_entrega < record.f_inicio:
                raise models.ValidationError('La fecha de entrega no puede ser anterior a la de inicio, ni posterior a la de retorno')
    
    # Definimos una función para controlar que los repartos de pocos km no se hagan en furgoneta,
    # ni los de muchos km en bicicleta
    @api.constrains('km', 'vehiculo')
    def _check_reparto_km(self):
        # Recorremos el modelo
        for record in self:
            # si los km son menores que 1 y el vehículo es una furgoneta lanzamos un error
            if record.km < 1 and record.vehiculo == 'furgoneta':
                raise models.ValidationError('Los repartos de menos de 1 Km no se pueden realizar en furgoneta')
            if record.km > 10 and record.vehiculo == 'bicicleta':
                raise models.ValidationError('Los repartos de más de 10 km no se pueden realizar en bicicleta')



    # MÉTODOS

    @api.depends('f_inicio')
    #Función para calcular el valor de pendientes.
    def _value_pendientes(self):
        # Almacenamos la fecha actual en la variable today
        today = fields.Datetime.now()
        #Para cada registro...
        for record in self:
            # Si el campo f_inicio no está vacío
            if record.f_inicio is not None:
                # Si la fecha actual es anterior a la fecha de inicio es que está pendiente
                if record.f_inicio > today:
                    record.pendientes = True
                else:
                    record.pendientes = False
            else:
                record.pendientes = False

    @api.depends('f_retorno')
    #Función para calcular el valor de realizados.
    def _value_realizados(self):
        # Almacenamos la fecha actual en la variable today
        today = fields.Datetime.now()
        #Para cada registro...
        for record in self:
            # Si el campo f_retorno no está vacío
            if record.f_retorno is not None:
                # Si la fecha actual es posterior a la fecha de retorno es que está realizado
                if record.f_retorno < today:
                    record.realizados = True
                else:
                    record.realizados = False
            else:
                record.realizados = False

    @api.depends('f_inicio', 'f_retorno')
    #Función para calcular el valor de en_proceso.
    def _value_en_proceso(self):
        # Almacenamos la fecha actual en la variable today
        today = fields.Datetime.now()
        #Para cada registro...
        for record in self:
            # Si los campos f_inicio y f_retorno no están vacíos
            if record.f_inicio is not None and record.f_retorno is not None:
                # Si la fecha actual es posterior a la fecha de inicio y anterior a la de retorno es que está en proceso
                if record.f_inicio < today < record.f_retorno:
                    record.en_proceso = True
                else:
                    record.en_proceso = False
            else:
                record.en_proceso = False
