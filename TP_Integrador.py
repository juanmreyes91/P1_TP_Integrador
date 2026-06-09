# El programa debe poder gestionar información sobre países,
# leer un archivo csv, realizar consultas y
# generar indicadores clave

# Estructuras: listas, diccionarios, funciones
# Archivos: CSV
# Una función, una responsabilidad
# Validación de entradas

####################################################
# Dataset: 
# Cada país estará representado por:
# Nombre (string)
# Población (int)
# Superficie en km**2 (int)
# Continente (string)
# nombre,población,superficie,continente
####################################################

####################################################
# Menú:
# Agregar un país (no se admiten campos vacíos)
# Actualizar los datos de población y superficie
# Buscar un país por nombre (coincidencia parcial o exacta)
# Filtrar países por: continente, rango de población y rango de superficies
# Ordenar países por: nombre, población y superficie (ascendente o descendente)
# Mostrar estadísticas: país con mayor y menor población, promedio de población, promedio de superficie y cantidad de países por continente
#####################################################

#####################################################
# Validaciones:
# Controlar errores de formato csv
# evitar fallos al ingresar filtros inválidos o búsquedas sin resultados
# mensajes claros de éxito/error
######################################################

######################################################
#######################  MENÚ  #######################
######################################################

# ACLARACIÓN!
#En los casos donde dice submenú podría pensarse de otra manera

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
            print("Debe ingresar un número válido.")
            op = input("Ingrese una opción del menú: ").strip()
        except Exception as e:
            print("Error: ", e)
            op = input("Ingrese una opción del menú: ").strip()
        else:
            return op

######################################################
#######################  MAIN  #######################
######################################################

#Definimos las estructuras de datos a utilizar
lista = []
diccionario = {}

#Inicializamos el menú
opcion = 0
while opcion != 7:
    opcion = menu()
    if opcion == 1:
        pass
    elif opcion == 2:
        pass
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass    
