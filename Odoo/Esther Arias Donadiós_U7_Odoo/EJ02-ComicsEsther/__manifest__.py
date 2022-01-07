# -*- coding: utf-8 -*-
{
    'name': "Biblioteca Comics",  # Titulo del módulo
    'summary': "Gestionar comics y socios",  # Resumen de la funcionaliadad
    'description': """
Gestor de bibliotecas
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
        #Cargamos las vistas de la biblioteca de comics
        'views/biblioteca_comic.xml',
        'views/biblioteca_socios.xml',
        'views/biblioteca_prestamos.xml'
    ]

}
