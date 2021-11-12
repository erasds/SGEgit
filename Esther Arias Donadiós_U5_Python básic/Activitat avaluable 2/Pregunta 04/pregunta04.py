escenarioMinas = [["0", "0", "-1", "0"],
                    ["-1", "0", "0", "-1"],
                    ["0", "-1", "0", "0"],
                    ["-1", "0", "-1", "0"]]

def contandoMinas(miCampo):
    # recorremos el array con dos bucles for
    for i in range(len(miCampo)):
        print("\n")
        for j in range(len(miCampo[i])):
            # definimos la variable suma donde vamos a ir almacenando los valores 
            # de cada posición cercana a una mina
            suma = 0
            # si la posición en la que nos encontramos es una mina, la imprimimos y no sumamos nada
            if miCampo[i][j] == "-1":
                print("-1", end = " ")
            else:
                # ahora vamos mirando en cada dirección y si al lado hay una mina sumamos 1 
                if i - 1 >= 0: # miro a la izquierda
                    if miCampo[i-1][j] == "-1":
                        suma += 1
                if j - 1 >= 0: # miro arriba
                    if miCampo[i][j-1] == "-1":
                        suma += 1
                if i + 1 < len(miCampo[i]): # miro a la derecha
                    if miCampo[i+1][j] == "-1":
                        suma += 1
                if j + 1 < len(miCampo[i]): # miro abajo
                    if miCampo[i][j + 1] == "-1":
                        suma += 1
                if i - 1 >= 0 and j - 1 >= 0: # diagonal noroeste
                    if miCampo[i-1][j-1] == "-1":
                        suma += 1
                if i + 1 < len(miCampo[i]): # diagonal noreste
                    if j - 1 >= 0:
                        if miCampo[i+1][j-1] == "-1":
                            suma += 1
                if i - 1 >= 0: # diagonal suroeste
                    if j + 1 < len(miCampo[i]):
                        if miCampo[i-1][j+1] == "-1":
                            suma += 1
                if i + 1 < len(miCampo[i]): # diagonal sureste
                    if j + 1 < len(miCampo[i]):
                        if miCampo[i+1][j+1] == "-1":
                            suma += 1
                print(suma, end= " ")

contandoMinas(escenarioMinas)


