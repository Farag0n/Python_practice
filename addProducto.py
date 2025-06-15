inventory = []

#Creamos una funcion para añadir productos al inventario
def addProduct():
    
    while True:
        
        

        print("-"*45)
        productName = input("\nNombre del producto que desea añadir: ").strip().lower()

        if len(productName) == 0:
            print("\n==== El nombre no puede estar vacio! =====")
            continue

        productPrice = (input("Precio unitario del producto: "))

        productQuantity = (input("Cantidad disponible del producto: "))

        try:
            productPrice = float(productPrice)
            if productPrice < 0:
                print("==== El precio no puede ser un nemero negativo ====")
                print("-"*45)               
                return

            productQuantity = int(productQuantity)
            if productQuantity <= 0:
                print("==== La cantidad no puede ser un numero negativo ====")
                print("-"*45)
                break

            print("-"*45)
            print("\n==== El producto se a añadido con exito! ====")
            print("-"*45)

            inventory.append({
                "name":productName,
                "price":productPrice,
                "quantity":productQuantity
            })

        except ValueError:
            print("==== El precio a la cantidad son invalidos ====")
            print("-"*45)

        repeat = input("Desea agregar otro producto?\n|Si|No|: ").strip().lower()
        if repeat == "no":
            print("Volviendo a el menu....")
            break
        elif repeat == "si":
            continue
        else:
            print("Opcion invalida, volviendo a el menu....\n")
            break