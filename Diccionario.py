numbers = {
    1:"Uno",
    2:"Dos",
    3:"Tres",
    4:"Cuatro",
    "Data":{
        "Nombre":"Jose andrea",
        "Cedula":1023242825,    
        "Numero":3008228812
        },
    5:"Cinco"
}

#Acceder a el valor de una clave
#print(numbers[4])

#Acceder a una valor con la clave, en este caso la clave es otro diccionario
#print(numbers["Data"])

#Entramos a numbers despues a el valor de Data y despues a el valor de numero
#print(numbers["Data"]["Numero"])

#----------------------------------------------------------------------------

#Lista con diccionario
numbersList = [{
    1:"Uno",
    2:"Dos",
    3:"Tres",
    4:"Cuatro",
    "Data":{
        "Nombre":"Jose andrea",
        "Cedula":1023242825,    
        "Numero":3008228812
        },
    5:"Cinco"
    },
    {
    "Motor":True,
    "Aceleracion":False,
    "Tanque":1.6
    }]

#Para acceder a los valores de diccionarios dentro de listas se usa el indice al que se desee acceder de la lista y despues a la clave del valor que queremos
print(numbersList[0][1])

#----------------------------------------------------------------------------

#Guardar datos en un diccionario
