import sys
import os
"""ACUERDATE!! comprobar con test unitari... ??? y sacar ejecutable"""
# leemos el fichero de entrada, cuyo nombre hemos recibido por consola como primer parámetro

fEntrada = open(sys.argv[1], "r")
fSalida = open(sys.argv[2], "w")


def esPalindromo(fichero):
    numsPalindromos = []
    numerosInvertidos = []
    lineas = fichero.readlines()
    lineas = [i.strip() for i in lineas]
    numeros = list(map(str, lineas))
    for num in range(len(numeros)):
        numInvertido = ""
        numInvertido = numeros[num][::-1]
        numerosInvertidos.append(numInvertido)
    for i in range(len(numeros)):
        for j in range(len(numerosInvertidos)):
            if numeros[i] == numerosInvertidos[j]:
                numsPalindromos.append(numeros[i])
    numerosPalindromos = list(map(int, numsPalindromos))
    return numerosPalindromos

def esPrimo(fichero):
    numerosPrimos = []
    numeros = fichero.readlines()
    for i in range(len(numeros)):
        if i > 2 and numeros[i] % i != 0:
            numerosPrimos.append(numeros[i])
    print(numerosPrimos)
    return numerosPrimos


def imprimirResultado(ficheroSalida):
    ficheroSalida = open(sys.argv[2],"w")
    ficheroSalida.write("Hay %s números palíndromos." % (len(esPalindromo(fEntrada))) + os.linesep)
    ficheroSalida.write("Hay %s números primos." % (len(esPrimo(fEntrada))) + os.linesep)
    palindromosOrdenados = sorted(esPalindromo(fEntrada))
    primosOrdenados = sorted(esPrimo(fEntrada))
    for i in range(len(palindromosOrdenados)):
        for j in range(len(primosOrdenados)):
            if palindromosOrdenados[i] == primosOrdenados[j]:
                ficheroSalida.write(palindromosOrdenados[i] + os.linesep)


imprimirResultado(fSalida)

fEntrada.close()
fSalida.close()