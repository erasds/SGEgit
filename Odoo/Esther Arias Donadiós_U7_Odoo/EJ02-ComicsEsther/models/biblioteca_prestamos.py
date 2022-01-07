# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


#Definimos modelo para Préstamos de la biblioteca
class BibliotecaPrestamos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'biblioteca.prestamos'

    _description = 'Préstamos de biblioteca'

    #Parametros de ordenacion por defecto
    _order = 'socio_id, comic_id'

    #ATRIBUTOS

    # atributo del que tomará el nombre
    _rec_name = 'comic_id'

    #Atributo nombre
    comic_id = fields.Many2one('biblioteca.comic', string="Título")
    # Atributo que indica el número del ejemplar
    numeroEjemplar = fields.Integer('Número de ejemplar')
    # Atributo para indicar el nombre del socio que lo tiene alquilado
    socio_id = fields.Many2one('biblioteca.socios', string="Socio")
    # Fecha de inicio del alquiler
    fecha_inicio_prestamo = fields.Date('Fecha inicio')
    # Fecha de fin del alquiler
    fecha_fin_prestamo = fields.Date('Fecha fin')

    # Definimos una función para controlar las condiciones de las fechas
    @api.constrains('fecha_inicio_prestamo', 'fecha_fin_prestamo')
    def _check_prestamo_date(self):
        # Recorremos el modelo
        for record in self:
            # Comprobamos que la fecha de inicio no sea posterior a la de hoy
            if record.fecha_inicio_prestamo > fields.Date.today():
                raise models.ValidationError('La fecha de inicio del alquiler no puede ser posterior a la fecha actual')
            # que la fecha de inicio no sea posterior a la fecha de fin
            elif record.fecha_inicio_prestamo > record.fecha_fin_prestamo :
                raise models.ValidationError('La fecha de inicio del alquiler no puede ser posterior a la fecha de finalización')
            # y que la fecha de fin no sea anterior a hoy
            elif record.fecha_fin_prestamo < fields.Date.today():
                raise models.ValidationError('La fecha fin del alquiler no puede ser anterior a la fecha actual')