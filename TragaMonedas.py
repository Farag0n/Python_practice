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
# def checkResult():
    