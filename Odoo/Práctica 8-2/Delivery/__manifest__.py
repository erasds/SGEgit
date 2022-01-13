# -*- coding: utf-8 -*-
{
    'name': "Delivery",  # Titulo del módulo
    'summary': "Gestionar una empresa de transporte",  # Resumen de la funcionaliadad
    'description': """
    Gestor de una Empresa de Transporte
    ==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Esther Arias",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [

      
        # Indicamos la politica de acceso del modelo
        'security/ir.model.access.csv',

        # Aqui indicamos las diferentes vistas de los modelos
        'views/liga_equipo.xml',
        'views/liga_equipo_clasificacion.xml',
        # Vista a los informes
        'report/liga_equipo_clasificacion_report.xml',
        'report/liga_partido_report.xml',
        # Aqui vista sobre los partidos
        'views/liga_partido.xml',
        # Añadimos un Wizard para introducir equipos
        'wizard/liga_equipo_wizard.xml',
        # Añadimos un Wizard para introducir partidos
        'wizard/liga_partido_wizard.xml'
        
    ],
}