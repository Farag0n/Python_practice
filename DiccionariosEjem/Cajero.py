saldo = 0
historial = []

while True:
    print("\nMenú de opciones:")
    print("1. Ver saldo")
    print("2. Retirar dinero")
    print("3. Depositar dinero")
    print("4. Ver historial de movimientos")
    print("5. Salir")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        print(f"Saldo actual: {saldo}")
    elif opcion == "2":
        try:
            dinero = float(input("Ingrese el dinero a retirar: "))
            if dinero > saldo:
                print("Fondos insuficientes")
            else:
                saldo -= dinero
                historial.append({"tipo": "retiro", "dinero": dinero})
                print(f"Retiro realizado con éxito. Saldo actual: {saldo}")
        except ValueError:
            print("dinero inválido")
    elif opcion == "3":
        try:
            dinero = float(input("Ingrese el dinero a depositar: "))
            if dinero <= 0:
                print("dinero inválido")
            else:
                saldo += dinero
                historial.append({"tipo": "depósito", "dinero": dinero})
                print(f"Depósito realizado con éxito. Saldo actual: {saldo}")
        except ValueError:
            print("Monto inválido")
    elif opcion == "4":
        print("Historial de movimientos:")
        for movimiento in historial:
            print(f"Tipo: {movimiento['tipo']}, dinero: {movimiento['dinero']}")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")
