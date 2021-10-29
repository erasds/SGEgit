import random

class Car(object):
# Amb el constructor per defecte definim els atributs que tindran tots els objectes que es creen de la clase
# els colors els definim en una llista per a poder aplicar el métode random i obtindre el valor de manera aleatoria
    def __init__(self, matricula):
        self.matricula = matricula
        colores = ["Red", "White", "Black", "Pink", "Blue"]
        self.color = random.choice(colores)

# Com tenía que crear dos métodes més, he decidit crear dos métodes getter
    def getMatricula(self): 
        return self.matricula 

    def getColor(self): 
        return self.color 

# Creem el métode per a imprimir
    def chapa_pintura(self):
        return "Matricula: %s. Color: %s." % (self.getMatricula(), self.getColor())
# Açí finalitzaría la clase Car

# Per a executarla li demanem un nombre al usuari que serà el nombre de instáncies de la clase que s'en van a crear
print("Indique el numero de coches a crear: ")
n = int(input())
# Com cada matrícula ha de tindre un nombre consecutiu desde 1 fins a "n", amb un bucle while li diem que 
# mentre l'índex siga menor que el nombre proporcionat per l'usuari, l'índex va a anar aumentant en 1 el seu valor
# i guardant cada un de eixos valors a la matrícula de cada objecte Car que es cree
i = int(0)
while i < n:
    i += 1
    coche = Car(matricula = i)
    # A més possem la condició de que sols imprima el resultat si l'índex es menor o igual a 10,
    # de esta manera obtendrem únicament els 10 primers valors.
    if i <= 10:
        print(coche.chapa_pintura())
        

