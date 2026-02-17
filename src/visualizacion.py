"""
Modulo para visualizar el laberinto y la solucion encontrada.
"""


def visualizar_laberinto(laberinto, camino=None):
    """
    Muestra el laberinto en consola.
    Si se proporciona un camino, lo marca con '*'.
    
    Args:
        laberinto (Laberinto): Instancia del laberinto
        camino (list): Lista de posiciones que forman el camino (opcional)
    """
    # Crear copia de la matriz para no modificar la original
    matriz_visual = [fila[:] for fila in laberinto.matriz]
    
    # Marcar el camino si existe
    if camino:
        for posicion in camino:
            fila, columna = posicion
            # No sobrescribir inicio y meta
            if matriz_visual[fila][columna] not in [2, 3]:
                matriz_visual[fila][columna] = 4  # 4 representa el camino
    
    # Simbolos consistentes con Laberinto.__str__
    simbolos = {
        0: '. ',  # Espacio libre
        1: '# ',  # Pared
        2: 'S ',  # Inicio (Start)
        3: 'M ',  # Meta
        4: '* '   # Camino
    }
    
    for fila in matriz_visual:
        linea = ''
        for celda in fila:
            linea += simbolos.get(celda, '? ')
        print(linea)


def imprimir_resultado(algoritmo, camino, nodos_explorados, tiempo=None):
    """
    Imprime los resultados de un algoritmo de busqueda.
    
    Args:
        algoritmo (str): Nombre del algoritmo
        camino (list): Camino encontrado (None si no hay solucion)
        nodos_explorados (int): Cantidad de nodos explorados
        tiempo (float): Tiempo de ejecucion en segundos (opcional)
    """
    print(f"\n{'='*50}")
    print(f"ALGORITMO: {algoritmo}")
    print(f"{'='*50}")
    
    if camino:
        print("Solucion encontrada!")
        print(f"Longitud del camino: {len(camino)}")
        print(f"Nodos explorados: {nodos_explorados}")
        if tiempo is not None:
            print(f"Tiempo de ejecucion: {tiempo:.6f} segundos")
        print(f"Camino: {camino}")
    else:
        print("No se encontro solucion")
        print(f"Nodos explorados: {nodos_explorados}")
        if tiempo is not None:
            print(f"Tiempo de ejecucion: {tiempo:.6f} segundos")


def comparar_algoritmos(resultados):
    """
    Muestra una comparacion entre los resultados de diferentes algoritmos.
    
    Args:
        resultados (dict): Diccionario con formato:
            {
                'nombre_algoritmo': {
                    'camino': [...],
                    'nodos_explorados': int,
                    'tiempo': float  (opcional)
                }
            }
    """
    print(f"\n{'='*80}")
    print("COMPARACION DE ALGORITMOS")
    print(f"{'='*80}")
    print(f"{'Algoritmo':<20} {'Longitud Camino':<20} {'Nodos Explorados':<20} {'Tiempo (s)':<15}")
    print(f"{'-'*80}")
    
    for nombre, datos in resultados.items():
        camino = datos['camino']
        nodos = datos['nodos_explorados']
        tiempo = datos.get('tiempo', None)
        longitud = len(camino) if camino else 'Sin solucion'
        tiempo_str = f"{tiempo:.6f}" if tiempo is not None else 'N/A'
        print(f"{nombre:<20} {str(longitud):<20} {nodos:<20} {tiempo_str:<15}")
