from odoo import models, fields, api    

class BibliotecaSocios(models.Model):
    #Nombre y descripción del modelo
    _name = 'biblioteca.socios'

    _description = 'Socios de biblioteca'

    #Parametros de ordenación por defecto
    _order = 'id, apellido, nombre_ids'

    #ATRIBUTOS
    _rec_name = 'nombre_ids'
    nombre_ids = fields.Char("Nombre")
    apellido = fields.Char("Apellido")
    id = fields.Integer("Id")

    #Constraints de SQL del modelo
    _sql_constraints = [
        ('id_uniq', 'UNIQUE (id)', 'El id del socio debe ser único'),
    ]