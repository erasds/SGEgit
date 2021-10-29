import sys

print(sys.argv)
"""
Si ara a la consola ens posicionem a la misma carpeta on es troba aquest 
arxiu Python i escribim:
python argv.py hola que tal
ens imprimirà la llista:
['argv.py', 'hola', 'que', 'tal']
Es a dir, cada cosa que escribim separada amb un espai el toma com un 
nou item de la llista.
"""
# Aquest es un exemple de sobrecàrrega de funcions on una de elles reb un nombre de arguments variable
def sobrecarga(num1, num2, num3):
    suma = int(num1) + int(num2) + int(num3)
    return suma

print(sobrecarga(sys.argv[1], sys.argv[2], sys.argv[3]))

def sobrecarga(*args):
    suma = (int(args[0])) + (int(args[1])) + (int(args[2]))
    return suma

print(sobrecarga(sys.argv[1], sys.argv[2], sys.argv[3]))

