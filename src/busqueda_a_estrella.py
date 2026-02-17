"""
Modulo que implementa el algoritmo de busqueda heuristica A*.
"""

import heapq
from src.nodo import Nodo, reconstruir_camino
from src.heuristica import distancia_manhattan


def busqueda_a_estrella(grafo, inicio, meta):
    """
    Implementa el algoritmo A* (A-Estrella).
    Usa una funcion de evaluacion f(n) = g(n) + h(n) donde:
    - g(n) es el costo real desde el inicio hasta n
    - h(n) es la heuristica estimada desde n hasta la meta
    
    Args:
        grafo (Grafo): Grafo del laberinto
        inicio (tuple): Posicion inicial
        meta (tuple): Posicion objetivo
        
    Returns:
        tuple: (camino, nodos_explorados) donde:
            camino es la lista de posiciones desde inicio a meta
            nodos_explorados es el numero de nodos visitados
    """
    nodo_inicio = Nodo(inicio)
    nodo_inicio.costo_g = 0
    nodo_inicio.costo_h = distancia_manhattan(inicio, meta)
    nodo_inicio.costo_f = nodo_inicio.costo_g + nodo_inicio.costo_h
    
    nodo_meta = Nodo(meta)
    
    # Cola de prioridad (min-heap) ordenada por costo_f
    lista_abierta = []
    heapq.heappush(lista_abierta, nodo_inicio)
    
    # Set de nodos cerrados (ya explorados)
    lista_cerrada = set()
    
    # Diccionario para rastrear el mejor costo_g a cada posicion
    mejor_costo_g = {inicio: 0}
    
    nodos_explorados = 0
    
    while lista_abierta:
        # Obtener el nodo con menor costo_f
        nodo_actual = heapq.heappop(lista_abierta)
        nodos_explorados += 1
        
        # Verificar si llegamos a la meta
        if nodo_actual.posicion == nodo_meta.posicion:
            camino = reconstruir_camino(nodo_actual)
            return camino, nodos_explorados
        
        # Agregar a lista cerrada
        lista_cerrada.add(nodo_actual.posicion)
        
        # Explorar vecinos
        vecinos = grafo.obtener_vecinos(nodo_actual.posicion)
        
        for posicion_vecino, peso in vecinos:
            # Saltar si ya fue explorado
            if posicion_vecino in lista_cerrada:
                continue
            
            # Calcular nuevo costo_g
            nuevo_costo_g = nodo_actual.costo_g + peso
            
            # Si encontramos un camino mejor o es la primera vez que visitamos este nodo
            if posicion_vecino not in mejor_costo_g or nuevo_costo_g < mejor_costo_g[posicion_vecino]:
                # Crear nodo vecino
                nodo_vecino = Nodo(posicion_vecino, nodo_actual)
                nodo_vecino.costo_g = nuevo_costo_g
                nodo_vecino.costo_h = distancia_manhattan(posicion_vecino, meta)
                nodo_vecino.costo_f = nodo_vecino.costo_g + nodo_vecino.costo_h
                
                # Actualizar mejor costo
                mejor_costo_g[posicion_vecino] = nuevo_costo_g
                
                # Agregar a lista abierta
                heapq.heappush(lista_abierta, nodo_vecino)
    
    # No se encontro camino
    return None, nodos_explorados
