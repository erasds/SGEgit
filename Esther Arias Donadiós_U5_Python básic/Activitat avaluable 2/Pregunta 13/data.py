import requests  #Importamos la librería requests

print("SOLICITANDO INFORMACION DE INTERNET")
print("espere....") 
URL = 'https://rickandmortyapi.com/api/character' #configuramos la url
#solicitamos la información y guardamos la respuesta en data.
print("Indique la especie que desea buscar:")
especie = input()
data = requests.get(URL) 

json = data.json() #convertimos la respuesta en dict

print(json['specie'])

"""for element in data[]: #iteramos sobre data
    print(element['name']) #Accedemos a sus valores"""