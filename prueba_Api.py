#Se importan las librerias necesarias
import urllib.request
import json
from datetime import datetime

#Se crea una funcion para hacer la llamada a la API
def informationClimate (ciudad, apiKey):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={apiKey}&units=metric&lang=es"

    #Esta parte del with todavia no la entiendo myu bien pero se que es la que pide y recibe los datos de la API
    #El as es para ponerle un alias a un modulo
    with urllib.request.urlopen(url) as response:
        
        #Se le asigna a data los datos de la api y los lee para guardarlos(los guarda en un JSON)
        jsonData = response.read()

        #Limpiamos el dato JSON trasnformandolo a un objeto en Python
        clearData = json.loads(jsonData)
        print(clearData)
        
        return clearData


#Se crea una funcion para la busqueda de un lugar especifico he imprimir la info
def searchTimeSet():

    searchLocation = input("Ingrese la ciudad de la que desea conocer el clima: ")

    infoReturn = informationClimate(searchLocation,"c9aa8face8464a021c4dd8e40531fdf1")
    
    sunrise = infoReturn['sys']['sunrise']
    sunset = infoReturn['sys']['sunset']

    dateHourRise =  1747369899
    dateHourSet = 17474222

    hourSunset = datetime.time(dateHourSet)
    hourSunrise = datetime.time(dateHourRise)

    print(f"Pais: {infoReturn['sys']['country']}\nCiudad: {infoReturn['name']}\nClima: {infoReturn['weather'][0]['description']}\nTemperatura: {infoReturn['main']['temp']}°C\nSensacion termica de: {infoReturn['main']['feels_like']}°C")
    print(f"Amanece a las: {hourSunrise}\nAnochese a las: {hourSunset}")



searchTimeSet()


