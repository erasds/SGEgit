# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError


# Modelo base, creado como modelo abstracto 
# Este modelo lo heredarara el modelo BibliotecaComic
class BaseArchive(models.AbstractModel):
    #Nombre y descripcion del modelo
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    #Introduce el atributo "Activo"
    activo = fields.Boolean(default=True)

    #Introduce metodo "archivar" que invierte el estado de "activo"
    def archivar(self):
        #Por cada registro del modelo
        for record in self:
            #Cambiamos el valor de activo a su version negada
            record.activo = not record.activo


#Definimos modelo Biblioteca comic
class BibliotecaComic(models.Model):

    #Nombre y descripcion del modelo
    _name = 'biblioteca.comic'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    _inherit = ['base.archive']

    _description = 'Comic de biblioteca'

    #Parametros de ordenacion por defecto
    _order = 'fecha_publicacion desc, nombre_ids'

    #ATRIBUTOS

    #Indicamos que atributo sera el que se usara para mostrar nombre.
    _rec_name = 'nombre_ids'

    #Atributo nombre
    nombre_ids = fields.Char('Titulo', required=True, index=True)
    #Atributo para seleccionar entre varios
    estado = fields.Selection(
        [('borrador', 'No disponible'),
         ('disponible', 'Disponible'),
         ('perdido', 'Perdido')],
        'Estado', default="borrador")
    #Campo con HTML (Sanitizado) donde se guarda la descripción del comic
    descripcion = fields.Html('Descripción', sanitize=True, strip_style=False)
    #Dato binario, para guardar un binario (en la vista indicaremos que es una imagen) con la portada del comic
    portada = fields.Image('Portada Comic', max_width=200,max_height=200)

    #Fecha de publicación
    fecha_publicacion = fields.Date('Fecha publicación')

    #Precio del libro    
    precio = fields.Float('Precio')
    #Numero de paginas. 
    paginas = fields.Integer('Numero de páginas',
        #Hace que este atributo este disponible para este grupo de seguridad 
        #Que en este caso son todos los usuarios
        groups='base.group_user',
        #Establece que si el estado es perdido, el numero de paginas no se puede cambiar
        estados={'perdido': [('readonly', True)]},
        #Texto a mostrar en la ayuda de la interfaz al dejar el ratón encima
        help='Total numero de paginas',
        #Si se pone a true, indica que si este atributo se aplica a distintas empresas en Odoo
        #para cada empresa ponga un valor distinto
        company_dependent=False)
 
    #Valoración lector, indicando como son los datos
    valoracion_lector = fields.Float(
        'Valoración media lectores',
        digits=(14, 4),
    )

    ejemplares = fields.Integer('Número de ejemplares')

    # Relación muchos a muchos de autores utilizando un "partner"
    # de Odoo (Es un elemento que puede ser empresa o individuo)
    autor_ids = fields.Many2many('res.partner', string='Autores')

    #Constraints de SQL del modelo
    #Util cuando la constraint se puede definir con sintaxis SQL
    _sql_constraints = [
        ('name_uniq', 'UNIQUE (nombre)', 'El titulo Comic debe ser único.'),
        ('positive_page', 'CHECK(paginas>0)', 'El comic debe tener al menos una página')
    ]

    #Indicamos que esta funcion es una "Constraints" de ese atributos
    #Dicho de otra forma, cada vez que se cambie ese atributo, se lanzara esta funcion
    #Y si la funcion detecta un cambio inadecuado, cambiara una instruccion
    #Util cuando la constraint no se puede definir con sintaxis SQL y debe indicar en una funcion
    @api.constrains('fecha_publicacion')
    def _check_release_date(self):
        # Recorremos el modelo
        for record in self:
            #Comprobamos de cada registro, primero que haya una fecha_publicacion
            #y tras ello, que la fecha no sea posterior a la actual.
            if record.fecha_publicacion and record.fecha_publicacion > fields.Date.today():
                #Si procede, lanzamos una excepcion
                raise models.ValidationError('La fecha de lanzamiento debe ser anterior a la actual')


