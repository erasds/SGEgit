import cv2
from pyzbar.pyzbar import decode
import os

# Primero definimos la función que va a leer los códigos de barras
def LectorCodigos(image):
    img = cv2.imread(image)
    detectedBarcodes = decode(img)
    # Para cada código de barras encontrado en la imagen
    for barcode in detectedBarcodes: 
        # Localiza la posición del código para poder leerlo
        (x, y, w, h) = barcode.rect
        cv2.rectangle(img, (x-10, y-10),
                    (x + w+10, y + h+10),
                    (255, 0, 0), 2)
        # Si no está "vacío"  
        if barcode.data!="":
            # Devolvemos e imprimimos la información del código de barras
            return barcode.data

# Ahora definimos una función que lea los archivos .png de un directorio
def LectorPngs(directorio):
    # primero leemos todos los archivos del directorio
    listadoArchivos = os.listdir(directorio)
    # definimos la variable nombres donde vamos a almacenar los nombres de las imágenes, 
    # que son los nombres de los Alumnos
    nombres = []
    # Para cada archivo en listadoArchivos
    for archivo in listadoArchivos:
        # separamos el nombre de la extensión
        nombre, extension = os.path.splitext(archivo)
        # si la extensión es .png
        if extension == ".png":
            # almacenamos el nombre en la lista
            nombres.append(nombre)
        # para cada elemento de la lista de nombres
        for i in range(len(nombres)):
            # si el nombre de la lista coincide con el nombre de los archivos png
            if nombres[i] == nombre:
                # hacemos una llamada a la función para leer los códigos de barras y almacenamos el valor en id
                id = str(LectorCodigos(archivo))
                # filtramos id para eliminar los caracteres que nos había añadido de más al crear el código de barras
                idFiltrado = id[2:-2]
                # imprimimos el resultado
                print("El nombre del alumno es %s y su ID es %s" % (nombre, idFiltrado))
# ejecutamos el programa
def main():
    LectorPngs(".")

if __name__ == "__main__":
    main()
