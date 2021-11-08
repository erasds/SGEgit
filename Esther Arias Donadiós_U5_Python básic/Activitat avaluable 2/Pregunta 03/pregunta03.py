# Pedimos la cadena al usuario
print("Introduzca una cadena de texto: ")
# La guardamos en la variable y la pasamos a mayúsculas para no hacer distinciones
cadena = input().upper()
# definimos la función que va a localizar y sumar los patrones
def numeroPatrones(text):
    # definimos el contador
    contador = 0
    # definimos cada patrón
    patron1 = "00"
    patron2 = "101"
    patron3 = "ABC"
    patron4 = "HO"
    # recorremos la cadena con un for
    for i in range(len(text)):
        # si desde la posición en la que se encuentra i, empieza el patrón1, suma 1 al contador
        # con text[i:] nos aseguramos de que no salta los patrones superpuestos
        # startswith() es un método predefinido de Python para comprobar si un string empieza por...
        if text[i:].startswith(patron1):
            contador = contador + 1
        # si desde la posición en la que se encuentra i, empieza el patrón2 ...
        if text[i:].startswith(patron2):
            contador = contador + 1
        if text[i:].startswith(patron3):
            contador = contador + 1
        if text[i:].startswith(patron4):
            contador = contador + 1
    # devuelve contador que va a ser la suma de todas las veces que se repite cada patrón
    return contador

print(numeroPatrones(cadena))
