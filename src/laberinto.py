"""
Modulo para manejar la lectura y representacion del laberinto.
"""

class Laberinto:
    """
    Representa un laberinto como matriz NxN.
    
    Attributos:
        matriz (list): Matriz NxN del laberinto
        dimensiones (int): Tamaño N del laberinto
        inicio (tuple): Coordenadas de la entrada (fila, columna)
        meta (tuple): Coordenadas del objetivo (fila, columna)
    """
    
    def __init__(self, matriz):
        """
        Inicializa el laberinto con una matriz.
        
        Args:
            matriz (list): Matriz NxN donde:
                0 = espacio libre
                1 = pared
                2 = inicio
                3 = meta
        """
        self.matriz = matriz
        self.dimensiones = len(matriz)
        self.inicio = None
        self.meta = None
        self._encontrar_inicio_y_meta()
    
    @staticmethod
    def desde_archivo(ruta_archivo):
        """
        Crea un laberinto leyendo desde un archivo de texto.
        
        Args:
            ruta_archivo (str): Ruta al archivo con la matriz del laberinto
            
        Returns:
            Laberinto: Nueva instancia de Laberinto
        """
        matriz = []
        with open(ruta_archivo, 'r') as archivo:
            for linea in archivo:
                fila = [int(valor) for valor in linea.strip().split()]
                matriz.append(fila)
        
        return Laberinto(matriz)
    
    def _encontrar_inicio_y_meta(self):
        """Busca las posiciones de inicio (2) y meta (3) en el laberinto"""
        for fila in range(self.dimensiones):
            for columna in range(self.dimensiones):
                if self.matriz[fila][columna] == 2:
                    self.inicio = (fila, columna)
                elif self.matriz[fila][columna] == 3:
                    self.meta = (fila, columna)
    
    def es_valido(self, fila, columna):
        """
        Verifica si una posicion es valida y transitable.
        
        Args:
            fila (int): Fila a verificar
            columna (int): Columna a verificar
            
        Returns:
            bool: True si la posicion es valida y no es pared
        """
        if 0 <= fila < self.dimensiones and 0 <= columna < self.dimensiones:
            return self.matriz[fila][columna] != 1
        return False
    
    def obtener_vecinos(self, posicion):
        """
        Obtiene las posiciones vecinas validas (arriba, abajo, izquierda, derecha).
        
        Args:
            posicion (tuple): Tupla (fila, columna)
            
        Returns:
            list: Lista de tuplas con posiciones vecinas validas
        """
        fila, columna = posicion
        vecinos = []
        
        # Movimientos: arriba, abajo, izquierda, derecha
        movimientos = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for mov_fila, mov_columna in movimientos:
            nueva_fila = fila + mov_fila
            nueva_columna = columna + mov_columna
            
            if self.es_valido(nueva_fila, nueva_columna):
                vecinos.append((nueva_fila, nueva_columna))
        
        return vecinos
    
    def __str__(self):
        """Representacion en string del laberinto"""
        resultado = ""
        for fila in self.matriz:
            for celda in fila:
                if celda == 0:
                    resultado += ". "
                elif celda == 1:
                    resultado += "# "
                elif celda == 2:
                    resultado += "S "
                elif celda == 3:
                    resultado += "M "
            resultado += "\n"
        return resultado