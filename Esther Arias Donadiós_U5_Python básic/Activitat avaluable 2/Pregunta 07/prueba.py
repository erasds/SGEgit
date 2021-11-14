import sys

# leemos el fichero de entrada, cuyo nombre hemos recibido por consola como primer parámetro
fEntrada = open(sys.argv[1], "r")


def esPalindromo(fichero):
    numerosPalindromos = []
    numeros = []
    numerosInvertidos = []
    lineas = fichero.readlines()
    for linea in range(len(lineas)):
        numeros.append(str(linea.strip()))
    for num in range(len(numeros)):
        numInvertido = ""
        for char in range(len(num)):
            numInvertido = char[::-1]
            numerosInvertidos.append(numInvertido)
    for i in range(len(numeros)):
        for j in range(len(numerosInvertidos)):
            if numeros[i] == numerosInvertidos[j]:
                numerosPalindromos.append(numeros[i])
    return numerosPalindromos




esPalindromo(fEntrada)

fEntrada.close()