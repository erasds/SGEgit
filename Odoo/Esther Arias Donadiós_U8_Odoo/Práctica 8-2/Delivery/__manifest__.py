# -*- coding: utf-8 -*-
{
    'name': "Delivery",  # Titulo del módulo
    'summary': "Gestionar una empresa de transporte",  # Resumen de la funcionalidad
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
        'views/delivery_empleados.xml',
        'views/delivery_clientes.xml',
        'views/delivery_vehiculos.xml',
        'views/delivery_repartos.xml',
        
        # Vista a los informes
        'report/delivery_pendientes_report.xml',

        # Añadimos un Wizard para crear repartos
        'wizard/delivery_repartos_wizard.xml' 
    ],
}