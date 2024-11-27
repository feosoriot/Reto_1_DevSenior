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
    nombreExp = input('\033[1;3;30mEscriba el nombre del experimento: \033[0m')
    fechaRealizacion_str = input('\033[1;3;30mIngrese la fecha en la que se realizo el experimento (DD/MM/YYYY): \033[0m')
    try:
        fechaRealizacion = datetime.strptime(fechaRealizacion_str, "%d/%m/%Y")
    except ValueError:
        print('\033[1;3;31mFecha no valida...')
        return
    print("\033[1;3;32m=====Seleccione el tipo de experimento===\033[0m")
    print("\033[1;3;32m1. Química")
    print("\033[1;3;32m2. Física")
    print("\033[1;3;32m3. Biología")
    tipoExp = input("\033[1;3;30mIngrese el número correspondiente al tipo de experimento: \033[0m")

    if tipoExp == '1':
        tipoExp = 'Química'
    elif tipoExp == '2':
        tipoExp = 'Física'
    elif tipoExp == '3':
        tipoExp = 'Biología'
    else:
        print('\033[1;3;31mSelección no válida...')
        return

    resultados_str = input('\033[1;3;30mIngrese los resultados, separados con coma (ej : 1,2,3,): \033[0m')
    try:
        resultados = list(map(float, resultados_str.split(',')))
    except ValueError:
        print('\033[1;3;31mLos resultados no son validos...')
        return

    investigacion = Invetigacion(nombreExp, fechaRealizacion, tipoExp, resultados)
    listaExp.append(investigacion)
    print('\033[1;3;32mInvestigacion agregada con exito...')


def eliminarEXP(listaExp):
    if not listaExp:
        print('\033[1;3;31mNo hay investigaciones registradas...')
        

    nombreExp = input('\033[1;3;30mIngrese el nombre del experimento que desea eliminar: ')
    for invetigacion in listaExp:
        if invetigacion.nombreExp == nombreExp:
            listaExp.remove(invetigacion)
            print(f'\033[1;3;32mLa investigazión {nombreExp} ha sido eliminada con éxito...')
            break
    else:
        print(f'\033[1;3;31mNo se encontró una investigazión con el nombre {nombreExp}...')


from tabulate import tabulate

def visualizarExp(listaExp):
    if not listaExp:
        print('\033[1;3;31mNo hay investigaciones registradas...')
        return

    datos = []
    for i, investigacion in enumerate(listaExp, start=1):
        datos.append([
            i,
            investigacion.nombreExp,
            investigacion.fechaRealizacion.strftime("%d/%m/%Y"),
            investigacion.tipoExp,
            ", ".join(map(str, investigacion.resultados)) 
        ])

    headers = ["#", "Nombre", "Fecha", "Tipo", "Resultados"]

    print("\n\033[1;3;32mInvestigaciones Registradas:")
    print(tabulate(datos, headers=headers, tablefmt="grid"))


def analizarResultados(listaExp):
    if not listaExp:
        print('\033[1;3;31mNo hay investigaciones registradas...')
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
            f'{promedio:.2f}', 
            maximo,
            minimo,
            desviacion
        ])

    headers = ["Nombre", "Fecha", "Tipo", "Promedio", "Máximo", "Mínimo","Desviacion"]

    print("\n\033[1;3;32mAnálisis de Resultados:")
    print(tabulate(datos, headers=headers, tablefmt="grid"))


def compararResultados(listaExp):
    if not listaExp:
        print('\033[1;3;31mNo hay investigaciones registradas...')
        return
    
    print("\033[1;3;32m==Seleccione el tipo de experimento a comparar==")
    print("\033[1;3;32m1. Química")
    print("\033[1;3;32m2. Física")
    print("\033[1;3;32m3. Biología")
    tipoExp = input("\033[1;3;30mIngrese el número correspondiente al tipo de experimento: ")

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
        print('\033[1;3;31mEl tipo de experimento no tiene datos registrados')
    else:
        print(f'\033[1;3;32mel dato con mejor desviación estandar es :')
        print(f'{elNumero} Nombre : {elNombre} fecha : {laFeha} tipo: {elTipo}')
        print(f'Promedio : {elPromedio}\n maximo : {eLmaximo} minimo : {elMinimo} desviacion : {elMenor}')
        print('\033[1;3;31mNo se encontro el tipo de experimento registrado')


def generarInf(listaExp):
    if not listaExp:
        print('\033[1;3;31mNo hay investigaciones registradas...')
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
        print('\033[3;1;36m=================================\033[0m')
        print('\033[3;1;33m|       📋 Menu de opciones     |\033[0m')
        print('\033[3;1;36m=================================\033[0m')
        print('\033[3;32m|1. ➕ Agregar investigación    |\033[0m')
        print('\033[3;32m|2. 📄 Ver investigaciones      |\033[0m')
        print('\033[3;32m|3. ❌ Eliminar investigaciones |\033[0m')
        print('\033[3;34m|4. 📊 Analizar resultados      |\033[0m')
        print('\033[3;34m|5. ⚖️ Comparar resultados       |\033[0m')
        print('\033[3;35m|6. 📝 Generar informe          |\033[0m')
        print('\033[3;31m|7. 🚪 Salir                    |\033[0m')
        print('\033[1;96m=================================\033[0m')

        
        opcion = input('\033[1;3;30mSeleccione una opción: \033[0m')

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