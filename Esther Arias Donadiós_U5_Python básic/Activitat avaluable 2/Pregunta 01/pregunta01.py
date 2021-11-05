import functools

""" Las funciones lambda o anónimas, son un tipo de funciones de una sola línea, no tienen nombre ni necesitan estar
precedidas de la palabra def, y pueden recibir varios parámetros. Para poder utilizarlas necesitamos guardarlas en una
variable, en este caso guardamos en la variable suma, una función lambda que recibe como parámetros x e y, y que
devuelve la suma de x más y.
"""
suma = lambda x, y: x + y
print(suma(3, 4))

# Le pedimos al usuario que introduzca una cadena de números
print("Introduzca una serie de números separados por espacios: ")
# Guardamos en la variable listaNumeros la cadena que ha escrito el usuario separándola por los espacios. 
# Con map lo que hacemos es aplicar la función int a todos los elementos de la cadena, pasándolos de string a int,
# y con list hacemos que el objeto iterable que devuelve map sea de tipo list.
listaNumeros = list(map(int, input().split(" ")))
print(listaNumeros)
# Ahora vamos a usar filter() para quitar (filtrar) de la cadena los números menores de 10.
listaFiltrada = list(filter(lambda x: x > 10, listaNumeros))
print(listaFiltrada)
# Y por último usamos reduce() con una función que vaya multiplicando los elementos de la lista
listaReducida = functools.reduce(lambda x, y: x * y, listaFiltrada)
print(listaReducida)