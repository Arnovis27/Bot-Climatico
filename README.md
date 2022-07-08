# Bot-Climatico
Proyecto python para Telegram usando Openweathermap

## Conexion
Se solicita la creacion del agente virtual de telegram para generar el token de validacion, luego se consume generar las entradas de cada parametro para investigar su realizacion, continuamente se evalua el funcionamiento, acontinuacion se solicita a la API del clima el token y  la clave para acceder a los datos solicitados

## Proceso
Mediante una peticion GET se llama a una URL que lleva como parametro la ciudad y el token, como el formato que nos da en respuesta es un JSON, para acceder a cada parametro necesitamos acceder a cada posicion de la matriz para: temperatura, humedad, clima max/min, velocidad del viento, latitud, longitud, descripcion.

## Servidor
Heroku es una plataforma que nos montar en un servidor por cierto limite de forma gratuita mensualmente, para subirlo necesitamos crear un archivo con ```pip freeze > requirements.txt``` , el cual es usado para que heroku instale las librerias usadas al momento de montar el proyecto, del mismo modo creamos un archivo llamado **Procfile** que es un mecanismo para declarar qué comandos ejecuta su aplicación en la plataforma Heroku
