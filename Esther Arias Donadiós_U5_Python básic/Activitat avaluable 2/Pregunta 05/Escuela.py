from .Profesor import Profesor
from .Alumno import Alumno

class Escuela:

    def __init__(self, nombre, localidad, responsable, listaAlumnos, listaProfes):
        self.nombre = nombre
        self.localidad = localidad
        self.responsable = responsable
        self.listaAlumnos = listaAlumnos
        self.listaProfes = listaProfes

    
    def matricularAlumno(self, objAlumno):
        self.listaAlumnos.append(objAlumno)

    def contratarProfe(self, objProfe):
        self.listaProfes.append(objProfe)

    def expulsarAlumno(self, objAlumno):
        self.listaAlumnos.remove(objAlumno)

    def despedirProfe(self, objProfe):
        self.listaProfes.remove(objProfe)
    
    def verAlumno(self, objAlumno):
        print(self.listaAlumnos[objAlumno])

    def verProfe(self, objProfe):
        print(self.listaProfes[objProfe])

    def modifNomAlumno(self, objAlumno, nuevoValor):
        Alumno.setNombre(objAlumno, nuevoValor)
    def modifCursoAlumno(self, objAlumno, nuevoValor):
        Alumno.setCurso(objAlumno, nuevoValor)
    def modifRespAlumno(self, objAlumno, nuevoValor):
        Alumno.setProfeResponsable(objAlumno, nuevoValor)

    def modifNomProfe(self, objProfesor, nuevoValor):
        Profesor.setNombre(objProfesor, nuevoValor)
    def modifTipoProfe(self, objProfesor, nuevoValor):
        Profesor.setTipo(objProfesor, nuevoValor)