######################################################
#######################  MAIN  #######################
######################################################
import Funciones as f

#Definimos las estructuras de datos a utilizar
lista = []
diccionario = {}

#Inicializamos el menú
opcion = 0
while opcion != 7:
    opcion = f.menu()
    if opcion == 1:
        f.agregar_pais("temp.csv")
    elif opcion == 2:
        f.actualizacion("temp.csv")
    elif opcion == 3:
        pass
    elif opcion == 4:
        pass
    elif opcion == 5:
        pass
    elif opcion == 6:
        pass    
