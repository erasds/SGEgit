import telebot
import requests

# definimos el token de nuestro bot como una constante
# el mio se llama Garuru_bot :)
API_TOKEN = "5078698425:AAH3Ah85otcCz832Av1JwzGc5-jzjDp4XwU"
# lo metemos dentro de la variable bot para poder usar las funciones de telebot
bot = telebot.TeleBot(API_TOKEN)


# Definimos una función donde vamos a redactar un mensaje de bienvenida del bot, 
# que además listará la información de los comandos que puede utilizar el usuario
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        'Bienvenid@, mi nombre es Garuru_bot \n' +
        '\n' +
        'He sido creado para ayudarte a realizar peticiones a la API-REST-Socios \n' +
        '\n' +
        'Tienes a tu disposición los siguientes comandos: \n' +
        '/crear : Para crear un nuevo socio \n' +
        '/modificar : Para modificar datos de un socio existente \n' +
        '/consultar : Para consultar información de un socio \n' +
        '/borrar : Para eliminar a un socio \n' +
        '/help : Para ver información sobre cómo usar los comandos'
    )

# Ahora definimos las funciones para cada uno de los comandos

# Definimos la función para el comando "help"
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(
        message.chat.id,
        'Para crear un socio escribe: \n' +
        '/crear ,nombre="nombre",apellidos="apellidos",num_socio="num_socio" \n' +
        'Para modificar un socio escribe: \n' +
        '/modificar ,nombre="nombre",apellidos="apellidos",num_socio="num_socio" \n' +
        'Para consultar un socio escribe: \n' +
        '/consultar ,num_socio="num_socio" \n' +
        'Para borrar un socio escribe: \n' +
        '/borrar ,num_socio="num_socio"'
    )

# Definimos la función para el comando "crear"
@bot.message_handler(commands=['crear'])
def crear_command(message):
    # guardamos el string del usuario en una variable
    datos = message.text
    # le indicamos que de ese string coja a partir de la posicion 8 (donde empieza "nombre...")
    # y hacemos los cambios para que tenga un formato que podamos usar en la llamada a la API
    datos = datos[8:].replace('=',':').replace('nombre','"nombre"').replace('apellidos','"apellidos"').replace('num_socio','"num_socio"')
    url = 'http://localhost:8069/gestion/apirest/socio?data={'+datos+'}'
    response = requests.post(url)
    # si la respuesta devuelve 200, es que se ha realizado correctamente 
    # y así lo indicamos con un mensaje al usuario
    if response.status_code == 200:
        bot.reply_to(
            message, 'Socio creado correctamente')
    # en caso contrario contestamos con un mensaje de error
    else:
        bot.reply_to(
            message, 'Alguno de los campos introducidos no es válido')

# Definimos la función para el comando "modificar"
@bot.message_handler(commands=['modificar'])
def modificar_command(message):
    # guardamos el string del usuario en una variable
    datos = message.text
    # le indicamos que de ese string coja a partir de la posicion 8 (donde empieza "nombre...")
    # y hacemos los cambios para que tenga un formato que podamos usar en la llamada a la API
    datos = datos[12:].replace('=',':').replace('nombre','"nombre"').replace('apellidos','"apellidos"').replace('num_socio','"num_socio"')
    url = 'http://localhost:8069/gestion/apirest/socio?data={'+datos+'}'
    response = requests.put(url)
    # si la respuesta devuelve 200, es que se ha realizado correctamente 
    # y así lo indicamos con un mensaje al usuario
    if response.status_code == 200:
        bot.reply_to(
            message, 'Socio modificado correctamente')
    # en caso contrario contestamos con un mensaje de error
    else:
        bot.reply_to(
            message, 'Alguno de los campos introducidos no es válido')

# Definimos la función para el comando "consultar"
@bot.message_handler(commands=['consultar'])
def consultar_command(message):
    # guardamos el string del usuario en una variable
    datos = message.text
    # le indicamos que de ese string coja a partir de la posicion 8 (donde empieza "num_socio...")
    # y hacemos los cambios para que tenga un formato que podamos usar en la llamada a la API
    datos = datos[12:].replace('=',':').replace('num_socio','"num_socio"')
    url = 'http://localhost:8069/gestion/apirest/socio?data={'+datos+'}'
    response = requests.get(url)
    salida = response.json()
    # si la respuesta devuelve 200, es que se ha realizado correctamente 
    # e imprimimos los datos del socio
    if response.status_code == 200:
        bot.reply_to(
            message, str(salida))
    # en caso contrario contestamos con un mensaje de error
    else:
        bot.reply_to(
            message, 'Alguno de los campos introducidos no es válido')

# Definimos la función para el comando "borrar"
@bot.message_handler(commands=['borrar'])
def borrar_command(message):
    # guardamos el string del usuario en una variable
    datos = message.text
    # le indicamos que de ese string coja a partir de la posicion 8 (donde empieza "num_socio...")
    # y hacemos los cambios para que tenga un formato que podamos usar en la llamada a la API
    datos = datos[9:].replace('=',':').replace('num_socio','"num_socio"')
    url = 'http://localhost:8069/gestion/apirest/socio?data={'+datos+'}'
    response = requests.delete(url)
    # si la respuesta devuelve 200, es que se ha realizado correctamente 
    # y así lo indicamos con un mensaje al usuario
    if response.status_code == 200:
        bot.reply_to(
            message, 'Socio eliminado correctamente')
    # en caso contrario contestamos con un mensaje de error
    else:
        bot.reply_to(
            message, 'Alguno de los campos introducidos no es válido')


def main() -> None:
    # Con polling indicamos que siga ejecutándose indefinidamente
    bot.polling()


# Iniciamos la aplicación
if __name__ == '__main__':
    main()