# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

# Clase del controlador web
class ControladorWebBorrarEmpates(http.Controller):
    #Decorador que indica que la url "/eliminarempates" atendera por HTTP
    #Devolvera texto que estará en formato html
    #Se puede probar accediendo a http://localhost:8069/eliminarempates
    @http.route('/eliminarempates', auth='user', type='http')
    def elimina_empates(self):
        # Primero obtenemos los registros de partidos (modelo liga.partido)
        partidos = request.env['liga.partido'].sudo().search([])
        # Creamos una variable para que sume los partidos eliminados
        eliminado = 0
        #Recorro los partidos
        for record in partidos:
            #Si han empatado
            if record.goles_casa == record.goles_fuera:
                #Elimino el registro y lo sumo al contador
                record.unlink()
                eliminado += 1
        # definimos el contenido de la página
        # (en este caso debe mostrar la cantidad de partidos eliminados)
        contenido="<html><body><p align='center'><b>Partidos eliminados:</p><h1 align='center' style='color:red'>"+str(eliminado)+"</h1></body></html>"
        return contenido

