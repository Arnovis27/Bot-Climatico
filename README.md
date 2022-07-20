# Bot-Climatico
Proyecto python para Telegram usando Openweathermap creacion de agente virtual para saber el estado del clima en alguna ciudad

## Funcionalidades
**Funcionalidad 1:** Consumir los datos en tiempo real de [OpenweatherApi](https://openweathermap.org/)  
**Funcionalidad 2:** Realizar la conexion a telegram para generar un bot  
**Funcionalidad 3:** Gestionar y enlazar el programa el bot creado en telegram  
**Funcionalidad 4:** Generar los comandos correspondientes del bot  
**Funcionalidad 5:** Devolver los datos del clima para la consulta correspondiente  
**Funcionalidad 6:** Montar el servicio en un servidor (HEROKU)

## Instalación
Puedes intalarlo clonando el repositorio con ```$ git clone url```

## Como se usa
Para iniciar el programa debes abrir desde el CMD el archivo ```app.py```

### Conexion
Se solicita la creacion del agente virtual de telegram para generar el token de validacion, luego se consume generar las entradas de cada parametro para investigar su realizacion, continuamente se evalua el funcionamiento, acontinuacion se solicita a la API del clima el token y  la clave para acceder a los datos solicitados

### Proceso
Mediante una peticion GET se llama a una URL que lleva como parametro la ciudad y el token, como el formato que nos da en respuesta es un JSON, para acceder a cada parametro necesitamos acceder a cada posicion de la matriz para: temperatura, humedad, clima max/min, velocidad del viento, latitud, longitud, descripcion.

### Servidor
Heroku es una plataforma que nos montar en un servidor por cierto limite de forma gratuita mensualmente, para subirlo necesitamos crear un archivo con ```pip freeze > requirements.txt``` , el cual es usado para que heroku instale las librerias usadas al momento de montar el proyecto, del mismo modo creamos un archivo llamado **Procfile** que es un mecanismo para declarar qué comandos ejecuta su aplicación en la plataforma Heroku

## Estado del proyecto
El proyecto se encuentra terminado
