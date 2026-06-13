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
    print("2) Actualizar los datos (submenú)")
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

def validar_submenu(op_sub):
    #Creamos una función de vallidación para las opciones del submenú
    while True:
        try:
            #Intentamos convertir la opción a entero
            op_sub = int(op_sub)
            #Analizamos si el usuario ingresó una opción válida para este menú
            if op_sub > 2 or op_sub < 1:
                raise Exception("La opción ingresada no es válida.")
        #Si hubo errores, notificar y volver a pedir una opción válida
        except ValueError:
            #Si el valor ingresado no es un dígito
            print("Debe ingresar un número válido.")
            op_sub = input("Ingrese una opción del menú: ").strip()
        except Exception as e:
            print("Error: ", e)
            op_sub = input("Ingrese una opción del submenú: ").strip()
        else:
            return op_sub

#####################################################
################### VALIDACIONES ####################
#####################################################
import csv

# Validación de nombre repetido
# Lectura basada en diccionarios
def validar_repetido(archivo, texto):
    try:
        with open(archivo, "r", encoding="utf-8") as ar:
            lector_dict = csv.DictReader(ar)
            for diccionario in lector_dict:
                if texto == diccionario['nombre']:
                    #si se ingresó un campo ya existente, notificamos el error
                    raise ValueError("El país ingresado ya está registrado!")
    except ValueError as e:
        print("Error:", e)
        print()
        return None
    return texto

def validar_existencia(archivo, texto):
    try:
        with open(archivo, "r", encoding="utf-8") as ar:
            lector_dict = csv.DictReader(ar)
            for diccionario in lector_dict:
                if texto == diccionario['nombre']:
                    return texto
            raise ValueError(f"El país {texto} no está en la lista.")
    except ValueError as e:
        print("Error:", e)
        print()
        return None


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

#############################################
############ FUNCIONES AUXILIARES ###########
#############################################

# Escritura basada en diccionarios
def escritura_archivo(archivo, diccionario):
    #Definimos el orden como claves del diccionario
    columnas = ["nombre", "poblacion" , "superficie", "continente"]
    with open(archivo, "a", encoding="utf-8",  newline="") as ar:
        #Creamos el escritor indicando los nombres de columnas
        escritor_dict = csv.DictWriter(ar, fieldnames=columnas)
        #Escribimos los datos
        escritor_dict.writerow(diccionario)

def actualizacion_archivo(archivo, texto, numero, submenu):
    #Definimos el orden como claves del diccionario
    columnas = ["nombre", "poblacion" , "superficie", "continente"]
    #Definimos una lista auxiliar de diccionarios
    lista =[]
    with open(archivo, "r", encoding="utf-8",  newline="") as ar:
        lector_dict = csv.DictReader(ar)
        for diccionario in lector_dict:
            if texto == diccionario['nombre']:
                if submenu == 1:
                    diccionario["poblacion"] = numero
                elif submenu == 2:
                    diccionario["superficie"] = numero
            #Agregamos todos los diccionarios como estaban + el corregido
            lista.append(diccionario)
    #Definimos el orden como claves del diccionario
    columnas = ["nombre", "poblacion" , "superficie", "continente"]
    with open(archivo, "w", encoding="utf-8",  newline="") as ar:
        #Creamos el escritor indicando los nombres de columnas
        escritor_dict = csv.DictWriter(ar, fieldnames=columnas)
        #Escribimos el encabezado
        escritor_dict.writeheader()
        #Actualizamos el archivo
        escritor_dict.writerows(lista)

def busqueda_parcial_total(archivo, texto):
    try:
        with open(archivo, "r", encoding="utf-8") as ar:
            #iniciamos un contador auxiliar
            i = 0
            #iniciamos una lista auxiliar
            aux_list = []
            lector_dict = csv.DictReader(ar)
            for diccionario in lector_dict:
                if texto == diccionario['nombre'] or texto in diccionario['nombre']:
                    aux_list.append(diccionario)
                    i += 1
            if i == 0:
                raise ValueError(f"El país {texto} no está en la lista.")
            else:
                print()
                print(f"Las coincidencias con {texto} encontradas son:")
                print("Nombre", end=" | ")
                print("Población", end=" | ")
                print("Superficie [km**2]", end=" | ")
                print("Continente")
                print("------------------------------------------------------")
                for diccionario in aux_list:
                    print(diccionario["nombre"], end=" | ")
                    print(diccionario["poblacion"], end=" | ")
                    print(diccionario["superficie"], end=" | ")
                    print(diccionario["continente"])
                print()
    except ValueError as e:
        print(e)
        print()
        return None

#############################################
################# OPCIÓN 1 ##################
#############################################

#Creamos la función de la opción 1
def agregar_pais(datos):
    #creamos el diccionario auxiliar
    datos_pais = {}
    #Le pedimos los datos al usuario
    nombre = input("Ingrese el nombre del país que desea agregar: ").strip().title()
    #validación
    nombre = validar_texto(nombre)
    nombre = validar_repetido(datos, nombre)
    # Si la validación de repetidos fue exitosa, continuamos con la carga de datos.
    # Sino, se vuelve al menú principal.
    if nombre:
        poblacion = input(f"Ingrese la población de {nombre}: ").strip()
        #validación
        poblacion = validar_entero(poblacion)
        superficie = input(f"Ingrese la superficie de {nombre} [km**2]: ").strip()
        #Validación
        superficie = validar_entero(superficie)
        continente = input(f"Ingrese el continente al que pertenece {nombre}: ").strip().title()
        #Validación
        continente = validar_texto(continente)
        #Agregamos los datos ya validados al diccionario
        datos_pais["nombre"] = nombre
        datos_pais["poblacion"] = poblacion
        datos_pais["superficie"] = superficie
        datos_pais["continente"] = continente
        #Invocamos a la función de escritura para agregar los datos al archivo
        escritura_archivo(datos, datos_pais)
        print(f"El país {nombre} se registró correectamente.")
        print()

#############################################
################# OPCIÓN 2 ##################
#############################################

# Creamos la función de la opción 2
def actualizacion(datos):
    #Desplegamos el submenú
    print("¿Qué datos desea actualizar?")
    print("1) Población")
    print("2) Superficie")
    #Le pedimos al usuario que ingrese una opción de submenú
    opcion_submenu = input("Ingrese 1 o 2: ").strip()
    #validación
    opcion_submenu = validar_submenu(opcion_submenu)
    #Le pedimos al usuario el nombre del país
    pais = input("¿Qué país desea actualizar? ").strip().title()
    #validación
    pais = validar_texto(pais)
    pais = validar_existencia(datos, pais)
    #si el país está en el archivo
    if pais:
        if opcion_submenu == 1:
            #se pide el dato de la población
            poblacion = input("Ingrese el valor actualizado de la población: ").strip()
            #validación
            poblacion = validar_entero(poblacion)
            #se invoca a la función que actualiza el archivo
            actualizacion_archivo(datos, pais, poblacion, opcion_submenu)
            print(f"Los datos de población de {pais} fueron actualizados correctamente.")
            print()
        elif opcion_submenu == 2:
            #se pide el dato de la superficie
            superficie = input("Ingrese el valor actualizado de la superficie: ").strip()
            #validación
            superficie = validar_entero(superficie)
            #se invoca a la función que actualiza el archivo
            actualizacion_archivo(datos, pais, superficie, opcion_submenu)
            print(f"Los datos de superficie de {pais} fueron actualizados correctamente.")
            print()

#############################################
################# OPCIÓN 3 ##################
#############################################

#Creamos la función de la opción 3
def buscar_pais(datos):
    #Le pedimos al usuario el dato a buscar
    pais = input("¿Qué país desea buscar? ").strip().title()
    #validamos el dato
    pais = validar_texto(pais)
    #Buscamos el país
    pais = busqueda_parcial_total(datos, pais)