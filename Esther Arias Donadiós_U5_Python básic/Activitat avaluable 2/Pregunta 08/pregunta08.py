import os
import shutil

# Para mostrar una lista con los archivos del directorio actual
listadoArchivos = os.listdir(".")
print(listadoArchivos)

# Para cada archivo en listadoArchivos
for archivo in listadoArchivos:
    # separamos el nombre de la extensión con os.path.splitext
    nombre, extension = os.path.splitext(archivo)
    # creamos una carpeta con el nombre de la extensión
    os.mkdir(extension)
    # movemos ese archivo a la carpeta con el nombre de la extensión
    shutil.move(archivo, extension)

