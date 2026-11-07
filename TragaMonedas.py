import random

itemsList = ["🥭","🍎","🍒"]

# ============================================================
# Esta version usa una funcion de la libreria random
# que permite hacer el juego de forma mas sencilla 
# def playGameEasy():
#     result = random.choices(itemsList, k=len(itemsList))
#     print(result)
# ============================================================

def resultGenerator():
    # Creamos dos variables, nItems para guardar la cantidad de items en la lista
    # y result que es donde se va a almacenar el resultado de la ijteracion
    nItems = len(itemsList)
    result =[]

    for i in range(nItems):
        # selectItems es una variable que se le asigna los items elegidos con la cantidad correcta
        selectItems = random.choice(itemsList)
        # se le agrega los items elegidos a eel resultado
        result.append(selectItems)
    return result

# Funcion para verificar si todos los items son iguales
def checkResult():
    resultValues = resultGenerator()
    jackpot = len(set(resultValues)) == 1
    if jackpot:
        print(f"{resultValues} Ganaste")
    else:
        print(f"{resultValues} Lo siento vuelve a intentar")

while True:
    select = input("Precione 1 para jugar o 0 para salir")

    match select:
        case "1":
            checkResult()
        case "0":
            print("Hasta la proxima")
            break
        
