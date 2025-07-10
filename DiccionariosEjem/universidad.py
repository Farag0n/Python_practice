estudiantes = {
 'a':{
       'Nombre': 'uhjasndaisdasdasasdd',
    'Edad' : '26',
    'Numero id': '3', 
    'Nota': 5.0
},
'b':{
       'Nombre ': 'uhjasndaisghjghdasdasasdd', 
    'Edad' : '27',
    'Numero id': '1', 
    'Nota': 3.7
 },
'c':{
       'Nombre ': 'uhjasdddndaisdasdasasdd',
    'Edad' : '18',
    'Numero id': '15',
    'Nota': 1.5
    },
'd':{
       'Nombre ': 'uhjasnd555aisdasdasasdd',
    'Edad' : '19',
    'Numero id': '12',
    'Nota': 3.1
    },
'e':{
       'Nombre ': 'uhjasndaisdayyysdasasdd', 
 'Edad' : '22',
 'Numero id': '11', 
 'Nota': 4.5
 },

}
def agregar_nuevos () :
    try:
        numero_id = input("Ingrese tu numero id: ")
        nombre = input("Ingrese tu nombre completo: ")
        edad = input("Ingrese tu edad ")
        nota = float(input("Ingrese tu nota (0.0 a 5.0):  "))

        nuevo = {

            "Nombre": nombre,
            "Edad" :  edad,
            "Nota" : nota
        }

        estudiantes[numero_id] = nuevo
        print("Estudiante agregado con éxito.")
        if numero_id not in estudiantes:          
            if nota < 0.0 or nota > 5.0 :
                            print ("Nota incorrecta, escribe otra entre 0.0 y 5.0 ")
            elif edad < 0 :
                            print ("Edad incorrecta, debe ser positivo")
            else:
                estudiantes[id] = {"nombre" : nombre, "edad" : edad, "nota" : nota }
                print ("Estudiante ha sido agregado correctamente ") 
        else:
             print ("Has introducido mal el id, pon otro " )
    except ValueError:
            print("Ingrese correctamente los datos ")
"""            
def buscar_estudiantes():
        opcion = input("Buscar por Nombre (1) o ID (2): ")
        if opcion == "1":
            Nombre_estudiante = input ("Ingrese el nombre del estudiante a buscar: ")
        elif opcion == "2":
            id_estudiante = input ("Ingese el id del estudiante a buscar")
        
                
        
        """
            
        # A este codigo le falta usar try except y el match case para el menu
while True:
    print("1. Agregar nuevos estudiantes")
    print("2. Buscar estudiantes (por ID o nombre):")
    print("3. Actualizar información de un estudiante:")
    print("4. Eliminar estudiantes:")
    print("5. Calcular el promedio de notas:")
    print("6. Listar estudiantes con notas inferiores a un umbral (por ejemplo, 3.0):")
    print(" Salir " )
    
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        agregar_nuevos()
    elif opcion == "2":
        ()
    elif opcion == "3":
       ()
    elif opcion == "4":
        ()
    elif opcion == "5":
        ()
    elif opcion == "6":
        break
    else:
        print("Opción inválida.")
















        
        

