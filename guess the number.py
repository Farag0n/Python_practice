#importamos la libreria random
import random

#declaramos varables globales
num = random.randint(0,50)
print("--------Start Game--------\nEl numero va de 0-50")
answer = int(input("¿Que numero es\n"))
stateWhile = True
counter = 0


#el while funciona mientras la respuesta sea incorrecta
while stateWhile:
    
    #contador de intentos
    counter += 1

    if num != answer:
        print("Ese no es, jajaja. Intenta de nuevo")

        #pistas
        if answer < num:
             print("(El numero es mayor)")
             answer = int(input())
        elif answer > num:
             print("(El numero es menor)")
             answer = int(input())
    #el while finaliza al ganar el juego
    elif num == answer:
        stateWhile = False
        print("--------Ganaste, el numero es correcto--------")
        print(f"Numero de intentos: {counter}\n")



    
        

    

