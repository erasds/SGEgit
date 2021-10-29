from operator import itemgetter
# “Key functions” per a ordenar llistes:
altura_peso = ([180,90],[170,60],[160,65],[190,90],[160,55])
peso = sorted(altura_peso, key=itemgetter(1))
# Primer ordenem per pes de menor a major
print(peso)
altura = sorted(peso, key=itemgetter(0), reverse=True)
# I mantenint l'ordre del pes, gràcies a haver-ho guardat en la variable, 
# ordenem per altura de major a menor.
print(altura)

"""
Les “key functions” son funcions d’un sol argument que son cridades 
una sola vegada per cada registre d’entrada. 
S’utilitzen per a ordenar de manera ràpida objectes complexos.
"""