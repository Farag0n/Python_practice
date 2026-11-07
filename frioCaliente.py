# hacer un juego en el que tengas que adivinar un numero
# y que puedas dar varias opciones y te diga si estas frio o caliente segun que tan cerca estes

import random

secret_number = random.randint(0, 100)

while True:
    
    try:
        guess = int(input("Ingrese un numero entre 0 y 100: \n"))

        if guess < 0 or guess > 100:
            print("El numero debe estar dentro del rango de 0-100")

    except ValueError:
        print("El valor ingresado es incorrecto o invalido")

    try:
        absResult = lambda a, b: abs(a - b)
        
        rangeNumber = absResult(secret_number, guess)
    except ValueError:
        print("Error inesperado")

    if rangeNumber == 0:
        print(f"Lo lograste el numero era: {secret_number}")
        break
    elif rangeNumber <= 5:
        print("Estas muy caliente")
    elif rangeNumber <= 20:
        print("Estas caliente")
    elif rangeNumber <= 29:
        print("Estas tibio")
    elif rangeNumber >= 30:
        print("Estas frio")
