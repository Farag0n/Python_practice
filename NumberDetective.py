
import random

base_characters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
attempt_counter = 0
max_attempts = 20


# Funcion para generar el codigo secreto
def createSecretCode():
    numberList = []

    for i in range(4):
        selectNumbers = random.choice(base_characters)
        numberList.append(str(selectNumbers))

    result = "".join(numberList)
    return result, numberList


# Funcion para validar el codigo ingresado
def inputCodeCheck(code):
    code = code.strip()

    if len(code) != 4 or not code.isdecimal():
        print("El codigo debe contener exactamente 4 digitos numericos")
        return False

    if not all(character in "0123456789" for character in code):
        print("El codigo contiene caracteres invalidos")
        return False

    return True


# Funcion para comparar ambos codigos
def compareCode(code, secret_code):
    if code == secret_code:
        print(f"Lo has conseguido.\nAmbos codigos son iguales: {secret_code} = {code}")
        return True

    return False


# Funcion para generar las pistas
def clueCode(code, secret_code):

    correctPosition = 0
    correctNumbers = 0

    secretRemaining = []
    guessRemaining = []

    # Comparamos los digitos en sus respectivas posiciones
    for secretDigit, guessDigit in zip(secret_code, code):

        if secretDigit == guessDigit:
            correctPosition += 1
        else:
            secretRemaining.append(secretDigit)
            guessRemaining.append(guessDigit)

    # Comprobamos si los digitos existen en otra posicion
    for digit in guessRemaining:

        if digit in secretRemaining:
            correctNumbers += 1
            secretRemaining.remove(digit)

    incorrectNumbers = 4 - correctPosition - correctNumbers

    print("\n--- Pistas ---")
    print(f"Digitos en posicion correcta: {correctPosition}")
    print(f"Digitos correctos en otra posicion: {correctNumbers}")
    print(f"Digitos incorrectos: {incorrectNumbers}")


# Generamos el codigo secreto
createResult = createSecretCode()
secret_code = createResult[0]


# Ciclo principal del juego
while attempt_counter < max_attempts:

    inputCode = input("\nIngrese un codigo numerico de 4 digitos: ")

    # Validamos la entrada
    if not inputCodeCheck(inputCode):
        continue

    # Registramos el intento
    attempt_counter += 1

    # Comprobamos si el usuario gano
    isFinish = compareCode(inputCode, secret_code)

    if isFinish:
        print(f"Intentos utilizados: {attempt_counter}")
        break

    # Generamos las pistas
    clueCode(inputCode, secret_code)

    print(f"Intentos restantes: {max_attempts - attempt_counter}")

    # Comprobamos si se agotaron los intentos
    if attempt_counter >= max_attempts:
        print(f"\nLo siento, has perdido. El codigo era: {secret_code}")
        break
