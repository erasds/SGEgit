class Alumno:
    # definimos el constructor de la clase
    def __init__(self, nombre, curso, profeResponsable):
        self.nombre = nombre
        self.curso = curso
        self.profeResponsable = profeResponsable
    # definimos getters
    def getNombre(self): 
        return self.nombre

    def getCurso(self): 
        return self.curso

    def getProfeResponsable(self):
        return self.profeResponsable
    # definimos setters
    def setNombre(self, name):
        self.nombre = name

    def setCurso(self, cursillo):
        self.curso = cursillo

    def setProfeResponsable(self, profResp):
        self.profeResponsable = profResp

alumno1 = Alumno("Esther", "Segundo", "Sergi")
alumno2 = Alumno("Alvaro", "Primero", "David")
alumno3 = Alumno("Pablo", "Seguno", "Oscar")