from copy import copy, deepcopy
# Per a copiar una llista podem usar el métode copy() :
lista_ori = [1, 2, 3]
copy_lista = lista_ori.copy()
print(copy_lista)
"""
Aixó es el que es coneguería com una còpia superficial o “shallow copy”, 
que vol dir que las dos apunten al mateix espai de memoria. 
Si volem evitar aixó y fer una còpia de la llista que actúe com un element nou e independent, 
necessitem fer una “deep copy”, o còpia profunda :
"""
deep_copy_lista = deepcopy(lista_ori)
print(deep_copy_lista)


# Amb “append” podem afegir elements al final d’una llista :
lista_ori.append(5)
print(lista_ori)


# Podem eliminar l’últim element d’una llista amb “pop” :
lista_ori.pop()
print(lista_ori)


# Per a crear una nova llista amb els últims elements d'altra, hem de definir el rang :
lista_dos = lista_ori[1:]
print(lista_dos)


# Per a convertir les paraules d’una cadena (separades per espai) a una llista. 
# Primer definim la cadena i després usem split indicant el caracter pel qual volem que faça la separació :
cadena = "Hola que tal"
lista_cadena = cadena.split(" ")
print(lista_cadena)


# Els comentaris d’una línia a Python s’escriuen precedits del símbol # :
# Esto es un comentario


# Els comentaris multilínea a Python s’escriuen acompanyats de “““ (tres cometes) a l’inici i al final :
"""
Esto es un
comentario
multilínea
"""