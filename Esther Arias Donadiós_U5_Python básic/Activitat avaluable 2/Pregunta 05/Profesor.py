class Profesor:
    # definimos el constructor de la clase
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    # definimos getters
    def getNombre(self): 
        return self.nombre

    def getTipo(self): 
        return self.tipo
    # definimos setters
    def setNombre(self, name):
        self.nombre = name

    def setTipo(self, type):
        self.tipo = type
