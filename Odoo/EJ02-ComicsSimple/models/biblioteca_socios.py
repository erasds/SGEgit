from odoo import models, fields, api    

class BaseArchive(models.AbstractModel):
    #Nombre y descripción del modelo
    _name = 'base.archive'
    _description = 'Fichero abstracto'

    #Introduce el atributo "Activo"
    activo = fields.Boolean(default=True)

    #Introduce metodo "archivar" que invierte el estado de "activo"
    #Recordamos se recive "self" como el modelo entero y no como un registro,
    #por ese motivo debemos iterar
    def archivar(self):
        #Por cada registro del modelo
        for record in self:
            #Cambiamos el valor de activo a su versión negada
            record.activo = not record.activo


class BibliotecaSocios(models.Model):
    #Nombre y descripción del modelo
    _name = 'biblioteca.socios'
    #Hereda de "base.archive" (el modelo abstracto creado antes)
    _inherit = ['base.archive']

    _description = 'Socios de biblioteca'

    #Parametros de ordenación por defecto
    _order = 'id, apellido, nombre'

    #ATRIBUTOS
    nombre = fields.Char("nombre")
    apellido = fields.Char("apellido")
    id = fields.Integer("id")

    #Constraints de SQL del modelo
    _sql_constraints = [
        ('id_uniq', 'UNIQUE (id)', 'El id del socio debe ser único')
    ]