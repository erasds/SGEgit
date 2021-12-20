# -*- coding: utf-8 -*-
{
    'name': "Instituto",  # Titulo del módulo
    'summary': "Instituto de Ciclos Formativos",  # Resumen de la funcionaliadad
    'description': """
Instituto
==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Esther Arias",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        #Cargamos las vistas
        'views/instituto_ciclos.xml',
        'views/instituto_modulos.xml',
        'views/instituto_alumnos.xml',
        'views/instituto_profesores.xml'
    ],
}
