# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

# Clase del controlador web
class ControladorWebEstadoRepartos(http.Controller):
    #Decorador que indica que la url "/seguimiento/<codigo>" atendera por HTTP
    #Devolvera texto que estará en formato html
    #Se puede probar accediendo a http://localhost:8069/seguimiento/<codigo>
    @http.route('/seguimiento/<codigo>', auth='user', type='http')
    def estado_repartos(self, codigo, **kw):
        # Primero obtenemos los registros de repartos
        repartos = request.env['liga.repartos'].sudo().search([])
        #Recorro los repartos
        for record in repartos:
            #Si el código del reparto coincide con el código introducido en el web controller
            if record.codigo == codigo:
                # almacenamos el estado del reparto en una variable
                estado = str(record.estado)
        # definimos el contenido de la página
        # (en este caso debe mostrar el estado del reparto seleccionado)
        contenido="<html><body><p align='center'><b>Estado del reparto:</p><h1 align='center'>"+estado+"</h1></body></html>"
        return contenido