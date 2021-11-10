import csv
from barcode import EAN13
from barcode.writer import ImageWriter

# Abrimos el archivo .csv
archivo = open("Alumnos.csv")
# en la variable dicc_alumnos guardamos el diccionario que se genera con los datos de cada linea del archivo
# gracias a la función csv.DictReader()
dicc_alumnos = csv.DictReader(archivo)
# Ahora le decimos que para cada elemento del diccionario...
for row in dicc_alumnos:
    # ...genere un ean cogiendo la clave ID, lo "escriba" en una imagen...
    ean = EAN13(row["ID"], writer = ImageWriter())
    # ...y que coja de mombre para dicha imagen la clave Alumno
    nombre = ean.save(row["Alumno"])

