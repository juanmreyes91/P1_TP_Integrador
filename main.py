#####################################################
####################### MENÚ ########################
#####################################################

def menu():
    OP_MAX = 7 # Contiene valor máximo del menú
    print("#############################################")
    print("Bienvenido al gestor de información de países")
    print("#############################################")
    print("Elija una opción del menú:")
    print("1) Agregar un país")
    print("2) Actualizar los datos")
    print("3) Buscar un país por nombre")
    print("4) Filtrar países")
    print("5) Ordenar países")
    print("6) Mostrar Estadísticas")
    print("7) Salir")
    #Le pedimos al usuario que ingrese una opción
    op_menu = input("Ingrese una opción: ").strip()
    #Validamos la opción ingresada
    op_menu = validar_menu(op_menu, OP_MAX)
    return op_menu

def validar_menu(op, max):
    #Creamos una función de vallidación para las opciones del menú
    while True:
        try:
            #Intentamos convertir la opción a entero
            op = int(op)
            #Analizamos si el usuario ingresó una opción válida para este menú
            if op > max or op < 1:
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

#####################################################
################### VALIDACIONES ####################
#####################################################

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
    except FileNotFoundError:
        print(f"Error: el archivo '{archivo}' no existe.")
        return None
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
    except FileNotFoundError:
        print(f"Error: el archivo '{archivo}' no existe.")
        return None
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
            elif not texto.isalpha():
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

# --- OPCIÓN 4: Filtrar países. FUNCIÓN PRINCIPAL ---
def menu_filtrar_paises():
    # Sub menú mostrado por pantalla
    OP_MAX = 3 # Contiene valor máximo del sub menú
    print("Filtrar países por:")
    print("1) Continente")
    print("2) Rango de población")
    print("3) Rango de superficie")

    op = input("Ingrese la opción: ").strip()
    op = validar_menu(op, OP_MAX)
    return op

def filtrar_paises(archivo):
    op = menu_filtrar_paises()
    try:
        with open(archivo, "r", encoding="utf-8") as ar:
            lector_dict = csv.DictReader(ar)
            if op == 1:
                filtrar_continente(lector_dict)
            elif op == 2:
                filtrar_población(lector_dict)
            elif op == 3:
                filtrar_superficie(lector_dict)
    except FileNotFoundError:
        print(f"Error: El archivo solicitado no existe")
        return None

# --- Opción 4.1: Filtrar por continente

def menu_continentes():
    OP_MAX = 5 # Valor máximo para este submenú
    print("\nContinentes:")
    print("1) América")
    print("2) África")
    print("3) Asia")
    print("4) Europa")
    print("5) Oceanía")
    
    op = input("¿Qué continente quiere consultar? ").strip()
    op = validar_menu(op, OP_MAX)
    return op

def filtrar_continente(lector):
    op = menu_continentes()
    # op usado como índice para lista 'continentes'
    continentes = ["América", "África", "Asia", "Europa", "Oceanía"]
    continente = continentes[op-1]
    aux_paises = []
    # Lista vacía que guardará países que coincidan con la búsqueda 
    for fila in lector:
        if fila["continente"] == continente:
            aux_paises.append(fila["nombre"])
    # Finalmente se muestran los resultados por pantalla
    if len(aux_paises) > 0:
        print(f"Los países de {continente} son:")
        for pais in aux_paises:
            print(f"- {pais}")
    else:
        print(f"No hay países registrados para {continente}")
    input("Presione Enter para continuar...")

# --- Opción 4.2: filtrar por población ---

def menu_rangos_poblacion():
    OP_MAX = 6 # Valor máximo para este submenú
    print("\nRangos de población:")
    print("1) Menos de 1 millón")
    print("2) De 1M a 10M")
    print("3) De 10M a 50M")
    print("4) De 50M a 200M")
    print("5) De 200M a 1.000M")
    print("6) Mayores a 1.000M")

    op = input("¿Qué rango quiere consultar? ").strip()
    op = validar_menu(op, OP_MAX)
    return op

def filtrar_población(lector):
    op = menu_rangos_poblacion()
    rangos = [{"minimo": 0, "maximo": 1000000}, # Menor a 1M
              {"minimo": 1000000, "maximo": 10000000}, # Entre 1M y 10M
              {"minimo": 10000000, "maximo": 50000000}, # Entre 10M y 50M
              {"minimo": 50000000, "maximo": 200000000}, # Entre 50M y 200M
              {"minimo": 200000000, "maximo": 1000000000}, # Entre 200M y 1.000M
              {"minimo": 1000000000, "maximo": float('inf')}] # Más de 1.000M
    aux_paises = []
    rango = rangos[op-1]
    for fila in lector: # Ahora fila es un diccionario
        if rango["minimo"] <= int(fila["poblacion"]) < rango["maximo"]:
            aux_paises.append(fila["nombre"])
    if len(aux_paises) > 0:
        # Si hay países dentro del rango, se muestran
        print(f"\nPaíses dentro del rango de población seleccionada: ")
        for pais in aux_paises:
            print(f"- {pais}")
    else:
        print("\nNo hay países registrados con ese rango de población")
    input("Presione Enter para continuar...")

# --- Opcion 4.3: Filtrar por superficie ---

# Muestra opciones de rangos de superficies en km2
# Y solocita elegir una opción
def menu_rangos_superficie():
    OP_MAX = 5 # Valor máximo para este submenú
    print("\nRangos de superficie:")
    print("1) Menos de 1000km2")
    print("2) De 1000 a 100000 km2")
    print("3) De 100000 a 1000000 km2")
    print("4) De 1M a 5M km2")
    print("5) Mayor a 5M km2")

    op = input("¿Qué rango quiere consultar? ").strip()
    op = validar_menu(op, OP_MAX)
    return op

# Imprime por pantalla países dentro del rango de superficie elegida
def filtrar_superficie(lector):
    op = menu_rangos_superficie()
    rangos = [{"minimo": 0, "maximo": 1000}, # Menor a 1.000km2
              {"minimo": 1000, "maximo": 100000}, # Entre 1.000 y 100.000km2
              {"minimo": 100000, "maximo": 1000000}, # Entre 100.000 y 1Mkm2
              {"minimo": 1000000, "maximo": 5000000}, # Entre 1M y 5M km2
              {"minimo": 5000000, "maximo": float('inf')}] # Más de 5M km2
    aux_paises = []
    rango = rangos[op-1]
    for fila in lector: # Ahora fila es un diccionario
        if rango["minimo"] <= int(fila["superficie"]) < rango["maximo"]:
            aux_paises.append(fila["nombre"])
    if len(aux_paises) > 0:
        # Si hay países dentro del rango, se muestran
        print(f"\nPaíses dentro del rango de superficie seleccionada: ")
        for pais in aux_paises:
            print(f"- {pais}")
    else:
        print("\nNo hay países registrados con ese rango de superficie")
    input("Presione Enter para continuar...")


# --- Opción 5: Ordenar países ---

def menu_ordenar_paises():
    # Sub menú mostrado por pantalla
    OP_MAX = 3 # Contiene valor máximo del sub menú
    print("Ordenar países por:")
    print("1) Nombre")
    print("2) Población")
    print("3) Superficie (ascendente o descendente)")

    op = input("Ingrese la opción: ").strip()
    op = validar_menu(op, OP_MAX)
    return op

# Sub-menú para elegir orden de superficie ascendente o descendente
def solicitar_orden():
    OP_MAX = 2
    print("1) Orden ascendente")
    print("2) Orden descendente")
    o = input("Ingrese opción: ").strip()
    o = validar_menu(o, OP_MAX)
    if o == 1:
        return False # Para orden ascendente
    else:
        return True # Para orden descendente

# Función principal, llama al menú, abre archivo y redirige el flujo
def ordenar_paises(archivo):
    op = menu_ordenar_paises()
    try:
        with open(archivo, "r", encoding="utf-8") as ar:
            lector_dict = csv.DictReader(ar)
            if op == 1:
                ordenar_x_criterio(lector_dict, "nombre")
            elif op == 2:
                ordenar_x_criterio(lector_dict, "poblacion")
            elif op == 3:
                orden = solicitar_orden()
                ordenar_x_criterio(lector_dict, "superficie", orden)
    except FileNotFoundError:
        print(f"Error: El archivo solicitado no existe")
        return None

# Imprime por pantalla los resultados según el criterio 

def ordenar_x_criterio(lector, criterio, ascendente=False):
    # Se determina el criterio de ordenamiento
    if criterio == "nombre":
        clave = lambda fila: fila["nombre"]
    elif criterio == "poblacion":
        clave = lambda fila: int(fila["poblacion"])
    elif criterio == "superficie":
        clave = lambda fila: int(fila["superficie"])
    # Se crea la lista ordenada
    paises = sorted(lector, key=clave, reverse=ascendente)
    # Se imprimen los resultados por pantalla
    print(f"\nPaíses ordenados por {criterio}: ")
    print("Nombre   | Población   | Superficie   | Continenete")
    for p in paises:
        print(f"{p["nombre"]} | {p["poblacion"]} | {p["superficie"]}km2 | {p["continente"]}")
    input("Presione Enter para continuar...")

# --- Opción 6: Mostrar estadísticas ---

# Sub menú de estadísticas
def menu_estadisticas():
    # Sub menú mostrado por pantalla
    OP_MAX = 4 # Contiene valor máximo del sub menú
    print("\nMostrar estadísticas de:")
    print("1) País con mayor y menor población")
    print("2) Promedio de población")
    print("3) Promedio de superficie")
    print("4) Cantidad de países por continente")

    op = input("Ingrese la opción: ").strip()
    op = validar_menu(op, OP_MAX)
    return op

# Abre archivo y direcciona el flujo según opción elegida
def estadisticas_paises(archivo):
    op = menu_estadisticas()
    try:
        with open(archivo, "r", encoding="utf-8") as ar:
            lector_dict = csv.DictReader(ar) # Se crea el iterable
            # Se redirecciona el flujo del programa según opción elegida
            if op == 1:
                mayor_menor_poblacion(lector_dict)
            elif op == 2:
                promedio_poblacion(lector_dict)
            elif op == 3:
                promedio_superficie(lector_dict)
            elif op == 4:
                cantidad_x_continente(lector_dict)
    except FileNotFoundError:
        print(f"Error: El archivo solicitado no existe")
        return None

# Opción 6.1: País con mayor y menor población
def mayor_menor_poblacion(lector):
    paises = sorted(lector, key= lambda clave: int(clave["poblacion"]))
    print(f"\nPaís con menor población: {paises[0]["nombre"]} \
con {paises[0]["poblacion"]} habitantes.")
    print(f"País con mayor población: {paises[-1]["nombre"]} \
con {paises[-1]["poblacion"]} habitantes.")
    input("Presione Enter para continuar...")

# Opción 6.2: Promedio de población
def promedio_poblacion(lector):
    suma = 0
    cantidad = 0
    for fila in lector: #fila tendrá la lista de diccionarios
        suma += int(fila["poblacion"]) #sumatoria de población
        cantidad += 1 #para contar total países
    promedio = suma / cantidad
    print(f"\nEl promedio de población es de {promedio} habitantes.")
    input("Presione Enter para continuar...")

# Opción 6.3: Promedio de superficie
def promedio_superficie(lector):
    suma = 0
    cantidad = 0
    for fila in lector: #fila tendrá la lista de diccionarios
        suma += int(fila["superficie"]) #sumatoria de superficie
        cantidad += 1 #para contar total países
    promedio = suma / cantidad
    print(f"\nEl promedio de superficie es de {promedio} km2.")
    input("Presione Enter para continuar...")

# Opción 6.4: Cantidad de países por continente
def cantidad_x_continente(lector):
    dic_aux = {} # Estructura auxiliar para contar países por continente
    for fila in lector:
        # Se agrega a diccionario auxiliar cantidad de países por continente
        dic_aux[fila["continente"]] = dic_aux.get(fila["continente"], 0) + 1
    for k, v in dic_aux.items():
        # Se imprimen por pantalla los resultados
        print(f"{k} tiene {v} países registrados")
    input("Presione Enter para continuar...")

#############################################
############ FUNCIONES AUXILIARES ###########
#############################################

# Escritura basada en diccionarios
def escritura_archivo(archivo, diccionario):
    try:
        #Definimos el orden como claves del diccionario
        columnas = ["nombre", "poblacion" , "superficie", "continente"]
        with open(archivo, "a", encoding="utf-8",  newline="") as ar:
            #Creamos el escritor indicando los nombres de columnas
            escritor_dict = csv.DictWriter(ar, fieldnames=columnas)
            #Escribimos los datos
            escritor_dict.writerow(diccionario)
    except FileNotFoundError:
        print(f"Error: el archivo '{archivo}' no existe.")
        return None

def actualizacion_archivo(archivo, texto, numero, submenu):
    try:
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
        with open(archivo, "w", encoding="utf-8",  newline="") as ar:
            #Creamos el escritor indicando los nombres de columnas
            escritor_dict = csv.DictWriter(ar, fieldnames=columnas)
            #Escribimos el encabezado
            escritor_dict.writeheader()
            #Actualizamos el archivo
            escritor_dict.writerows(lista)
    except FileNotFoundError:
        print(f"Error: el archivo '{archivo}' no existe.")
        return None

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
    except FileNotFoundError:
        print(f"Error: el archivo '{archivo}' no existe.")
        return None
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
        print(f"El país {nombre} se registró correctamente.")
        print()

#############################################
################# OPCIÓN 2 ##################
#############################################

# Creamos la función de la opción 2
def actualizacion(datos):
    OP_MAX = 2
    #Desplegamos el submenú
    print("¿Qué datos desea actualizar?")
    print("1) Población")
    print("2) Superficie")
    #Le pedimos al usuario que ingrese una opción de submenú
    opcion_submenu = input("Ingrese 1 o 2: ").strip()
    #validación
    opcion_submenu = validar_menu(opcion_submenu, OP_MAX)
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

######################################################
#######################  MAIN  #######################
######################################################
import csv
#Inicializamos el menú
opcion = 0
while opcion != 7:
    opcion = menu()
    if opcion == 1:
        agregar_pais("datos_paises.csv")
    elif opcion == 2:
        actualizacion("datos_paises.csv")
    elif opcion == 3:
        buscar_pais("datos_paises.csv")
    elif opcion == 4:
        filtrar_paises("datos_paises.csv")
    elif opcion == 5:
        ordenar_paises("datos_paises.csv")
    elif opcion == 6:
        estadisticas_paises("datos_paises.csv")
        
     
