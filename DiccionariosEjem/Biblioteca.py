
libros = {}

#Función para agregar un nuevo libro
def crear_libro():
    id_libro = input("Ingrese el ID del libro: ")
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año_publicacion = input("Ingrese el año de publicación del libro: ")
    
    libro = {
        "Título": titulo,
        "Autor": autor,
        "Año de publicación": año_publicacion
    }
    
    libros[id_libro] = libro
    print("Libro agregado con éxito.")

#Función para mostrar todos los libros
def leer_libros():
    if not libros:
        print("No hay libros registrados.")
    else:
        for id_libro, libro in libros.items():
            print(f"ID: {id_libro}")
            print(f"Título: {libro['Título']}")
            print(f"Autor: {libro['Autor']}")
            print(f"Año de publicación: {libro['Año de publicación']}")
            print("------------------------")

#Función para buscar un libro por ID o título
def buscar_libro():
    opcion = input("Buscar por ID (1) o Título (2): ")
    
    if opcion == "1":
        id_libro = input("Ingrese el ID del libro: ")
        if id_libro in libros:
            libro = libros[id_libro]
            print(f"ID: {id_libro}")
            print(f"Título: {libro['Título']}")
            print(f"Autor: {libro['Autor']}")
            print(f"Año de publicación: {libro['Año de publicación']}")
        else:
            print("Libro no encontrado.")
    elif opcion == "2":
        titulo = input("Ingrese el título del libro: ")
        encontrado = False
        for id_libro, libro in libros.items():
            if libro["Título"].lower() == titulo.lower():
                print(f"ID: {id_libro}")
                print(f"Título: {libro['Título']}")
                print(f"Autor: {libro['Autor']}")
                print(f"Año de publicación: {libro['Año de publicación']}")
                encontrado = True
        if not encontrado:
            print("Libro no encontrado.")
    else:
        print("Opción inválida.")

#Función para actualizar un libro
def actualizar_libro():
    id_libro = input("Ingrese el ID del libro: ")
    if id_libro in libros:
        libro = libros[id_libro]
        print("Ingrese la nueva información (deje en blanco para no cambiar):")
        titulo = input(f"Título ({libro['Título']}): ")
        autor = input(f"Autor ({libro['Autor']}): ")
        año_publicacion = input(f"Año de publicación ({libro['Año de publicación']}): ")
        
        if titulo:
            libro["Título"] = titulo
        if autor:
            libro["Autor"] = autor
        if año_publicacion:
            libro["Año de publicación"] = año_publicacion
        
        print("Libro actualizado con éxito.")
    else:
        print("Libro no encontrado.")

#Función para eliminar un libro
def eliminar_libro():
    id_libro = input("Ingrese el ID del libro: ")
    if id_libro in libros:
        del libros[id_libro]
        print("Libro eliminado con éxito.")
    else:
        print("Libro no encontrado.")

#Menú principal
while True:
    print("1. Agregar libro")
    print("2. Mostrar libros")
    print("3. Buscar libro")
    print("4. Actualizar libro")
    print("5. Eliminar libro")
    print("6. Salir")
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        crear_libro()
    elif opcion == "2":
        leer_libros()
    elif opcion == "3":
        buscar_libro()
    elif opcion == "4":
        actualizar_libro()
    elif opcion == "5":
        eliminar_libro()
    elif opcion == "6":
        break
    else:
        print("Opción inválida.")
