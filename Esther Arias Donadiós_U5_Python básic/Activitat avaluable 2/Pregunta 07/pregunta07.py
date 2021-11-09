import sys
import os

fEntrada = open(sys.argv[0], "r")


def esPalindromo(num):
    numerosPalindromos = []
    numInvertido = 0
    while num > 0:
        digito = num % 10
        numInvertido += 10
        numInvertido += digito
        num //= 10
    if numInvertido == num:
        numerosPalindromos.append(num)
    return numerosPalindromos


def esPrimo(num):
    numerosPrimos = []
    for n in range(2, num):
        if num % n != 0:
            numerosPrimos.append(num)
    return numerosPrimos

fSalida = open(sys.argv[1],"w")
fSalida.write("Hay %s números palíndromos." % (len(numerosPalindromos)) + os.linesep)
fSalida.write("Hay %s números primos." % (len(numerosPrimos)) + os.linesep)


fEntrada.close()
fSalida.close()

