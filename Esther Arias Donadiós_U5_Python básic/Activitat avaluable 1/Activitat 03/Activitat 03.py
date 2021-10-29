import hashlib
# Primer definim la llista amb les parelles d'usuari i contrasenya
user_password = [["Antonio", "lerele18"], ["Elena", "passw0rd"], ["Ruben", "MLN678"], ["Dario", "StupidFlanders"], ["Cristina", "Cris123"]]
# Ara anem a codificar cada una de les contrasenyes.
# Anem a fer-ho creant una nova instància de hashlib a la que li pasem com a 
# paràmetres el codi en el que volem fer la codificació ("sha1"), i la contrasenya
h0 = hashlib.new("sha1", b"lerele18")
user_password[0][1] = h0.hexdigest()
# Per últim cambiem la contrasenya original per la modificada a la llista
h1 = hashlib.new("sha1", b"passw0rd")
user_password[1][1] = h1.hexdigest()

h2 = hashlib.new("sha1", b"MLN678")
user_password[2][1] = h2.hexdigest()

h3 = hashlib.new("sha1", b"StupidFlanders")
user_password[3][1] = h3.hexdigest()

h4 = hashlib.new("sha1", b"Cris123")
user_password[4][1] = h4.hexdigest()
# Imprimim la llista per a poder vore el resultat
print(user_password)

# Ara anem a fer el mateix amb un diccionari on les claus seran el nom dels usuaris, i el valor, la contrasenya
dicc_user_pass = {"Antonio":"lerele18", "Elena":"passw0rd", "Ruben":"MLN678", "Dario":"StupidFlanders", "Cristina":"Cris123"}
# Per fer-ho un poc diferent anem a cambiar la forma en la que cridem al métode
# i també el resultat, en lugar de codificar-ho en hexadecimal, utilitzarem digest().
ha0 = hashlib.sha1(b"lerele18")
dicc_user_pass["Antonio"] = ha0.digest()
# Repetim el procés d'intercambiar les contrasenyes per el resultat, utilitzant la clau per a indicar la posició
ha1 = hashlib.sha1(b"passw0rd")
dicc_user_pass["Elena"] = ha1.digest()

ha2 = hashlib.sha1(b"MLN678")
dicc_user_pass["Ruben"] = ha2.digest()

ha3 = hashlib.sha1(b"StupidFlanders")
dicc_user_pass["Dario"] = ha3.digest()

ha4 = hashlib.sha1(b"Cris123")
dicc_user_pass["Cristina"] = ha4.digest()
# Imprimim el diccionari per a poder vore el resultat
print(dicc_user_pass)

