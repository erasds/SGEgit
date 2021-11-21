from .Alumno import Alumno
from .Profesor import Profesor
from .Escuela import Escuela

def main():
    alumno1 = Alumno("Esther", "Segundo", "Sergi")
    alumno2 = Alumno("Alvaro", "Primero", "David")
    alumno3 = Alumno("Pablo", "Seguno", "Oscar")
    alumno4 = Alumno("Carla", "Primero", "Oscar")
    profe1 = Profesor("Sergi", "Mixto")
    profe2 = Profesor("David", "Ciencias")
    profe3 = Profesor("Oscar", "Letras")
    escuela1 = Escuela("Serra Perenxisa", "Torrent", "Manuel", "", "")
    escuela2 = Escuela("Henri Matisse", "Paterna", "Pilar", "", "")

    escuela1.matricularAlumno(alumno1)
    escuela1.matricularAlumno(alumno2)
    escuela2.matricularAlumno(alumno3)
    escuela2.matricularAlumno(alumno4)
    escuela1.contratarProfe(profe1)
    escuela1.contratarProfe(profe2)
    escuela2.contratarProfe(profe3)
    escuela2.expulsarAlumno(alumno3)
    escuela1.despedirProfe(profe2)
    escuela1.verAlumno(alumno1)
    escuela1.verProfe(profe1)
    escuela2.modifTipoProfe(profe3, "Mixto")
    escuela2.verProfe(profe3)
    escuela1.modifCursoAlumno(alumno2, "Segundo")
    escuela1.verAlumno(alumno2)

if __name__ == "__main__":
    main()

