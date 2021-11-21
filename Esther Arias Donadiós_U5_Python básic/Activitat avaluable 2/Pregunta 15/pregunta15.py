import pyperclip
# Primero abrimos el fichero con las palabras prohibidas, para poder trabajar con él
palabrasProhibidas = open("palabras.txt")
# definimos la función que va a censurar las palabras
def censurarPalabras(fichero):
    # primero leemos el fichero por líenas y creamos una lista con las palabras prohibidas
    words = fichero.readlines()
    words = [i.strip() for i in words]
    # definimos y copiamos en el portapapeles la frase que tenemos que censurar
    frase = "Un trueno lejano, el cielo nublado"
    pyperclip.copy(frase)
    # convertimos la frase en una cadena para poder recorrerla palabra a palabra
    listaFrase = list(frase.split(" "))
    # recorremos las palabras de la frase y las de la lista de palabras prohibidas con dos bucles for
    for palabrita in range(len(listaFrase)):
        for line in range(len(words)):
            # si alguna de las palabras coincide en ambas listas
            if listaFrase[palabrita] == words[line]:
                # guardamos la palabra repetida en una lista donde cada elemento será una de las letras de la palabra
                palabraSinCensurar = list(listaFrase[palabrita])
                # recorremos cada letra con un bucle for
                for letra in range(len(palabraSinCensurar)):
                    # cambiamos cada letra por un asterisco
                    palabraSinCensurar[letra] = "*"
                # unimos las letras para que vuelvan a formar una palabra gracias al método join()
                palabraCensurada = "".join(palabraSinCensurar)
                # cambiamos la palabra de la frase copiada en el portapapeles por su versión censurada
                listaFrase[palabrita] = palabraCensurada
    # unimos la frase convirtiéndola de nuevo en un string
    frase = " ".join(listaFrase)
    # volvemos a copiar la frase, pero esta vez se trata de su versión censurada
    pyperclip.copy(frase)
    # devolvemos el paste con la frase censurada
    return pyperclip.paste()
# hacemos la llamada a la función pasándole el fichero con las palabras prohibidas.
censurarPalabras(palabrasProhibidas)
# Si ahora hacemos control+v el texto que nos va a pegar será "Un ****** lejano, ** cielo *******".
# Cerramos el fichero
palabrasProhibidas.close()