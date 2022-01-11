# -*- coding: utf-8 -*-
{
    'name': "Generador de imágenes de píxeles",  # Titulo del módulo
    'summary': "A partir de una llamada web, genera una imagen formada por píxeles aleatorios",  # Resumen de la funcionaliadad
    'description': """
    A partir de una llamada web, genera una imagen formada por píxeles aleatorios
    ==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Esther Arias",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],


    #Dependencias externas de https://pypi.org/project/Pillow/
    'external_dependencies': {"python": ['python-barcode',"python-barcode[images]"], "bin": []},
    'data': [
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
