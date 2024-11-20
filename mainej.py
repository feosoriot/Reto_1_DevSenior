import datetime

"""atributos de un experimento: nombre, fecha, tipo y resultados numericos"""

listaDeExpeimentos = [
    ['Experiento 1','16/11/2024', 'Quimca',[5,3,4,5,6,4]]
]

def agregarExperimento():
    """Permite egregar nuevo experimento"""
    pass

def eliminarExperimento():
    """Permite eliminar experimento"""
    pass

def fechaExperimento():
    """Permite agregar llas fechas en las que se realizaron los documentos"""
    pass

def visualizarExperimentos():
    """Permite visualizar los experimentos"""
    pass

def calcularEstisticas():
    """Clacula estadisticas basicas promendio,maxima, minima"""
    pass

def compararExperimentos():
    """Comparar dos o mas experimento para determinar los mejores resultados"""
    pass

def generarInforme():
    """Generar informe de kis experimentos y sus estadisticas"""
    pass

def menu():
    """Menu interactivo para los usuarios"""
    print('\n====Menu de opciones====')
    print('==Gestion de experimentos==')
    print('1. Agregar Experimento')
    print('2. Eliminar Experimento')
    print('3. Visualizar expermentos')
    print('=====Analisis de datos=====')
    print('4. Calcular estadisticas')
    print('5. Comparar estadisticas')
    print('=====Informes====')
    print('6. Generar informe')
    print('======Salir=====')
    print('7. Salir')
    pass

def main():
    """Controla el flujo """
    menu()

main()

