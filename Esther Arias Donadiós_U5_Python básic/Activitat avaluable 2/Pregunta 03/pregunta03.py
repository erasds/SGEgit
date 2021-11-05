import re
# Pedimos la cadena al usuario
print("Introduzca una cadena de texto: ")
cadena = input()
# Definimos los patrones que posteriormente buscaremos dentro de la cadena
patron1 = re.compile('00')
patron2 = re.compile( '101')
# Con re.IGNORECASE le indicamos que no haga distinciones entre mayúsculas y minúsculas
patron3 = re.compile('ABC', re.IGNORECASE)
patron4 = re.compile('HO', re.IGNORECASE)
# El método findall recorre la cadena y nos devuelve las coincidencias 
# en forma de lista, que almacenamos en la variable
listaPatron1 = patron1.findall(cadena)
listaPatron2 = patron2.findall(cadena)
listaPatron3 = patron3.findall(cadena)
listaPatron4 = patron4.findall(cadena)
# listaPatrones = [[listaPatron1], [listaPatron2], [listaPatron3], [listaPatron4]]

"""def numeroPatrones(text):
    repeticiones = len(text)
    return repeticiones

print(numeroPatrones(listaPatrones))
"""
def numeroPatrones(text1, text2, text3, text4):
    patron1 = len(text1)
    patron2 = len(text2)
    patron3 = len(text3)
    patron4 = len(text4)
    sumaPatrones = patron1 + patron2 + patron3 + patron4
    return sumaPatrones

print(numeroPatrones(listaPatron1, listaPatron2, listaPatron3, listaPatron4))