def hello (name, lastName):
    print("Hello", name, lastName)

hello("Jorge", "Hernandez")

def multiplicarSum (a, b, num1, num2):
    resultadoMulti = a * b
    resultadoSum = num1 + num2
    return resultadoMulti, resultadoSum

valorMulti, valorSum = multiplicarSum(2,5,50,50)
#Formas de acceder a los datos dentro de una funcion
print(valorSum)
print(valorMulti)

total = multiplicarSum(5,2,100,100)
print(total[0])
