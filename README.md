<h1>Reto_1_DevSenior <img src="https://www.academiadevsenior.com/_next/static/media/original.5eebb33a.png" width="60px"></h1>

<h2> Poyecto de Investigación Cientifica en Python 🐍</h2>
<h3>Participantes 👨‍💻: Andres Camilo Neira Pacalagua, Fabian Esteban Osorio Torres</h3>

<h2>Introducción 🙋‍♂️</h2>

Este es un proyecto creado en Python para la gestión de de experimentos, en el cual podemos agregar, eliminar, visualizar, comparar y crear un informe en archivo .txt los experimetos que pueden ser agredados son de tres tipos:

* Tipo 1: Química.🔬
* Tipo 2: Física. 📉
* Tipo 3: Biología.🌎

<h2> Funcionalidades 🔧</h2>

* Agregar Investigación 📝: Nos permite agregar detalles de los experimentos, como su nombre, fecha de realización, tipo y los resultados obtenidos.
* Ver investigaciones 📖: Muestra una tabla con las investigaciones registradas, donde se incluye su nombre, fecha, tipo y resultados.
* Eliminar investigaciones ❌: Permite eliminar una investigación registrada previamenta, buscando esta por su nombre.
* Análisis de resultados 📄: Calcula los resultados obtenidos de los experimentos y de estos saca un promedio, máximo y mínimo.
* Comparador de resultados 📑: Compara los resultados de diferentes experimentos y muestra el que cuenta con una mejor desviación estandar.
* Generar informe 🖨️: Se genera un informe con toda la información de los experimentos, este informe se crea en un archivo .txt.

<h2>Requisitos 💻</h2>

    Python 3.x 🐍
    Bibliotecas 📚
        * tabulate 📇(Para mostrar las tablas)
        * datetime 📅 (Para agregar fechas)
        * statistics 📈(Para calcular estadisticas)

<h4>Para instalar las dependencias necesarias, se ejecuto el comando</h2>

    pip install tabulate

<h2>Uso 👨‍💻</h2>

1. Ejecutar el archivo main.py para iniciar el programa.
2. Al iniciar el archivo main.py podemos ver el suguiente menu: 

    ![alt text](image.png)

<h2>Ejemplo de ejecución 💻</h2>

    Menú de opciones
    1. Agregar investigación
    2. Ver investigaciones
    3. Eliminar investigaciones
    4. Analizar resultados
    5. Comparar resultados
    6. Generar informe
    7. Salir
    Seleccione una opción: 1
    Escriba el nombre del experimento: Experimento de Física
    Ingrese la fecha en la que se realizo el experimento (DD/MM/YYYY): 01/10/2024
    Seleccione el tipo de experimento:
    1. Química
    2. Física
    3. Biología
    Ingrese el número correspondiente al tipo de experimento: 2
    Ingrese los resultados, separados con coma (ej : 1,2,3,): 1,2,3
    Investigación agregada con exito...

    Ver los experimento agregados selecciona la opción: 2. 
    Eliminar algún experimento selecciona opción: 3.
    Analiza resultados de todos los experimentos opción: 4.
    Comparar resultados de diferentes experimentos opción: 5.
    Para generar informe opción: 6. 
    Para salir opción: 7.
