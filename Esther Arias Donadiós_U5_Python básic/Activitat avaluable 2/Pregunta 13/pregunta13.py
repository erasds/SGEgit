import requests  #Importamos la librería requests
# Solicitamos la especie que se desea buscar
print("Indique la especie que desea buscar:")
especie = input()
print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....") 
# configuramos la url
URL = 'https://rickandmortyapi.com/api/character/?species'
# solicitamos la información y guardamos la respuesta en data, 
# además encadenamos a la url la variable especie para que filtre los resultados por ese tipo.
data = requests.get(URL + "=" + especie) 
# Convertimos la respuesta en diccionario
data = data.json() 
# imprimimos los resultados
print(data)
