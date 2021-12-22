from odoo import models, fields, api    

class InstitutoModulos(models.Model):
    #Nombre y descripción del modelo
    _name = 'instituto.modulos'

    _description = 'Módulos del ciclo formativo'

    #Parametros de ordenación por defecto
    _order = 'modulo'

    #ATRIBUTOS
    _rec_name = 'modulo'
    #campo para indicar el nombre del módulo
    modulo = fields.Char("Módulo")
    # campo many2many donde podemos elegir todos los ciclos donde se imparta ese módulo
    ciclo_modulo = fields.Many2many('instituto.ciclos', string="Ciclo formativo")
    # campo many2many donde podemos elegir todos los alumnos matriculados en dicho módulo
    alumnos_modulo = fields.Many2many('instituto.alumnos', string='Alumnos matriculados')
    # campo many2many donde podemos elegir al profesor que imparta la asignatura
    profesores_modulo = fields.Many2many('instituto.profesores', string='Profesor del módulo')