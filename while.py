# el while s e usa para inciar el bucle de un bloque de codigo si una condicion se cumple o no
pasword = "Triqui_tracatelas17"
userPass = input("------ingrese la contraseña------\n")

while pasword != userPass:
    print("------Error,clave incorrecta------")
    userPass = input("Ingrese denuevo la contraseña\n")
else:
    print("Clave correcta")
#hay bastantes metodos que se suelen utilizar para cuando se necesita "retornar" algo si el ciclo no se cumple
#como usar el else, el break para terminar el ciclo o incluso if para cumplir alguna condicion dentro del mismo ciclo

