
#if se suele usar para la primera condicion y el elif para cuando se necesita hace mas "verificaciones"


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
        #el else es cuando no se cumple ninguna y al no cumplirse ninguna deber "retornar" algo
        