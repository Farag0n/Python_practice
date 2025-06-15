#El usuario ingresa su edad
years = int(input("Ingrese su edad: \n"))



#validamos la informacion y damos la salida correspondiente
if years >= 60:
    print("Eres un adulto mayor")
elif years > 17 and years < 60:
    print("Eres un adulto")
elif years >= 12 and years <= 17:
    print("Eres un adolecente")
elif years < 12: 
    print("Eres un niño")
else:
    print("Error, por favor intente de nuevo")