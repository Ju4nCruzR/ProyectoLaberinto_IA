"""
Modulo para calcular funciones heuristicas.
"""

def distancia_manhattan(posicion_actual, posicion_meta):
    """
    Calcula la distancia Manhattan entre dos posiciones.
    La distancia Manhattan es la suma de las diferencias absolutas
    de las coordenadas: |x1 - x2| + |y1 - y2|
    
    Es una heuristica admisible para laberintos con movimientos
    solo en 4 direcciones (arriba, abajo, izquierda, derecha).
    
    Args:
        posicion_actual (tuple): Tupla (fila, columna) actual
        posicion_meta (tuple): Tupla (fila, columna) objetivo
        
    Returns:
        int: Distancia Manhattan entre las dos posiciones
    """
    fila_actual, columna_actual = posicion_actual
    fila_meta, columna_meta = posicion_meta
    
    return abs(fila_actual - fila_meta) + abs(columna_actual - columna_meta)


def distancia_euclidiana(posicion_actual, posicion_meta):
    """
    Calcula la distancia Euclidiana entre dos posiciones.
    Es la distancia en linea recta: sqrt((x1-x2)^2 + (y1-y2)^2)
    
    No es tan precisa como Manhattan para laberintos con movimientos
    solo en 4 direcciones, pero puede usarse como alternativa.
    
    Args:
        posicion_actual (tuple): Tupla (fila, columna) actual
        posicion_meta (tuple): Tupla (fila, columna) objetivo
        
    Returns:
        float: Distancia Euclidiana entre las dos posiciones
    """
    fila_actual, columna_actual = posicion_actual
    fila_meta, columna_meta = posicion_meta
    
    return ((fila_actual - fila_meta)**2 + (columna_actual - columna_meta)**2)**0.5


def calcular_heuristica_laberinto(laberinto):
    """
    Calcula la heuristica desde cada posicion transitable hasta la meta.
    Genera un diccionario con todas las distancias Manhattan precalculadas.
    
    Args:
        laberinto (Laberinto): Instancia del laberinto
        
    Returns:
        dict: Diccionario {posicion: distancia_a_meta}
    """
    tabla_heuristica = {}
    meta = laberinto.meta
    
    for fila in range(laberinto.dimensiones):
        for columna in range(laberinto.dimensiones):
            posicion = (fila, columna)
            
            # Solo calcular para posiciones transitables
            if laberinto.es_valido(fila, columna):
                tabla_heuristica[posicion] = distancia_manhattan(posicion, meta)
    
    return tabla_heuristica
