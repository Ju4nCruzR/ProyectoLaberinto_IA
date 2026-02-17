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
    
    # Imprimir la matriz
    simbolos = {
        0: '0 ',  # Espacio libre
        1: '1 ',  # Pared
        2: 'S ',  # Inicio (Start)
        3: 'M ',  # Meta
        4: '* '   # Camino
    }
    
    for fila in matriz_visual:
        linea = ''
        for celda in fila:
            linea += simbolos.get(celda, '? ')
        print(linea)


def imprimir_resultado(algoritmo, camino, nodos_explorados):
    """
    Imprime los resultados de un algoritmo de busqueda.
    
    Args:
        algoritmo (str): Nombre del algoritmo
        camino (list): Camino encontrado (None si no hay solucion)
        nodos_explorados (int): Cantidad de nodos explorados
    """
    print(f"\n{'='*50}")
    print(f"ALGORITMO: {algoritmo}")
    print(f"{'='*50}")
    
    if camino:
        print(f"Solucion encontrada!")
        print(f"Longitud del camino: {len(camino)}")
        print(f"Nodos explorados: {nodos_explorados}")
        print(f"Camino: {camino}")
    else:
        print(f"No se encontro solucion")
        print(f"Nodos explorados: {nodos_explorados}")


def comparar_algoritmos(resultados):
    """
    Muestra una comparacion entre los resultados de diferentes algoritmos.
    
    Args:
        resultados (dict): Diccionario con formato:
            {
                'nombre_algoritmo': {
                    'camino': [...],
                    'nodos_explorados': int
                }
            }
    """
    print(f"\n{'='*70}")
    print(f"COMPARACION DE ALGORITMOS")
    print(f"{'='*70}")
    print(f"{'Algoritmo':<20} {'Longitud Camino':<20} {'Nodos Explorados':<20}")
    print(f"{'-'*70}")
    
    for nombre, datos in resultados.items():
        camino = datos['camino']
        nodos = datos['nodos_explorados']
        longitud = len(camino) if camino else 'Sin solucion'
        print(f"{nombre:<20} {str(longitud):<20} {nodos:<20}") 
