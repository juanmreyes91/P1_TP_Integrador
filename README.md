# Sistema de Gestión de Países
## Alumnos: Juan Manuel Reyes Lima y Carolina Rodríguez

### Descripción

Este proyecto fue desarrollado para la materia Programación I, de la carrera Tecnicatura Universitaria en Programación a Distancia, Universidad Tecnológica Nacional.

El programa permite gestionar información de países a partir del archivo datos_paises.CSV, realizando consultas, búsquedas, filtrados, ordenamientos y cálculos estadísticos sobre los datos almacenados.

El objetivo principal es aplicar estructuras de datos como listas y diccionarios, modularización mediante funciones, lectura de archivos y técnicas de procesamiento de información.

### Requisitos 
* Python 3.x
* Archivo CSV con los datos de países (datos_paises.CSV)

### Instrucciones de uso
* Descargar o clonar el repositorio: git clone https://github.com/juanmreyes91/P1_TP_Integrador.git
* Verificar que el archivo CSV se encuentre en la misma carpeta que el código main.py
* Ejecutar el programa:  python main.py
* Seleccionar la opción deseada del menú principal
* Seguir las instrucciones mostradas en pantalla

### Funcionalidades

* Agregar países al archivo datos_paises.CSV
* Actualizar datos de población o de superficie
* Buscar países (coincidencia parcial o total)
* Filtrar países por continente, población o superficie
* Ordenar países por nombre, población o superficie (ascendente o descendente)
* Mostrar estadísticas de países con mayor o menor población, promedio de población, promedio de superficie, o cantidad de países por continente.

### Ejemplos de uso

```text
#############################################
Bienvenido al gestor de información de países
#############################################

Elija una opción del menú:
1) Agregar un país
2) Actualizar los datos
3) Buscar un país por nombre
4) Filtrar países
5) Ordenar países
6) Mostrar Estadísticas
7) Salir

Ingrese una opción: 3

¿Qué país desea buscar? arg

Las coincidencias con Arg encontradas son:

Nombre | Población | Superficie [km**2] | Continente
------------------------------------------------------
Argentina | 46735004 | 2780400 | América
Argelia | 28347298742 | 4039241475 | África

#############################################
Bienvenido al gestor de información de países
#############################################

Elija una opción del menú:
1) Agregar un país
2) Actualizar los datos
3) Buscar un país por nombre
4) Filtrar países
5) Ordenar países
6) Mostrar Estadísticas
7) Salir

Ingrese una opción:
```

### Estructura del proyecto

```text
P1_TP_Integrador/
├── Documentacion_Academica_Tecnica.pdf
├── main.py
├── datos_paises.csv
└── README.md
```

### Participación de los integrantes

* Juan Manuel Reyes Lima: Creación del repositorio en GitHub, creación del archivo datos_paises.csv, responsable de las funciones 4, 5 y 6 del programa.
* Carolina Rodríguez: Creación de la rama main y de la subrama de trabajo en GitHub, creación del archivo .gitignore para evitar cargas de datos no deseados al repositorio, responsable de la función menú, 1, 2 y 3 del programa.
* Responsabilidad compartida: Verificación del funcionamiento del programa y de las respectivas validaciones, pull request y discusiones previas al merge final, redacción de informe técnico, README.md y realización del video explicativo y demostrativo.

### Link del video explicatvo y demostrativo

* https://drive.google.com/file/d/1dfH3JNMHQ8Fpku8xrcqnfFGBYqYgTS3n/view?usp=sharing