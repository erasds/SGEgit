import telebot
import requests
from telebot.types import ForceReply
from telegram import replymarkup



# definimos el token de nuestro bot como una constante
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
        '/borrar : Para eliminar a un socio \n'
    )

# Ahora definimos una función para cada comando que pida los datos al usuario y haga la llamada al api rest

# Definimos la función para el comando "crear"
@bot.message_handler(commands=['crear'])
def crear_command(message):
    bot.send_message(message.chat.id, "Indique el campo nombre:", reply_markup=ForceReply(selective=True))
    nombre = message.text, replymarkup
    bot.reply_to(message, "Indique el campo apellidos:", reply_markup=ForceReply(selective=True))
    apellidos = message.text
    bot.reply_to(message, "Indique el número de socio:", reply_markup=ForceReply(selective=True))
    num_socio = message.text
    url = 'http://localhost:8069/gestion/apirest/socio?data={"num_socio":'+num_socio+', "nombre":'+nombre+',"apellidos":'+apellidos+'}'
    response = requests.post(url, timeout=0.20)
    if response.status_code == 200:
        data = response.json()
        bot.send_message(
            message.chat.id, data[0]['name'])
    else:
        bot.reply_to(
            message, 'Alguno de los campos introducidos no es válido')

# Definimos la función para el comando "modificar"
@bot.message_handler(commands=['modificar'])
def modificar_command(message):
    bot.send_message("Indique el campo nombre:")
    nombre = message.text
    bot.send_message("Indique el campo apellidos:")
    apellidos = message.text
    bot.send_message("Indique el número de socio:")
    num_socio = message.text
    url = 'http://localhost:8069/gestion/apirest/socio?data={"num_socio":'+num_socio+', "nombre":'+nombre+',"apellidos":'+apellidos+'}'
    response = requests.put(url, timeout=0.01)
    if response.status_code == 200:
        data = response.json()
        bot.send_message(
            message.chat.id, data[0]['name'])
    else:
        bot.reply_to(
            message, 'Alguno de los campos introducidos no es válido')

# Definimos la función para el comando "consultar"
@bot.message_handler(commands=['consultar'])
def consultar_command(message):
    bot.send_message("Indique el número de socio:")
    num_socio = message.text
    url = 'http://localhost:8069/gestion/apirest/socio?data={"num_socio":'+num_socio+'}'
    response = requests.get(url, timeout=0.01)
    if response.status_code == 200:
        data = response.json()
        bot.send_message(
            message.chat.id, data[0]['name'])
    else:
        bot.reply_to(
            message, 'El número de socio no es válido')

# Definimos la función para el comando "borrar"
@bot.message_handler(commands=['borrar'])
def borrar_command(message):
    bot.send_message("Indique el número de socio:")
    num_socio = message.text
    url = 'http://localhost:8069/gestion/apirest/socio?data={"num_socio":'+num_socio+'}'
    response = requests.delete(url, timeout=0.01)
    if response.status_code == 200:
        data = response.json()
        bot.send_message(
            message.chat.id, data[0]['name'])
    else:
        bot.reply_to(
            message, 'El número de socio no es válido')



def main() -> None:
    # Con polling indicamos que siga ejecutándose indefinidamente
    bot.polling()


# Iniciamos la aplicación
if __name__ == '__main__':
    main()