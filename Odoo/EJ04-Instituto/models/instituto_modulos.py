from odoo import models, fields, api    

class InstitutoModulos(models.Model):
    #Nombre y descripción del modelo
    _name = 'instituto.modulos'

    _description = 'Módulos del ciclo formativo'

    #Parametros de ordenación por defecto
    _order = 'modulo'

    #ATRIBUTOS
    _rec_name = 'modulo'
    modulo = fields.Char("Módulo")
    ciclo_modulo = fields.Many2many('instituto.ciclos', string="Ciclo formativo")
    alumnos_modulo = fields.Many2many('instituto.alumnos', string='Alumnos matriculados')
    profesores_modulo = fields.Many2one('instituto.profesores', string='Profesor del módulo')