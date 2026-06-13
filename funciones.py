import csv

def menu():
    OP_MAX = 7 # Contiene valor máximo del menú
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
    op_menu = validar_menu(op_menu, OP_MAX)
    return op_menu

def validar_menu(op, op_max):
    #Creamos una función de vallidación para las opciones del menú
    while True:
        try:
            #Intentamos convertir la opción a entero
            op = int(op)
            #Analizamos si el usuario ingresó una opción válida para este menú
            if op > op_max or op < 1:
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

def filtrar_paises():
    op = menu_filtrar_paises()
    with open("temp.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        if op == 1:
            filtrar_continente(lector)
        elif op == 2:
            filtrar_población(lector)
        elif op == 3:
            filtrar_superficie(lector)    

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
def ordenar_paises():
    op = menu_ordenar_paises()
    with open("temp.csv", "r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        if op == 1:
            ordenar_x_criterio(lector, "nombre")
        elif op == 2:
            ordenar_x_criterio(lector, "poblacion")
        elif op == 3:
            orden = solicitar_orden()
            ordenar_x_criterio(lector, "superficie", orden)


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
