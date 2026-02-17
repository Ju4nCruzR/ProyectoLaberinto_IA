"""
Tests para verificar el funcionamiento del solucionador de laberintos.
"""

import unittest
import sys
import os

# Agregar el directorio raiz al path para importar modulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.laberinto import Laberinto
from src.grafo import Grafo
from src.busqueda_ciega import busqueda_anchura, busqueda_profundidad
from src.busqueda_a_estrella import busqueda_a_estrella


class TestLaberinto(unittest.TestCase):
    """Tests para la clase Laberinto"""
    
    def setUp(self):
        """Crea un laberinto simple para pruebas"""
        self.matriz = [
            [2, 0, 1],
            [1, 0, 1],
            [1, 0, 3]
        ]
        self.laberinto = Laberinto(self.matriz)
    
    def test_creacion_laberinto(self):
        """Prueba que se pueda crear un laberinto correctamente"""
        self.assertEqual(self.laberinto.filas, 3)
        self.assertEqual(self.laberinto.columnas, 3)
        self.assertEqual(self.laberinto.inicio, (0, 0))
        self.assertEqual(self.laberinto.meta, (2, 2))
    
    def test_laberinto_sin_inicio(self):
        """Prueba que lance error si no hay inicio"""
        matriz = [
            [0, 0, 1],
            [1, 0, 1],
            [1, 0, 3]
        ]
        with self.assertRaises(ValueError):
            Laberinto(matriz)
    
    def test_laberinto_sin_meta(self):
        """Prueba que lance error si no hay meta"""
        matriz = [
            [2, 0, 1],
            [1, 0, 1],
            [1, 0, 0]
        ]
        with self.assertRaises(ValueError):
            Laberinto(matriz)


class TestGrafo(unittest.TestCase):
    """Tests para la clase Grafo"""
    
    def setUp(self):
        self.laberinto = Laberinto([
            [2, 0, 1],
            [1, 0, 1],
            [1, 0, 3]
        ])
        self.grafo = Grafo(self.laberinto)
    
    def test_transformacion_grafo(self):
        """Prueba que la transformacion a grafo funcione correctamente"""
        self.assertGreater(len(self.grafo.lista_adyacencia), 0)
        self.assertIn(self.laberinto.inicio, self.grafo.lista_adyacencia)
        self.assertIn(self.laberinto.meta, self.grafo.lista_adyacencia)


class TestAlgoritmos(unittest.TestCase):
    """Tests para los algoritmos de busqueda"""
    
    def setUp(self):
        self.laberinto = Laberinto([
            [2, 0, 1],
            [1, 0, 1],
            [1, 0, 3]
        ])
        self.grafo = Grafo(self.laberinto)
    
    def test_bfs_encuentra_solucion(self):
        """Prueba que BFS encuentre una solucion"""
        camino, nodos = busqueda_anchura(self.grafo, self.laberinto.inicio, self.laberinto.meta)
        self.assertIsNotNone(camino)
        self.assertGreater(len(camino), 0)
        self.assertEqual(camino[0], self.laberinto.inicio)
        self.assertEqual(camino[-1], self.laberinto.meta)
    
    def test_dfs_encuentra_solucion(self):
        """Prueba que DFS encuentre una solucion"""
        camino, nodos = busqueda_profundidad(self.grafo, self.laberinto.inicio, self.laberinto.meta)
        self.assertIsNotNone(camino)
        self.assertGreater(len(camino), 0)
        self.assertEqual(camino[0], self.laberinto.inicio)
        self.assertEqual(camino[-1], self.laberinto.meta)
    
    def test_a_estrella_encuentra_solucion(self):
        """Prueba que A* encuentre una solucion"""
        camino, nodos = busqueda_a_estrella(self.grafo, self.laberinto.inicio, self.laberinto.meta)
        self.assertIsNotNone(camino)
        self.assertGreater(len(camino), 0)
        self.assertEqual(camino[0], self.laberinto.inicio)
        self.assertEqual(camino[-1], self.laberinto.meta)
    
    def test_bfs_y_a_estrella_misma_longitud(self):
        """BFS y A* deben encontrar caminos de la misma longitud (ambos son optimos)"""
        camino_bfs, _ = busqueda_anchura(self.grafo, self.laberinto.inicio, self.laberinto.meta)
        camino_a, _ = busqueda_a_estrella(self.grafo, self.laberinto.inicio, self.laberinto.meta)
        self.assertEqual(len(camino_bfs), len(camino_a))


class TestSinSolucion(unittest.TestCase):
    """Tests para laberintos sin solucion"""
    
    def test_laberinto_sin_solucion(self):
        """Prueba que los algoritmos retornen None si no hay camino"""
        laberinto = Laberinto([
            [2, 1, 0],
            [1, 1, 0],
            [0, 0, 3]
        ])
        grafo = Grafo(laberinto)
        
        camino_bfs, _ = busqueda_anchura(grafo, laberinto.inicio, laberinto.meta)
        camino_dfs, _ = busqueda_profundidad(grafo, laberinto.inicio, laberinto.meta)
        camino_a, _ = busqueda_a_estrella(grafo, laberinto.inicio, laberinto.meta)
        
        self.assertIsNone(camino_bfs)
        self.assertIsNone(camino_dfs)
        self.assertIsNone(camino_a)


if __name__ == "__main__":
    unittest.main()
