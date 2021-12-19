# -*- coding: utf-8 -*-
{
    'name': "Hospital",  # Titulo del módulo
    'summary': "Gestionar datos de méidcos, pacietes y sus diagnósticos",  # Resumen de la funcionaliadad
    'description': """
Gestor de un hospital
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
        'views/hospital_medicos.xml',
        'views/hospital_pacientes.xml',
        'views/hospital_diagnosticos.xml'
    ],
}
