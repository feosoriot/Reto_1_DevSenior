from tabulate import tabulate
from datetime import datetime
import statistics


class Invetigacion:
    def __init__(self, nombreExp, fechaRealizacion, tipoExp, resultados):
        self.nombreExp = nombreExp
        self.fechaRealizacion = fechaRealizacion
        self.tipoExp = tipoExp
        self.resultados = resultados

def agregarExp(listaExp):
    nombreExp = input('Escriba el nombre del experimento: ')
    fechaRealizacion_str = input('Ingrese la fecha en la que se realizo el experimento (DD/MM/YYYY): ')
    try:
        fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y")
    except ValueError:
        print('Fecha no valida...')
        return
    print("Seleccione el tipo de experimento:")
    print("1. Química")
    print("2. Física")
    print("3. Biología")
    tipoExp = input("Ingrese el número correspondiente al tipo de experimento: ")

    if tipoExp == '1':
        tipoExp = 'Química'
    elif tipoExp == '2':
        tipoExp = 'Física'
    elif tipoExp == '3':
        tipoExp = 'Biología'
    else:
        print('Selección no válida...')
        return

    resultados_str = input('Ingrese los resultados, separados con coma (ej : 1,2,3,): ')
    try:
        # Corregido: Usamos split para separar por comas y luego convertir a float
        resultados = list(map(float, resultados_str.split(',')))
    except ValueError:
        print('Los resultados no son validos...')
        return

    investigacion = Invetigacion(nombreExp, fechaRealizacion, tipoExp, resultados)
    listaExp.append(investigacion)
    print('Investigacion agregada con exito...')


def eliminarEXP(listaExp):
    if not listaExp:
        print('No hay investigaciones registradas...')
        return

    nombreExp = input('Ingrese el nombre del experimento que desea eliminar: ')
    for invetigacion in listaExp:
        if invetigacion.nombreExp == nombreExp:
            listaExp.remove(invetigacion)
            print(f'La investigazión {nombreExp} ha sido eliminada con éxito...')

    print(f'No se encontró una investigazión con el nombre {nombreExp}...')


from tabulate import tabulate

def visualizarExp(listaExp):
    if not listaExp:
        print('No hay investigaciones registradas...')
        return

    datos = []
    for i, investigacion in enumerate(listaExp, start=1):
        datos.append([
            i,
            investigacion.nombreExp,
            investigacion.fechaRealizacion.strftime("%d/%m/%Y"),
            investigacion.tipoExp,
            ", ".join(map(str, investigacion.resultados))  # Convertimos los resultados a cadenas
        ])

    headers = ["#", "Nombre", "Fecha", "Tipo", "Resultados"]

    print("\nInvestigaciones Registradas:")
    print(tabulate(datos, headers=headers, tablefmt="grid"))


def analizarResultados(listaExp):
    if not listaExp:
        print('No hay investigaciones registradas...')
        return

    datos = []
    for investigacion in listaExp:
        promedio = statistics.mean(investigacion.resultados)
        maximo = max(investigacion.resultados)
        minimo = min(investigacion.resultados)
        desviacion=statistics.stdev(investigacion.resultados)
        datos.append([
            investigacion.nombreExp,
            investigacion.fechaRealizacion.strftime('%d/%m/%Y'),
            investigacion.tipoExp,
            f'{promedio:.2f}',  # Formato correcto para 2 decimales
            maximo,
            minimo,
            desviacion
        ])

    headers = ["Nombre", "Fecha", "Tipo", "Promedio", "Máximo", "Mínimo","Desviacion"]

    print("\nAnálisis de Resultados:")
    print(tabulate(datos, headers=headers, tablefmt="grid"))


def compararResultados(listaExp):
    if not listaExp:
        print('No hay investigaciones registradas...')
        return
    print("Seleccione el tipo de experimento a comparar:")
    print("1. Química")
    print("2. Física")
    print("3. Biología")
    tipoExp = input("Ingrese el número correspondiente al tipo de experimento: ")

    if tipoExp == '1':
        tipoExp = 'Química'
    elif tipoExp == '2':
        tipoExp = 'Física'
    elif tipoExp == '3':
        tipoExp = 'Biología'
    elMenor=100000000
    for i, investigacion in enumerate(listaExp, start=1):
        if tipoExp==investigacion.tipoExp:
            promedio = statistics.mean(investigacion.resultados)
            maximo = max(investigacion.resultados)
            minimo = min(investigacion.resultados)
            desviacionr=statistics.stdev(investigacion.resultados)
            if desviacionr<=elMenor:
                elMenor=desviacionr
                elPromedio=promedio
                elMinimo=minimo
                eLmaximo=maximo
                elNumero=i
                elNombre=investigacion.nombreExp,
                laFeha=investigacion.fechaRealizacion.strftime('%d/%m/%Y'),
                elTipo=investigacion.tipoExp
        else:
            elTipo="No existe"
    if elTipo=="No existe":
        print('El tipo de experimento no tiene datos registrados')
    else:
        print(f'el dato con mejor desviación estandar es :')
        print(f'{elNumero} Nombre : {elNombre} fecha : {laFeha} tipo: {elTipo}')
        print(f'Promedio : {elPromedio}\n maximo : {eLmaximo} minimo : {elMinimo} desviacion : {elMenor}')
        print('No se encontro el tipo de experimento registrado')


def generarInf(listaExp):
    if not listaExp:
        print('No hay investigaciones registradas...')
        return 
    
    with open('informe_investigacion_experimentos.txt', 'w') as archivo:
        for investigacion in listaExp:
            archivo.write(f'Nombre de la investigación: {investigacion.nombreExp}\n')
            archivo.write(f'Fecha de realización: {investigacion.fechaRealizacion}\n')
            archivo.write(f'Tipo de experimento: {investigacion.tipoExp}\n')
            archivo.write(f'Resultados de la investigación: {investigacion.resultados}\n')
            archivo.write(f'\n')
    print("Informe generado como 'informe_investigacion_experimentos.txt'")

def menu():
    listaExp = []
    while True:
        print('\nMenu de opciones')
        print('1. Agregar investigación')
        print('2. Ver investigaciones')
        print('3. Eliminar investigaciones')
        print('4. Analizar resultados')
        print('5. Comparar resultados')
        print('6. Generar informe')
        print('7. Salir')
        
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            agregarExp(listaExp)
        elif opcion == '2':
            visualizarExp(listaExp)
        elif opcion == '3':
            eliminarEXP(listaExp)
        elif opcion == '4':
            analizarResultados(listaExp)
        elif opcion == '5':
            compararResultados(listaExp)
        elif opcion == '6':
            generarInf(listaExp)
        elif opcion == '7':
            print('Saliendo del programa...')
            break
        else:
            print('Opción inválida...')

if __name__ == "__main__":
    menu()