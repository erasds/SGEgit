# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

#Necesario para trabajar con base64
import base64
#Biblioteca para guardar la imagen en memoria antes de pasarla a base64
from io import BytesIO


from PIL import Image
import os
#Bibiliotecas
import barcode
from barcode.writer import ImageWriter

# Clase del controlador web
class GenerarImgPixeles(http.Controller):
    
    '''
    
    Decorador que indica que la url "/generador/numero" atendera por HTTP, sin autentificacion
    Se puede probar accediendo a http://localhost:8069/generadorimagenes/600/600
    Y nos devolvera via web una imagen

    '''

    @http.route('/generadorimagenes/<alto>/<ancho>', auth='public', cors='*', type='http')
    def crearImg(self, alto, ancho, **kw):
        medidas = (alto, ancho)
        img = Image.new('RGB', medidas)
        def ran():
            return os.urandom(alto*ancho)
        pixels = zip(ran(), ran(), ran())
        img.putdata(list(pixels))
        img.show()

        byte_io = BytesIO()
        Image.save(byte_io, 'PNG')
        