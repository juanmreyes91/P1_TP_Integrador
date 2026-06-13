def menu():
    print("#############################################")
    print("Bienvenido al gestor de información de países")
    print("#############################################")
    print("Elija una opción del menú:")
    print("1) Agregar un país")
    print("2) Actualizar los datos de Población y Superficie")
    print("3) Buscar un país por nombre")
    print("4) Filtrar países (submenú)")
    print("5) Ordenar países (submenú)")
    print("6) Mostrar Estadísticas (submenú)")
    print("7) Salir")
    #Le pedimos al usuario que ingrese una opción
    op_menu = input("Ingrese una opción: ").strip()
    #Validamos la opción ingresada
    op_menu = validar_menu(op_menu)
    return op_menu

def validar_menu(op):
    #Creamos una función de vallidación para las opciones del menú
    while True:
        try:
            #Intentamos convertir la opción a entero
            op = int(op)
            #Analizamos si el usuario ingresó una opción válida para este menú
            if op > 7 or op < 1:
                raise Exception("La opción ingresada no es válida.")
        #Si hubo errores, notificar y volver a pedir una opción válida
        except ValueError:
            #Si el valor ingresado no es un dígito
            print("Error: Debe ingresar un caracter numérico.")
            op = input("Ingrese una opción del menú: ").strip()
        except Exception as e:
            print("Error: ", e)
            op = input("Ingrese una opción del menú: ").strip()
        else:
            return op
        
# Validación de texto ingresado
def validar_texto(texto):
    while True:
        try:
            if texto == "":
                #si se ingresó un campo vacío, notificamos el error
                raise ValueError("No se admiten campos vacíos.")
            elif texto.isdigit():
                raise TypeError("Solo se admiten letras en este campo.")
        except ValueError as e:
            print("Error: ", e)
            #seguimos pidiendo hasta que ingrese un campo válido
            texto = input("Intente nuevamente: ").strip().title()
        except TypeError as error:
            print("Error:", error)
            #seguimos pidiendo hasta que ingrese un campo válido
            texto = input("Intente nuevamente: ").strip().title()
        else:
            return texto
        
# Validación de enteros
def validar_entero(num):
    while True:
        try:
            #Intentamos convertir el número a entero
            num = int(num)
            #Analizamos que el usuario haya ingresado un número válido
            if num < 0:
                raise Exception("La cantidad ingresada debe ser positiva.")
        except ValueError:
            #Si el valor ingresado no es un dígito
            print("Error: Debe ingresar caracteres numéricos.")
            num = input("Intente nuevamente: ").strip()
        except Exception as e:
            #si el número ingresado no cumple con lo requerido por el sistema
            print("Error: ", e)
            num = input("Intente nuevamente: ").strip()
        else:
            return num
