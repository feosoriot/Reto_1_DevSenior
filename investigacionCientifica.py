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

def visualizarExp(listaExp):
    if not listaExp:
        print('No hay investigaciones registradas...')
        return
    
    for i, investigacion in enumerate(listaExp, start=1):
        print(f'\nInvestigacion {i}')
        print(f'Nombre de la investigación: {investigacion.nombreExp} ')
        print(f'Fecha de realización: {investigacion.fechaRealizacion.strftime("%d/%m/%Y")}')
        print(f'Tipo del experimento: {investigacion.tipoExp}')
        print(f'Resultados: {investigacion.resultados}')
        
def analizarResultados(listaExp):
    if not listaExp:
        print('No hay investigaciones registradas...')
        return
    
    for investigacion in listaExp:
        promedio = statistics.mean(investigacion.resultados)
        maximo = max(investigacion.resultados)
        minimo = min(investigacion.resultados)
        print(f'\nAnálisis de resultados')
        print(f'Promedio de resultados: {promedio}')
        print(f'Máximo de resultados: {maximo}')
        print(f'Mínimo de resultados: {minimo}')

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
        print('3. Analizar resultados')
        print('4. Generar informe')
        print('5. Salir')
        
        opcion = input('Seleccione una opción: ')

        if opcion == '1':
            agregarExp(listaExp)
        elif opcion == '2':
            visualizarExp(listaExp)
        elif opcion == '3':
            analizarResultados(listaExp)
        elif opcion == '4':
            generarInf(listaExp)
        elif opcion == '5':
            print('Saliendo del programa...')
            break
        else:
            print('Opción inválida...')

if __name__ == "__main__":
    menu()