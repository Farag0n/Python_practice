#sistemas de gestion de calificaciones
# nuevo conocimiento: - Exception as e, guardar la mayoria de excepciones en una variable, no un unico error. 

import sys


class GradingSystem:
    """
    Sistema para gestionar calificaciones de estudiantes.
    Incluye manejo de errores.
    """

    def __init__(self):
        """Inicializa el sistema de calificaciones."""
        # Lista para almacenar las calificaciones ingresadas por el usuario
        self.grades = []
        # Umbral para considerar una calificación como aprobatoria (0-100)
        # Puedes ajustar este valor (ej. 70)
        self.passing_threshold= self.ask_for_threshold()
        self.llamarMenu= self.__menu__()
        #self.passing_threshold = 60 


    def ask_for_threshold(self):
        valor = input("Introduce el umbral de aprobación (decimal entre 0 y 100): ")
        try:
            valor_float = float(valor)
            if 0 <= valor_float <= 100:
                return valor_float
            else:
                print("El número debe estar entre 0 y 100.")
                return self.ask_for_threshold()
        except ValueError:
            print("Entrada inválida. Debe ser un número decimal.")
            return self.ask_for_threshold()


    def __print_option_menu__(self):
        """Imprime el menú de opciones en la consola."""
        
        print("\n" + "="*45)
        print(" === SISTEMA DE GESTIÓN DE CALIFICACIONES ===")
        print("="*45)
        # Muestra la lista actual
        print(f"  Lista actual: {self.grades}")
        # Muestra el umbral
        print(f"  Umbral de aprobación: {self.passing_threshold}")
        print("-"*45)
        print("  [1] Determinar estado de aprobación (Individual)")
        print("  [2] Ingresar/Actualizar lista de calificaciones")
        print("  [3] Calcular promedio de la lista")
        print("  [4] Contar calificaciones > valor (en lista)")
        print("  [5] Buscar y contar calificación (en lista)")
        print("  [6] Salir")
        print("-"*45)


    def __pause_and_continue__(self):
        """Pausa la ejecución hasta que el usuario presione Enter."""
        input("\n    Pulsa Enter para continuar...")


    # --- Menú Principal ---
    def __menu__(self):
        """Muestra el menú principal y maneja la selección del usuario."""
        while True:
            # Imprime el menú
            self.__print_option_menu__()
            # Pide la elección al usuario
            choice_str = input("  Introduce tu elección (1-6) > ")

            try:
                choice = int(choice_str)
               
                # Llama al método correspondiente según la elección
                if choice == 1:
                    print("\n--> [Opción 1: Determinar estado de aprobación (Individual)]")
                    self.check_individual_passing_status() # LLAMADA AL MÉTODO 
                    self.__pause_and_continue__()
                elif choice == 2:
                    print("\n--> [Opción 2: Ingresar/Actualizar lista de calificaciones]")
                    self.manage_grade_list() # LLAMADA AL MÉTODO 
                    self.__pause_and_continue__()
                elif choice == 3:
                    print("\n--> [Opción 3: Calcular promedio de la lista]")
                    self.calculate_average() # LLAMADA AL MÉTODO
                    self.__pause_and_continue__()
                elif choice == 4:
                    print("\n--> [Opción 4: Contar calificaciones > valor]")
                    self.count_grades_above_value() # LLAMADA AL MÉTODO
                    self.__pause_and_continue__()
                elif choice == 5:
                    print("\n--> [Opción 5: Buscar y contar calificación específica]")
                    self.find_and_count_specific_grade() # LLAMADA AL MÉTODO 
                    
                    self.__pause_and_continue__()
                elif choice == 6:
                    # Mensaje de salida
                    print("\nSaliendo del sistema. ¡Hasta luego!")
                    sys.exit() # Sale del programa
                else:
                    # Opción numérica fuera de rango
                    print(f"\n(!) Error: '{choice}' no es una opción válida. Elige entre 1 y 6.")
                    self.__pause_and_continue__()

            except ValueError:
                # La entrada no fue un número entero
                print(f"\n(!) Error: '{choice_str}' no es un número válido. Introduce un número entero.")
                self.__pause_and_continue__()
            except Exception as e:
                # Captura cualquier otro error inesperado en el menú
                print(f"\n(!) Ocurrió un error inesperado en el menú: {e}")
                self.__pause_and_continue__()    


    # --- Opción 1: Determinar estado de aprobación ---
    def check_individual_passing_status(self):
        """Solicita una calificación y determina si aprobó o reprobó."""
        try:
            grade_str = input("   Introduce la calificación numérica (0-100): ")
            # Convertir a número decimal
            grade = float(grade_str)

            if 0 <= grade <= 100:
                if grade >= self.passing_threshold:
                    # Mensaje de APROBADO 
                    print(f"   Resultado: APROBADO (Calificación: {grade}, Umbral: {self.passing_threshold})")
                else:
                    # Mensaje de REPROBADO 
                    print(f"   Resultado: REPROBADO (Calificación: {grade}, Umbral: {self.passing_threshold})")
            else:
                # Error de rango
                print("   (!) Error: La calificación debe estar entre 0 y 100.")

        except ValueError:
            # Error de conversión numérica
            print(f"   (!) Error: '{grade_str}' no es una entrada numérica válida.")
        except Exception as e:
            # Otro error
            print(f"   (!) Ocurrió un error inesperado: {e}")


    # --- Opción 2: Ingresar/Actualizar lista de calificaciones ---
    def manage_grade_list(self):
        """Solicita una lista de calificaciones separadas por comas y actualiza la lista interna."""
        
        print("   Introduce las calificaciones separadas por comas (ej: 75, 88, 92.5, 60)")
        
        grade_list_str = input("    ")

        temporary_grades = []
        
        # Divide la entrada por comas
        items = grade_list_str.split(',')
        
        # Bandera para validar la entrada completa
        is_valid = True

        for item in items:
            try:
                # Limpiar espacios y convertir a número
                grade_num = float(item.strip())
                if 0 <= grade_num <= 100:
                    temporary_grades.append(grade_num)
                else:
                    # Error: Calificación fuera de rango
                    print(f"   (!) Error: La calificación '{item.strip()}' está fuera del rango (0-100). No se actualizará la lista.")
                    is_valid = False
                    # Detener el proceso si una calificación es inválida
                    break
            except ValueError:
                 # Error: Elemento no es un número
                print(f"   (!) Error: El elemento '{item.strip()}' no es un número válido. No se actualizará la lista.")
                is_valid = False
                 # Detener el proceso si un elemento no es número
                break

        # Solo actualiza si todo fue válido y hay algo que añadir
        if is_valid and temporary_grades:
            self.grades = temporary_grades
             # Mensaje de éxito 
            print(f"   Lista de calificaciones actualizada: {self.grades}")
        elif not is_valid:
             # Mensaje si hubo errores
             print("   La lista de calificaciones no ha sido modificada debido a errores.")
        else:
             # Mensaje si no se ingresaron calificaciones válidas
            print("   No se ingresaron calificaciones válidas.")


 # --- Opción 3: Calcular promedio de la lista ---
    def calculate_average(self):
        """Calcula y muestra el promedio de la lista actual de calificaciones."""
        # Verifica si la lista está vacía
        if not self.grades:
            print("   (!) Error: La lista de calificaciones está vacía. Ingresa calificaciones primero (Opción 2).")
             # Salir del método si no hay calificaciones
            return

        try:
            # Calcula el promedio 
            average = sum(self.grades) / len(self.grades)
             # Muestra el promedio formateado 
            print(f"   El promedio de las {len(self.grades)} calificaciones es: {average:.2f}")
        
        except ZeroDivisionError:
             print("   (!) Error: No se puede dividir por cero (lista vacía).")
        except Exception as e:
            # Otro error
            print(f"   (!) Ocurrió un error inesperado al calcular el promedio: {e}")


    # --- Opción 4: Contar calificaciones mayores a un valor ---
    def count_grades_above_value(self):
        """Pregunta por un valor y cuenta cuántas calificaciones en la lista son mayores."""
         # Verifica si la lista está vacía
        if not self.grades:
            print("   (!) Error: La lista de calificaciones está vacía. Ingresa calificaciones primero (Opción 2).")
            return

        try:
            # Pide el valor de referencia
            value_str = input("   Introduce la nota de referencia para comparar: ")
            reference_value = float(value_str)

            # Inicializa contador
            counter = 0
            # Recorre la lista de calificaciones 
            for grade in self.grades:
                if grade > reference_value:
                    counter += 1
            # Muestra el resultado
            print(f"   Hay {counter} calificaciones mayores que {reference_value} en la lista.")

        except ValueError:
             # Error de conversión numérica
            print(f"   (!) Error: '{value_str}' no es un número válido.")
        except Exception as e:
             # Otro error
             print(f"   (!) Ocurrió un error inesperado: {e}")


    # --- Opción 5: Buscar y contar calificación específica ---
    def find_and_count_specific_grade(self):
        """Busca una calificación específica en la lista y cuenta sus apariciones usando continue."""
         # Verifica si la lista está vacía
        if not self.grades:
            print("   (!) Error: La lista de calificaciones está vacía. Ingresa calificaciones primero (Opción 2).")
            return

        try:
            # Pide la calificación a buscar
            search_grade_str = input("   Introduce la calificación específica a buscar y contar: ")
            searched_grade = float(search_grade_str)

            # Inicializa contador 
            counter = 0
            found = False
            # Recorre la lista 
            for grade in self.grades:
                
                # Si no es la calificación buscada, simplemente continuamos con la siguiente
                
                if grade != searched_grade:
                    continue
                counter += 1
                found = True
                

            if found:
        
                times_str = "vez" if counter == 1 else "veces"
                print(f"   La calificación {searched_grade} aparece {counter} {times_str} en la lista.")
            else:
                
                print(f"   La calificación {searched_grade} no se encontró en la lista.")

        except ValueError:
             
            print(f"   (!) Error: '{search_grade_str}' no es un número válido.")
        except Exception as e:
             
            print(f"   (!) Ocurrió un error inesperado: {e}")


    
  


GradeManager=GradingSystem()
#GradeManager.__menu__()