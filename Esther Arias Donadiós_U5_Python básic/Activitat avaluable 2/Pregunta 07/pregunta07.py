import sys
import os
"""ACUERDATE!! comprobar con test unitari... ??? y sacar ejecutable"""

fEntrada = open(sys.argv[1], "r")
fSalida = open(sys.argv[2], "w")

def leerLineas(fichero):
    lineas = fichero.readlines()
    lineas = [i.strip() for i in lineas]
    numeros = list(map(int, lineas))
    return numeros


def esPalindromo():
    numsPalindromos = []
    numerosInvertidos = []
    cadenaNumeros = list(map(str, leerLineas(fEntrada)))
    for num in range(len(cadenaNumeros)):
        numInvertido = ""
        numInvertido = cadenaNumeros[num][::-1]
        numerosInvertidos.append(numInvertido)
    for i in range(len(cadenaNumeros)):
        for j in range(len(numerosInvertidos)):
            if cadenaNumeros[i] == numerosInvertidos[j]:
                numsPalindromos.append(cadenaNumeros[i])
    numerosPalindromos = list(map(int, numsPalindromos))
    return numerosPalindromos

def esPrimo():
    numerosPrimos = []
    numeros = leerLineas(fEntrada)
    print(numeros)
    for i in range(len(numeros)):
        if numeros[i] > 1:
            for n in range(2, numeros[i]):
                if numeros[i] % n == 0:
                    print("entra al if con ", numeros[i] + "y de rango n: ", n)
                    continue
                else:
                    print("entra al else imprimimos numeros[i]", numeros[i])
                    numerosPrimos.append(numeros[i])
                    print("e imprimo numerosPrimos que se supone que acaba de añadir un numero", numerosPrimos)
    print(numerosPrimos)
    return numerosPrimos


def imprimirResultado(ficheroSalida):
    ficheroSalida = open(sys.argv[2],"w")
    ficheroSalida.write("Hay %s números palíndromos." % (len(esPalindromo())) + os.linesep)
    ficheroSalida.write("Hay %s números primos." % (len(esPrimo())) + os.linesep)
    palindromosOrdenados = sorted(esPalindromo())
    primosOrdenados = sorted(esPrimo())
    for i in range(len(palindromosOrdenados)):
        for j in range(len(primosOrdenados)):
            if palindromosOrdenados[i] == primosOrdenados[j]:
                ficheroSalida.write(palindromosOrdenados[i] + os.linesep)


imprimirResultado(fSalida)

fEntrada.close()
fSalida.close()