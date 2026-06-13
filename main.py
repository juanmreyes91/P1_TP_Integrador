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
import funciones as f

######################################################
#######################  MAIN  #######################
######################################################

#Definimos las estructuras de datos a utilizar
lista = []
diccionario = {}

#Inicializamos el menú
opcion = 0
while opcion != 7:
    opcion = f.menu()
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
