import random

class Car:
    matricula = 0
    color = ""
# Amb el constructor per defecte definim els atributs que tindran tots els objectes que es creen de la clase
    def __init__(self, matricula, color):
        self.matricula = matricula
        self.color = color
# per a triar els colors de manera aleatoria els definim en una llista i apliquem el métode random
    def colorRandom(self):
        colores = ["Red", "White", "Black", "Pink", "Blue"]
        self.colorElegido = random.choice(colores)
        return self.colorElegido

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
def main():
    print("Indique el numero de coches a crear: ")
    n = int(input())
    # Com cada matrícula ha de tindre un nombre consecutiu desde 1 fins a "n", amb un bucle while li diem que 
    # mentre l'índex siga menor que el nombre proporcionat per l'usuari, l'índex va a anar aumentant en 1 el seu valor
    # i guardant cada un de eixos valors a la matrícula de cada objecte Car que es cree
    i = int(0)
    while i < n:
        i += 1
        coche = Car(matricula = i, color = "Red")
        coche.color = coche.colorRandom()
        # A més possem la condició de que sols imprima el resultat si l'índex es menor o igual a 10,
        # de esta manera obtendrem únicament els 10 primers valors.
        if i <= 10:
            print(coche.chapa_pintura())

if __name__ == "__main__":
    main()
        


