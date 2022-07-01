from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
from telegram import ChatAction
import requests, urllib
import os
#from Credential import TOKENKEY, SECRET

TOKENKEY= os.getenv("TOKENKEY")#Esta linea es para heroku, comentala y decomenta la de arriba
SECRET= os.getenv("SECRET")

INPUT_TEXT=0

def start(update, context):
    user = update.message.from_user #usuario
    update.message.reply_text("Bienvendio "+user['first_name']+" "+ user['last_name']+", Consultemos el clima con los comandos.")

def climatico(update,context):
    update.message.reply_text("Nombre de la ciudad")
    return INPUT_TEXT

def input_text(update, context):
    text= update.message.text
    proceso(text,update,context)
    return ConversationHandler.END

def proceso(text,update,context):
    city= text

    try:
        url= "https://api.openweathermap.org/data/2.5/weather?q={}&lang=es&appid={}&units=metric".format(city,SECRET)

        res= requests.get(url)
        data= res.json()

        temp= data["main"]["temp"]
        temp_min= data["main"]["temp_min"]
        temp_max= data["main"]["temp_max"]
        humidity= data["main"]["humidity"]
        wind_speed= data["wind"]["speed"]

        latitude= data["coord"]["lat"]
        longitude= data["coord"]["lat"]

        description= data["weather"][0]["description"]
        update.message.reply_text("Ciudad: {}\nTemperatura °C: {}\nMIN/MAX °C: {}/{}\nHumedad %: {}\nVelocidad del viento m/s: {}\nLatitud: {}\nLongitud: {}\nDescripcion: {}".format(city,temp,temp_min,temp_max,humidity,wind_speed,latitude,longitude,description))
    except KeyError:
        update.message.reply_text("La ciudad es invalida, ingrese nuevamente el comando")

if __name__ == '__main__':

    updater= Updater(token=TOKENKEY, use_context=True)
    
    dp= updater.dispatcher

    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('weather',climatico),
        ],
        states={
            INPUT_TEXT:[MessageHandler(Filters.text, input_text)],
        },
        fallbacks=[]
    ))

    updater.start_polling()
    print("Bot Running")
    updater.idle()