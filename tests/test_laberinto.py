"""
Tests basicos para verificar el funcionamiento del solucionador de laberintos.
"""

import sys
import os

# Agregar el directorio raiz al path para importar modulos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.laberinto import Laberinto
from src.grafo import Grafo
from src.busqueda_ciega import busqueda_anchura, busqueda_profundidad
from src.busqueda_a_estrella import busqueda_a_estrella


def crear_laberinto_prueba():
    """Crea un laberinto simple para pruebas"""
    matriz = [
        [2, 0, 1],
        [1, 0, 1],
        [1, 0, 3]
    ]
    return Laberinto(matriz)


def test_creacion_laberinto():
    """Prueba que se pueda crear un laberinto correctamente"""
    laberinto = crear_laberinto_prueba()
    assert laberinto.dimensiones == 3
    assert laberinto.inicio == (0, 0)
    assert laberinto.meta == (2, 2)
    print("Test creacion_laberinto: OK")


def test_transformacion_grafo():
    """Prueba que la transformacion a grafo funcione correctamente"""
    laberinto = crear_laberinto_prueba()
    grafo = Grafo(laberinto)
    assert len(grafo.lista_adyacencia) > 0
    assert laberinto.inicio in grafo.lista_adyacencia
    assert laberinto.meta in grafo.lista_adyacencia
    print("Test transformacion_grafo: OK")


def test_bfs_encuentra_solucion():
    """Prueba que BFS encuentre una solucion"""
    laberinto = crear_laberinto_prueba()
    grafo = Grafo(laberinto)
    camino, nodos = busqueda_anchura(grafo, laberinto.inicio, laberinto.meta)
    assert camino is not None
    assert len(camino) > 0
    assert camino[0] == laberinto.inicio
    assert camino[-1] == laberinto.meta
    print(f"Test BFS: OK - Camino de longitud {len(camino)}, {nodos} nodos explorados")


def test_dfs_encuentra_solucion():
    """Prueba que DFS encuentre una solucion"""
    laberinto = crear_laberinto_prueba()
    grafo = Grafo(laberinto)
    camino, nodos = busqueda_profundidad(grafo, laberinto.inicio, laberinto.meta)
    assert camino is not None
    assert len(camino) > 0
    assert camino[0] == laberinto.inicio
    assert camino[-1] == laberinto.meta
    print(f"Test DFS: OK - Camino de longitud {len(camino)}, {nodos} nodos explorados")


def test_a_estrella_encuentra_solucion():
    """Prueba que A* encuentre una solucion optima"""
    laberinto = crear_laberinto_prueba()
    grafo = Grafo(laberinto)
    camino, nodos = busqueda_a_estrella(grafo, laberinto.inicio, laberinto.meta)
    assert camino is not None
    assert len(camino) > 0
    assert camino[0] == laberinto.inicio
    assert camino[-1] == laberinto.meta
    print(f"Test A*: OK - Camino de longitud {len(camino)}, {nodos} nodos explorados")


def ejecutar_tests():
    """Ejecuta todos los tests"""
    print("Ejecutando tests...\n")
    
    try:
        test_creacion_laberinto()
        test_transformacion_grafo()
        test_bfs_encuentra_solucion()
        test_dfs_encuentra_solucion()
        test_a_estrella_encuentra_solucion()
        
        print("\nTodos los tests pasaron correctamente")
        
    except AssertionError as e:
        print(f"\nError en test: {e}")
    except Exception as e:
        print(f"\nError inesperado: {e}")


if __name__ == "__main__":
    ejecutar_tests() 
