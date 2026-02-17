"""
Modulo que implementa algoritmos de busqueda a ciegas: BFS y DFS.
"""

from collections import deque
from src.nodo import Nodo

def reconstruir_camino(nodo_actual):
    """
    Reconstruye el camino desde el inicio hasta el nodo actual.
    
    Args:
        nodo_actual (Nodo): Nodo final del camino
        
    Returns:
        list: Lista de posiciones que forman el camino
    """
    camino = []
    while nodo_actual is not None:
        camino.append(nodo_actual.posicion)
        nodo_actual = nodo_actual.padre
    return camino[::-1]  # Invertir para tener el camino desde inicio a meta


def busqueda_anchura(grafo, inicio, meta):
    """
    Implementa el algoritmo BFS (Breadth-First Search).
    Explora el grafo por niveles usando una cola FIFO.
    
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
    nodo_meta = Nodo(meta)
    
    # Cola FIFO para BFS
    cola = deque([nodo_inicio])
    
    # Set de nodos visitados
    visitados = set()
    visitados.add(nodo_inicio.posicion)
    
    nodos_explorados = 0
    
    while cola:
        nodo_actual = cola.popleft()
        nodos_explorados += 1
        
        # Verificar si llegamos a la meta
        if nodo_actual == nodo_meta:
            camino = reconstruir_camino(nodo_actual)
            return camino, nodos_explorados
        
        # Explorar vecinos
        vecinos = grafo.obtener_vecinos(nodo_actual.posicion)
        for posicion_vecino, peso in vecinos:
            if posicion_vecino not in visitados:
                nodo_vecino = Nodo(posicion_vecino, nodo_actual)
                visitados.add(posicion_vecino)
                cola.append(nodo_vecino)
    
    # No se encontro camino
    return None, nodos_explorados


def busqueda_profundidad(grafo, inicio, meta):
    """
    Implementa el algoritmo DFS (Depth-First Search).
    Explora el grafo en profundidad usando una pila LIFO.
    
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
    nodo_meta = Nodo(meta)
    
    # Pila LIFO para DFS
    pila = [nodo_inicio]
    
    # Set de nodos visitados
    visitados = set()
    visitados.add(nodo_inicio.posicion)
    
    nodos_explorados = 0
    
    while pila:
        nodo_actual = pila.pop()
        nodos_explorados += 1
        
        # Verificar si llegamos a la meta
        if nodo_actual == nodo_meta:
            camino = reconstruir_camino(nodo_actual)
            return camino, nodos_explorados
        
        # Explorar vecinos
        vecinos = grafo.obtener_vecinos(nodo_actual.posicion)
        for posicion_vecino, peso in vecinos:
            if posicion_vecino not in visitados:
                nodo_vecino = Nodo(posicion_vecino, nodo_actual)
                visitados.add(posicion_vecino)
                pila.append(nodo_vecino)
    
    # No se encontro camino
    return None, nodos_explorados 
