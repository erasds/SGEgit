print("Suelo seguro: 0 ", "Suelo minado: -1")
print("Pinte la primera línea del escenario: ")
linea1 = input().split(" ")
print("Pinte la segunda línea del escenario: ")
linea2 = input().split(" ")
escenarioMinas = [linea1,linea2]
print(escenarioMinas)

def contandoMinas(miCampo):
    for i in range(len(miCampo)):
        print("\n")
        for j in range(len(miCampo[i])):
            suma = 0
            if miCampo[i][j] == "-1":
                print("-1", end = " ")
            else:
                if i - 1 >= 0: # miro a la izquierda
                    if miCampo[i-1][j] == "-1":
                        suma += 1
                if j - 1 >= 0: # miro arriba
                    if miCampo[i][j-1] == "-1":
                        suma += 1
                if i + 1 < len(miCampo): # miro a la derecha
                    if miCampo[i+1][j] == "-1":
                        suma += 1
                if j + 1 < len(miCampo[i]): # miro abajo
                    if miCampo[i][j + 1] == "-1":
                        suma += 1
                if i - 1 & j - 1 >= 0: # diagonal noroeste
                    if miCampo[i-1][j-1] == "-1":
                        suma += 1
                if i + 1 < len(miCampo): # diagonal noreste
                    if j - 1 >= 0:
                        if miCampo[i+1][j-1] == "-1":
                            suma += 1
                if i - 1 >= 0: # diagonal suroeste
                    if j + 1 < len(miCampo[i]):
                        if miCampo[i-1][j+1] == "-1":
                            suma += 1
                if i + 1 < len(miCampo): # diagonal sureste
                    if j + 1 >= 0:
                        if miCampo[i+1][j+1] == "-1":
                            suma += 1
                print(suma, end= " ")

contandoMinas(escenarioMinas)


