# Abrimos el fichero del sudoku y lo leemos por filas con la funcion readlines()
with open("Sudoku.in") as file:
    sudoku = file.readlines()
# aplicamos el método strip a cada fila para quitarle el \n del final
sudoku = [i.strip() for i in sudoku]
# ahora hacemos que cada línea sea una lista distinta y con split hacemos que 
# cada caracter de cada línea sea un elemento distinto de la cadena
for i in range(len(sudoku)):
    sudoku[i] = list(sudoku[i].split())

# definimos la función para comprobar las filas
def comprobarFilas(miSudoku):
    # definimos la variable sumaTotal que será la suma de cada dígito del sudoku
    sumaTotal = 0
    #recorremos todas las lineas del sudoku con dos bucles for
    for j in range(len(miSudoku)):
        # definimos la variable suma donde se va a almacenar la suma de cada línea del sudoku
        suma = 0
        # para cada línea vamos a sumar todos sus números con un bucle for
        for i in range(len(miSudoku[j])):
            suma += int(miSudoku[j][i])
            # si la suma da 45 la añadimos a la sumaTotal, 
            # si no diera 45 no haría falta seguir sumando porque no sería correcto
            if suma == 45:
                sumaTotal += 45
    # si el total de todos los dígitos del sudoku da 405 
    # pasamos a comprobar que no haya números repetidos en cada línea
    if sumaTotal == 405:
        # recorremos cada línea
        for j in range(len(miSudoku)):
            # hacemos una copia de cada fila aplicandole el método set() 
            # que recoge solo los elementos únicos de una lista, comparamos la longitud de ambas 
            # y si es correcto es porque en la fila original no había valores repetidos
            if len(miSudoku[j][i]) == len(set(miSudoku[j][i])):
                # si todas estas operaciones son correctas la función devolverá True
                return True
    else:
        # en caso contrario devolverá False
        return False

# definimos la función para comprobar las columnas
def comprobarColumnas(miSudoku):
    # aquí vamos a hacer lo mismo que en la función de comprobar las filas pero invierto el orden de los índices 
    # para "avanzar" recorriendo el sudoku hacia abajo en lugar de hacia la derecha
    sumaTotal = 0
    for i in range(len(miSudoku)):
        suma = 0
        for j in range(len(miSudoku[i])):
            suma += int(miSudoku[i][j])
            if suma == 45:
                sumaTotal += 45
    if sumaTotal == 405:
        for i in range(len(miSudoku)):
            if len(miSudoku[i][j]) == len(set(miSudoku[i][j])):
                return True
    else:
        return False

# definimos la función para comprobar las cajas
def comprobarCajas(miSudoku):
    # definimos la variable para la suma de todas las cajas
    sumaTotal = 0
    # definimos la lista con las posiciones de la primera caja
    caja1 = [miSudoku[0][0], miSudoku[1][0], miSudoku[2][0], 
            miSudoku[0][1], miSudoku[1][1], miSudoku[2][1],
            miSudoku[0][2], miSudoku[1][2], miSudoku[2][2]]
    # definimos la variable para la suma de los números dentro de la primera caja
    suma1 = 0
    # recorremos la primera caja sumando los numeros y si da 45 lo añadimos a la sumaTotal
    for j in range(len(caja1)):
        suma1 += int(caja1[j])
        if suma1 == 45:
            sumaTotal += 45
    # definimos la lista con las posiciones de la segunda caja
    caja2 = [miSudoku[3][0], miSudoku[4][0], miSudoku[5][0], 
            miSudoku[3][1], miSudoku[4][1], miSudoku[5][1],
            miSudoku[3][2], miSudoku[4][2], miSudoku[5][2]]
    # definimos la variable para la suma de los números dentro de la segunda caja
    suma2 = 0
    # recorremos la segunda caja sumando los numeros y si da 45 lo añadimos a la sumaTotal
    for j in range(len(caja2)):
        suma2 += int(caja2[j])
        if suma2 == 45:
            sumaTotal += 45
    # definimos la lista con las posiciones de la tercera caja
    caja3 = [miSudoku[6][0], miSudoku[7][0], miSudoku[8][0], 
            miSudoku[6][1], miSudoku[7][1], miSudoku[8][1],
            miSudoku[6][2], miSudoku[7][2], miSudoku[8][2]]
    # definimos la variable para la suma de los números dentro de la tercera caja
    suma3 = 0
    # recorremos la tercera caja sumando los numeros y si da 45 lo añadimos a la sumaTotal
    for j in range(len(caja3)):
        suma3 += int(caja3[j])
        if suma3 == 45:
            sumaTotal += 45
    # definimos la lista con las posiciones de la cuarta caja
    caja4 = [miSudoku[0][3], miSudoku[1][3], miSudoku[2][3], 
            miSudoku[0][4], miSudoku[1][4], miSudoku[2][4],
            miSudoku[0][5], miSudoku[1][5], miSudoku[2][5]]
    # definimos la variable para la suma de los números dentro de la cuarta caja
    suma4 = 0
    # recorremos la cuarta caja sumando los numeros y si da 45 lo añadimos a la sumaTotal
    for j in range(len(caja4)):
        suma4 += int(caja4[j])
        if suma4 == 45:
            sumaTotal += 45
    # definimos la lista con las posiciones de la quinta caja
    caja5 = [miSudoku[3][3], miSudoku[4][3], miSudoku[5][3], 
            miSudoku[3][4], miSudoku[4][4], miSudoku[5][4],
            miSudoku[3][5], miSudoku[4][5], miSudoku[5][5]]
    # definimos la variable para la suma de los números dentro de la quinta caja
    suma5 = 0
    # recorremos la quinta caja sumando los numeros y si da 45 lo añadimos a la sumaTotal
    for j in range(len(caja5)):
        suma5 += int(caja5[j])
        if suma5 == 45:
            sumaTotal += 45
    # definimos la lista con las posiciones de la sexta caja
    caja6 = [miSudoku[6][3], miSudoku[7][3], miSudoku[8][3], 
            miSudoku[6][4], miSudoku[7][4], miSudoku[8][4],
            miSudoku[6][5], miSudoku[7][5], miSudoku[8][5]]
    # definimos la variable para la suma de los números dentro de la sexta caja
    suma6 = 0
    # recorremos la sexta caja sumando los numeros y si da 45 lo añadimos a la sumaTotal
    for j in range(len(caja6)):
        suma6 += int(caja6[j])
        if suma6 == 45:
            sumaTotal += 45
    # definimos la lista con las posiciones de la septima caja
    caja7 = [miSudoku[0][6], miSudoku[1][6], miSudoku[2][6], 
            miSudoku[0][7], miSudoku[1][7], miSudoku[2][7],
            miSudoku[0][8], miSudoku[1][8], miSudoku[2][8]]
    # definimos la variable para la suma de los números dentro de la septima caja
    suma7 = 0
    # recorremos la septima caja sumando los numeros y si da 45 lo añadimos a la sumaTotal
    for j in range(len(caja7)):
        suma7 += int(caja7[j])
        if suma7 == 45:
            sumaTotal += 45
    # definimos la lista con las posiciones de la octava caja
    caja8 = [miSudoku[3][6], miSudoku[4][6], miSudoku[5][6], 
            miSudoku[3][7], miSudoku[4][7], miSudoku[5][7],
            miSudoku[3][8], miSudoku[4][8], miSudoku[5][8]]
    # definimos la variable para la suma de los números dentro de la octava caja
    suma8 = 0
    # recorremos la octava caja sumando los numeros y si da 45 lo añadimos a la sumaTotal
    for j in range(len(caja8)):
        suma8 += int(caja8[j])
        if suma8 == 45:
            sumaTotal += 45
    # definimos la lista con las posiciones de la novena caja
    caja9 = [miSudoku[6][6], miSudoku[7][6], miSudoku[8][6], 
            miSudoku[6][7], miSudoku[7][7], miSudoku[8][7],
            miSudoku[6][8], miSudoku[7][8], miSudoku[8][8]]
    # definimos la variable para la suma de los números dentro de la novena caja
    suma9 = 0
    # recorremos la novena caja sumando los numeros y si da 45 lo añadimos a la sumaTotal
    for j in range(len(caja9)):
        suma9 += int(caja9[j])
        if suma9 == 45:
            sumaTotal += 45
    # si la suma de cada caja es correcta y la sumaTotal es igual a 405
    if sumaTotal == 405:
        # comprobamos que no haya números repetidos
        for j in range(len(caja1)):
            if len(caja1[j]) == len(set(caja1[j])):
                continue
        for j in range(len(caja2)):
            if len(caja2[j]) == len(set(caja2[j])):
                continue
        for j in range(len(caja3)):
            if len(caja3[j]) == len(set(caja3[j])):
                continue
        for j in range(len(caja4)):
            if len(caja4[j]) == len(set(caja4[j])):
                continue
        for j in range(len(caja5)):
            if len(caja5[j]) == len(set(caja5[j])):
                continue
        for j in range(len(caja6)):
            if len(caja6[j]) == len(set(caja6[j])):
                continue
        for j in range(len(caja7)):
            if len(caja7[j]) == len(set(caja7[j])):
                continue
        for j in range(len(caja8)):
            if len(caja8[j]) == len(set(caja8[j])):
                continue
        for j in range(len(caja9)):
            if len(caja9[j]) == len(set(caja9[j])):
                continue
        # si no los hay, las cajas son correctas y devolvemos True
        return True
    else:
        # si no son correctas devolvemos False
        return False


# Definimos la función para comprobar si el Sudoku es correcto
def esSudokuCorrecto(miArrayBi):
    # esta función realiza una llamada a las tres funciones que comprueban cada condición del sudoku, 
    # si las tres devuelven True entonces el sudoku es correcto
    if comprobarFilas(miArrayBi) == True and comprobarColumnas(miArrayBi) == True and comprobarCajas(miArrayBi) == True:
        return print("Es correcte")
    # solo con que una devuelva False sería incorrecto
    else:
        return print("Es incorrecte")


# cerramos el fichero
file.close()

# Llamamos a la función
esSudokuCorrecto(sudoku)
