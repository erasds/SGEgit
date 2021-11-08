# Primero abrimos el fichero con el Sudoku
file = open("Sudoku.in", "r")
# Después lo leemos convirtiendo cada línea en una lista
linea1 = file.read(17).split()
file.seek(19)
linea2 = file.read(17).split()
file.seek(38)
linea3 = file.read(17).split()
file.seek(57)
linea4 = file.read(17).split()
file.seek(76)
linea5 = file.read(17).split()
file.seek(95)
linea6 = file.read(17).split()
file.seek(114)
linea7 = file.read(17).split()
file.seek(133)
linea8 = file.read(17).split()
file.seek(152)
linea9 = file.read(17).split()
# E introducimos esas listas en otra que abarca todo el sudoku
sudoku = [linea1, linea2, linea3, linea4, linea5, linea6, linea7, linea8, linea9]
print(sudoku)
# Definimos la función para comprobar si el Sudoku es correcto
"""def esSudokuCorrecto(miArrayBi):
    for i in range(len(miArrayBi)):
        for j in range(len(miArrayBi[i])):


# Llamamos a la función
esSudokuCorrecto(sudoku)"""
# cerramos el ficher
file.close()