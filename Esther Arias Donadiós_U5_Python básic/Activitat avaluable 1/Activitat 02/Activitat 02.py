# Funció que rev 2 nombres i torna la suma. 
def suma(x,y):
	return x + y

suma(2,2)


# Funció que rev una llista i modifica eixa mateixa llista (referència) doblant els valors de tots els elements. No retornar res. 
def doblar_lista(lista):
	lista_doblada = [i*2 for i in lista]

	
# Funció que rev una llista i torna una còpia de la mateixa llista (referència) doblant els valors de tots els elements. 
# Sense modificar la llista original. 
def doblar_lista_nueva(lista):
	lista_doblada = copy.deepcopy(lista)
	lista_doblada = [i*2 for i in lista_doblada]
	return lista_doblada

lista_ori = [1, 2, 3]
doblar_lista_nueva(lista_ori)