import sys
import os
# Vamos a recibir el nombre de los ficheros con los que vamos a trabajar por parámetros de consola, así que le indicamos las posiciones
fEntrada = open(sys.argv[1], "r")
fSalida = open(sys.argv[2], "w")
# Procesamos el fichero de entrada, lo leemos por líneas, eliminamos los saltos de línea,
# y gracias a la función map al final tendremos una lista de int donde cada elemento es uno de los números del fichero
lineas = fEntrada.readlines()
lineas = [i.strip() for i in lineas]
numeros = list(map(int, lineas))
# Definimos la función para comprobar si un número es palíndromo
def esPalindromo():
    numsPalindromos = []
    numerosInvertidos = []
    # vamos a convertir la lista de los números en una lista de String para poder invertirlos
    cadenaNumeros = list(map(str, numeros))
    for num in range(len(cadenaNumeros)):
        numInvertido = ""
        # con [::-1] lo que hacemos es invertir la cadena en la posición cadenaNumeros[num]
        numInvertido = cadenaNumeros[num][::-1]
        # y esto lo almacenamos en una lista donde vamos a ir guardando todos los números invertidos
        numerosInvertidos.append(numInvertido)
    for i in range(len(cadenaNumeros)):
        for j in range(len(numerosInvertidos)):
            # recorremos las dos listas y si alguno de los números originales coincide con uno de los números invertidos es que es palíndromo
            if cadenaNumeros[i] == numerosInvertidos[j]:
                # lo añadimos a la lista de números palíndromos, que una vez esté completa volvemos a convertir en Int
                numsPalindromos.append(cadenaNumeros[i])
    numerosPalindromos = list(map(int, numsPalindromos))
    return numerosPalindromos
# Ahora definimos la función para comprobar si un número es primo
def esPrimo():
    numerosPrimos = []
    for i in range(len(numeros)):
        # la primera condición será que el número sea mayor que 1, ya que el 0 no es divisible
        if numeros[i] > 1:
            contador = 0
            # ahora vamos a coger cada número, lo vamos a ir dividiendo por los números comprendidos entre 2 y sí mismo, 
            # y si alguna de esas divisiones es exacta (resto 0), sabemos que tampoco es un número primo. 
            for n in range(2, numeros[i] + 1):
                if numeros[i] % n == 0:
                    contador += 1
            # Con la variable contador vamos sumando las veces que entra en la división con cada número, 
            # y si es más de una ya sabemos que no es primo, en caso contrario lo añadimos a la lista de números primos.
            if contador == 1:
                numerosPrimos.append(numeros[i])
    return numerosPrimos
# Por último creamos la función para imprimir los resultados en el fichero de salida
def imprimirResultado(ficheroSalida):
    # para ello lo abrimos, escribimos las líneas indicando el número de números palíndromos y primos que nos hemos encontrado en el fichero de entrada, 
    # haciendo las llamadas correspondientes a cada función de las definidas anteriormente
    ficheroSalida = open(sys.argv[2],"w")
    ficheroSalida.write("Hay %s números palíndromos." % (len(esPalindromo())) + os.linesep)
    ficheroSalida.write("Hay %s números primos." % (len(esPrimo())) + os.linesep)
    # ahora para poder saber cuales de estos números son ambas cosas, vamos a ordenar las listas y a ir comparando cada posición, 
    # las que coincidan serán los números que escribiremos también en el fichero de salida
    palindromosOrdenados = sorted(esPalindromo())
    primosOrdenados = sorted(esPrimo())
    for i in range(len(palindromosOrdenados)):
        for j in range(len(primosOrdenados)):
            if palindromosOrdenados[i] == primosOrdenados[j]:
                palindromosStr = list(map(str, palindromosOrdenados))
                ficheroSalida.write(palindromosStr[i] + os.linesep)
# llamamos a la función que imprime los resultados
imprimirResultado(fSalida)
# cerramos los ficheros
fEntrada.close()
fSalida.close()