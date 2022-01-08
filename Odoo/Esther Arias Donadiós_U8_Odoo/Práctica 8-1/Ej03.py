import telebot
import logging
import requests
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# definimos el token de nuestro bot como una constante
API_TOKEN = "5078698425:AAH3Ah85otcCz832Av1JwzGc5-jzjDp4XwU"
# lo metemos dentro de la variable bot para poder usar las funciones de telebot
bot = telebot.TeleBot(API_TOKEN)

# Permitimos el inicio de sesión
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Definimos un mensaje incial que saltará con el comando /start
def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr'Hola {user.mention_markdown_v2()}\! He sido creado para ayudarte a realizar peticiones a la API REST Socios, utiliza el comando /help para ver las opciones disponibles\.',
        reply_markup=ForceReply(selective=True),
    )

# Definimos un mensaje con todos los comandos disponibles, que aparecerá cuando el usuario escriba "/help"
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Tienes a tu disposición los siguientes comandos: \n' +
        '/crear : Para crear un nuevo socio \n' +
        '/modificar : Para modificar datos de un socio existente \n' +
        '/consultar : Para consultar información de un socio \n' +
        '/borrar : Para eliminar a un socio \n')

# Definimos el comando "/crear" que se encargará de lanzar una llamada a la api rest
# y crear un nuevo socio con los datos proporcionados por el usuario
def crear_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Indica el nombre del socio:', reply_markup=ForceReply(selective=True),)
    nombre = update.message.text
    bot.register_next_step_handler(nombre, post)
    update.message.reply_text('Indica los apellidos del socio:', reply_markup=ForceReply(selective=True),)
    apellidos = update.message
    bot.register_next_step_handler(apellidos, post)
    update.message.reply_text('Indica el número de socio:', reply_markup=ForceReply(selective=True),)
    num_socio = update.message.reply_text
    bot.register_next_step_handler(num_socio, post)

def post(message):
    url = 'http://localhost:8069/gestion/apirest/socio?data={"num_socio":'+message+', "nombre":'+message+',"apellidos":'+message+'}'
    response = requests.post(url, timeout=0.20)
    if response.status_code == 200:
        data = response.json()
        message.reply_text(data[0]['name'])
    else:
        message.reply_text('Alguno de los campos introducidos no es válido')


def main() -> None:
    # Iniciamos el bot indicando el Token
    updater = Updater("5078698425:AAH3Ah85otcCz832Av1JwzGc5-jzjDp4XwU")
    dispatcher = updater.dispatcher

    # Indicamos la respuesta a los diferentes comandos en Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))
    dispatcher.add_handler(CommandHandler("crear", crear_command))

    # on non command i.e message - echo the message on Telegram
    #☻dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Iniciamos el bot de forma indefinida
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
