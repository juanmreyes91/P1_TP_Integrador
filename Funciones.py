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

#####################################################
###################### FUNCIONES ####################
#####################################################

# Escritura basada en diccionarios
def escritura_archivo(archivo, diccionario):
    #Definimos el orden como claves del diccionario
    columnas = ["nombre", "poblacion" , "superficie", "continente"]
    with open(archivo, "a", encoding="utf-8") as ar:
        #Creamos el escritor indicando los nombres de columnas
        escritor_dict = csv.DictWriter(archivo, fieldnames=columnas)
        #Escribimos los datos
        escritor_dict.writerow(diccionario)

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
                raise ValueError("La cantidad ingresada debe ser positiva.")
        except ValueError:
            #Si el valor ingresado no es un dígito
            print("Debe ingresar un número válido.")
            num = input("Intente nuevamente: ").strip()
        except Exception as e:
            #si el número ingresado no cumple con lo requerido por el sistema
            print("Error: ", e)
            num = input("Intente nuevamente: ").strip()
        else:
            return num
        
#Validación de nombre repetido
def validar_repetido(texto):
    while True:
        try:
            pass
        except:
            pass
        else:
            return texto


#Creamos la función de la opción 1
def agregar_pais(datos):
    #creamos el diccionario auxiliar
    datos_pais = {}
    #Le pedimos los datos al usuario
    nombre = input("Ingrese el nombre del país que desea agregar: ").strip().title()
    #validación
    nombre = validar_texto(nombre)
    nombre = validar_repetido(nombre)
    poblacion = input("Ingrese la población de dicho país: ").strip()
    #validación
    poblacion = validar_entero(poblacion)
    superficie = input("Ingrese la superficie del país: ").strip()
    #Validación
    superficie = validar_entero(superficie)
    continente = input("Ingrese el continente al que pertenece el país: ").strip().title()
    #Validación
    continente = validar_texto(continente)
    #FALTA VALIDAR REPETIDOS
    #Agregamos los datos ya validados al diccionario
    datos_pais["nombre"] = nombre
    datos_pais["población"] = poblacion
    datos_pais["superficie"] = superficie
    datos_pais["continente"] = continente
    #Invocamos a la función de escritura para agregar los datos al archivo
    escritura_archivo(datos, datos_pais)