from .Profesor import Profesor
from .Alumno import Alumno

class Escuela:

    def __init__(self, nombre, localidad, responsable):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
