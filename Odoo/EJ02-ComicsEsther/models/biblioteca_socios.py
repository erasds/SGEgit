from odoo import models, fields, api    

# Definimos modelo para los socios de la biblioteca
class BibliotecaSocios(models.Model):
    #Nombre y descripción del modelo
    _name = 'biblioteca.socios'

    _description = 'Socios de biblioteca'

    #Parametros de ordenación por defecto
    _order = 'id, apellido, nombre_ids'

    #ATRIBUTOS

    # el atributo del que cogerá el nombre
    _rec_name = 'nombre_ids'

    # nombre del socio
    nombre_ids = fields.Char("Nombre")
    # apellido del socio
    apellido = fields.Char("Apellido")
    # id del socio, que debe ser único
    id = fields.Integer("Id")
    #Dato binario, para guardar un binario (en la vista indicaremos que es una imagen) con la portada del comic
    foto = fields.Image('Avatar', max_width=200,max_height=200)

    #Constraints de SQL del modelo, para controlar que el id sea único
    _sql_constraints = [
        ('id_uniq', 'UNIQUE (id)', 'El id del socio debe ser único')
    ]