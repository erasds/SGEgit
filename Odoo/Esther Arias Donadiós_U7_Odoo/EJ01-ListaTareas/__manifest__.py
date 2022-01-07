# -*- coding: utf-8 -*-
{
    'name': "Lista de tareas",

    'summary': """
    Sencilla Lista de tareas""",

    'description': """
    Sencilla lista de tareas utilizadas para crear un nuevo módulo con un nuevo modelo de datos
    """,

    'author': "Esther Arias",
    #Indicamos que es una aplicación
    'application': True,

    'category': 'Productivity',
    'version': '0.1',

    # Indicamos que depende del modulo "base"
    'depends': ['base'],

    'data': [
        #Indicamos la politica de acceso del modelo
        'security/ir.model.access.csv',
        #Cargamos las vistas y las plantillas
        'views/views.xml',
    ]
}
