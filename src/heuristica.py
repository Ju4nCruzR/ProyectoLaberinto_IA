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

