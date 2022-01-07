# -*- coding: utf-8 -*-
{
    'name': "Gestionar liga de futbol",  # Titulo del módulo
    'summary': "Gestionar una liga de futbol",  # Resumen de la funcionaliadad
    'description': """
    Gestor de Liga de futbol
    ==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Esther Arias",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [

      
        #Estos dos primeros ficheros:
        #1) El primero indica grupo de seguridad basado en rol
        #2) El segundo indica la politica de acceso del modelo
        #'security/groups.xml',
        'security/ir.model.access.csv',

        #Aqui distintas vistas de equipo (vistas diferentes, mismo modelo)
        'views/liga_equipo.xml',
        'views/liga_equipo_clasificacion.xml',
        #Vista a los informes
        'report/liga_equipo_clasificacion_report.xml',
        'report/liga_partido_report.xml',
        #Aqui vista sobre los partidos
        'views/liga_partido.xml',
        #Añadimos un Wizard para introducir equipos
        'wizard/liga_equipo_wizard.xml',
        #Añadimos un Wizard para introducir partidos
        'wizard/liga_partido_wizard.xml'
        
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
