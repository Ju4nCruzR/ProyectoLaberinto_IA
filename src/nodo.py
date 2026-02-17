"""
Modulo que define la clase Nodo para representar estados en el grafo.
"""

class Nodo:
    """
    Representa un nodo en el grafo del laberinto.
    
    Attributos:
        posicion (tuple): Coordenadas (fila, columna) en el laberinto
        padre (Nodo): Nodo padre en el camino de busqueda
        costo_g (int): Costo desde el nodo inicial
        costo_h (int): Heuristica estimada al objetivo
        costo_f (int): Costo total f = g + h
    """
    
    def __init__(self, posicion, padre=None):
        self.posicion = posicion
        self.padre = padre
        self.costo_g = 0
        self.costo_h = 0
        self.costo_f = 0
    
    def __eq__(self, otro):
        """Compara dos nodos por su posicion"""
        return self.posicion == otro.posicion
    
    def __lt__(self, otro):
        """Comparacion para ordenar nodos en cola de prioridad"""
        return self.costo_f < otro.costo_f
    
    def __hash__(self):
        """Permite usar nodos en sets y como keys de diccionarios"""
        return hash(self.posicion)
    
    def __repr__(self):
        """Representacion en string del nodo"""
        return f"Nodo(pos={self.posicion}, g={self.costo_g}, h={self.costo_h}, f={self.costo_f})"
