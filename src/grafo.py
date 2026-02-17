"""
Modulo para transformar el laberinto en un grafo representado como lista de adyacencia.
"""

from src.laberinto import Laberinto

class Grafo:
    """
    Representa el laberinto como un grafo usando lista de adyacencia.
    
    Attributos:
        laberinto (Laberinto): Instancia del laberinto
        lista_adyacencia (dict): Diccionario donde cada nodo apunta a sus vecinos
    """
    
    def __init__(self, laberinto):
        """
        Inicializa el grafo a partir de un laberinto.
        
        Args:
            laberinto (Laberinto): Instancia de la clase Laberinto
        """
        self.laberinto = laberinto
        self.lista_adyacencia = {}
        self._construir_grafo()
    
    def _construir_grafo(self):
        """
        Construye la lista de adyacencia recorriendo todas las celdas transitables.
        Cada nodo (posicion) se mapea a sus vecinos validos con peso 1.
        """
        for fila in range(self.laberinto.dimensiones):
            for columna in range(self.laberinto.dimensiones):
                posicion = (fila, columna)
                
                # Solo agregamos nodos transitables (no paredes)
                if self.laberinto.es_valido(fila, columna):
                    vecinos = self.laberinto.obtener_vecinos(posicion)
                    
                    # Guardamos los vecinos con peso 1 (cada movimiento cuesta 1)
                    self.lista_adyacencia[posicion] = [(vecino, 1) for vecino in vecinos]
    
    def obtener_vecinos(self, posicion):
        """
        Obtiene los vecinos de una posicion desde la lista de adyacencia.
        
        Args:
            posicion (tuple): Tupla (fila, columna)
            
        Returns:
            list: Lista de tuplas (vecino, peso)
        """
        return self.lista_adyacencia.get(posicion, [])
    
    def __str__(self):
        """Representacion en string del grafo"""
        resultado = "Grafo (Lista de Adyacencia):\n"
        for nodo, vecinos in self.lista_adyacencia.items():
            resultado += f"{nodo}: {vecinos}\n"
        return resultado
